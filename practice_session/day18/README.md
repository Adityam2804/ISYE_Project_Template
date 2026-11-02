# Day 18 Practice Session — Building an Interface, Part I

This practice lives in the **team repository**. It is not a separate individual-student repo.

## Start the practice

From the repository root:

```bash
python practice_session/day18/setup_practice_db.py
streamlit run practice_session/day18/app.py
```

Open forwarded port **8501** when Codespaces prompts you.

The repository's existing devcontainer already installs the root `requirements.txt`, including Streamlit and pandas.

## Class flow

### 1. Follow along with Prof. Trapp — `app.py`

Start with the working hard-coded Shipment Monitor. During the live demo, change it into a database-backed interface:

1. Replace the hard-coded shipment status with a Streamlit selection.
2. Pass the selected status to SQLite with a `?` placeholder and `params=(status,)`.
3. Add a minimum-quantity slider.
4. Extend the query to use two placeholders in the correct order.
5. Confirm that the metrics and evidence table change with the controls.

### 2. Independent in-class challenge — `challenge.py`

Build a **Regional Shipment Dashboard**.

The user chooses:
- region
- shipment status

The page must show:
- matching shipment count
- total quantity
- an evidence table
- a bar chart of quantity by camp

Use `Camps JOIN Shipments` and pass both widget values as SQL parameters.

## Homework extension

Continue from the in-class dashboard and extend it to use:

- `Camps`
- `Shipments`
- `Items`

Add an **Item category** control, multiple query parameters, at least two headline metrics, an evidence table, one meaningful chart, and a short interpretation/decision statement.

Keep the script organized with comments for:
- presentation tier
- data tier
- logic tier

### Optional bonus

Add a **Reviewed** button whose count survives reruns using `st.session_state`.

## Team-repository note

During the live practice, students may work in their own Codespaces without pushing changes. This avoids unnecessary merge conflicts in the shared team repository. The team can decide later which completed version, if any, should be committed.

## Reset the database

If the practice database is changed, rebuild it with:

```bash
python practice_session/day18/setup_practice_db.py
```

The generated `practice.db` is intentionally ignored by Git.
