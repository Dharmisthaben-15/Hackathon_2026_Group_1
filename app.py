"""PeoplePulse dashboard overview page."""

import plotly.express as px
import streamlit as st

from dashboard_utils import configure_page, get_scored_data, hero

configure_page(
    "PeoplePulse | Overview",
    "📊",
    "Overview of workforce attrition patterns and risk signals.",
)
data = get_scored_data()

hero(
    "PeoplePulse: Attrition Intelligence",
    "See where attrition concentrates, understand the signals, and prioritise supportive retention action.",
)

total_employees = len(data)
leavers = int(data["AttritionBinary"].sum())
overall_rate = leavers / total_employees
high_risk = int((data["Risk band"] == "High").sum())

metric_cols = st.columns(4)
metric_cols[0].metric("👥 Employees", f"{total_employees:,}")
metric_cols[1].metric("🚪 Historical attrition", f"{overall_rate:.1%}")
metric_cols[2].metric("⚠️ High-risk profiles", f"{high_risk:,}")
metric_cols[3].metric("🎯 Risk bands", "Low / Medium / High")

st.markdown('<p class="section-label">Workforce hotspots</p>', unsafe_allow_html=True)
left, right = st.columns(2)
with left:
    st.markdown('<div class="section-bar">📊 Attrition by job role</div>', unsafe_allow_html=True)
    role_rates = (
        data.groupby("JobRole", as_index=False)["AttritionBinary"]
        .mean()
        .assign(AttritionRate=lambda frame: frame["AttritionBinary"] * 100)
        .sort_values("AttritionRate")
    )
    figure = px.bar(
        role_rates,
        x="AttritionRate",
        y="JobRole",
        orientation="h",
        text_auto=".1f",
        labels={"AttritionRate": "Attrition rate (%)", "JobRole": ""},
        color="AttritionRate",
        color_continuous_scale=["#8bd3c7", "#f59e0b", "#d64545"],
    )
    figure.update_layout(coloraxis_showscale=False, height=430, paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(figure, use_container_width=True)

with right:
    st.markdown('<div class="section-bar">🏢 Attrition by department</div>', unsafe_allow_html=True)
    department_rates = (
        data.groupby("Department", as_index=False)["AttritionBinary"]
        .mean()
        .assign(AttritionRate=lambda frame: frame["AttritionBinary"] * 100)
    )
    figure = px.bar(
        department_rates,
        x="Department",
        y="AttritionRate",
        text_auto=".1f",
        labels={"AttritionRate": "Attrition rate (%)", "Department": ""},
        color="AttritionRate",
        color_continuous_scale=["#8bd3c7", "#f59e0b", "#d64545"],
    )
    figure.update_layout(coloraxis_showscale=False, height=430, paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(figure, use_container_width=True)

st.info(
    "💡 Use **Risk triage** in the sidebar to find priority employee segments. "
    "Use **Hypotheses & actions** to connect the data to practical retention planning."
)
