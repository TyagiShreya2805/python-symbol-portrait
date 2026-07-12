from pathlib import Path

import cv2
import numpy as np


def load_image(path: Path) -> np.ndarray:
    """
    Load an image from the provided file path.

    Parameters
    ----------
    path:
        Path of the image to load.

    Returns
    -------
    numpy.ndarray
        The image loaded as an OpenCV NumPy array.
    """

    if not path.exists():
        raise FileNotFoundError(f"Image not found: {path}")

    image = cv2.imread(str(path))

    if image is None:
        raise ValueError(f"Unable to read the image: {path}")

    return image


def save_image(image: np.ndarray, path: Path) -> None:
    """
    Save an OpenCV image to the provided file path.
    """

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    saved_successfully = cv2.imwrite(
        str(path),
        image,
    )

    if not saved_successfully:
        raise RuntimeError(f"Unable to save the image: {path}")