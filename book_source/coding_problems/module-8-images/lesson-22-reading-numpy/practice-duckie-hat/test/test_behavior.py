import unittest

import imageio
import main
import numpy as np


class TestBehavior(unittest.TestCase):
    def _test_and_compare_images(self, img, expected_path):
        old_image = img.copy()

        solution = np.load(expected_path)

        student = main.duckie_hat(img)

        self.assertTrue(
            np.all(np.isclose(old_image, img)), "Function should not modify input image"
        )
        self.assertEquals(
            solution.shape,
            student.shape,
            f"Expected {solution.shape}, Received {student.shape}",
        )
        self.assertTrue(
            np.all(np.isclose(solution, student)),
            f"Returned image does not match expected one",
        )

    def test_example(self):
        """
        #name(Using example image: duck.jpg)
        """
        duck = imageio.imread("duck.jpg")
        self._test_and_compare_images(duck, "test/expected_out.npy")

    def test_larger_image(self):
        """
        #name(Test with a larger image of a duck)
        """
        scale_height, scale_width = (2, 2)
        duck = imageio.imread("duck.jpg")
        height, width, channels = duck.shape
        new_duck = np.zeros((height * scale_height, width * scale_width, channels))
        for i in range(scale_height):
            for j in range(scale_width):
                new_duck[
                    i * height : (i + 1) * height, j * width : (j + 1) * width, :
                ] = duck
        self._test_and_compare_images(new_duck, "test/expected_large_out.npy")
