import matplotlib
matplotlib.use("Agg")

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential 
from keras.layers import Activation 
from keras.optimizers import SGD
from keras.layers import Dense
from keras.utils import np_utils
from imutils import paths
import os
import argparse
import pickle
import numpy as np
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
        help="dataset of images")
ap.add_argument("-m", "--model", required=True,
        help="output of trained model")
ap.add_argument("-l", "--label-bin", required=True,
        help="label binarizer")
args = vars(ap.parse_args())


data = []
labels = []

# grabs the image and randomly shuffles it
imagePaths = sorted(list(paths.list_image(args["dataset"])))
random.seed(42)
random.shuffle(imagePaths)
