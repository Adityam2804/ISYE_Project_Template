"""truck_app.py: Ellis's truck behind two sliders: the model, solved once for each pair of limits.
Needs pulp below 4.0 (3.3.2 tested), the versions that include CBC. Run from this folder:  streamlit run truck_app.py"""
import streamlit as st
from pulp import *

KG = {"Hygiene Kits": 100, "Blankets": 250, "Medical Kits": 250, "Food Packs": 450, "Water": 500}
M3 = {"Hygiene Kits": 1, "Blankets": 6, "Medical Kits": 2, "Food Packs": 3, "Water": 4}
POINTS = {"Hygiene Kits": 30, "Blankets": 40, "Medical Kits": 50, "Food Packs": 60, "Water": 70}


def page_header(text):
    """The page's title in a light blue band."""
    st.markdown('<div style="background:#CFE6F7; color:#14283C; font-size:1.5rem; font-weight:700; '
                'padding:0.6rem 1rem; border-radius:6px; margin-bottom:0.6rem">' + text + '</div>',
                unsafe_allow_html=True)


@st.cache_data
def solve_truck(weight, volume):
    model = LpProblem("truck", LpMaximize)
    take = {n: LpVariable(n, cat="Binary") for n in KG}
    model += lpSum(POINTS[n] * take[n] for n in KG)
    model += lpSum(KG[n] * take[n] for n in KG) <= weight
    model += lpSum(M3[n] * take[n] for n in KG) <= volume
    model += take["Blankets"] + take["Food Packs"] >= 1
    model.solve(PULP_CBC_CMD(msg=0))
    chosen = [n for n in KG if take[n].value() == 1]
    points = int(value(model.objective))
    return chosen, points


st.set_page_config(layout="wide")
weight = st.sidebar.slider(
    "Weight (kg)", 600, 1300,
    value=1000, step=100)
volume = st.sidebar.slider(
    "Volume (m3)", 6, 13,
    value=10, step=1)
chosen, points = solve_truck(
    weight, volume)
page_header("Ellis's best load")
st.metric("Total points", points, border=True)
st.subheader(", ".join(chosen))
st.caption("Limitations: the points are Ellis's judgment, and the model plans one trip")
