# SpaceX Data Science Capstone

IBM Applied Data Science Capstone — Falcon 9 first-stage landing analysis.

## Labs in this repository
- [Data wrangling](labs-jupyter-spacex-Data%20wrangling-v2.ipynb): missing-value review, site/orbit counts, landing labels.
- [EDA with visualization](jupyter-labs-eda-dataviz-v2.ipynb): six required visualizations and feature engineering.
- [Classification](SpaceX-Machine-Learning-Prediction-Part-5-v1.ipynb): Logistic Regression, SVM, Decision Tree and KNN with 10-fold GridSearchCV.
- [Dash application](spacex_dash_app.py): launch-site outcome pie chart and payload/flight scatter plot.
- [Dependencies](requirements.txt).

## Data
The notebooks use the IBM Skills Network course CSV datasets hosted at the URLs in the notebook cells. Data availability depends on the upstream host and network access. This repository contains starter-course notebooks and does not claim that SpaceX API calls or Wikipedia scraping were run in this environment.

## Execution notes
The notebook code cells have been completed in the repository. Executed notebook outputs, data snapshots, static evidence charts, Folium HTML maps and an interactive Plotly HTML dashboard are supplied in the local companion bundle generated for this task; these are not all committed to this repository.

For local execution:
```bash
python -m pip install -r requirements.txt
jupyter notebook
```

For the Dash app, place `dataset_part_2.csv` in `data/` or repository root, then run:
```bash
python spacex_dash_app.py
```
