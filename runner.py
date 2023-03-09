"""Runner file for K-Means wrapped in GUI."""

from gui.gui import GUI


def main():
    """Standard main function."""

    GUI.run_and_draw_kmeans(random_points=10000, clusters=6)


if __name__ == "__main__":
    main()
