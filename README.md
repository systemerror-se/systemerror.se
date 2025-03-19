# Systemerror Collective

## Requirements
- Python 

## Installation
```bash
python -m venv .venv
.\.venv\Scripts\pip install pelican[Markdown]
```

## Run
```bash
.\.venv\Scripts\pelican -r -l
```

Pages is served at `http://localhost:8000`

## Folder Structure
```
.
├── .github        // Github Actions (publish)
├── src
│   ├── content    // Content (markdown)
│   ├── theme      // Theme (css, html)
├── pelicanconf.py // Pelican configuration
```
