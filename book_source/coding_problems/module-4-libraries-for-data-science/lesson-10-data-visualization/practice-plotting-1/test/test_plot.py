import unittest

import main
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set()


class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        main.main()

        self.attempt_title = plt.gca().get_title()
        self.attempt_x_label = plt.gca().get_xlabel()
        self.attempt_y_label = plt.gca().get_ylabel()

        plt.close()

    def test_labels(self):
        assert (
            self.attempt_title == "Petal Width vs Length"
        ), f'Expected the plot to have "Petal Width vs Length" as the title, but received "{self.attempt_title}"'
        assert (
            self.attempt_x_label == "Petal Width (cm)"
        ), f'Expected the plot to have "Petal Width (cm)" as the x-axis label, but received "{self.attempt_x_label}"'
        assert (
            self.attempt_y_label == "Petal Length (cm)"
        ), f'Expected the plot to have "Petal Length (cm)" as the y-axis label, but received "{self.attempt_y_label}"'

    def test_plot(self):
        # Read attempt and solution
        attempt = plt.imread("plot.png")
        soln = plt.imread("test/expected.png")

        assert attempt.shape == soln.shape, (
            f"Expected a {soln.shape[0]} by {soln.shape[1]} plot, but received {attempt.shape[0]} by {attempt.shape[1]}"
            + "\nYou might want to run your solution and compare your plot visually with the one shown in the description"
        )

        close = np.isclose(attempt[:, :, :3], soln[:, :, :3])

        score = close.sum() / close.size
        assert score > 0.95, (
            f"Expected graphs to match, current match: {score * 100:.2f}%"
            + "\nCheck that your plot looks the same as the one in the description!"
        )


if __name__ == "__main__":
    unittest.main()

