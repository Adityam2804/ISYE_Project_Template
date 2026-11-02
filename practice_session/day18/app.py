from pathlib import Path
import sqlite3

import pandas as pd
import streamlit as st

DB_PATH = Path(__file__).resolve().parent / "practice.db"

# ------------------------------------------------------------
# Presentation tier
# ------------------------------------------------------------
st.title("Shipment Monitor")
st.caption("Day 18 follow-along: turn a fixed database query into an interface.")

# TODO 1 — TYPE WITH PROF. TRAPP
# Replace this hard-coded value with a Streamlit selectbox.
status = "delivered"

# ------------------------------------------------------------
# Data tier
# ------------------------------------------------------------
con = sqlite3.connect(DB_PATH)

# TODO 2 — TYPE WITH PROF. TRAPP
# Replace the hard-coded SQL value with a ? placeholder.
# Then supply the selected widget value with params=(status,).
shipments = pd.read_sql_query(
    """
    SELECT shipment_id, camp_id, item_id, qty, status
    FROM Shipments
    WHERE status = 'delivered'
    ORDER BY shipment_id
    """,
    con,
)

con.close()

# ------------------------------------------------------------
# Logic tier
# ------------------------------------------------------------
shipment_count = len(shipments)
total_qty = int(shipments["qty"].sum()) if not shipments.empty else 0

# ------------------------------------------------------------
# Presentation tier
# ------------------------------------------------------------
left, right = st.columns(2)
left.metric("Matching shipments", shipment_count)
right.metric("Total quantity", total_qty)
st.dataframe(shipments, use_container_width=True)

st.divider()
st.subheader("Guided extension")
st.markdown(
    """
After the status filter works:

1. Add a sidebar slider called **Minimum quantity**.
2. Extend the SQL to include `AND qty >= ?`.
3. Pass **two parameters** in the same order as the placeholders.
4. Verify that both metrics and the evidence table change.
"""
)
