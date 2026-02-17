#!/usr/bin/env python3
"""
Generate dark-themed maps for The CK: Amelia V2.

Produces:
  1. world_map.png        — Overview of SW England (zoom 7), region pins only, NO labels
  2. map_london.png       — Zoomed London (zoom 13), location pins + labels
  3. map_plymouth.png     — Zoomed Plymouth (zoom 14), location pins + labels
  4. map_cornwall.png     — Zoomed Cornwall (zoom 10), location pins + labels

Uses CartoDB dark_all tiles (© OpenStreetMap contributors, © CARTO).
"""

import math
import os
import urllib.request
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

# ── Output ───────────────────────────────────────────────────────────────────
OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "Amelia_V2", "game", "images", "ui"
)

TILE_URL = "https://basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png"
TILE_SIZE = 256

GOLD = (212, 165, 116)
DARK_BG = (10, 10, 10)

# ── Location data ────────────────────────────────────────────────────────────
LOCATIONS = {
    "london": [
        ("James Family Home",     -0.0076,  51.4065),
        ("Bromley Park",          -0.0276,  51.3945),
        ("Mr. Osei's Bookshop",   -0.0176,  51.4005),
    ],
    "plymouth": [
        ("University of Plymouth", -4.1427,  50.3755),
        ("Plymouth Hoe",           -4.1430,  50.3650),
        ("Student Union",          -4.1350,  50.3770),
        ("Halls of Residence",     -4.1250,  50.3790),
    ],
    "cornwall": [
        ("Bodmin Moor",            -4.6000,  50.5500),
        ("Mên-an-Tol",            -5.5950,  50.1530),
        ("Merry Maidens",          -5.5880,  50.0700),
        ("Madron Holy Well",       -5.5400,  50.1400),
        ("The Fogou",              -5.4500,  50.1200),
        ("Tintagel",               -4.7580,  50.6640),
        ("Eden Project",           -4.7440,  50.3600),
    ],
}

REGION_CENTRES = {
    "london":   (-0.015,  51.400),
    "plymouth": (-4.135,  50.375),
    "cornwall": (-5.050,  50.350),
}


# ── Projection ───────────────────────────────────────────────────────────────

def to_world(lon, lat, zoom):
    n = 2 ** zoom
    x = (lon + 180.0) / 360.0 * n * TILE_SIZE
    lat_rad = math.radians(lat)
    y = (1.0 - math.log(math.tan(lat_rad) + 1.0 / math.cos(lat_rad))
         / math.pi) / 2.0 * n * TILE_SIZE
    return x, y


def lonlat_to_pixel(lon, lat, zoom, center_lon, center_lat, w, h):
    cx, cy = to_world(center_lon, center_lat, zoom)
    wx, wy = to_world(lon, lat, zoom)
    return int(wx - cx + w / 2), int(wy - cy + h / 2)


# ── Tile fetching ────────────────────────────────────────────────────────────

_tile_cache = {}

def download_tile(z, tx, ty):
    key = (z, tx, ty)
    if key in _tile_cache:
        return _tile_cache[key]
    url = TILE_URL.format(z=z, x=tx, y=ty)
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "TheCK-MapGen/1.0 (student project)"
        })
        data = urllib.request.urlopen(req, timeout=15).read()
        img = Image.open(BytesIO(data)).convert("RGB")
        _tile_cache[key] = img
        return img
    except Exception as e:
        print(f"  Warning: tile {z}/{tx}/{ty} failed: {e}")
        return None


