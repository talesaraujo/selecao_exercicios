#!/usr/bin/env python3
import os, sys
import argparse
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

from keras.preprocessing import image
from cnn import create_model


# Get rid of tf logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# Load model pretrained weights
MODEL_WEIGHTS = 'model_weights_20200605035425.h5'
# Make image dimentions default
IMG_HEIGHT, IMG_WIDTH = (200, 200)


def load_image(img_path):

    img = image.load_img(img_path, target_size=(IMG_HEIGHT, IMG_WIDTH))
    
    # (height, width, channels)
    img_tensor = image.img_to_array(img)                    

    # (1, height, width, channels), add a dimension because the model expects this shape:
    # (batch_size, height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         

    # imshow expects values in the range [0, 1]
    img_tensor /= 255.                                     

    return img_tensor


def classify(model, img_path):
    # Load a single image
    new_image = load_image(img_path)

    # Check prediction
    pred = model.predict(new_image)

    prob = pred[0][0]

    print("DOG") if prob > 0.5 else print("CAT")

    return prob


def show_image(img_path):
    img = cv.imread(img_path)
    
    # Convert to RGB
    b,g,r = cv.split(img)  # get b, g, r
    rgb_img = cv.merge([r,g,b])

    plt.figure(figsize=(12, 6))
    plt.imshow(rgb_img)
    plt.show()


def main():
    model = create_model()
    model.load_weights(f"models/{MODEL_WEIGHTS}")

    parser = argparse.ArgumentParser(description="A cat-and-dog classifier")
    parser.add_argument('-i', '--input', help="The folder directory in which the image is located on")
    parser.add_argument('-s', '--show', action="store_true", help="Display the current image file")

    args = parser.parse_args()

    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)

    if args.input:
        try:
            classify(model, args.input)

            if args.show:
                show_image(args.input)

        except FileNotFoundError:
            print("Error: No such folder. Try again")
            sys.exit(1)

    
if __name__ == "__main__":
    main()
