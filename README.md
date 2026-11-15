# Flight Deals Tracker (work in progress)

A Python project that reads a list of destinations and prices from a Google Sheet (through
[Sheety](https://sheety.co)) and is meant to find cheap flights for them.

## Status
- Done: reading the sheet and updating rows with IATA codes (`data_manager.py`).
- Not done yet: flight search (`flight_search.py`), flight data (`flight_data.py`) and
  notifications (`notification_manager.py`) are still placeholders.

## Setup
```
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in your values:

```
SHEET_URL_GET=<your Sheety prices endpoint>
AUTH=<your base64 basic-auth token>
```

The `.env` file is ignored by git and must never be committed.

## Run
```
python main.py
```
