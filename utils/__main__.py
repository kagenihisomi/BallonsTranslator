import cv2
from fire import Fire
from utils.textblock_mask import connected_canny_flood


def process_image(image_path):
    # Load the image from the given path
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Image not found or unable to open: {image_path}")

    # Call the connected_canny_flood function with the loaded image
    return connected_canny_flood(img)#, show_process=True)


if __name__ == "__main__":
    # Expose the process_image function to the command line
    Fire(process_image)
