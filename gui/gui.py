"""File for storing Graphical User Interface feature."""

import matplotlib.pyplot as plt
import numpy as np

from libs.k_means import KMeans


class GUI:
    """
    Class responsible for launching the functionality of the Graphical User Interface and some algorithms
    (like K-Means algorithm).
    """

    _TITLE_BASE = 'K-Means'

    @staticmethod
    def run_and_draw_kmeans(random_points: int, clusters: int) -> None:
        """
        Static method responsible for starting the drawing of the graph and performing calculations for the
        K-Means algorithm.
        """

        plt.title(GUI._TITLE_BASE)

        colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']

        random_array = np.random.rand(random_points, 2)

        plt.title(f'{GUI._TITLE_BASE} • Clusters: {clusters}, points: {len(random_array)}')

        kmeans = KMeans(k=clusters, data=random_array)
        kmeans.run_kmeans()

        x_coordinate = [centroid_coordinates['x'] for centroid_id, centroid_coordinates in kmeans.centroids.items()]
        y_coordinate = [centroid_coordinates['y'] for centroid_id, centroid_coordinates in kmeans.centroids.items()]
        plt.plot(x_coordinate, y_coordinate, 'ks')

        for _, point_data in kmeans.points.items():
            x_coordinate = point_data['x']
            y_coordinate = point_data['y']
            if point_data['closest_centroid']['id']:
                centroid_color_index = int(point_data['closest_centroid']['id']) - 1
            else:
                centroid_color_index = 6
            plt.plot(x_coordinate, y_coordinate, f'{colors[centroid_color_index]}o')

        plt.show()
