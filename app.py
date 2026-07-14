from pathlib import Path

from src.face_detector import (
    crop_face,
    detect_faces,
    select_largest_face,
)
from src.image_loader import load_image, save_image
from src.preprocessing import (
    convert_to_grayscale,
    resize_for_symbols,
)
from src.renderer import save_symbol_portrait
from src.symbol_mapper import image_to_symbol_lines


PROJECT_ROOT = Path(__file__).parent

INPUT_PATH = PROJECT_ROOT / "input" / "portrait.jpg"

GRAYSCALE_OUTPUT_PATH = (
    PROJECT_ROOT
    / "output"
    / "grayscale_face.jpg"
)

SYMBOL_OUTPUT_PATH = (
    PROJECT_ROOT
    / "output"
    / "symbol_portrait.txt"
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

    resized_face = resize_for_symbols(
        grayscale_face,
        output_width=100,
    )

    symbol_lines = image_to_symbol_lines(
        resized_face
    )

    save_image(
        grayscale_face,
        GRAYSCALE_OUTPUT_PATH,
    )

    save_symbol_portrait(
        symbol_lines,
        SYMBOL_OUTPUT_PATH,
    )

    print("Symbol portrait created successfully!")
    print(f"Face shape        : {cropped_face.shape}")
    print(f"Symbol grid shape : {resized_face.shape}")
    print(f"Saved at          : {SYMBOL_OUTPUT_PATH}")


if __name__ == "__main__":
    main()