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
from src.renderer import (
    save_symbol_portrait,
    save_symbol_portrait_html,
)
from src.symbol_mapper import image_to_symbol_lines


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

SYMBOL_OUTPUT_PATH = (
    PROJECT_ROOT
    / "output"
    / "symbol_portrait.txt"
)

HTML_OUTPUT_PATH = (
    PROJECT_ROOT
    / "output"
    / "symbol_portrait.html"
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
        resized_face,
        style="ascii",
        block_size=1,
    )

    save_image(
        cropped_face,
        CROPPED_OUTPUT_PATH,
    )

    save_image(
        grayscale_face,
        GRAYSCALE_OUTPUT_PATH,
    )

    save_symbol_portrait(
        symbol_lines,
        SYMBOL_OUTPUT_PATH,
    )

    save_symbol_portrait_html(
        symbol_lines,
        HTML_OUTPUT_PATH,
    )

    print("ASCII portrait created successfully!")
    print(f"Faces initially detected : {len(faces)}")
    print(f"Cropped face shape       : {cropped_face.shape}")
    print(f"Symbol grid shape        : {resized_face.shape}")
    print(f"Cropped image saved at   : {CROPPED_OUTPUT_PATH}")
    print(f"Grayscale image saved at : {GRAYSCALE_OUTPUT_PATH}")
    print(f"Symbol portrait saved at : {SYMBOL_OUTPUT_PATH}")


if __name__ == "__main__":
    main()