# Svenska översättningar för gallery_screens.rpy

translate swedish strings:

    old "Overview"
    new "Översikt"

    old "Characters"
    new "Karaktärer"

    old "World"
    new "Värld"

    old "Narrative"
    new "Berättelse"

    old "{b}Cast of Characters{/b}"
    new "{b}Rollgalleri{/b}"

    old "< Previous"
    new "< Föregående"

    old "Close"
    new "Stäng"

    old "Next >"
    new "Nästa >"

    old "Amelia's World"
    new "Amelias värld"

    old "Click a region to explore the places in the story."
    new "Klicka på en region för att utforska platserna i berättelsen."

    old "London"
    new "London"

    old "Plymouth"
    new "Plymouth"

    old "Cornwall"
    new "Cornwall"

    old "< Back to overview"
    new "< Tillbaka till översikten"

    old "Locations"
    new "Platser"

    old "{b}The Hero's Journey{/b}"
    new "{b}Hjältens resa{/b}"

    old "Amelia's story follows the twelve stages of Joseph Campbell's Monomyth — the universal pattern that underpins every transformative journey, from Odysseus to Luke Skywalker to a first-year psychology student from south-east London."
    new "Amelias berättelse följer de tolv stadierna i Joseph Campbells monomyt — det universella mönstret som ligger till grund för varje omvälvande resa, från Odysseus till Luke Skywalker till en förstaårsstudent i psykologi från sydöstra London."

    old "Beneath the Hero's Journey lies a second structure: the four stages of alchemical transformation — {b}Nigredo{/b} (blackening), {b}Albedo{/b} (whitening), {b}Citrinitas{/b} (yellowing), and {b}Rubedo{/b} (reddening). The colours of the game shift with Amelia's inner work."
    new "Under hjältens resa finns en andra struktur: de fyra stadierna av alkemisk transformation — {b}Nigredo{/b} (svärta), {b}Albedo{/b} (vithet), {b}Citrinitas{/b} (gulhet) och {b}Rubedo{/b} (rödhet). Spelets färger skiftar med Amelias inre arbete."

    old "SELECT CHAPTER"
    new "VÄLJ KAPITEL"

    old "Version [config.version!t]\n"
    new "Version [config.version!t]\n"

    old "{b}Art & Music{/b}\nDancing Salamanders — {a=https://dancingsalamanders.com}dancingsalamanders.com{/a}\n"
    new "{b}Konst & Musik{/b}\nDancing Salamanders — {a=https://dancingsalamanders.com}dancingsalamanders.com{/a}\n"

    old "Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"
    new "Skapad med {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"

