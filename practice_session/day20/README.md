# Day 20 Practice — Decision Models with PuLP

This folder contains the truck-loading decision model used in class.

## 1. Plain Python model

Run:

```bash
python practice_session/day20/truck.py
```

Expected starting result:

```text
Optimal ['Water', 'Blankets', 'Medical Kits'] 160.0
```

During the lecture, uncomment the volume constraint in `truck.py` and run again.
The objective becomes `150.0`.

Then uncomment the shelter/food need constraint and run again.
The objective becomes `140.0`.

## 2. Streamlit what-if app

Run:

```bash
streamlit run practice_session/day20/truck_app.py
```

Codespaces will forward port 8501 and open the Streamlit app.

The sliders change the truck's weight and volume limits and re-solve the
same binary optimization model.

## Notes

- `pulp` is installed from the repository `requirements.txt`.
- Streamlit is already part of the course environment.
- The professor-specific Windows `.bat` file and `.vscode/settings.json`
  are intentionally not included because they contain local machine paths.
