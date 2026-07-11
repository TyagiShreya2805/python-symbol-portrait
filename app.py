from pathlib import Path

import cv2


#INPUT_PATH = Path("input/portrait.jpg")
#OUTPUT_PATH = Path("output/grayscale_portrait.jpg") 
# we have changed the above two lines with the below project root so that if we run this file through terminal or vs code we dont get any error. VS code shows an error
# because it is looking for the directory and cannot find the image. Professionals solve this issue by using PROJECT ROOT
PROJECT_ROOT = Path(__file__).parent

INPUT_PATH = PROJECT_ROOT / "input" / "portrait.jpg"

OUTPUT_PATH = PROJECT_ROOT / "output" / "grayscale_portrait.jpg"

def load_image(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"Image not found: {path}")

    image = cv2.imread(str(path))

    if image is None:
        raise ValueError("Unable to read the image.")

    return image


def convert_to_grayscale(image):
    grayscale_image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY,
    )

    return grayscale_image


def save_image(image, path: Path):
    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    saved = cv2.imwrite(
        str(path),
        image,
    )

    if not saved:
        raise RuntimeError("Unable to save the image.")


def main():
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