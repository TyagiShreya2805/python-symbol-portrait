from pathlib import Path


def save_symbol_portrait(
    lines: list[str],
    output_path: Path,
) -> None:
    """
    Save symbol portrait lines as a text file.
    """

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    portrait = "\n".join(lines)

    output_path.write_text(
        portrait,
        encoding="utf-8",
    )