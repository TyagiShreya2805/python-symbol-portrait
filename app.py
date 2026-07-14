from pathlib import Path

from src.face_detector import (
    crop_face,
    detect_faces,
    select_largest_face,
)
from src.image_loader import load_image, save_image
from src.preprocessing import convert_to_grayscale


PROJECT_ROOT = Path(__file__).parent

INPUT_PATH = PROJECT_ROOT / "input" / "portrait.jpg"

CROPPED_OUTPUT_PATH = (
    PROJECT_ROOT
    / "output"
    / "cropped_face.jpg"
)

GRAYSCALE_OUTPUT_PATH = (
    PROJECT_ROOT
    / "output"
    / "grayscale_face.jpg"
)


def main() -> None:
    image = load_image(INPUT_PATH)

    faces = detect_faces(image)

    if not faces:
        print("No face was detected.")
        return

    largest_face = select_largest_face(faces)

    cropped_face = crop_face(
        image,
        largest_face,
        padding=0.25,
    )

    grayscale_face = convert_to_grayscale(
        cropped_face
    )

    save_image(
        cropped_face,
        CROPPED_OUTPUT_PATH,
    )

    save_image(
        grayscale_face,
        GRAYSCALE_OUTPUT_PATH,
    )

    print("Face cropped successfully!")
    print(f"Faces initially detected : {len(faces)}")
    print(f"Cropped face shape       : {cropped_face.shape}")
    print(f"Colour crop saved at     : {CROPPED_OUTPUT_PATH}")
    print(f"Grayscale crop saved at  : {GRAYSCALE_OUTPUT_PATH}")


if __name__ == "__main__":
    main()