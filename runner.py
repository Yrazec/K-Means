"""Runner file for K-Means wrapped in GUI."""

from gui.gui import GUI


def main():
    """Standard main function."""

    # Maximum clusters is 6 because there are 6 colors ('r', 'g', 'b', 'c', 'm', 'y' and 'k' but only for centroids)
    GUI.run_and_draw_kmeans(random_points=300, clusters=4)


if __name__ == "__main__":
    main()
