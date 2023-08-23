"""Runner file for K-Means wrapped in GUI."""

from gui.gui import GUI

# Maximum clusters is 6 because there are 6 colors
# ('r', 'g', 'b', 'c', 'm', 'y' and 'k' but only for centroids)
CLUSTERS = 6
POINTS = 600


def main():
    """Standard main function."""

    GUI.run_and_draw_kmeans(random_points=POINTS, clusters=CLUSTERS)


if __name__ == "__main__":
    main()
