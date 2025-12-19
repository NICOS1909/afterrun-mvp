# AfterRun – Your Running Coach (MVP)

An MVP app for reflecting on individual running sessions within a training context.
Import formats: GPX/TCX (manual). Primary focus: running.

## Out of scope (MVP)
- Creating or adapting training plans
- Medical advice
- Race performance predictions
- Directive language (e.g. "you should", "you must")

## Tech (MVP)
Python + Streamlit + SQLite, importer-adapter (GPX/TCX), AI feedback as a service.

## Python Guidelines (Consider)
- Follow PEP 8 for code style.
- Use type hints for public APIs and functions where practical.
- Pin dependencies in `requirements.txt` and use a virtual environment.
- Add unit tests (pytest) for core logic and run them in CI.
- Keep modules small and focused; prefer single-responsibility functions/classes.

