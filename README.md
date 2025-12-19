# AfterRun – Dein Laufcoach (MVP)

MVP-App zur Reflexion einzelner Laufeinheiten im Trainingskontext.
Import: GPX/TCX (manuell). Fokus: Laufen.

## Out of scope (MVP)
- Trainingspläne erstellen/anpassen
- Medizinische Aussagen
- Wettkampfprognosen
- Direktive Sprache ("du solltest", "du musst")

## Tech (MVP)
Python + Streamlit + SQLite, Importer-Adapter (GPX/TCX), AI-Feedback als Service.

## Python Guidelines (Consider)
- Follow PEP 8 for code style.
- Use type hints for public APIs and functions where practical.
- Keep dependencies pinned in `requirements.txt` and use a virtual environment.
- Add unit tests (pytest) for core logic and CI to run them.
- Use small, well-named modules and single-responsibility classes/functions.
# afterrun-mvp
AfterRun – Dein Laufcoach (MVP)
