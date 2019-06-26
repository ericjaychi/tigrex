import cv2
import requests
import shutil


def main():
    get_card()
    apply_threshold()


def get_card():

    url = "https://api.scryfall.com/cards/named?exact=watery+grave&format=image"

    response = requests.get(url, stream=True)

    # TODO: Need to create a constant for the images
    # TODO: Might need to get the card name or something so that it can added into
    # Opens a file with the image name. Has write access and binary access.
    with open("images/img.jpg", "wb") as output_file:
        shutil.copyfileobj(response.raw, output_file)
    del response


def apply_threshold():
    # Load an color image in grayscale
    original = cv2.imread("images/img.jpg")
    greyscale = cv2.imread("images/img.jpg", 0)

    # Is pretty good for stock images from the looks of it.
    retval, threshold = cv2.threshold(greyscale, 125, 255, cv2.THRESH_BINARY)

    # Might be better for worse lighting, but for stock images, its pretty bad.
    gaussian = cv2.adaptiveThreshold(greyscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

    cv2.imshow("original", original)
    cv2.imshow("greyscale", greyscale)

    cv2.imshow("threshold", threshold)
    cv2.imshow("gaussian", gaussian)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


main()