translate swedish python:

    _characters = [
        ("amelia", "Amelia James", "Huvudperson",
         "18 år, kandidat i psykologi vid Plymouth. Nyfiken, empatisk, konflikträdd. Hennes år motsvarar det alkemiska Magnum Opus — från Nigredos mörker genom Albedos reflektion till Rubedos helhet.",
         "images/characters/amelia/amelia_anchor_image.png"),
        ("ella", "Ella Chen", "Barndomsvän",
         "18 år, engelsk litteratur vid Queen Mary London. Den gyllene tråden till den vanliga världen. Hon och Amelia har varit vänner sedan årskurs 3. Deras vänskap kommer att prövas av avståndet.",
         None),
        ("lucas", "Lucas Adeyemi", "Den tyste tänkaren",
         "19 år, psykologi. Läser Jung, citerar Fanon, lyssnar mer än han talar. Han ser saker hos Amelia som hon inte har märkt ännu. Representerar Animus-arketypen.",
         None),
        ("zara", "Zara Okafor", "Det röda lejonet",
         "20 år, psykologi med kriminologi. Eldigt, lojalt, roligt. Uppvuxen i Tottenham, bär levd erfarenhet av rasism med vrede och grace. Hon kämpar — för sig själv, för andra.",
         None),
        ("raj", "Raj Sharma", "Hjärtat",
         "21 år, psykologi. Emotional kärna i varje grupp. När folk faller samman lagar Raj mat. Biryani fixar allt — eller gör det åtminstone uthärdligt.",
         None),
        ("sarah", "Sarah Whitmore", "Spegeln",
         "18 år, psykologi, lantliga Devon. Tyst, mild, kämpar under ytan. Hennes historia är spelets största vägval. Amelia måste bestämma vad hon är villig att göra.",
         None),
        ("liz", "Liz Torres", "Rumskamraten",
         "18 år, marinbiologi, Cardiff. Glad, kaotisk, evigt sen. Amelias första vän i Plymouth och den som drar henne till studentkåren första kvällen.",
         None),
        ("maya", "Maya Patel", "Mystikern",
         "20 år, filosofi med psykologi, Bristol. Kristaller, tarot, meditation i gryningen. Hon är antingen djupt vis eller lite galen — möjligen båda. Representerar Svavel.",
         None),
        ("tasha", "Tasha Reynolds", "Skuggan",
         "20 år, psykologi, Surrey. Jungiansk skugga personifierad. Osäker, vass i tonen, olycklig hemma. Hon kan förändras om Amelia väljer medkänsla framför konfrontation.",
         None),
        ("sophia", "Sophia Langford", "Den vita drottningen",
         "19 år, psykologi, Oxfordfamilj. Briljant, precis, ensam bakom fasaden. Akademisk rival som kan bli en oväntad allierad.",
         None),
        ("hawthorne", "Prof. Arthur Hawthorne", "Mentor — Salt",
         "58 år, prefekt för psykologi. Rationell, precis, Earl Grey i en porslinskop. Hans kontor har böcker från golv till tak och en Caravaggio-tryck. Låses upp genom akademisk excellens.",
         None),
        ("simmons", "Dr. Nadia Simmons", "Mentor — Kvicksilver",
         "38 år, lektor i positiv psykologi. Varm, omhändertagande, tror på vänlighetens vetenskap. Hennes kontor har växter överallt och en liten fontän. Låses upp genom medkänsla.",
         None),
        ("elena", "Elena Trevorran", "Mentor — Soror Mystica",
         "45 år, kornisk pellar. Väktare av gammal kunskap, beskyddare av fogoun. Hon dyker upp när du är redo. Låses upp genom den ockulta kunskapsvägen.",
         None),
        ("david", "David James", "Amelias far",
         "46 år, IT-support, jamaicanskt arv. Tyst, stadig, fixar saker med händerna. Kärlek uttryckt genom handlingar: matpackar, skjuts till stationen, en kram vid dörren.",
         None),
        ("grace", "Grace James", "Amelias mor",
         "44 år, lärarassistent, jamaicanskt arv. Varm, pratsam, skickar omsorgspaket. Hon är den som frågar 'Äter du ordentligt?' tre gånger i veckan.",
         None),
        ("lily", "Lily James", "Amelias kusin",
         "16 år, går fortfarande i skolan. Ser upp till Amelia. Ifrågasätter sin sexualitet och försöker ta reda på vem hon är. Amelias brev till henne är bland det mest ärliga skrivandet i spelet.",
         None),
    ]

    _chapters = [
        (1, "chapter_1", "Den vanliga världen",
         "Sista dagarna före avfärden. London är gyllene, nostalgiskt — och på väg att lämnas bakom.",
         "Slutet av september", "#D4A574"),
        (2, "chapter_2", "Kallelsen till äventyret",
         "Resan till Plymouth. Ett tåg, en ny stad och den nervösa spänningen av att allt börjar.",
         "Början av oktober", "#D4A574"),
        (3, "chapter_3", "Avvisandet av kallelsen",
         "Första terminens svårigheter. Studierna är tunga, människorna är främmande och hemma känns väldigt långt bort.",
         "Oktober–november", "#D4A574"),
        (4, "chapter_4", "Mötet med mentorn",
         "Mentortilldelning och en första resa till Cornwall. Något gammalt och märkligt vaknar.",
         "November", "#A8C0D4"),
        (5, "chapter_5", "Att korsa tröskeln",
         "Fullständig fördjupning. Fördjupade relationer, att hitta sin rytm. Plymouth börjar kännas som hemma.",
         "November–december", "#A8C0D4"),
        (6, "chapter_6", "Prövningar, allierade och fiender",
         "Spänning, konflikt, samhörighet. Jullovet avslöjar hur mycket som har förändrats. Skuggan dyker upp.",
         "December–januari", "#A8C0D4"),
        (7, "chapter_7", "Närmandet",
         "Återkomst efter jul. Något växer. Cornwall kallar igen, djupare denna gång.",
         "Januari–februari", "#A8C0D4"),
        (8, "chapter_8", "Prövningen",
         "Det yttersta provet. Sarahs kris. Ett telefonsamtal i natten som förändrar allt.",
         "Februari", "#DAA520"),
        (9, "chapter_9", "Belöningen",
         "Efterspel. Gruppen samlas igen. Sköra förhoppningar. Något har vunnits genom smärta.",
         "Mars", "#DAA520"),
        (10, "chapter_10", "Vägen tillbaka",
         "Påsk hemma. London är sig likt; Amelia är det inte. Bittersöt klarhet.",
         "April", "#C04040"),
        (11, "chapter_11", "Uppståndelsen",
         "Sista provet. Syntes. Fogoun. Allt Amelia har lärt sig ställs inför det yttersta provet.",
         "Maj", "#C04040"),
        (12, "chapter_12", "Återkomst med elixiret",
         "Sju möjliga slut. Sommartermin, sista veckorna. Vem har Amelia blivit?",
         "Juni", "#C04040"),
    ]

    _region_data = {
        "london": {
            "name": "London",
            "summary": "Sydöstra London. Bromley, Lewisham, utkanterna där staden övergår i något lugnare. Här började Amelia — och hit återvänder hon, förändrad.",
            "locations": [
                ("Familjen James hem",
                 "Ett radhus där Amelia växte upp. Köket doftar av ackee och saltfisk. Väggarna bär sexton års fotografier."),
                ("Bromley Park",
                 "Parkbänken där Amelia läser. Den vetter mot väster och fångar kvällsljuset. Här börjar berättelsen."),
                ("Mr Oseis bokhandel",
                 "En trång, överfull bokhandel. Mr Osei känner varje bok på känn. Här hittar Amelia Paracelsus-texten som öppnar den ockulta kunskapsvägen."),
            ],
        },
        "plymouth": {
            "name": "Plymouth",
            "summary": "En hamnstad där hedarna möter havet. Brutalistiska universitetsbyggnader, The Hoe i solnedgången, studentkåren klockan två på natten. Här blir Amelia sig själv.",
            "locations": [
                ("University of Plymouth",
                 "Psykologibyggnaden, femvåningsbiblioteket, föreläsningssalarna där allt förändras. Betong och gröna innergårdar."),
                ("Plymouth Hoe",
                 "Smeatons torn, Drakes staty, havet som sträcker sig mot horisonten. Viktiga känslosamma scener utspelar sig här — i gryningen, i skymningen, i regnet."),
                ("Studentkåren",
                 "Karaokenätter, billiga öl, vänskaper smidda klockan två. Där Amelias sociala värld expanderar — och där spänningar kokar över."),
                ("Studentbostäderna",
                 "Amelias rum: en enkelsäng, ett skrivbord, ett fönster mot staden. Gemensamma köket där Raj lagar mat och bråk uppstår."),
            ],
        },
        "cornwall": {
            "name": "Cornwall",
            "summary": "Den uråldriga halvön. Stencirklar, heliga brunnar, fogoun. Där slöjan mellan det rationella och det numinösa tunnas ut.",
            "locations": [
                ("Bodmin Moor",
                 "Vilda ponnyer, granitklippor, överväldigande stjärnor. Nigredo-landskapet — rått, urtida, avskalat. På natten är mörkret absolut."),
                ("Mên-an-Tol",
                 "Den genomborrade stenen. Tretusen år gammal. Elena kallar den 'athanor-öppningen' — ingången till den alkemiska ugnen."),
                ("Merry Maidens",
                 "En stencirkel nära Penzance. Nitton stenar i en perfekt ring. Legenden säger att de var flickor som förvandlades till sten för att de dansade på sabbaten."),
                ("Madron Holy Well",
                 "Gömd i skog ovanför Penzance. Bönetrasor hänger från grenar. Vattnet är kallt och klart. Elena kallar den 'albedo-poolen'."),
                ("Fogoun",
                 "En underjordisk kammare. Järnålder, kanske äldre. Sval, mörk, fullständigt tyst. Den sista Elena-scenen utspelar sig här. Valens buk."),
                ("Tintagel",
                 "Arthurruiner på klippranden. Vind, stänk, legend lagrat på legend. Mayas väg leder hit. Bron mellan världar."),
                ("Eden Project",
                 "Biomdomer i ett återställt stenbrott. Dr Simmons tar gruppen hit. Tillväxt ur förödelse — hela platsen är en metafor."),
            ],
        },
    }
