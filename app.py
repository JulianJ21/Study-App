import streamlit as st
import random

st.set_page_config(page_title="📘 Marketing Lern-App", layout="wide")

# --------------------
# LERNMODULE DEFINIEREN
# --------------------
modules = [
    {
        "title": "1. Grundlagen des Marketing",
        "core_insight": "Marketing ist die konsequente Ausrichtung des Unternehmens an den Bedürfnissen der Kunden.",
        "content": '''
• Definition: Marketing = marktorientierte Unternehmensführung
• Ziel: Bedürfnisbefriedigung + Unternehmensziele
• Grundprinzipien: Kundenorientierung, Wettbewerbsvorteile, Integration aller Bereiche
• Entwicklung: vom Absatzdenken (1950) über Strategisches Marketing (1990) bis zum heutigen Relationship Marketing
        ''',
        "story": "Marketing ist wie ein Kompass für das ganze Unternehmen: Alles richtet sich nach dem Kunden aus."
    },
    {
        "title": "2. Marktbegriff & Marktformen",
        "core_insight": "Ein Markt ist der Ort, an dem Angebot und Nachfrage aufeinandertreffen.",
        "content": '''
• Marktarten: Konsumgüter, Investitionsgüter, Dienstleistungsmarkt, B2B, B2C
• Marktformen: Monopol, Oligopol, Polypol
• Kriterien: Anzahl Anbieter/Nachfrager, Markttransparenz
        ''',
        "story": "Stell dir einen Markt wie eine Arena vor: Anbieter und Nachfrager kämpfen dort täglich um Aufmerksamkeit, Preise und Qualität."
    },
    {
        "title": "3. Marketingziele & Strategien",
        "core_insight": "Marketingziele leiten sich aus den Unternehmenszielen ab und bestimmen die Richtung des Handelns.",
        "content": '''
• Zielarten: ökonomisch (z.B. Umsatz), psychologisch (z.B. Image)
• Zielhierarchie: Unternehmensziele > Bereichsziele > Funktionsziele
• Strategien: Marktpenetration, Produktentwicklung, Diversifikation, Marktentwicklung
• Segmentierungsstrategien: Massenmarketing, Zielgruppenmarketing, One-to-One
        ''',
        "story": "Marketingziele sind wie Koordinaten – ohne sie weiß niemand, in welche Richtung das Unternehmen navigieren soll."
    },
    {
        "title": "4. Marktforschung",
        "core_insight": "Marktforschung liefert die Datenbasis für fundierte Marketingentscheidungen.",
        "content": '''
• Primärforschung (Befragung, Beobachtung, Experiment)
• Sekundärforschung (interne/externe Quellen)
• Panel, Pretest, Testmärkte
• Kriterien: Objektivität, Validität, Reliabilität
        ''',
        "story": "Marktforschung ist das Ohr am Markt – sie sagt dir, was Kunden wirklich denken und wollen."
    },
    {
        "title": "5. Preiselastizität (⚠️ Häufig abgefragt)",
        "core_insight": "Preiselastizität zeigt, wie stark die Nachfrage auf Preisänderungen reagiert.",
        "content": '''
• Formel: Preiselastizität = (% Mengenänderung) / (% Preisänderung)
• Interpretation:
    > |e| > 1: elastisch (z.B. Luxusgüter)
    > |e| < 1: unelastisch (z.B. Grundnahrungsmittel)
• Einflussfaktoren: Verfügbarkeit von Substituten, Dringlichkeit, Zeit
        ''',
        "story": "Je elastischer die Nachfrage, desto stärker wirkt sich der Preis auf den Absatz aus – wie ein Gummiband am Geldbeutel."
    }
]
modules += [
    {
        "title": "6. Preisstrategien & Preispsychologie (⚠️ Häufig abgefragt)",
        "core_insight": "Preisstrategien bestimmen langfristig das Preisniveau und beeinflussen die Wahrnehmung.",
        "content": '''
• Strategien:
    - Skimming (Abschöpfung)
    - Penetration (Einführungspreis)
    - Preisdifferenzierung (zeitlich, räumlich, personell)
• Psychologische Preisaspekte:
    - Schwellenpreise (z. B. 0,99 €)
    - Preis-Qualitäts-Anmutung
    - Preis als Vertrauenselement
• Klausurformulierung (SS23): „Welche Preisstrategie würden Sie für ein neues innovatives Produkt wählen?“
  > Musterantwort: Skimming, da hohe Innovationsbereitschaft + Zahlungsbereitschaft vorhanden.
        ''',
        "story": "Preise sind wie Signale – sie zeigen, ob ein Produkt exklusiv, günstig oder innovativ wahrgenommen wird."
    },
    {
        "title": "7. Produktpolitik",
        "core_insight": "Die Produktpolitik umfasst alle Entscheidungen rund um Eigenschaften, Gestaltung und Programmstruktur von Produkten.",
        "content": '''
• Produktkern, -zusatz, -gestaltung
• Verpackung, Serviceleistungen
• Programmbreite vs. -tiefe
• Relaunch vs. Innovation
• Produktlebenszyklus (Einführung, Wachstum, Reife, Sättigung, Degeneration)
        ''',
        "story": "Produkte sind wie Lebewesen – sie werden geboren, wachsen, altern und müssen manchmal neu erfunden werden."
    },
    {
        "title": "8. Distributionspolitik",
        "core_insight": "Die Distributionspolitik regelt den Weg des Produkts vom Anbieter zum Kunden.",
        "content": '''
• Absatzwege: direkt vs. indirekt
• Vertriebsorgane: unternehmensintern (Außendienst), -extern (Handel)
• Kriterien: Kosten, Kontrolle, Kundenkontakt
• Logistik, E-Commerce
• Multi-Channel-Strategien
        ''',
        "story": "Stell dir Distribution wie ein Transportsystem vor – je besser die Route, desto schneller kommt dein Produkt an."
    },
    {
        "title": "9. Kommunikationspolitik",
        "core_insight": "Kommunikationspolitik macht das Produkt im Kopf des Kunden sichtbar und verständlich.",
        "content": '''
• Werbung, Verkaufsförderung, PR, Sponsoring, persönlicher Verkauf
• AIDA-Modell: Attention, Interest, Desire, Action
• Ziel: Wahrnehmung, Wissen, Einstellung, Verhalten
• ⚠️ Klausur: „Welche Kommunikationsinstrumente eignen sich für ein erklärungsbedürftiges B2B-Produkt?“
  > Musterlösung: Persönlicher Verkauf + Fachmessen + technische PR
        ''',
        "story": "Kommunikation im Marketing ist wie Bühne & Mikrofon – du musst sichtbar, verständlich und überzeugend auftreten."
    },
    {
        "title": "10. Mediaentscheidungen & TKP (⚠️ Rechenaufgabe)",
        "core_insight": "Die Mediaentscheidung bestimmt, wo und wie Werbung geschaltet wird – mit Effizienzkennzahlen wie dem TKP.",
        "content": '''
• Mediaplanung: Zielgruppe – Medium – Zeit – Budget
• Tausenderkontaktpreis (TKP) = (Kosten / Bruttoreichweite) × 1.000
• Vergleichbarkeit von Medien
• ⚠️ Klausurformel (SS25): TKP bei 50.000 Reichweite & 2.000 € Kosten?
  > Lösung: (2.000 / 50.000) × 1.000 = 40 €
        ''',
        "story": "Der TKP ist wie der Benzinverbrauch pro 100 km – er zeigt, wie viel dich 1.000 Sichtkontakte kosten."
    }
]
modules += [
    {
        "title": "11. Zielgruppen & Marktsegmentierung",
        "core_insight": "Zielgruppenanalyse ermöglicht passgenaue Marketingmaßnahmen.",
        "content": '''
• Kriterien: geografisch, demografisch, psychografisch, verhaltensorientiert
• Vorgehen: Marktsegmentierung → Zielmarktfestlegung → Positionierung
• Persona-Modelle
• Klausur (SS23): „Welche Segmentierungskriterien würden Sie bei einem Bio-Lebensmittelanbieter anwenden?“
  > Lösung: Psychografisch (Gesundheitsbewusstsein), Verhalten (Kaufverhalten), Demografisch (Alter)
        ''',
        "story": "Segmentierung ist wie ein Filter – du sortierst aus dem großen Markt die Menschen heraus, für die dein Angebot passt."
    },
    {
        "title": "12. Positionierung",
        "core_insight": "Positionierung schafft ein klares Bild in den Köpfen der Zielgruppe.",
        "content": '''
• Ziel: Differenzierung, Wiedererkennung, klares Nutzenversprechen
• USP, UAP, UCP
• Wahrnehmungskarte (Perceptual Map)
• Relevanz von Markenimage und -assoziationen
        ''',
        "story": "Eine starke Positionierung ist wie ein klarer Geruch – sofort erkennbar, unverwechselbar, emotional aufgeladen."
    },
    {
        "title": "13. Markenpolitik",
        "core_insight": "Markenpolitik dient dem Aufbau, Schutz und der Führung starker Marken.",
        "content": '''
• Funktionen: Orientierungs-, Vertrauens-, Identifikationsfunktion
• Markenstrategien: Einzel-, Familien-, Dachmarke
• Markendehnung vs. -diversifikation
• Rechtlicher Schutz: Markeneintragung, Plagiate
        ''',
        "story": "Eine gute Marke ist wie ein Versprechen mit Persönlichkeit – sie bleibt im Gedächtnis und schafft Vertrauen."
    },
    {
        "title": "14. Werbewirkung & Werbeerfolgskontrolle (⚠️ Klausur)",
        "core_insight": "Werbung muss wirken – das zeigen Kennzahlen und Modelle.",
        "content": '''
• Modelle: AIDA, DAGMAR, Involvement-Theorie
• Pretest, Recalltest, Recognitiontest
• Kriterien: Bekanntheit, Sympathie, Kaufabsicht
• Klausurfrage (SoSe23): „Nennen Sie zwei geeignete Methoden zur Messung von Werbewirkung.“
  > Antwort: Recalltest, Recognitiontest
        ''',
        "story": "Werbung ohne Wirkung ist wie ein Schrei im Wald – teuer, aber ungehört. Wirkungskontrolle bringt Licht ins Dunkel."
    },
    {
        "title": "15. Budgetierung & Streuplanung (⚠️ Rechenaufgabe)",
        "core_insight": "Effizienter Mitteleinsatz entscheidet über Werbeerfolg.",
        "content": '''
• Budgetierungsmethoden: Ziel-Maßnahmen-Methode, Prozent-vom-Umsatz
• Streuplanung = Budgetverteilung nach Zielgruppe, Medium, Zeit
• Rechenbeispiel (SS25): 10.000 € Budget, drei Kanäle: TV (50 %), Online (30 %), Print (20 %)
  > Lösung: TV = 5.000 €, Online = 3.000 €, Print = 2.000 €
        ''',
        "story": "Budgetverteilung ist wie Wasser auf einem Feld – wohin du gießt, da wächst Aufmerksamkeit."
    }
]
modules += [
    {
        "title": "16. Customer Journey & Touchpoints",
        "core_insight": "Die Customer Journey beschreibt die Stationen der Kundenreise – vom Erstkontakt bis zur Bindung.",
        "content": '''
• Phasen: Awareness – Consideration – Purchase – Retention – Advocacy
• Touchpoints: Online, Offline, Social Media, Service
• Ziel: positive, konsistente Erlebnisse schaffen
        ''',
        "story": "Die Customer Journey ist wie eine Liebesgeschichte – vom ersten Blick bis zur langjährigen Beziehung."
    },
    {
        "title": "17. Customer Relationship Management (CRM)",
        "core_insight": "CRM stärkt langfristige Kundenbeziehungen durch systematisches Informationsmanagement.",
        "content": '''
• Ziel: Kundenzufriedenheit, -bindung, -wert steigern
• Datenbanken, CRM-Systeme, Personalisierung
• Key Metrics: Customer Lifetime Value (CLV), Churn Rate
        ''',
        "story": "CRM ist wie ein Gedächtnis fürs Marketing – es erinnert sich an Vorlieben, Käufe und Probleme jedes Kunden."
    },
    {
        "title": "18. Online-Marketing (⚠️ Klausurthema)",
        "core_insight": "Online-Marketing nutzt digitale Kanäle zur gezielten Kundenansprache.",
        "content": '''
• Kanäle: Website, SEO, SEA, Social Media, E-Mail
• Tools: Google Ads, Meta Ads, Analytics
• Messgrößen: Click-Through-Rate, Bounce Rate, Conversion Rate
• Klausur (SS25): „Nennen Sie drei Vorteile von Online-Marketing gegenüber klassischer Werbung.“
  > Lösung: Zielgruppengenauigkeit, Messbarkeit, Interaktivität
        ''',
        "story": "Online-Marketing ist wie ein Laser – präzise, messbar und individuell steuerbar."
    },
    {
        "title": "19. Influencer-Marketing & Content-Marketing",
        "core_insight": "Influencer und Inhalte beeinflussen Vertrauen, Reichweite und Kaufverhalten.",
        "content": '''
• Influencer: Reichweite, Authentizität, Zielgruppenfit
• Content-Arten: Blog, Video, Podcast, Meme
• Ziele: Engagement, Viralität, Brand Awareness
        ''',
        "story": "Influencer sind wie moderne Markenbotschafter – sie tragen deine Botschaft direkt in die Lebenswelt der Zielgruppe."
    },
    {
        "title": "20. KPIs & Erfolgsmessung im Digital Marketing",
        "core_insight": "Kennzahlen zeigen, ob digitale Maßnahmen ihre Ziele erreichen.",
        "content": '''
• Metriken: Impressions, Clicks, CTR, Leads, CAC, ROI
• Tools: Google Analytics, Meta Insights, CRM-Auswertung
• ⚠️ Klausur: „Wie berechnet man den ROI einer Kampagne?“
  > Antwort: (Umsatz – Kosten) / Kosten
        ''',
        "story": "KPIs im Digital Marketing sind wie das Cockpit eines Flugzeugs – ohne sie fliegst du blind."
    }
]
modules += [
    {
        "title": "21. Nachhaltigkeit & CSR im Marketing",
        "core_insight": "Nachhaltigkeit ist ein strategischer Erfolgsfaktor im modernen Marketing.",
        "content": '''
• CSR = Corporate Social Responsibility
• Green Marketing, Eco-Label, Nachhaltigkeitskommunikation
• Triple Bottom Line: People, Planet, Profit
• Wirkung auf Markenimage, Kundenbindung, Differenzierung
        ''',
        "story": "Nachhaltigkeit im Marketing ist wie eine Langzeitbeziehung – sie braucht Werte, Konsistenz und Glaubwürdigkeit."
    },
    {
        "title": "22. Ethik & Konsumentenverantwortung",
        "core_insight": "Ethik im Marketing verhindert Manipulation und sichert Vertrauen.",
        "content": '''
• Problemfelder: Greenwashing, versteckte Werbung, Datenmissbrauch
• Prinzipien: Transparenz, Fairness, Wahrheit
• Verantwortung gegenüber Konsumenten, Gesellschaft, Umwelt
        ''',
        "story": "Marketing ohne Ethik ist wie ein schönes Haus ohne Fundament – es sieht gut aus, aber stürzt irgendwann ein."
    },
    {
        "title": "23. Digitalisierung & Automatisierung",
        "core_insight": "Digitale Tools und Automatisierung ermöglichen Effizienz und Personalisierung.",
        "content": '''
• Technologien: CRM, AI, Chatbots, Recommendation Engines
• Marketing Automation: E-Mail, Lead Nurturing, Retargeting
• Datengetriebenes Marketing
• Vorteile: Skalierbarkeit, Relevanz, Zeitersparnis
        ''',
        "story": "Marketing-Automation ist wie ein persönlicher Assistent, der rund um die Uhr mit Kunden spricht – automatisch und präzise."
    },
    {
        "title": "24. Zukunft des Marketings (⚠️ offenes Essaythema)",
        "core_insight": "Das Marketing der Zukunft wird datengetriebener, dialogorientierter und verantwortungsvoller.",
        "content": '''
• Trends: Personalisierung, Voice Search, AI, Nachhaltigkeit
• Human Centric Marketing
• Wertebasiertes Storytelling
• Essay-Klausur (SS25): „Skizzieren Sie Ihre Vision eines ethischen Marketings im Jahr 2030.“
  > Musterelemente: Transparenz, Nachhaltigkeit, Individualisierung, Menschlichkeit trotz Digitalisierung
        ''',
        "story": "Die Zukunft des Marketings ist kein Trend – sie ist ein Versprechen: für mehr Relevanz, mehr Menschlichkeit und mehr Verantwortung."
    }
]
# ----------------------------
# FLASHCARDS & QUIZMODUS
# ----------------------------
flashcards = [
    {"question": "Was ist Marketing im Kern?", "answer": "Konsequente Kundenorientierung – Ausrichtung des gesamten Unternehmens an Kundennutzen."},
    {"question": "⚠️ Klausur: Formel für Preiselastizität?", "answer": "Preiselastizität = (% Mengenänderung) / (% Preisänderung)"},
    {"question": "⚠️ Klausur: Was ist der Tausenderkontaktpreis (TKP)?", "answer": "TKP = (Kosten / Bruttoreichweite) × 1.000"},
    {"question": "Was bedeutet USP?", "answer": "Unique Selling Proposition – Alleinstellungsmerkmal eines Produkts."},
    {"question": "⚠️ Klausur: Welche Werbewirkungstests gibt es?", "answer": "Recalltest, Recognitiontest, Pretest"},
    {"question": "Was misst die Conversion Rate?", "answer": "Anteil der Website-Besucher, die eine gewünschte Aktion ausführen."},
    {"question": "Was versteht man unter CRM?", "answer": "Customer Relationship Management – Pflege langfristiger Kundenbeziehungen durch systematische Daten- und Interaktionsnutzung."},
    {"question": "⚠️ Klausur: Nenne 3 Phasen der Customer Journey.", "answer": "Awareness – Consideration – Purchase"},
    {"question": "Wie lautet die AIDA-Formel?", "answer": "Attention – Interest – Desire – Action"},
    {"question": "⚠️ Klausur: Wofür steht Triple Bottom Line?", "answer": "People – Planet – Profit (Nachhaltigkeitsperspektive)"},
    {"question": "Was ist ein Perceptual Map?", "answer": "Wahrnehmungskarte zur grafischen Darstellung der Markenposition im Markt."},
    {"question": "Was bedeutet Markendehnung?", "answer": "Übertragung einer Marke auf neue Produkte"},
    {"question": "Was ist ein Skimming-Preis?", "answer": "Hoher Einführungspreis zur Abschöpfung von Innovationsrendite"}
]

