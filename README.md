# API Contract Diff

Compare local compact API contract documents for added/removed fields, type changes, and requiredness changes.

```bash
cat contracts.json | python tool.py
python -m unittest -v
```

It expects a narrow `{ "fields": ... }` format. Adapt it before using with a full OpenAPI or JSON Schema workflow.
