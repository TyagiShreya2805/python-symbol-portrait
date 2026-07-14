from html import escape
from pathlib import Path


def save_symbol_portrait(
    lines: list[str],
    output_path: Path,
) -> None:
    """
    Save the symbol portrait as a plain text file.
    """

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    portrait_text = "\n".join(lines)

    output_path.write_text(
        portrait_text,
        encoding="utf-8",
    )


def save_symbol_portrait_html(
    lines: list[str],
    output_path: Path,
) -> None:
    """
    Save the symbol portrait as an HTML file
    using a monospace font.
    """

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    portrait_text = "\n".join(lines)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Python Symbol Portrait</title>

    <style>
        body {{
            margin: 0;
            padding: 24px;
            background-color: white;
        }}

        pre {{
            margin: 0;
            font-family: "Courier New", Courier, monospace;
            font-size: 8px;
            line-height: 0.85;
            white-space: pre;
        }}
    </style>
</head>

<body>
    <pre>{escape(portrait_text)}</pre>
</body>
</html>
"""

    output_path.write_text(
        html_content,
        encoding="utf-8",
    )