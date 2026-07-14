import cv2
import numpy as np


def detect_faces(image: np.ndarray) -> list[tuple[int, int, int, int]]:
    """
    Detect faces in an OpenCV image.

    Returns
    -------
    list of tuples
        Each tuple contains:
        (x, y, width, height)
    """

    grayscale_image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY,
    )

    cascade_path = (
        cv2.data.haarcascades
        + "haarcascade_frontalface_default.xml"
    )

    face_classifier = cv2.CascadeClassifier(cascade_path)

    if face_classifier.empty():
        raise RuntimeError("Unable to load the face detection model.")

    faces = face_classifier.detectMultiScale(
        grayscale_image,
        scaleFactor=1.1,
        minNeighbors=8,
        minSize=(150, 150),
    )

    return [
        (int(x), int(y), int(width), int(height))
        for x, y, width, height in faces
    ]

def select_largest_face(
    faces: list[tuple[int, int, int, int]],
) -> tuple[int, int, int, int]:
    """
    Return the largest detected face.
    """

    if not faces:
        raise ValueError("No faces were detected.")

    return max(
        faces,
        key=lambda face: face[2] * face[3],
    )


def draw_face_boxes(
    image: np.ndarray,
    faces: list[tuple[int, int, int, int]],
) -> np.ndarray:
    """
    Draw a rectangle around every detected face.
    """

    output_image = image.copy()

    for x, y, width, height in faces:
        cv2.rectangle(
            output_image,
            (x, y),
            (x + width, y + height),
            (0, 255, 0),
            thickness=3,
        )

    return output_image

def crop_face(
    image: np.ndarray,
    face: tuple[int, int, int, int],
    padding: float = 0.25,
) -> np.ndarray:
    """
    Crop a detected face with additional space around it.

    Parameters
    ----------
    image:
        Original OpenCV image.

    face:
        Face coordinates in the form:
        (x, y, width, height)

    padding:
        Additional space around the detected face.
        A value of 0.25 adds 25% padding.

    Returns
    -------
    numpy.ndarray
        Cropped face image.
    """

    x, y, width, height = face

    image_height, image_width = image.shape[:2]

    horizontal_padding = int(width * padding)
    vertical_padding = int(height * padding)

    x1 = max(0, x - horizontal_padding)
    y1 = max(0, y - vertical_padding)

    x2 = min(
        image_width,
        x + width + horizontal_padding,
    )

    y2 = min(
        image_height,
        y + height + vertical_padding,
    )

    cropped_face = image[y1:y2, x1:x2]

    if cropped_face.size == 0:
        raise ValueError("The detected face could not be cropped.")

    return cropped_face