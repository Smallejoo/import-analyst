# Import analyst

A Python/Flask learning project for exploring Israeli import records from the data.gov.il datastore API. It retrieves tabular records and creates charts with pandas and matplotlib, with a browser interface for selecting fields and chart options.

## Architecture

- `server.py`: Flask page, JSON data endpoint and generated chart endpoint.
- `suportB/dataManagment.py`: public-data retrieval and chart generation.
- `templates/mainHtml.html`: page template.
- `supportFE/`: browser JavaScript and CSS.

## Run locally

Use Python 3.12 and an internet connection. From the repository root:

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python server.py
```

On macOS/Linux, replace `.venv\Scripts\python` with `.venv/bin/python`. Open http://127.0.0.1:5000. The Flask debug server is for local development only.

## Data and limitations

The code queries resource `6d3b03e1-de9c-42a8-bb08-91ba564c2f34` at `https://data.gov.il/api/3/action/datastore_search`. Availability and column definitions depend on the upstream dataset. This is an exploratory dashboard, not a validated financial/statistical reporting tool.

There is no automated test suite yet. Manually verify record retrieval and each chart option; some graph-type spelling and validation paths need further work. Add request timeouts, input validation, upstream-error handling and tests before deployment. Dependency ranges are declared; a tested lockfile and demo screenshots are still to be added.
