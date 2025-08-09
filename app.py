# app.py
# PLB Exam Memorizer — Master Sheet + Deltas
# Streamlit app for focused study on Produktion, Logistik, Beschaffung
# by GPT-5 Thinking

import math
import random
from dataclasses import dataclass
from typing import List, Dict, Tuple
import streamlit as st

# -------------------
# ---- THEME / UI ----
# -------------------
st.set_page_config(
    page_title="PLB Exam Memorizer",
    page_icon="🧠",
    layout="wide"
)

PRIMARY = "#3a86ff"
ACCENT = "#ff006e"
BG = "#0f1220"
CARD = "#171a2b"
TEXT = "#e6eaf2"
MUTED = "#b3b9c9"
GOOD = "#31c48d"
WARN = "#f59e0b"
BAD = "#ef4444"

CUSTOM_CSS = f"""
<style>
    .stApp {{
        background: radial-gradient(80rem 60rem at 90% -20%, #1b1f36 10%, {BG} 60%);
        color: {TEXT};
        font-family: Inter, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
    }}
    .headline {{
        font-size: 2.2rem; font-weight: 800; letter-spacing: -0.02em; 
        margin: .2rem 0 1.2rem 0; color: {TEXT};
    }}
    .subtle {{
        color: {MUTED}; font-size: 0.95rem;
    }}
    .pill {{
        display: inline-block; padding: .25rem .6rem; border-radius: 999px; 
        background: linear-gradient(90deg, {PRIMARY}, {ACCENT});
        color: white; font-weight: 700; font-size: .8rem; letter-spacing: .02em;
        margin-right:.5rem;
    }}
    .card {{
        background: {CARD}; border: 1px solid #1e2240; border-radius: 16px; padding: 1.1rem 1.2rem; 
        box-shadow: 0 10px 30px rgba(0,0,0,.25);
        margin-bottom: .75rem;
    }}
    .btn-row button[kind="primary"] {{
        background: linear-gradient(90deg, {PRIMARY}, {ACCENT}) !important;
        border: none !important;
        color: white !important;
        font-weight: 700 !important;
    }}
    .good {{ color: {GOOD}; font-weight: 700; }}
    .bad {{ color: {BAD}; font-weight: 700; }}
    .warn {{ color: {WARN}; font-weight: 700; }}
    .metric {{
        display:flex; align-items:center; gap:.6rem; 
        background:#12162a; border:1px solid #222748; padding:.6rem .8rem; border-radius:12px;
        width: fit-content;
    }}
    .metric .num {{ font-size:1.2rem; font-weight:800; }}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------------------------------
# ---- CONTENT (MASTER + DELTA) ----
# ---------------------------------

MASTER = {
    "Exam Setup": [
        "Termin: Fr, 15.08.2025, 08:00–09:30; 90 Punkte Gesamt.",
        "Produktion+Beschaffung: 60 P. (davon Produktion ca. 50 P., Beschaffung ca. 10 P.), Logistik: 30 P.",
        "Fragetypen: Offene Fragen (~40 P.), Richtig/Falsch (~20 P.).",
        "Schwerpunkte offen: Minimalkostenkombination (MKK), Produktionsprogramm mit mehreren Engpässen (LP), Kapazitäten (Anlagen-, Personal-, effektiv nutzbar).",
        "Ausgrenzungen: Teil 1 (18–30; 56–58), Teil 4 (128; 157–160), Teil 5 (172–185), Teil 6 (205), Übung 1 (8–11)."
    ],
    "Produktion – MKK (Substitution & Leontief)": [
        "Ziel: vorgegebene Ausbringung x zu minimalen Kosten.",
        "Isokosten: K = w1*r1 + w2*r2. Tangentialbed.: MRTS = (∂x/∂r1)/(∂x/∂r2) = w1/w2.",
        "Leontief/limitational: feste Einsatzverhältnisse → Eckenlösung über Produktionskoeffizienten."
    ],
    "Produktion – Programmplanung": [
        "Kein Engpass: Alle Produkte mit DB>0 bis Absatzgrenze.",
        "Ein Engpass: relative DB = (p − kv) / (ZE je ME im Engpass); nach rel. DB sortieren, Restkapazität fortschreiben.",
        "Mehrere Engpässe: lineare Programmierung. Zielfunktion DB-Max, Nebenbedingungen (Kapazität/Absatz/Beschaffung)."
    ],
    "Produktion – EF vs FB": [
        "Mit Engpass kann Fremdbezug Kapazität sparen. Erst FB-Limits ziehen, dann Rest via rel. DB.",
        "Ohne Engpass: EF wenn DB_EF positiv; FB nur vorteilhaft, wenn DB_FB > DB_EF oder Kapazitäts-/Risikoargumente."
    ],
    "Kapazitäten": [
        "Anlagen-, Personal-, effektiv nutzbare Kapazität (EK) unterscheiden.",
        "Kurzfristige Anpassung: kombinierte Anpassung (Mengen, Zeiten, Bestände)."
    ],
    "Beschaffung – Definition & Abgrenzungen": [
        "Beschaffung (i.w.S.): Management externer Ressourcen zur Verfügbarkeit aller Güter/DL/Fähigkeiten zu günstigen Bedingungen.",
        "Abgrenzung: Einkauf (operativ vs. gestaltend), Materialwirtschaft (objektbezogen enger), Logistik (räumlich/zeitlich), SCM (integrierte Ketten, SCOR: Plan/Source/Make/Deliver/Return)."
    ],
    "Logistik & SCM – Globalisierung": [
        "Dornier’s Four Forces: Markt-, Kosten-, Technologie-, politische/makroökonomische Kräfte.",
        "Onshoring (Produktion im Absatzmarkt), Offshoring (Verlagerung ins Ausland), Outsourcing (Leistung an Dritte)."
    ],
    "Logistik & SCM – Bullwhip & Netzwerke": [
        "Bullwhip: Ursachen (Signalverarb., Bündelung, Preisschwankungen, Engpasspoker), Wirkungen (Kosten/Bestände), Gegenmaßnahmen (Transparenz, zentrale Planung, kleinere Bestellungen, abgestimmte Aktionen).",
        "Netzwerke: Direkt, Milkrun, Hub-and-Spoke, DC/Cross-Docking; Trade-offs Transport/Lager/Service.",
        "Bestandszentralisierung: Risk-Pooling senkt Gesamtbestand.",
        "Postponement & Entkopplungspunkt: Lean bis DC-Point, danach agil; Assembly/Packaging/Labeling/Geo."
    ]
}

DELTAS = {
    "Produktion – Typ A Details": [
        "Ceteris-paribus: genau 1 variabler Input r_j; Bedingungen: einstufig, Teilbarkeit, c konstant, periphere Substitution, konstante Qualität, unveränderte Technik.",
        "Durchschnittsertrag = Steigung des Fahrstrahls; Grenzprodukt = Steigung der Gesamtertragskurve; typische 4 Phasen I–IV."
    ],
    "Relativer DB – Formelpräzision": [
        "rel. DB = (p − kv) / Produktionskoeffizient (ZE/ME im Engpass). Reihenfolge strikt danach.",
        "Restkapazitäts-Nebenrechnung sauber führen; letzte Position ggf. anteilig."
    ],
    "LP – Hinweis": [
        "Bei mehreren Engpässen ist rel. DB NICHT zulässig → LP mit Zielfunktion + Kapazitäts-, Beschaffungs-, Absatzgrenzen."
    ],
    "Kapazitätsformeln & Fallen": [
        "Faust: PK = PB·α·AZ·β; AK = M·μ·BZ; EK aus Minimum von bereichsweisen Engpässen ableiten.",
        "Kurzfristige EK-Erweiterung ≠ Outsourcing (dauerhaft) — typische R/F-Falle."
    ],
    "Beschaffung – Zeitstrahl & Herausforderungen": [
        "Entwicklungsstufen: Versorgung um jeden Preis → Beschaffungsmarketing → Procurement 4.0/KI.",
        "Herausforderungen: Inflation/Rohstoffe/Energie, Resilienz, Nachhaltigkeit, Digitalisierung, Politik/Handel, Recht (z.B. Lieferkettengesetz)."
    ],
    "Übungen – FB/EF Stolpersteine": [
        "Bei limitiertem Fremdbezug zuerst FB-Teilmengen festziehen, dann EF nach rel. DB; Rundungsvorgaben beachten.",
        "Explizite Reihenfolgen aus Beispielaufgaben korrekt wiedergeben (inkl. Restkapazität & Gesamt-DB aus FB+EF)."
    ]
}

# True/False bank (mix of conceptual traps)
TF_BANK = [
    ("Bei mehreren Engpässen lässt sich das Produktionsprogramm mit relativen DBs optimal bestimmen.", False, "Mehrere Engpässe ⇒ LP, rel. DB reicht nicht."),
    ("Beim Leontief-Fall ist die Minimalkostenkombination immer eine Eckenlösung.", True, "Limitational: feste Verhältnisse ⇒ Ecke."),
    ("Outsourcing ist eine kurzfristige Maßnahme zur temporären EK-Erweiterung.", False, "Outsourcing ist i.d.R. dauerhaft/strukturell."),
    ("Bestandszentralisierung senkt bei gleichem Servicegrad typischerweise den Sicherheitsbestand.", True, "Risk-Pooling-Effekt."),
    ("Bullwhip-Effekt entsteht u.a. durch Auftragsbündelung und Preisaktionen.", True, "Klassische Ursachen."),
    ("SCOR-Prozesse lauten: Plan, Source, Make, Deliver, Return.", True, "Standardliste."),
    ("Onshoring bedeutet Auslagerung an einen ausländischen Drittanbieter.", False, "Onshoring = Produktion im Absatzmarkt."),
    ("Relativer DB ist (p−kv)·(ZE/ME).", False, "Es ist (p−kv) / (ZE/ME)."),
    ("Bei einem Engpass wird stets das Produkt mit dem höchsten absoluten DB priorisiert.", False, "Kriterium ist relativer DB."),
    ("Postponement verschiebt kundenspezifische Schritte nach hinten und reduziert Varianz-/Bestandsrisiken.", True, "Zielgenaue Anpassung spät.")
]

# Flashcards (front/back)
FLASHCARDS = [
    ("Tangentialbedingung MKK", "MRTS = (∂x/∂r1)/(∂x/∂r2) = w1/w2; dann in Produktionsfunktion einsetzen."),
    ("Relativer Deckungsbeitrag", "rel. DB = (p − kv) / (ZE je ME im Engpass) — danach priorisieren."),
    ("LP – Basisform", "max Σ(p_i−kv_i)x_i  s.t.  Ax ≤ b; 0 ≤ x_i ≤ Absatz_i."),
    ("SCOR", "Plan / Source / Make / Deliver / Return."),
    ("Bullwhip – 4 Ursachen", "Nachfragesignale, Auftragsbündelung, Preisschwankungen, Engpasspoker."),
    ("Bestandszentralisierung", "Risk-Pooling senkt Gesamt- und Sicherheitsbestände bei gleichem Servicegrad."),
    ("Postponement", "Assembly/Packaging/Labeling/Geographisch; Lean→DC-Point→Agil."),
    ("Kapazitäten", "PK=PB·α·AZ·β; AK=M·μ·BZ; EK = min-gebundene wirksame Kapazität.")
]

# Small calc drills
@dataclass
class RelDBInstance:
    name: str
    p: float
    kv: float
    ze_per_me: float

RELDB_SAMPLE = [
    RelDBInstance("P1", 120, 80, 4),
    RelDBInstance("P2", 180, 135, 3),
    RelDBInstance("P3", 80, 50, 1),
    RelDBInstance("P4", 140, 90, 2),
]

LP_SAMPLE = {
    "desc": "Zwei Produkte A,B; DB_A=100, DB_B=50; M1: 5A+5B ≤ 400; M2: 1A+4B ≤ 300; Absatz: 30≤A≤90, 10≤B≤50.",
    "opt": {"A": 70, "B": 10, "DB": 7500}
}

# -------------------------
# ---- STATE & HELPERS ----
# -------------------------
if "card_idx" not in st.session_state:
    st.session_state.card_idx = 0
if "known_cards" not in st.session_state:
    st.session_state.known_cards = set()
if "tf_idx" not in st.session_state:
    st.session_state.tf_idx = 0
if "tf_correct" not in st.session_state:
    st.session_state.tf_correct = 0
if "tf_total" not in st.session_state:
    st.session_state.tf_total = 0
if "rdb_attempts" not in st.session_state:
    st.session_state.rdb_attempts = 0
if "rdb_correct" not in st.session_state:
    st.session_state.rdb_correct = 0

def card_progress() -> Tuple[int, int]:
    return (len(st.session_state.known_cards), len(FLASHCARDS))

def next_card():
    st.session_state.card_idx = (st.session_state.card_idx + 1) % len(FLASHCARDS)

def prev_card():
    st.session_state.card_idx = (st.session_state.card_idx - 1) % len(FLASHCARDS)

def mark_known():
    st.session_state.known_cards.add(st.session_state.card_idx)
    next_card()

def tf_progress() -> Tuple[int, int]:
    return (st.session_state.tf_correct, st.session_state.tf_total)

def grade_color(p):
    if p >= 0.85: return GOOD
    if p >= 0.7: return WARN
    return BAD

# -------------------
# ---- SIDEBAR UI ----
# -------------------
st.sidebar.markdown(f"<div class='pill'>PLB Memorizer</div>", unsafe_allow_html=True)
st.sidebar.title("🧭 Navigation")
mode = st.sidebar.radio(
    label="Mode auswählen",
    options=["📖 Read", "🗂️ Deltas", "🧩 Flashcards", "✅ True/False", "🧮 Calc Trainer", "📊 Progress"],
    index=0
)

with st.sidebar.expander("🎨 View Options"):
    compact = st.checkbox("Compact cards", value=False)
    if compact:
        st.markdown("<style>.card{padding:.8rem 1rem;}.headline{margin-bottom:.8rem;}</style>", unsafe_allow_html=True)

# ----------------------
# ---- MODE: READ  -----
# ----------------------
if mode == "📖 Read":
    st.markdown("<div class='headline'>Master Sheet</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtle'>Everything you need at a glance. Use this as your reference before drilling.</div>", unsafe_allow_html=True)
    cols = st.columns(2)
    left_keys = list(MASTER.keys())[:len(MASTER)//2+1]
    right_keys = list(MASTER.keys())[len(MASTER)//2+1:]

    with cols[0]:
        for k in left_keys:
            with st.container():
                st.markdown(f"<div class='card'><b>{k}</b></div>", unsafe_allow_html=True)
                for item in MASTER[k]:
                    st.markdown(f"<div class='card subtle'>• {item}</div>", unsafe_allow_html=True)

    with cols[1]:
        for k in right_keys:
            with st.container():
                st.markdown(f"<div class='card'><b>{k}</b></div>", unsafe_allow_html=True)
                for item in MASTER[k]:
                    st.markdown(f"<div class='card subtle'>• {item}</div>", unsafe_allow_html=True)

# -----------------------
# ---- MODE: DELTAS -----
# -----------------------
elif mode == "🗂️ Deltas":
    st.markdown("<div class='headline'>Delta List (Paranoid Sweep)</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtle'>Extra items surfaced during the verification pass. Treat these as must-memorize add-ons.</div>", unsafe_allow_html=True)
    for k, items in DELTAS.items():
        st.markdown(f"<div class='card'><b>{k}</b></div>", unsafe_allow_html=True)
        for it in items:
            st.markdown(f"<div class='card subtle'>• {it}</div>", unsafe_allow_html=True)

# --------------------------
# ---- MODE: FLASHCARDS ----
# --------------------------
elif mode == "🧩 Flashcards":
    st.markdown("<div class='headline'>Flashcards (Leitner-lite)</div>", unsafe_allow_html=True)
    known, total = card_progress()
    pct = known/total if total else 0.0
    st.markdown(
        f"<div class='metric'><span class='num'>{known}/{total}</span> mastered &nbsp; "
        f"<span style='color:{grade_color(pct)}; font-weight:800'>{int(pct*100)}%</span></div>",
        unsafe_allow_html=True
    )
    idx = st.session_state.card_idx
    front, back = FLASHCARDS[idx]

    st.markdown(f"<div class='card'><b>Q:</b> {front}</div>", unsafe_allow_html=True)
    if st.button("Show Answer", type="primary"):
        st.session_state["show_answer"] = True
    if st.session_state.get("show_answer", False):
        st.markdown(f"<div class='card' style='border-left:4px solid {PRIMARY}'><b>A:</b> {back}</div>", unsafe_allow_html=True)

    colA, colB, colC, colD = st.columns(4)
    with colA:
        if st.button("⏮️ Prev"):
            st.session_state["show_answer"] = False
            prev_card()
    with colB:
        if st.button("🔀 Shuffle"):
            random.shuffle(FLASHCARDS)
            st.session_state.card_idx = 0
            st.session_state.known_cards = set()
            st.session_state["show_answer"] = False
    with colC:
        if st.button("⏭️ Next"):
            st.session_state["show_answer"] = False
            next_card()
    with colD:
        if st.button("✅ I knew this"):
            mark_known()
            st.session_state["show_answer"] = False

# ---------------------------
# ---- MODE: TRUE/FALSE -----
# ---------------------------
elif mode == "✅ True/False":
    st.markdown("<div class='headline'>True / False Drills</div>", unsafe_allow_html=True)
    i = st.session_state.tf_idx % len(TF_BANK)
    stmt, truth, expl = TF_BANK[i]

    st.markdown(f"<div class='card'><b>Statement:</b> {stmt}</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,1,2])
    def answer(choice: bool):
        st.session_state.tf_total += 1
        correct = (choice == truth)
        if correct:
            st.session_state.tf_correct += 1
            st.success("Correct ✅")
        else:
            st.error("Not quite ❌")
        st.info(expl)
        st.session_state.tf_idx += 1

    with col1:
        if st.button("True", use_container_width=True):
            answer(True)
    with col2:
        if st.button("False", use_container_width=True):
            answer(False)
    with col3:
        c, t = tf_progress()
        p = c/t if t else 0
        st.markdown(
            f"<div class='metric'><span class='num'>{c}/{t}</span> correct &nbsp; "
            f"<span style='color:{grade_color(p)}; font-weight:800'>{int(p*100)}%</span></div>",
            unsafe_allow_html=True
        )

# ----------------------------
# ---- MODE: CALC TRAINER ----
# ----------------------------
elif mode == "🧮 Calc Trainer":
    st.markdown("<div class='headline'>Calculation Trainer</div>", unsafe_allow_html=True)
    tabs = st.tabs(["Relative DB (1 Engpass)", "LP Intuition"])

    with tabs[0]:
        st.markdown("<div class='subtle'>Compute relative DB for each product, rank, and identify the top priority.</div>", unsafe_allow_html=True)
        cols = st.columns(4)
        for k, inst in enumerate(RELDB_SAMPLE):
            with cols[k % 4]:
                st.markdown(f"<div class='card'><b>{inst.name}</b><br>"
                            f"p={inst.p}, kv={inst.kv}, ZE/ME={inst.ze_per_me}</div>", unsafe_allow_html=True)
        st.latex(r"\text{rel. DB}_i=\frac{p_i-k_{v,i}}{\text{ZE/ME}_i}")
        user_rank = st.text_input("Enter product names in descending order of rel. DB (comma-separated), e.g. P3,P4,P2,P1")
        if st.button("Check ranking", type="primary"):
            st.session_state.rdb_attempts += 1
            # Compute true ranking
            calc = [(inst.name, (inst.p - inst.kv)/inst.ze_per_me) for inst in RELDB_SAMPLE]
            calc.sort(key=lambda x: x[1], reverse=True)
            true_order = [n for n,_ in calc]
            try:
                user_order = [s.strip() for s in user_rank.split(",") if s.strip()]
                correct = (user_order == true_order)
                if correct:
                    st.success(f"Perfect! ✅ True order: {true_order}")
                    st.session_state.rdb_correct += 1
                else:
                    st.warning(f"Close. True order: {true_order}")
            except Exception as e:
                st.error("Could not parse your input.")
        atts, corr = st.session_state.rdb_attempts, st.session_state.rdb_correct
        p = corr/atts if atts else 0
        st.markdown(
            f"<div class='metric'><span class='num'>{corr}/{atts}</span> correct &nbsp; "
            f"<span style='color:{grade_color(p)}; font-weight:800'>{int(p*100)}%</span></div>",
            unsafe_allow_html=True
        )

    with tabs[1]:
        st.markdown("<div class='subtle'>Use constraints to reason about the optimal corner. The known optimum is provided so you can debug your logic.</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card'><b>Problem:</b> {LP_SAMPLE['desc']}</div>", unsafe_allow_html=True)
        st.latex(r"\text{Maximize } DB=100A+50B")
        st.latex(r"\text{s.t. } 5A+5B\le 400,\; A+4B\le 300,\; 30\le A\le 90,\; 10\le B\le 50")
        a = st.number_input("Your A", min_value=0, max_value=999, value=70)
        b = st.number_input("Your B", min_value=0, max_value=999, value=10)
        if st.button("Check feasibility & DB"):
            feas1 = 5*a + 5*b <= 400
            feas2 = a + 4*b <= 300
            feas3 = (30 <= a <= 90) and (10 <= b <= 50)
            feas = feas1 and feas2 and feas3
            db = 100*a + 50*b
            st.info(f"Feasible: {feas} | DB={db}")
            st.caption(f"Known optimum: A={LP_SAMPLE['opt']['A']}, B={LP_SAMPLE['opt']['B']}, DB={LP_SAMPLE['opt']['DB']}")

# -------------------------
# ---- MODE: PROGRESS -----
# -------------------------
elif mode == "📊 Progress":
    st.markdown("<div class='headline'>Your Progress</div>", unsafe_allow_html=True)
    known, total = card_progress()
    tfc, tft = tf_progress()
    rdb_c = st.session_state.rdb_correct
    rdb_a = st.session_state.rdb_attempts

    cols = st.columns(3)
    with cols[0]:
        pct = known/total if total else 0
        st.markdown(f"<div class='card'><b>Flashcards</b><br><span class='metric'><span class='num'>{known}/{total}</span>&nbsp; "
                    f"<span style='color:{grade_color(pct)};font-weight:800'>{int(pct*100)}%</span></span></div>", unsafe_allow_html=True)
    with cols[1]:
        p = tfc/tft if tft else 0
        st.markdown(f"<div class='card'><b>True/False</b><br><span class='metric'><span class='num'>{tfc}/{tft}</span>&nbsp; "
                    f"<span style='color:{grade_color(p)};font-weight:800'>{int(p*100)}%</span></span></div>", unsafe_allow_html=True)
    with cols[2]:
        p = rdb_c/rdb_a if rdb_a else 0
        st.markdown(f"<div class='card'><b>Rel. DB Trainer</b><br><span class='metric'><span class='num'>{rdb_c}/{rdb_a}</span>&nbsp; "
                    f"<span style='color:{grade_color(p)};font-weight:800'>{int(p*100)}%</span></span></div>", unsafe_allow_html=True)

    st.markdown("<div class='subtle'>Tip: cycle Read → Flashcards → T/F → Calc Trainer, then revisit Deltas before sleeping.</div>", unsafe_allow_html=True)