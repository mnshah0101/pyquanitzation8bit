import numpy as np
from itertools import combinations_with_replacement


class KMeans:
    def __init__(self, array, k, iters):
        self.array = np.asarray(array)
        self.k = k
        self.iterations = iters
        self.raveled = self.array.ravel()
        self.iteration = 0
        self.clusters = np.random.randint(256, size=(1, k))
        self.previous_clusters = np.zeros((1, k))
        self.distance_array = np.zeros((self.raveled.size, k))

    def train(self):
        x = self.raveled.reshape(-1, 1)
        print('training')
        while (self.iteration < self.iterations):
            print("Iteration: " + str(self.iteration))
            self.previous_clusters = np.vstack(
                (self.previous_clusters, self.clusters))
            np.abs(np.array([1, 2, 3, 4, 5]) - 3)
            for i in range(len(self.raveled)):
                self.distance_array[i] = np.abs(self.raveled[i]-self.clusters)

            min_indices = np.argmin(self.distance_array, axis=1)

            min_values = np.min(self.distance_array, axis=1)

            new_matrix = np.zeros((self.clusters.size, self.raveled.size))

            for i in range(self.clusters.size):
                col_index = min_indices[i]
                new_matrix[i, col_index] = self.raveled[i]

            non_zero_rows = new_matrix[~np.all(new_matrix == 0, axis=1)]

            self.clusters = (
                self.clusters + np.mean(non_zero_rows, axis=1)).astype(int)

            if (self._converged()):
                break

            self.iteration += 1

    def _converged(self):

        if (self.clusters == self.previous_clusters[-1]).all():
            print('converged')
            return True
        else:
            return False

    def predict(self):
        differences = np.abs(self.raveled[:, np.newaxis] - self.clusters)

        closest_indices = np.argmin(differences, axis=1)

        closest_integers = self.clusters.reshape(-1, 1)[closest_indices]

        return closest_integers.reshape((-1, 3))

    def getPallette(self):
        clusters = self.clusters.tolist()[0]
        pallette = list(combinations_with_replacement(clusters, 3))
        return pallette