# ----------------------------
# STREAMLIT-OBERFLÄCHE
# ----------------------------
st.title("📘 Marketing Lern-App")

tab1, tab2, tab3 = st.tabs(["📚 Lernmodule", "🃏 Quizkarten", "💬 Studienpartner"])

# Modulansicht
with tab1:
    for i, m in enumerate(modules):
        with st.expander(f"{m['title']}"):
            st.markdown(f"**🧠 Kernaussage:** {m['core_insight']}")
            st.markdown("**📋 Inhalt:**")
            st.info(m["content"])
            if st.checkbox("Story anzeigen", key=f"story_{i}"):
                st.success(m["story"])

# Quizkarten
with tab2:
    for i, card in enumerate(flashcards):
        st.markdown(f"**Frage {i+1}:** {card['question']}")
        if st.button(f"Antwort zeigen ({i+1})", key=f"btn_{i}"):
            st.success(card["answer"])
        st.markdown("---")

# Studienpartner-Modus
with tab3:
    if "q" not in st.session_state:
        st.session_state.q = random.choice(flashcards)
        st.session_state.waiting = True

    if st.session_state.waiting:
        st.markdown(f"**Frage:** {st.session_state.q['question']}")
        answer = st.text_input("Deine Antwort:", key="antwort_user")
        if st.button("Antwort prüfen"):
            st.success(st.session_state.q["answer"])
            st.session_state.waiting = False
    else:
        if st.button("Nächste Frage"):
            st.session_state.q = random.choice(flashcards)
            st.session_state.waiting = True
