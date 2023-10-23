import PIL
import numpy as np
import matplotlib.pyplot as plt
from KMeans import KMeans
from itertools import combinations


class Image:

    def __init__(self, path, colors):
        self.path = path

        new_path = self.path.split(".")
        new_path[0] += str(colors)
        self.new_path = (".").join(new_path)

        self.k = colors

        try:
            self.image = PIL.Image.open(path)
        except:
            print("Print a valid Picture")
        self.array = np.asarray(self.image)

        self.raveled_array = self.array.ravel()

        self.smaller_image = []
        self.pallette = 0

    def create_image(self, array):
        array = np.array(array, dtype=np.uint8).reshape(self.array.shape)
        return_image = PIL.Image.fromarray(array)
        return self.save_image(return_image)

    def save_image(self, img):
        try:
            img.save(self.new_path, format="PNG")
            return True
        except:
            return False

    def graph_image_channels(self):
        plt.figure(figsize=(16, 6))
        plt.hist(self.raveled_array, bins=np.arange(
            256), density=True, linewidth=0)
        plt.xlabel("Value")
        plt.ylabel("Density")

    def train_image(self):
        kmeans = KMeans(self.raveled_array, self.k, 100)
        kmeans.train()
        self.smaller_image = kmeans.predict()
        self.pallette = np.array(kmeans.getPallette()).ravel()
        return np.array(self.smaller_image, dtype=np.uint8).reshape(self.array.shape)
