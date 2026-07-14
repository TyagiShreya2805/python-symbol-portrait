import numpy as np


SYMBOLS = "@%#*+=-:. "


def brightness_to_symbol(
    brightness: int,
    symbols: str = SYMBOLS,
) -> str:
    """
    Convert a grayscale brightness value into a symbol.

    Brightness values range from:
    0   = black
    255 = white
    """

    symbol_index = int(
        brightness / 255 * (len(symbols) - 1)
    )

    return symbols[symbol_index]


def image_to_symbol_lines(
    grayscale_image: np.ndarray,
    symbols: str = SYMBOLS,
) -> list[str]:
    """
    Convert a grayscale image into rows of symbols.
    """

    lines = []

    for row in grayscale_image:
        line = "".join(
            brightness_to_symbol(
                int(pixel),
                symbols,
            )
            for pixel in row
        )

        lines.append(line)

    return lines