# ss25_module.py

ss25_questions = [
    {
        "type": "open",
        "question": "Beschreibe den Begriff 'Elaboration' und skizziere das Elaboration Likelihood Modell.",
        "answer": "Elaboration = Umfang zu dem eine Person die relevanten Informationen sorgfältig kognitiv verarbeitet.\nModellskizze: Zwei Routen – zentrale Route (hohe Elaboration), periphere Route (geringe Elaboration)."
    },
    {
        "type": "open",
        "question": "Was ist ein Buying Center? Nenne drei zentrale Rollen.",
        "answer": "Gedanklicher Zusammenschluss der an einer Kaufentscheidung beteiligten Personen. Rollen: Initiator, Entscheider, Benutzer, Einkäufer, Beeinflusser, Gatekeeper."
    },
    {
        "type": "open",
        "question": "Beschreibe die Schritte der Strategieentwicklung im Marketing anhand eines Beispiels.",
        "answer": "1. Analyse, 2. Alternativen, 3. Bewertung, 4. Auswahl, 5. Umsetzung. Beispiel: Fahrradhersteller – neue Modelle zur Diversifikation prüfen, mit Zielkriterien bewerten, umsetzen und kontrollieren."
    },
    {
        "type": "open",
        "question": "Trage die vier zentralen Arten digitaler Plattformen in ein Koordinatensystem ein und benenne die Achsen.",
        "answer": "Achsen: Nutzeranzahl (einseitig/zweiseitig) und Beitrag zur Wertschöpfung. Plattformtypen: Forum Maker, Matchmaker, Enabler, Hub."
    },
    {
        "type": "open",
        "question": "Berechne die Preiselastizität bei p = 20 € für x(p) = 1000 - 40p. Interpretiere das Ergebnis.",
        "answer": "Elastizität = (-40) * 20 / (1000 - 40*20) = -800 / 200 = -4. Interpretation: Absatz sinkt um 4% bei 1% Preissteigerung – überproportional elastisch."
    },
    {
        "type": "open",
        "question": "Berechne den gewinnmaximalen Preis für x(p) = 260.000 - 200.000p, K(x) = 520.000 + 0,25x.",
        "answer": "G = -200.000p² + 310.000p - 585.000 → G'(p) = -400.000p + 310.000 = 0 → p = 0,78 €"
    },
    {
        "type": "open",
        "question": "Was ist die Nettoreichweite? Und worin liegt der Unterschied zur Bruttoreichweite?",
        "answer": "Nettoreichweite = Anzahl erreichter Personen. Unterschied: Brutto zählt Kontakte (auch Mehrfachkontakte), Netto zählt individuelle Personen."
    },
    {
        "type": "open",
        "question": "Berechne die Bruttoreichweite anhand gegebener Mediadaten.",
        "answer": "4•5,1 Mio + 3•3,6 Mio + 6•2,4 Mio = 45,6 Mio Kontakte"
    },
    {
        "type": "open",
        "question": "Nenne zwei Kriterien zur Vertriebswegeentscheidung und zwei proaktive Kriterien für Key Account Auswahl.",
        "answer": "Vertriebsweg: Produktbezogen, Endabnehmerbezogen. KAM: Wirtschaftliches Potenzial, Know-How des Kunden."
    },
    {
        "type": "open",
        "question": "Welche Datenquellen/Methoden nutzt man für Zufriedenheit und Layout-Tests? Wie ist die Schätzfunktion zu beurteilen?",
        "answer": "Zufriedenheit: Online-Befragung (Primärdaten). Layout-Test: A/B-Test (Primärdaten). Schätzfunktion: geringe Güte – Punkte liegen weit entfernt von Regressionsgerade."
    }
]

