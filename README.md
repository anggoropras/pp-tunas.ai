# TUNAS AI

**TUNAS AI** is a Legal Document Q&A Assistant designed to help users query and understand Indonesian government regulation documents using Retrieval-Augmented Generation (RAG).

## Project Focus

The initial capstone focus is **PP No. 17 Tahun 2025 (PP TUNAS)**.

## Architecture

```text
Legal Document → Loader → Chunking → Embeddings → Vector DB → Retriever → LLM → TUNAS AI
```

## Security

- API keys are stored in `.env` and excluded from Git.
- Raw PDF/legal documents are excluded from Git.
- Local vector databases are excluded from Git.
- Use `.env.example` as the configuration template.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```

## Project status

Initial production-oriented repository structure established.
