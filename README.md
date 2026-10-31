# SpaceX Data Science Capstone

IBM Applied Data Science Capstone — Falcon 9 first-stage landing analysis.

## Laboratory notebooks
- [Data collection with SpaceX API](jupyter-labs-spacex-data-collection-api-v2.ipynb) — REST API requests, enrichment by rocket/payload/launchpad/core IDs, and data cleaning.
- [Historical launch web scraping](jupyter-labs-webscraping.ipynb) — BeautifulSoup extraction of Falcon 9 launch-history tables.
- [Data wrangling](labs-jupyter-spacex-Data%20wrangling-v2.ipynb) — missing-value review, site/orbit counts and landing labels.
- [EDA with visualization](jupyter-labs-eda-dataviz-v2.ipynb) — six required charts and one-hot feature engineering.
- [EDA with SQL](jupyter-labs-eda-sql-coursera_sqllite.ipynb) — ten SQLite query tasks.
- [Launch-site mapping with Folium](lab-jupyter-launch-site-location-v2.ipynb) — site markers, outcome clusters, distance calculations and proximity map.
- [Machine-learning prediction](SpaceX-Machine-Learning-Prediction-Part-5-v1.ipynb) — Logistic Regression, SVM, Decision Tree and KNN with 10-fold GridSearchCV.
- [Dash application](spacex_dash_app.py) — site outcome pie chart and payload/flight scatter plot.

## Install and run
```bash
python -m pip install -r requirements.txt
jupyter notebook
```

The notebooks use the course datasets at IBM Skills Network or documented public CSV mirrors. The Dash app can load the course CSV from the local `data/` folder or use a public course-data mirror if the local file is absent:
```bash
python spacex_dash_app.py
```

## Reproducibility and validation
The missing task cells in the starter notebooks have been filled. Locally executed notebooks and presentation evidence are included in the companion package generated for this project. The local run used 90 Falcon 9 landing records for EDA/ML and a separate 97-row historical mission table for SQL; these are different source tables and should not be merged without a documented reconciliation step.

## Important execution limitations
- The SpaceX API and Wikipedia scraping notebooks require external network access to their endpoints. Their task code is complete, but those live requests could not be re-run in the restricted execution environment used to prepare this update.
- The Folium and SQL notebooks' missing tasks are filled. Local companion Folium maps and SQLite query outputs were executed using the available course data/mirror.
- A standalone Plotly dashboard HTML and Dash app source are supplied. The Dash server was not launched in the preparation environment because Dash was not installed there.
- KSC LC 39A proximity buffers in the companion map are user-defined radii. They are not nearest-road/rail/coastline measurements without verified GIS feature coordinates.
- Model accuracy is based on an 18-row held-out test set and is descriptive; additional validation is required before operational use.

## Results (90-row Falcon 9 landing dataset)
- Successful first-stage landings: 60/90 (66.7%).
- Site success: CCSFS SLC 40 60.0% (33/55); KSC LC 39A 77.3% (17/22); VAFB SLC 4E 76.9% (10/13).
- Best model in this local run: Decision Tree, 88.9% test accuracy; confusion matrix [[4, 2], [0, 12]].

## Presentation
The completed slide deck, execution report, static charts, Folium HTML maps and Plotly dashboard are provided in the companion ZIP bundle; the GitHub repository contains the completed lab code and app source.
