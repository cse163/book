import unittest

import imageio
import main
import numpy as np


class TestBehavior(unittest.TestCase):
    def _test_and_compare_images(
        self,
        img,
        expected_file_path,
        assert_dtype=None,
        assert_unmodified=True,
        show_value_error=True,
    ):
        old_image = img.copy()

        solution = np.load(expected_file_path)

        student = main.collapse(img)

        if assert_unmodified:
            self.assertTrue(
                np.all(np.isclose(old_image, img)),
                "Function should not modify input image",
            )
        if assert_dtype:
            self.assertEquals(
                assert_dtype,
                student.dtype,
                f"Expected dtype {assert_dtype} but received {student.dtype}",
            )

        self.assertEquals(
            solution.shape,
            student.shape,
            f"Expected {solution.shape}, Received {student.shape}",
        )

        if show_value_error:
            msg = f"Expected values {solution}, Received {student}"
        else:
            msg = f"Returned result does not match expected one"
        self.assertTrue(np.all(np.isclose(solution, student)), msg)

    def test_example(self):
        """
        #name(Using example from spec)
        """
        values = np.arange(12).reshape((3, 4))
        self._test_and_compare_images(
            values, "test/example_out.npy", assert_dtype="int64"
        )

    def test_larger_image(self):
        """
        #name(Test with a larger image of a penguin)
        """
        penguin = imageio.imread("test/penguin.jpg")
        self._test_and_compare_images(
            penguin, "test/large_example_out.npy", assert_dtype="int64"
        )
