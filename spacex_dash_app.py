"""SpaceX Falcon 9 launch outcomes dashboard.
Run: pip install -r requirements.txt && python spacex_dash_app.py
Dataset expected at data/dataset_part_2.csv (or set SPACEX_DATASET).
"""
from pathlib import Path
import os
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

DATA_PATH = Path(os.getenv("SPACEX_DATASET", "data/dataset_part_2.csv"))
if not DATA_PATH.exists():
    DATA_PATH = Path("dataset_part_2.csv")
df = pd.read_csv(DATA_PATH)
app = Dash(__name__)
app.layout = html.Div([
    html.H1("SpaceX Falcon 9 Launch Success Dashboard"),
    html.Label("Launch site"),
    dcc.Dropdown(
        id="site", options=[{"label": s, "value": s} for s in sorted(df.LaunchSite.unique())],
        value=sorted(df.LaunchSite.unique())[0], clearable=False
    ),
    dcc.Graph(id="success-pie"),
    html.Label("Payload range (kg)"),
    dcc.RangeSlider(
        id="payload", min=float(df.PayloadMass.min()), max=float(df.PayloadMass.max()),
        step=500, value=[float(df.PayloadMass.min()), float(df.PayloadMass.max())],
        tooltip={"placement": "bottom", "always_visible": True}
    ),
    dcc.Graph(id="payload-outcome")
], style={"maxWidth": "1100px", "margin": "auto", "fontFamily": "Arial"})

@app.callback(Output("success-pie", "figure"), Input("site", "value"))
def update_pie(site):
    d = df[df.LaunchSite == site]
    counts = d.Class.map({0: "Unsuccessful", 1: "Successful"}).value_counts().rename_axis("Outcome").reset_index(name="Launches")
    return px.pie(counts, names="Outcome", values="Launches", title=f"Launch outcome — {site}", hole=.35)

@app.callback(Output("payload-outcome", "figure"), Input("site", "value"), Input("payload", "value"))
def update_scatter(site, payload):
    d = df[(df.LaunchSite == site) & df.PayloadMass.between(payload[0], payload[1])]
    return px.scatter(d, x="FlightNumber", y="PayloadMass", color=d.Class.astype(str),
                      hover_data=["BoosterVersion", "Orbit", "Outcome"],
                      labels={"color": "Class"}, title="Payload vs flight number — selected payload range")

if __name__ == "__main__":
    app.run(debug=True)
