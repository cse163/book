import io

import unittest

from contextlib import redirect_stdout

from test.grading_utils import assert_equals, error_message
from student import Student


def capture_output(fun, *args):
    buf = io.StringIO()
    with redirect_stdout(buf):
        fun(*args)
    return buf.getvalue()


def import_client():
    import main
    return main


class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        self.arlo = Student(1231231, 'arlo.txt')
        self.pablo = Student(1551515, 'pablo.txt')
        self.suzie = Student(1111111, 'test/suzie.txt')
        self.empty = Student(10, 'test/empty.txt')

    def compare_student(self, student, name=None,
                        student_num=None, classes=None):
        if name is not None:
            assert_equals(self, name, student.name)

        if student_num is not None:
            assert_equals(self, student_num, student.student_number)

        if classes is not None:
            self.assertEquals(len(classes), len(student.classes),
                             f'Expected classes field to have {len(classes)} classes but found {len(student.classes)}')
            for c in classes:
                self.assertTrue(c in student.classes, f'Expected classes to have key {c}')
                assert_equals(self, classes[c], student.classes[c])

            self.assertEquals(student.classes.keys(), classes.keys(), f'Expected field to have the same classes as were originally provided')


    def test_initializer_example(self):
        """
        #name(Call Student initializer on arlo_schedule.txt)
        """
        self.compare_student(self.arlo,
                             name='arlo',
                             student_num=1231231,
                             classes={
                                 'CSE163': 4,
                                 'MATH126': 5,
                                 'PHYS123': 5,
                                 'CSE373': 4
                             })

    def test_initializer_single(self):
        """
        #name(Call Student initializer on single-line file)
        """
        self.compare_student(self.suzie,
                             name='suzie',
                             student_num=1111111,
                             classes={'CMS302': 3})

    def test_initializer_empty(self):
        """
        #name(Call Student initializer on empty file)
        """
        self.compare_student(self.empty,
                             name='empty',
                             student_num=10,
                             classes={})

    def test_get_name(self):
        """
        #name(Student get_name correct for Arlo)
        """
        assert_equals(self, 'arlo', self.arlo.get_name())

    def test_get_student_number(self):
        """
        #name(Student student_number correct for Pablo)
        """
        assert_equals(self, 1551515, self.pablo.get_student_number())

    def test_get_credits_for_example(self):
        """
        #name(Student get_credits_for('CSE163'\) correct for Arlo)
        """
        assert_equals(self, 4, self.arlo.get_credits_for('CSE163'))

    def test_get_credits_for_single(self):
        """
        #name(Student get_credits_for('SOMECLASS'\) correct when class not taken)
        """
        assert_equals(self, None, self.suzie.get_credits_for('CSE153'))

    def test_get_credits_for_empty(self):
        """
        #name(Student get_credits_for('SOMECLASS'\) correct when class not taken)
        """
        assert_equals(self, None, self.empty.get_credits_for('CSE153'))

    def test_get_classes(self):
        """
        #name(get correct classes for arlo)
        """
        assert_equals(self, ['CSE163','MATH126','PHYS123','CSE373'], self.arlo.get_classes())

    def test_uses_main_method_pattern(self):
        """
        #name(Uses main method pattern)
        """
        val = capture_output(import_client)
        ans = ''
        self.assertEqual(ans, val, 'Code does not use main method pattern')

    def test_client(self):
        """
        #name(Test main produces right output)
        """
        import main
        val = capture_output(main.main)
        ans = '''pablo 1551515 None
arlo 1231231 4'''
        self.assertEqual(ans.strip(), val.strip(), error_message(ans, val))


