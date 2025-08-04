
import streamlit as st
import random

st.set_page_config(page_title="📘 Marketing Lern-App", layout="wide")

modules = [
    {
        "title": "1. Grundlagen des Marketings",
        "core_insight": "Marketing ist die konsequente Ausrichtung aller Unternehmensaktivitäten auf den Kunden.",
        "content": "Marketing umfasst Planung, Koordination und Kontrolle sämtlicher auf aktuelle und potenzielle Märkte ausgerichteter Unternehmensaktivitäten.",
        "story": "Stell dir Marketing wie einen Radar vor – es scannt permanent, was der Kunde braucht, und steuert alle Unternehmensaktionen darauf aus."
    },
    {
        "title": "2. Preiselastizität (⚠️ Klausur)",
        "core_insight": "Preiselastizität misst, wie stark Kunden auf Preisänderungen reagieren.",
        "content": "Formel: Preiselastizität = (% Mengenänderung) / (% Preisänderung).",
        "story": "Wenn der Preis fällt und viel mehr Leute kaufen, ist die Nachfrage elastisch – wie ein Gummiband, das sich leicht dehnen lässt."
    }
]

flashcards = [
    {"question": "Was ist das Ziel des Marketings?", "answer": "Kundenorientierung und langfristiger Unternehmenserfolg durch Bedürfnisbefriedigung."},
    {"question": "Formel für Preiselastizität?", "answer": "Preiselastizität = Prozentuale Mengenänderung / Prozentuale Preisänderung"},
    {"question": "⚠️ Klausurfrage: Was misst der TKP?", "answer": "Kosten pro 1.000 erreichte Kontakte"},
    {"question": "Was sind die 4 P des Marketing-Mix?", "answer": "Product, Price, Place, Promotion"}
]

st.title("📘 Marketing Lern-App")
tab1, tab2, tab3 = st.tabs(["📚 Lernmodule", "🃏 Quizkarten", "💬 Studienpartner"])

with tab1:
    for i, m in enumerate(modules):
        with st.expander(f"{m['title']}"):
            st.markdown(f"**Kernaussage:** {m['core_insight']}")
            st.markdown("**Inhalt:**")
            st.info(m["content"])
            if st.checkbox("Story anzeigen", key=f"story_{i}"):
                st.success(m["story"])

with tab2:
    for i, card in enumerate(flashcards):
        st.markdown(f"**Frage {i+1}:** {card['question']}")
        if st.button(f"Antwort zeigen ({i+1})", key=f"btn_{i}"):
            st.success(card["answer"])
        st.markdown("---")

with tab3:
    if "q" not in st.session_state:
        st.session_state.q = random.choice(flashcards)
        st.session_state.waiting = True

    if st.session_state.waiting:
        st.markdown(f"**Frage:** {st.session_state.q['question']}")
        answer = st.text_input("Deine Antwort:", key="user_input")
        if st.button("Antwort prüfen"):
            st.success(st.session_state.q["answer"])
            st.session_state.waiting = False
    else:
        if st.button("Nächste Frage"):
            st.session_state.q = random.choice(flashcards)
            st.session_state.waiting = True
