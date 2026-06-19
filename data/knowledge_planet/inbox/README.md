# Knowledge Planet Inbox

Put Knowledge Planet source files here before importing them into the research system.

Recommended inputs:

- `.md` or `.txt`: best for copied posts and daily digests.
- `.pdf`: best for downloaded sell-side reports.
- `.png` or `.jpg`: best for screenshots; keep them as source evidence and run OCR later.
- `.csv`: useful when you batch-export manually curated items.

For post streams like market jokes, seller comments, weekly data snippets, and short notes, prefer one Markdown file per day:

`YYYY-MM-DD_knowledge_planet_digest.md`

Use `post_template.md` as the block format. One post should be one block. Screenshots can be stored next to the Markdown file and referenced in `source_file`.

After import, processed files can be moved to:

`data/knowledge_planet/processed/`

Files that fail parsing can be moved to:

`data/knowledge_planet/failed/`
