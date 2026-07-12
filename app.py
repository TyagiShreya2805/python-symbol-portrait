from pathlib import Path

from src.image_loader import load_image, save_image
from src.preprocessing import convert_to_grayscale


PROJECT_ROOT = Path(__file__).parent

INPUT_PATH = PROJECT_ROOT / "input" / "portrait.jpg"
OUTPUT_PATH = PROJECT_ROOT / "output" / "grayscale_portrait.jpg"


def main() -> None:
    image = load_image(INPUT_PATH)

    grayscale_image = convert_to_grayscale(image)

    save_image(
        grayscale_image,
        OUTPUT_PATH,
    )

    print("Grayscale image created successfully!")
    print(f"Original shape  : {image.shape}")
    print(f"Grayscale shape : {grayscale_image.shape}")
    print(f"Saved at        : {OUTPUT_PATH}")


if __name__ == "__main__":
    main()