ss25_mc_questions = [
    {
        "question": "Welche Umfeldfaktoren des Konsumentenverhaltens kennen Sie?",
        "options": ["Physisches Umfeld", "Soziales Umfeld", "Psychisches Umfeld", "Kulturelles Umfeld"],
        "correct_answers": [0,1,3]
    },
    {
        "question": "Welche Aussagen zu Emotion und Motivation sind korrekt?",
        "options": ["Maslow = Emotionstheorie", "Emotion = körperliche Erregung", "Motivation = Denkhaltung", "Motivation = Zielorientierung"],
        "correct_answers": [1,3]
    },
    {
        "question": "Warum ist High- vs. Low-Involvement wichtig?",
        "options": ["Informationsbedarf", "Zufriedenheit", "Preiselastizität", "Emotionale Werbung"],
        "correct_answers": [0]
    },
    # … (weitere 12 MC-Fragen analog)
]
import streamlit as st

st.set_page_config(page_title="SS25 Klausurquiz", layout="centered")

st.title("📝 SS25 Klausurquiz – Marketing")

# Offene Fragen
st.header("📘 Offene Fragen")
open_questions = [
    {
        "question": "Beschreibe den Begriff 'Elaboration' und skizziere das Elaboration Likelihood Modell.",
        "answer": "Elaboration = Umfang der kognitiven Verarbeitung.\nELM = zentrale vs. periphere Route – abhängig vom Involvement."
    },
    {
        "question": "Was ist ein Buying Center? Nenne drei zentrale Rollen.",
        "answer": "Initiator, Entscheider, Benutzer, Einkäufer, Beeinflusser, Gatekeeper."
    },
    {
        "question": "Berechne die Preiselastizität bei p = 20 € für x(p) = 1000 - 40p.",
        "answer": "Elastizität = -800 / 200 = -4 (hoch elastisch)"
    },
    # … (weitere Fragen ergänzbar)
]

