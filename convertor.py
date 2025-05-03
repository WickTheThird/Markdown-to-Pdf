import os
from markdown_it import MarkdownIt
from mdit_py_plugins.tasklists import tasklists_plugin
from mdit_py_plugins.footnote import footnote_plugin
from weasyprint import HTML

def md_to_pdf(md_path, pdf_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    md = (
        MarkdownIt("commonmark", {"html": True, "linkify": True})
        .enable("table")
        .enable("strikethrough")
        .use(tasklists_plugin)
        .use(footnote_plugin)
    )
    html_body = md.render(md_text)

    css = """
    body {
        font-family: sans-serif;
        margin: 2em;
        line-height: 1.6;
    }
    pre {
        background: #f4f4f4;
        padding: 1em;
        overflow-x: auto;
        white-space: pre-wrap;
        word-wrap: break-word;
    }
    code {
        font-family: monospace;
        white-space: pre-wrap;
        background-color: #eee;
        padding: 2px 4px;
        border-radius: 4px;
    }
    table {
        width: 100%;
        table-layout: fixed;
        border-collapse: collapse;
        margin: 1em 0;
    }
    th, td {
        border: 1px solid #ccc;
        padding: 0.5em;
        text-align: left;
        word-break: break-word;
        white-space: normal;
    }
    img {
        max-width: 100%;
        height: auto;
    }
    """

    full_html = f"""<!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <style>{css}</style>
      </head>
      <body>{html_body}</body>
    </html>"""

    base = os.path.dirname(os.path.abspath(md_path)) or "."
    HTML(string=full_html, base_url=base).write_pdf(pdf_path)

if __name__ == "__main__":
    md_to_pdf("TechinicalSpecification.md", "output.pdf")
