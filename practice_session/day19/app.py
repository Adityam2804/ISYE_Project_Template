from pathlib import Path
import sqlite3
import pandas as pd
import streamlit as st

DB_PATH = Path(__file__).resolve().parent / "practice.db"

st.title("Relief Decision Dashboard")
st.caption("Day 19 unified practice")

# Q1 (3 min) -------------------------------------------------
# TODO 1: Replace the fixed region with a sidebar selectbox.
# Choices: North, South, East, West.
region = "North"


# Q2 (3 min) -------------------------------------------------
# TODO 2: Cache this connection with @st.cache_resource.
# Also add check_same_thread=False.
def get_connection():
    return sqlite3.connect(DB_PATH)


# Q3 (4 min) -------------------------------------------------
SQL = """
SELECT
    s.shipment_id,
    c.name AS camp,
    c.capacity,
    i.name AS item,
    i.category,
    s.qty,
    s.status
FROM Shipments s
JOIN Camps c ON s.camp_id = c.camp_id
JOIN Items i ON s.item_id = i.item_id
WHERE c.region = ?
ORDER BY s.shipment_id
"""

# TODO 3:
# Add @st.cache_data above this function.
# Keep region as an argument and keep params=(region,).
def load_shipments(region):
    return pd.read_sql_query(
        SQL,
        get_connection(),
        params=(region,),
    )


# Q6 (3 min) -------------------------------------------------
# Do this after Q1-Q5.
# TODO 6: Add a sidebar Refresh button.
# If pressed, call st.cache_data.clear() BEFORE load_shipments().

frame = load_shipments(region)


# Q4 (5 min) -------------------------------------------------
st.subheader(f"Shipments to {region}")

# TODO 4: Using only `frame`, show:
# 1. metric: total units shipped
# 2. bar chart: total qty by camp
# 3. evidence table: frame
st.info("TODO 4: headline + chart + evidence table")


# Q5 (4 min) -------------------------------------------------
st.subheader("Threshold view")

# TODO 5:
# Add a sidebar slider:
#   Minimum shipment quantity, 0 to 400, default 100, step 25
# Filter the EXISTING frame:
#   visible = frame[frame["qty"] >= minimum]
# Show a metric:
#   "X of Y shipments shown"
# Do not call load_shipments() again.
st.info("TODO 5: filter the existing frame; do not requery")


# Q7 (6 min) -------------------------------------------------
st.subheader("Decision recommendation")

# TODO 7:
# Consider DELIVERED shipments only.
# For each camp compute:
#       delivered units / camp capacity
# Recommend the camp with the LOWEST value for resupply first.
#
# Show:
# 1. st.metric("Resupply first", <camp>, <ratio text>)
# 2. one sentence stating the rule
# 3. one limitation:
#    different item types are added together as if comparable.
#
# Hint:
# delivered = frame[frame["status"] == "delivered"].copy()
# Group by camp and capacity, sum qty, then divide.
st.info("TODO 7: recommendation + rule + limitation")
