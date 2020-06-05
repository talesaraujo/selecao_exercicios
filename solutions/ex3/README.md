# cats-vs-dogs classifier

This tool aims to make guesses over some *kitties* and some *doggos*' photos, intending to properly identify them. A deep neural network has been pre-trained for such purpose, and the two notebook files provided the basis for the main script development.

The way these files were placed helped model improvement and made it possible to tweak it with a fairly ease, allowing it to further tweaking as well. They have yielded a file with the optimum weights meant to be loaded into the actual classifier model.

[Jump to usage](#usage)

## The problem
To *correctly* classify images. In this example, dogs and cats. To do so, the analysis was based on the Kaggle's [`dogs-vs-cats`](https://www.kaggle.com/c/dogs-vs-cats/) dataset in order to build and train the model.

## The model
### Convolutional Neural Network
Convolutional Neural Networks (or CNNs) are a category of Neural Networks that have proven quite effective in areas such as image classification and recognition. There are basically four main operations performed by a CNN, and they are:

- **Convolution:** Tries to extract features from the input image. It preserves the spatial relationship between pixels by learning image features using small squares of input data.
- **NonLinearity (ReLU):** An element wise operation (applied per pixel), it replaces all negative pixel values in the feature map by zero. Adds non-linearity, compatible with real-world problems.
- **Pooling or SubSampling:** Reduces the dimensionality of each feature map but retains the most important information. An excelent performance promoter.
- **Classification:** Performed by a tradicional neural network, the purpose of this operation is to make use of the high-level features from the previous layers for classifying the input image into one of the classes on the training dataset.

###  Model architecture
Three convolution steps (convolution + nonlinearity + pooling) were added in a row to the model, each of which apply progressively 32, 64 and 128 filters over the image tensor, additionally to a dropout layer in order to increase regularization and attempt to avoid overfitting.

## Usage
### Requirements
```bash
pip install -r requirements.txt
```

### How to classify an image
```bash
python classificar.py --input '/path/to/image'
```
You can use the optional flag `--show` to display the image as well.
