# learn-python

Cesta od nuly k AI-enhanced software inženýrovi. Start 2026-09-28, kontrolní bod 2026-12-27, pokračování do 2027-02-14.
Plán, checklisty a log: `~/Documents/AIOS/JARVIS/learning/`.

## Pravidla tohoto repa

1. Kód ve `week-XX/` a `projects/` píšu **bez AI**. Kód od agenta vzniká jen ve větvích `ai/…` a `agent/…` a do `main` jde, až každý řádek umím vysvětlit. Co agent udělal špatně, je v `AGENT_LOG.md` projektu.
2. **Řešení psetů CS50P sem nepatří.** Pravidla kurzu zakazují je zveřejnit. Psety řeším na cs50.dev.
3. Inline návrhy AI jsou v tomto repu vypnuté (`.vscode/settings.json`).
4. Každé cvičení má test. `uv run pytest` musí projít před commitem.
5. Každý den commit. Commit message říká, co jsem se naučil, ne co jsem změnil.

## Spuštění

```bash
uv sync            # jednou, vytvoří .venv s Pythonem 3.12
uv run pytest      # všechny testy
uv run ruff check  # lint
uv run python week-01/d1_sazba.py
```

## Struktura

- `week-01/` až `week-20/`: denní cvičení a páteční testy
- `projects/00_nabidka`: kalkulačka nabídky (mini projekt)
- `projects/01_digest`: Projekt 1, CLI digest veřejného zdroje s HTML reportem
- `projects/02_…`: Projekt 2, datová pipeline pro skutečnou firmu
- `projects/03_triage`: první LLM skript se structured output a analýzou chyb
- `projects/04_ai_app`: Projekt 3, AI aplikace s RAG, evals a nasazením
