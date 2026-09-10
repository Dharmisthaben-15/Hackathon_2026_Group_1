"""Risk triage page for prioritising retention conversations."""

import streamlit as st

from dashboard_utils import configure_page, get_scored_data, hero

configure_page(
    "PeoplePulse | Risk Triage",
    "⚠️",
    "Filter and prioritise employees for supportive retention conversations.",
)
data = get_scored_data()
hero(
    "Risk triage",
    "Move from a model score to a focused, human-led retention conversation.",
)

filter_cols = st.columns(3)
with filter_cols[0]:
    selected_department = st.selectbox(
        "Department", ["All"] + sorted(data["Department"].unique().tolist())
    )

available_roles = sorted(
    data.loc[
        data["Department"].eq(selected_department)
        if selected_department != "All"
        else data["Department"].notna(),
        "JobRole",
    ].unique().tolist()
)
with filter_cols[1]:
    selected_role = st.selectbox(
        "Job role", ["All"] + available_roles,
        help="Roles are limited to the selected department.",
    )
with filter_cols[2]:
    selected_band = st.selectbox("Risk band", ["All", "High", "Medium", "Low"])

filtered = data.copy()
if selected_department != "All":
    filtered = filtered[filtered["Department"] == selected_department]
if selected_role != "All":
    filtered = filtered[filtered["JobRole"] == selected_role]
if selected_band != "All":
    filtered = filtered[filtered["Risk band"] == selected_band]

metric_cols = st.columns(3)
metric_cols[0].metric("Matching employees", f"{len(filtered):,}")
metric_cols[1].metric(
    "Average predicted risk",
    f"{filtered['Risk probability'].mean():.1%}" if len(filtered) else "n/a",
)
metric_cols[2].metric(
    "High-risk in selection",
    f"{(filtered['Risk band'] == 'High').sum():,}",
)

display_columns = [
    "EmployeeNumber",
    "Department",
    "JobRole",
    "MonthlyIncome",
    "YearsSinceLastPromotion",
    "OverTime",
    "JobSatisfaction",
    "Risk probability",
    "Risk band",
]
st.dataframe(
    filtered.sort_values("Risk probability", ascending=False)[display_columns].style.format(
        {"Risk probability": "{:.1%}"}
    ),
    use_container_width=True,
    hide_index=True,
)
st.warning(
    "⚖️ Model scores are decision support, not a judgement about an individual. "
    "Validate context with managers and employees before taking action."
)
st.subheader("Suggested conversation themes")
st.markdown(
    """
    - **Career:** discuss progression, skills development, and promotion pathways.
    - **Workload:** review overtime, manager support, and work-life balance.
    - **Recognition:** check whether pay, feedback, and contribution feel fair.
    - **Belonging:** explore team experience, travel demands, and practical barriers.
    """
)
