import numpy as np


SYMBOL_SETS = {
    "ascii": "@%#*+=-:. ",
    "python": "(){}[]<>:=+-*/., ",
    "binary": "10",
    "blocks": "█▓▒░ ",
    "minimal": "@#.",
}


def get_symbol_set(style: str) -> str:
    """
    Return the symbol set for a selected rendering style.
    """

    if style not in SYMBOL_SETS:
        available_styles = ", ".join(SYMBOL_SETS)

        raise ValueError(
            f"Unknown style: {style}. "
            f"Available styles: {available_styles}"
        )

    return SYMBOL_SETS[style]


def brightness_to_symbol(
    brightness: float,
    symbols: str,
) -> str:
    """
    Convert a grayscale brightness value into one symbol.

    0 represents black.
    255 represents white.
    """

    brightness = max(0, min(255, brightness))

    symbol_index = int(
        brightness / 255 * (len(symbols) - 1)
    )

    return symbols[symbol_index]


def image_to_symbol_lines(
    grayscale_image: np.ndarray,
    style: str = "ascii",
    block_size: int = 8,
) -> list[str]:
    """
    Convert a grayscale image into symbol lines using
    average brightness calculated from square pixel blocks.
    """

    if grayscale_image.ndim != 2:
        raise ValueError(
            "image_to_symbol_lines expects a grayscale image."
        )

    if block_size <= 0:
        raise ValueError("block_size must be greater than zero.")

    symbols = get_symbol_set(style)

    image_height, image_width = grayscale_image.shape

    lines = []

    for row_start in range(0, image_height, block_size):
        line_symbols = []

        for column_start in range(
            0,
            image_width,
            block_size,
        ):
            block = grayscale_image[
                row_start:row_start + block_size,
                column_start:column_start + block_size,
            ]

            average_brightness = float(block.mean())

            symbol = brightness_to_symbol(
                average_brightness,
                symbols,
            )

            line_symbols.append(symbol)

        lines.append("".join(line_symbols))

    return lines