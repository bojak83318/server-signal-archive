# Server Signal Archive 📡

**Objective:** Automated tracking of High-Performance VPS offers suitable for Local AI Inference (GLM-4 / Llama-3).

## Architecture
- **Scraper:** Runs hourly via GitHub Actions (residential proxy routing).
- **Analyzer:** Filters offers for `Ryzen/EPYC` CPUs + `16GB+ RAM`.
- **Database:** Incremental Markdown archive in `/offers`.
- **Output:** `glm4_candidates.csv` (The "Best Buy" list).

## Usage
- **View Deals:** Check [glm4_candidates.csv](glm4_candidates.csv).
- **Run Locally:** Use `local_run.sh` (requires `PROXY_URL` env var).

*Maintained by the Professor.*
