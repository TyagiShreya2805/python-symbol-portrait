import cv2
import numpy as np


def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Convert a colour OpenCV image from BGR to grayscale.
    """

    grayscale_image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY,
    )

    return grayscale_image

def resize_for_symbols(
    image: np.ndarray,
    output_width: int = 100,
) -> np.ndarray:
    """
    Resize an image for text-based symbol rendering.

    The height is adjusted because text characters are
    usually taller than they are wide.
    """

    original_height, original_width = image.shape[:2]

    aspect_ratio = original_height / original_width

    character_height_correction = 0.5

    output_height = max(
        1,
        int(
            output_width
            * aspect_ratio
            * character_height_correction
        ),
    )

    resized_image = cv2.resize(
        image,
        (output_width, output_height),
        interpolation=cv2.INTER_AREA,
    )

    return resized_image