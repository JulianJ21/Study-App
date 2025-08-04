
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Marketing Lern-App", layout="wide")

# ------------------------
# DATA SETUP
# ------------------------

# Each module will be a dict with:
# title, content (summary), core_insight, story_explanation
modules = [
    {
        "title": "1. Grundlagen des Marketings",
        "core_insight": "Marketing ist der zentrale Treiber der Kundenorientierung.",
        "content": """Marketing ist das Herzstück eines Unternehmens. Es richtet alle Aktivitäten auf die Bedürfnisse und Wünsche der Kunden aus. Dabei geht es nicht nur um Werbung oder Verkauf, sondern um die ganzheitliche Steuerung des Marktgeschehens.""",
        "story": "Stell dir Marketing wie das Navigationssystem eines Unternehmens vor: Es zeigt an, wo der Kunde steht, wohin er möchte und wie man ihn am besten begleitet – mit Produkt, Preis, Kommunikation und Verfügbarkeit."
    },
    {
        "title": "2. Marketingziele und Strategien",
        "core_insight": "Ziele geben die Richtung vor, Strategien zeigen den Weg.",
        "content": """Marketingziele können ökonomisch (z. B. Umsatz, Gewinn) oder psychologisch (z. B. Bekanntheit, Vertrauen) sein. Strategien legen fest, wie diese Ziele erreicht werden – etwa durch Differenzierung, Kostenführerschaft oder Marktdurchdringung.""",
        "story": "Man kann sich Marketingziele wie einen Berg vorstellen: Du willst auf den Gipfel (Umsatz, Vertrauen, Bekanntheit). Die Strategie ist der Weg – steil, flach, direkt oder über Umwege. Hauptsache: du kommst an."
    }
    # → Weitere Module können hier ergänzt werden
]

flashcards = [
    {"question": "Was ist das Ziel von Marketing?", "answer": "Kundenbedürfnisse erkennen, befriedigen und dadurch langfristige Wettbewerbsvorteile schaffen."},
    {"question": "Nenne die vier klassischen P’s des Marketing-Mix.", "answer": "Product, Price, Place, Promotion"},
    {"question": "Was bedeutet Preiselastizität?", "answer": "Sie misst, wie stark sich die Nachfrage bei Preisänderungen verändert."},
    {"question": "Wie lautet die Formel für den Tausenderkontaktpreis (TKP)?", "answer": "TKP = (Kosten der Schaltung / Bruttoreichweite) × 1.000"},
    {"question": "⚠️ Klausurfrage: Was sind typische Merkmale von B2B-Märkten?", "answer": "Wenige Kunden, hoher Wert je Auftrag, Buying Center, langfristige Beziehungen"}
    # Weitere Karten möglich
]

# ------------------------
# MODULAR LEARNING VIEW
# ------------------------

st.title("📘 Marketing Lern-App")

tab1, tab2, tab3 = st.tabs(["📚 Lernmodule", "🃏 Quizkarten", "💬 Studienpartner"])

with tab1:
    st.header("📚 Modulweises Lernen")
    for i, module in enumerate(modules):
        with st.expander(f"📌 {module['title']}"):
            st.markdown(f"**Kernaussage:** {module['core_insight']}")
            st.markdown("**Zusammenfassung:**")
            st.info(module["content"])
            if st.checkbox(f"🧠 Story-Ansicht anzeigen (Modul {i+1})", key=f"story_{i}"):
                st.success(module["story"])

# ------------------------
# FLASHCARD QUIZ MODE
# ------------------------

with tab2:
    st.header("🃏 Quizkarten üben")
    for i, card in enumerate(flashcards):
        st.markdown(f"**Frage {i+1}:** {card['question']}")
        if st.button(f"Antwort anzeigen ({i+1})", key=f"show_{i}"):
            st.success(card["answer"])
        st.markdown("---")

# ------------------------
# SIMULATED STUDY PARTNER
# ------------------------

with tab3:
    st.header("💬 Simulierter Studienpartner")
    st.write("Ich stelle dir Fragen – du antwortest. Dann bekommst du Feedback.")

    import random
    if "current_question" not in st.session_state:
        st.session_state.current_question = random.choice(flashcards)
        st.session_state.awaiting_answer = True

    if st.session_state.awaiting_answer:
        st.markdown(f"**Frage:** {st.session_state.current_question['question']}")
        user_input = st.text_input("Deine Antwort:", key="user_answer_input")
        if st.button("Antwort abgeben"):
            st.markdown("**Musterantwort:**")
            st.success(st.session_state.current_question["answer"])
            st.session_state.awaiting_answer = False
    else:
        if st.button("Nächste Frage"):
            st.session_state.current_question = random.choice(flashcards)
            st.session_state.awaiting_answer = True

# ------------------------
# FOOTER
# ------------------------

st.markdown("---")
st.caption("📦 Entwickelt für das Offline-Lernen mit Streamlit. Alle Inhalte basieren auf deiner Marketing-Zusammenfassung.")

