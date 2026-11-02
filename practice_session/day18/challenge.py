from pathlib import Path
import sqlite3

import pandas as pd
import streamlit as st

DB_PATH = Path(__file__).resolve().parent / "practice.db"

# ------------------------------------------------------------
# Presentation tier: choices
# ------------------------------------------------------------
st.title("Regional Shipment Dashboard")

regions = ["North", "South", "East", "West"]
statuses = ["delivered", "planned", "in transit", "delayed"]

region = st.sidebar.selectbox("Region", regions)
status = st.sidebar.selectbox("Shipment status", statuses)

# ------------------------------------------------------------
# Data tier
# ------------------------------------------------------------
con = sqlite3.connect(DB_PATH)

# TODO 1
# Query Camps JOIN Shipments.
# Return at least: shipment_id, camp, qty, status.
# Filter using BOTH c.region = ? and s.status = ?.
# Pass the widget values through params in the correct order.
# Replace this empty starter frame with your query result.
rows = pd.DataFrame(columns=["shipment_id", "camp", "qty", "status"])

con.close()

# ------------------------------------------------------------
# Logic tier
# ------------------------------------------------------------
# TODO 2
# Calculate matching_count and total_qty from the returned rows.
matching_count = 0
total_qty = 0

# ------------------------------------------------------------
# Presentation tier: headline numbers
# ------------------------------------------------------------
# TODO 3
# Display both headline metrics.
st.info("TODO 3: add the matching-shipment and total-quantity metrics.")

# ------------------------------------------------------------
# Presentation tier: evidence
# ------------------------------------------------------------
# TODO 4
# Display the evidence table.
st.info("TODO 4: display the returned rows as the evidence table.")

# TODO 5
# Add a useful bar chart showing quantity by camp.
# If more than one shipment goes to the same camp, decide whether
# the chart should show individual rows or a camp-level total.
st.info("TODO 5: add a bar chart of quantity by camp.")
