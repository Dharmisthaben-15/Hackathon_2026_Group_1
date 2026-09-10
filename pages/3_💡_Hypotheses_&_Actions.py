"""Hypothesis evidence and retention action page."""

import plotly.express as px
import streamlit as st

from dashboard_utils import configure_page, get_scored_data, hero

configure_page(
    "PeoplePulse | Hypotheses & Actions",
    "💡",
    "Translate attrition patterns into practical retention actions.",
)
data = get_scored_data()
hero(
    "Hypotheses & retention actions",
    "The strongest observed patterns help HR decide where to investigate first.",
)

def rate(column: str, value: object) -> float:
    subset = data[data[column] == value]
    return float(subset["AttritionBinary"].mean()) if len(subset) else 0.0


st.markdown('<p class="section-label">Evidence snapshot</p>', unsafe_allow_html=True)
evidence = [
    {
        "Hypothesis": "Attrition differs by job role",
        "Comparison": "Sales Representative vs Research Director",
        "Observed result": f"{rate('JobRole', 'Sales Representative'):.1%} vs {rate('JobRole', 'Research Director'):.1%}",
        "Priority": "High",
    },
    {
        "Hypothesis": "Lower income is associated with attrition",
        "Comparison": "Lowest vs highest income quartile",
        "Observed result": (
            f"{data.loc[data['MonthlyIncome'].rank(pct=True) <= .25, 'AttritionBinary'].mean():.1%} "
            "vs "
            f"{data.loc[data['MonthlyIncome'].rank(pct=True) > .75, 'AttritionBinary'].mean():.1%}"
        ),
        "Priority": "High",
    },
    {
        "Hypothesis": "Overtime is associated with attrition",
        "Comparison": "Overtime vs no overtime",
        "Observed result": f"{rate('OverTime', 'Yes'):.1%} vs {rate('OverTime', 'No'):.1%}",
        "Priority": "High",
    },
    {
        "Hypothesis": "Promotion history is associated with attrition",
        "Comparison": "No promotion in recent history vs others",
        "Observed result": f"{rate('YearsSinceLastPromotion', 0):.1%} for 0 years",
        "Priority": "Investigate",
    },
]
st.dataframe(evidence, use_container_width=True, hide_index=True)

st.markdown('<p class="section-label">Retention playbook</p>', unsafe_allow_html=True)
actions = {
    "🧭 High-risk job roles": "Review workload, manager capability, onboarding, and progression pathways in the most exposed roles.",
    "💰 Income and fairness": "Run pay benchmarking and make reward criteria transparent, especially for lower-income groups.",
    "🚀 Progression": "Create career check-ins, mentoring, and visible promotion milestones for employees with limited progression.",
    "🌿 Sustainable work": "Review overtime patterns and improve flexibility, staffing, and work-life balance support.",
}
for title, action in actions.items():
    with st.expander(title, expanded=True):
        st.write(action)

st.subheader("Overtime signal")
overtime = (
    data.groupby("OverTime", as_index=False)["AttritionBinary"]
    .mean()
    .assign(AttritionRate=lambda frame: frame["AttritionBinary"] * 100)
)
st.plotly_chart(
    px.bar(
        overtime,
        x="OverTime",
        y="AttritionRate",
        text_auto=".1f",
        labels={"AttritionRate": "Attrition rate (%)", "OverTime": "Works overtime"},
        color="AttritionRate",
        color_continuous_scale=["#8bd3c7", "#d64545"],
    ).update_layout(coloraxis_showscale=False, paper_bgcolor="rgba(0,0,0,0)"),
    use_container_width=True,
)
