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
        self.clusters = []

    def floyd_steinberg_dithering_bw(self):
        self.train_image()
        image = self.image.convert('L')

        img_array = np.array(image)

        palette = np.array(self.clusters, dtype=np.uint8).reshape((-1, 1))

        error = np.zeros_like(img_array, dtype=np.float32)

        height, width = img_array.shape

        for y in range(height):
            for x in range(width):
                old_pixel = img_array[y, x]
                new_pixel = np.argmin(np.abs(palette - old_pixel))
                img_array[y, x] = palette[new_pixel]
                quant_error = old_pixel - palette[new_pixel]

                if x < width - 1:
                    error[y, x + 1] += quant_error * 7 / 16
                if y < height - 1:
                    if x > 0:
                        error[y + 1, x - 1] += quant_error * 3 / 16
                    error[y + 1, x] += quant_error * 5 / 16
                    if x < width - 1:
                        error[y + 1, x + 1] += quant_error * 1 / 16

        dithered_image = PIL.Image.fromarray(img_array)
        return dithered_image

    def floyd_steinberg_dithering_color(self):
        self.train_image()

        img_array = np.array(self.image)

        palette = np.array(self.clusters, dtype=np.uint8).reshape((-1, 1))

        # Initialize error matrices for each channel
        error_r = np.zeros_like(img_array[:, :, 0], dtype=np.float32)
        error_g = np.zeros_like(img_array[:, :, 1], dtype=np.float32)
        error_b = np.zeros_like(img_array[:, :, 2], dtype=np.float32)

        height, width, _ = img_array.shape

        for y in range(height):
            for x in range(width):
                for channel in range(3):  # 0: Red, 1: Green, 2: Blue
                    old_pixel = img_array[y, x, channel]
                    new_pixel = np.argmin(np.abs(palette - old_pixel))
                    img_array[y, x, channel] = palette[new_pixel]
                    quant_error = old_pixel - palette[new_pixel]

                    # Distribute the error to neighboring pixels
                    if x < width - 1:
                        if channel == 0:
                            error_r[y, x + 1] += quant_error * 7 / 16
                        elif channel == 1:
                            error_g[y, x + 1] += quant_error * 7 / 16
                        else:
                            error_b[y, x + 1] += quant_error * 7 / 16
                    if y < height - 1:
                        if x > 0:
                            if channel == 0:
                                error_r[y + 1, x - 1] += quant_error * 3 / 16
                            elif channel == 1:
                                error_g[y + 1, x - 1] += quant_error * 3 / 16
                            else:
                                error_b[y + 1, x - 1] += quant_error * 3 / 16
                        if channel == 0:
                            error_r[y + 1, x] += quant_error * 5 / 16
                        elif channel == 1:
                            error_g[y + 1, x] += quant_error * 5 / 16
                        else:
                            error_b[y + 1, x] += quant_error * 5 / 16
                        if x < width - 1:
                            if channel == 0:
                                error_r[y + 1, x + 1] += quant_error * 1 / 16
                            elif channel == 1:
                                error_g[y + 1, x + 1] += quant_error * 1 / 16
                            else:
                                error_b[y + 1, x + 1] += quant_error * 1 / 16

        dithered_image = PIL.Image.fromarray(img_array)
        return dithered_image

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
        self.clusters = kmeans.clusters
        return np.array(self.smaller_image, dtype=np.uint8).reshape(self.array.shape)