def stitch_and_crop(zoom, center_lon, center_lat, w, h):
    center_tx_f = (center_lon + 180.0) / 360.0 * (2 ** zoom)
    lat_rad = math.radians(center_lat)
    center_ty_f = (1.0 - math.log(math.tan(lat_rad) + 1.0 / math.cos(lat_rad))
                   / math.pi) / 2.0 * (2 ** zoom)

    extra = max(3, int(math.ceil(max(w, h) / TILE_SIZE / 2)) + 1)
    min_tx = int(center_tx_f) - extra
    max_tx = int(center_tx_f) + extra + 1
    min_ty = int(center_ty_f) - extra
    max_ty = int(center_ty_f) + extra + 1

    n_tiles = (max_tx - min_tx) * (max_ty - min_ty)
    print(f"  Downloading {n_tiles} tiles (zoom {zoom})...")

    big_w = (max_tx - min_tx) * TILE_SIZE
    big_h = (max_ty - min_ty) * TILE_SIZE
    big = Image.new("RGB", (big_w, big_h), DARK_BG)

    for tx in range(min_tx, max_tx):
        for ty in range(min_ty, max_ty):
            tile_img = download_tile(zoom, tx, ty)
            if tile_img:
                px = (tx - min_tx) * TILE_SIZE
                py = (ty - min_ty) * TILE_SIZE
                big.paste(tile_img, (px, py))

    off_x = center_tx_f - min_tx
    off_y = center_ty_f - min_ty
    cx_px = off_x * TILE_SIZE
    cy_px = off_y * TILE_SIZE

    left = int(cx_px - w / 2)
    top  = int(cy_px - h / 2)
    return big.crop((left, top, left + w, top + h))


def get_font(size):
    for name in ["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"]:
        try:
            return ImageFont.truetype(name, size)
        except:
            pass
    return ImageFont.load_default()


# ── Generate maps ────────────────────────────────────────────────────────────

def generate_overview():
    zoom, clon, clat, w, h = 7, -2.80, 50.74, 805, 680
    print("\n[world_map] Overview map (no text labels)...")
    img = stitch_and_crop(zoom, clon, clat, w, h)
    draw = ImageDraw.Draw(img, "RGBA")

    for region_id, (rlon, rlat) in REGION_CENTRES.items():
        x, y = lonlat_to_pixel(rlon, rlat, zoom, clon, clat, w, h)
        if not (0 <= x < w and 0 <= y < h):
            continue
        draw.ellipse([x-16, y-16, x+16, y+16],
                     fill=(212, 165, 116, 60), outline=GOLD)
        draw.ellipse([x-8, y-8, x+8, y+8],
                     fill=GOLD, outline=(26, 20, 16))

    font_s = get_font(10)
    draw.text((w - 280, h - 16), "OpenStreetMap contributors / CARTO",
              fill=(100, 100, 100), font=font_s)

    out = os.path.join(OUTPUT_DIR, "world_map.png")
    img.save(out, "PNG", optimize=True)
    print(f"  Saved {out}")

    print("  Region pixel coords for Ren'Py:")
    for region_id, (rlon, rlat) in REGION_CENTRES.items():
        x, y = lonlat_to_pixel(rlon, rlat, zoom, clon, clat, w, h)
        print(f'    ("{region_id}", "{region_id.upper()}", {x}, {y}),')


def generate_region(region_id, zoom, clon, clat):
    w, h = 805, 680
    fname = f"map_{region_id}"
    print(f"\n[{fname}] Region map for {region_id}...")
    img = stitch_and_crop(zoom, clon, clat, w, h)
    draw = ImageDraw.Draw(img, "RGBA")
    font = get_font(13)
    font_s = get_font(10)

    locs = LOCATIONS.get(region_id, [])
    for loc_name, lon, lat in locs:
        x, y = lonlat_to_pixel(lon, lat, zoom, clon, clat, w, h)
        if not (0 <= x < w and 0 <= y < h):
            print(f"  WARNING: {loc_name} at ({x},{y}) is OFF-SCREEN")
            continue

        r = 6
        draw.ellipse([x-r, y-r, x+r, y+r], fill=GOLD, outline=(26, 20, 16))
        lx, ly = x + 12, y - 8
        draw.text((lx+1, ly+1), loc_name, fill=(0, 0, 0, 200), font=font)
        draw.text((lx, ly), loc_name, fill=GOLD, font=font)

    draw.text((w - 280, h - 16), "OpenStreetMap contributors / CARTO",
              fill=(100, 100, 100), font=font_s)

    out = os.path.join(OUTPUT_DIR, f"{fname}.png")
    img.save(out, "PNG", optimize=True)
    print(f"  Saved {out}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    generate_overview()
    generate_region("london",   13, -0.015, 51.400)
    generate_region("plymouth", 14, -4.135, 50.375)
    generate_region("cornwall", 10, -5.050, 50.350)
    print("\nAll maps generated!")


if __name__ == "__main__":
    main()
