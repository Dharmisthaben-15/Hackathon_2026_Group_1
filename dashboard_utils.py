"""Shared presentation and data helpers for the PeoplePulse dashboard."""

from pathlib import Path

import streamlit as st

from ml_model import feature_columns, load_or_train_model, risk_band


@st.cache_resource
def get_model():
    """Load the persisted model once per Streamlit session."""
    return load_or_train_model(Path("models/employee_attrition_pipeline.joblib"))


@st.cache_data
def get_scored_data():
    """Return the employee data with model probabilities and risk bands."""
    model, data = get_model()
    scored = data.copy()
    scored["Risk probability"] = model.predict_proba(
        scored[feature_columns(scored)]
    )[:, 1]
    scored["Risk band"] = scored["Risk probability"].map(risk_band)
    return scored


def configure_page(title: str, icon: str, subtitle: str) -> None:
    """Apply the common PeoplePulse page configuration and visual theme."""
    st.set_page_config(page_title=title, page_icon=icon, layout="wide")
    st.markdown(
        """
        <style>
        :root {
            --navy: #102a43;
            --blue: #1565c0;
            --teal: #00897b;
            --gold: #f59e0b;
            --mist: #f4f8fc;
        }
        .stApp {
            background: linear-gradient(135deg, #f4f8fc 0%, #eef5f4 100%);
        }
        .block-container { padding: 2.4rem 3rem 3rem; max-width: 1500px; }
        h1, h2, h3 { color: var(--navy); letter-spacing: -0.02em; }
        h1 { font-weight: 800; }
        [data-testid="stMetric"] {
            background: rgba(255, 255, 255, 0.86);
            border: 1px solid #dce8f2;
            border-radius: 16px;
            padding: 16px;
            box-shadow: 0 5px 18px rgba(16, 42, 67, 0.06);
        }
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #102a43 0%, #174a63 100%);
        }
        [data-testid="stSidebar"] * { color: #f5fbff !important; }
        [data-testid="stSidebarNav"] { display: none; }
        .side-nav-title {
            color: #9edbd3 !important;
            font-size: .72rem;
            font-weight: 800;
            letter-spacing: .12em;
            margin: 1.35rem 0 .45rem;
            text-transform: uppercase;
        }
        .section-bar {
            background: linear-gradient(90deg, #102a43 0%, #1565c0 100%);
            border-radius: 10px;
            color: white !important;
            font-size: 1rem;
            font-weight: 700;
            margin: .2rem 0 .8rem;
            padding: .65rem .9rem;
        }
        .hero {
            background: linear-gradient(115deg, #102a43 0%, #1565c0 52%, #00897b 100%);
            border-radius: 20px;
            padding: 2rem 2.2rem;
            color: white;
            margin-bottom: 1.5rem;
            box-shadow: 0 12px 30px rgba(16, 42, 67, 0.18);
        }
        .hero h1, .hero p { color: white; margin: 0; }
        .hero p { margin-top: .65rem; opacity: .9; font-size: 1.05rem; }
        .section-label {
            color: var(--teal);
            font-size: .78rem;
            font-weight: 800;
            letter-spacing: .12em;
            text-transform: uppercase;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.sidebar.markdown("## 🧭 PeoplePulse")
    st.sidebar.caption("Evidence-led retention planning")
    st.sidebar.markdown("---")
    st.sidebar.markdown('<div class="side-nav-title">Workspace</div>', unsafe_allow_html=True)
    st.sidebar.page_link("app.py", label="📊  Overview")
    st.sidebar.page_link("pages/2_⚠️_Risk_Triage.py", label="⚠️  Risk triage")
    st.sidebar.page_link("pages/3_💡_Hypotheses_&_Actions.py", label="💡  Hypotheses & actions")
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**{icon} {title}**")
    st.sidebar.caption(subtitle)


def hero(title: str, subtitle: str) -> None:
    """Render the shared gradient page header."""
    st.markdown(
        f'<div class="hero"><h1>{title}</h1><p>{subtitle}</p></div>',
        unsafe_allow_html=True,
    )
