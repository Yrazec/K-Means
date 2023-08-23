"""File for storing Graphical User Interface feature."""

import matplotlib.pyplot as plt
import numpy as np

from libs.k_means import KMeans


class InvalidData(Exception):
    """Exception regarding invalid data."""


class GUI:
    """
    Class responsible for launching the functionality of the Graphical User Interface and some algorithms
    (like K-Means algorithm).
    """

    _TITLE_BASE = 'K-Means'
    _WINDOW_TITLE = _TITLE_BASE

    @staticmethod
    def run_and_draw_kmeans(random_points: int, clusters: int) -> None:
        """
        Static method responsible for starting the drawing of the graph and performing calculations for the
        K-Means algorithm.
        """

        if (clusters > 6) or (clusters < 1):
            raise InvalidData(' '.join([
                'The number of clusters is less than 1 or greater than 6!',
                'You can only enter values: 1, 2, 3, 4, 5 or 6.'
            ]))

        plt.figure().canvas.manager.set_window_title(GUI._WINDOW_TITLE)

        plt.title(GUI._TITLE_BASE)

        points_colors = ['r', 'g', 'b', 'c', 'm', 'y']
        centroids_color = 'k'  # Black
        centroids_shape = 's'  # Square

        random_array = np.random.rand(random_points, 2)

        plt.title(f'{GUI._TITLE_BASE} • Clusters: {clusters}, points: {len(random_array)}')

        kmeans = KMeans(k=clusters, data=random_array)
        kmeans.run_kmeans()

        x_coordinates = [centroid_coordinates['x'] for centroid_id, centroid_coordinates in kmeans.centroids.items()]
        y_coordinates = [centroid_coordinates['y'] for centroid_id, centroid_coordinates in kmeans.centroids.items()]
        clusters_x_coordinates = x_coordinates.copy()
        clusters_y_coordinates = y_coordinates.copy()

        for _, point_data in kmeans.points.items():
            x_coordinates = point_data['x']
            y_coordinates = point_data['y']
            if point_data['closest_centroid']['id']:
                centroid_color_index = int(point_data['closest_centroid']['id']) - 1
            else:
                centroid_color_index = 6
            plt.plot(x_coordinates, y_coordinates, f'{points_colors[centroid_color_index]}o')

        plt.plot(clusters_x_coordinates, clusters_y_coordinates, f'{centroids_color}{centroids_shape}')

        plt.show()
