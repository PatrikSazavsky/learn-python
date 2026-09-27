# learn-python

90denní cesta od nuly k junior AI inženýrovi. Start 2026-09-28, konec 2026-12-26.
Plán, checklisty a log: `~/Documents/AIOS/JARVIS/learning/`.

## Pravidla tohoto repa

1. Kód v `week-XX/` a `projects/` je psaný **bez AI** (40 min denně). Výjimka je označená komentářem `# AI:` na začátku souboru.
2. Každý den má commit. Commit message říká, co jsem se naučil, ne co jsem změnil.
3. Každé cvičení má test. `uv run pytest` musí projít před commitem.
4. Když něco nechápu, jde to do `~/Documents/AIOS/JARVIS/learning/log.md`, ne pod koberec.

## Spuštění

```bash
uv sync            # jednou, vytvoří .venv s Pythonem 3.12
uv run pytest      # všechny testy
uv run ruff check  # lint
uv run python week-01/uloha.py
```

## Struktura

- `week-01/` … `week-13/` — denní cvičení a páteční testy
- `projects/` — tři portfolio projekty (digest CLI, lead pipeline, agent s evals)