for q in open_questions:
    with st.expander("❓ " + q["question"]):
        if st.button("Antwort anzeigen", key=q["question"]):
            st.markdown("✅ **Antwort:**\n" + q["answer"])

# Multiple-Choice Fragen
st.header("🧠 Multiple-Choice Fragen")
mc_questions = [
    {
        "question": "Welche Umfeldfaktoren des Konsumentenverhaltens kennen Sie?",
        "options": ["Physisches Umfeld", "Soziales Umfeld", "Psychisches Umfeld", "Kulturelles Umfeld"],
        "correct": [0,1,3]
    },
    {
        "question": "Welche Aussagen zu Emotion und Motivation sind korrekt?",
        "options": ["Maslow = Emotionstheorie", "Emotion = körperliche Erregung", "Motivation = Denkhaltung", "Motivation = Zielorientierung"],
        "correct": [1,3]
    }
    # … weitere MC-Fragen einfügbar
]

for idx, q in enumerate(mc_questions):
    st.subheader(f"Frage {idx+1}: {q['question']}")
    selections = st.multiselect("Wähle aus:", q["options"], key=f"mc_{idx}")
    if st.button("Antwort prüfen", key=f"check_{idx}"):
        if set(selections) == set([q["options"][i] for i in q["correct"]]):
            st.success("✅ Richtig!")
        else:
            st.error("❌ Leider falsch. Richtige Antworten:\n" + ", ".join([q["options"][i] for i in q["correct"]]))
            # app_ss23_quiz.py

import streamlit as st

st.set_page_config(page_title="SS23 Klausurquiz", layout="centered")
st.title("📝 SS23 Klausurquiz – Marketing")

st.header("📘 Offene Fragen")

open_questions = [
    {
        "question": "Welche Segmentierungskriterien würden Sie für einen Bio-Lebensmittelanbieter anwenden?",
        "answer": "Psychografisch: z. B. Gesundheitsbewusstsein\nVerhaltensorientiert: z. B. Kaufmotive\nDemografisch: z. B. Alter, Bildung"
    },
    {
        "question": "Welche Preisstrategie würden Sie für ein neues innovatives Produkt wählen?",
        "answer": "Skimming-Strategie – hohe Zahlungsbereitschaft bei Innovatoren, schnelles Abschöpfen"
    },
    {
        "question": "Nennen Sie zwei Maßnahmen im Rahmen eines Relaunchs.",
        "answer": "Überarbeitung der Verpackung, neue Kommunikationsstrategie, Produktverbesserung"
    },
    {
        "question": "Welche Kommunikationsinstrumente sind für ein erklärungsbedürftiges B2B-Produkt geeignet?",
        "answer": "Persönlicher Verkauf, Technische PR, Messeauftritt"
    }
]

for q in open_questions:
    with st.expander("❓ " + q["question"]):
        if st.button("Antwort anzeigen", key=q["question"]):
            st.markdown("✅ **Antwort:**\n" + q["answer"])
            # app_sose23_quiz.py

import streamlit as st

st.set_page_config(page_title="SoSe23 Klausurquiz", layout="centered")
st.title("📝 SoSe23 Probeklausur – Marketing")

st.header("📘 Offene Fragen")

open_questions = [
    {
        "question": "Nennen Sie drei Ziele der Kommunikationspolitik.",
        "answer": "Bekanntheit steigern, Einstellung verbessern, Kaufverhalten beeinflussen"
    },
    {
        "question": "Beschreiben Sie das AIDA-Modell anhand eines Beispiels.",
        "answer": "A = Aufmerksamkeit (Eyecatcher)\nI = Interesse (Produktnutzen)\nD = Wunsch (Besitzwille)\nA = Handlung (Kauf)"
    },
    {
        "question": "Berechnen Sie die Preiselastizität bei einer Preisänderung von 10 % und einer Mengenänderung von +15 %.",
        "answer": "E = 15 % / -10 % = -1,5 (elastisch)"
    },
    {
        "question": "Berechnen Sie den TKP bei 2.000 € Kosten und 50.000 Reichweite.",
        "answer": "TKP = (2000 / 50000) × 1000 = 40 €"
    },
    {
        "question": "Nennen Sie zwei Verfahren zur Messung von Werbewirkung.",
        "answer": "Recall-Test, Recognition-Test"
    },
    {
        "question": "Nennen Sie drei Vorteile von Online-Marketing gegenüber klassischer Werbung.",
        "answer": "Zielgruppengenauigkeit, Interaktivität, Messbarkeit"
    }
]

for q in open_questions:
    with st.expander("❓ " + q["question"]):
        if st.button("Antwort anzeigen", key=q["question"]):
            st.markdown("✅ **Antwort:**\n" + q["answer"])