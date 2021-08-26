import ast
import io
import unittest

from contextlib import redirect_stdout

from test.grading_utils import error_message

from my_set import MySet


def capture_output(fun, *args):
    buf = io.StringIO()
    with redirect_stdout(buf):
        fun(*args)
    return buf.getvalue()


def import_client():
    import my_set_client
    return my_set_client


class NoLoops(ast.NodeVisitor):
    def __init__(self):
        self.has_loops = False

    def visit_FunctionDef(self, node):
        # Ignore checking __init__
        if node.name != '__init__':
            self.generic_visit(node)

    def visit_For(self, node):
        self.has_loops = True

    def visit_While(self, node):
        self.has_loops = True


class NoSpecialCalls(ast.NodeVisitor):
    def __init__(self):
        self.has_special_calls = False

    def visit_Call(self, node):
        if type(node.func) is ast.Attribute:
            name = node.func.attr
        elif type(node.func) is ast.Name:
            name = node.func.id

        self.generic_visit(node)
        if name.startswith('__') and name.endswith('__'):
            self.has_special_calls = True


def has_loops(file_name):
    with open(file_name) as f:
        source = ast.parse(f.read())
        nl = NoLoops()
        nl.visit(source)
        return nl.has_loops


def has_special_calls(file_name):
    with open(file_name) as f:
        source = ast.parse(f.read())
        nl = NoSpecialCalls()
        nl.visit(source)
        return nl.has_special_calls


class Test(unittest.TestCase):
    def test_constructor(self):
        """
        #name(Test empty set contains no values and has len 0)
        """
        ms = MySet()

        ans = 0
        val = len(ms)
        self.assertEquals(ans, val, f'Expected {ans}, but received {val}')

        self.assertFalse(2 in ms, 'Empty MySet should not contain any values')

    def test_set_with_one_element(self):
        """
        #name(Test set after adding value 4)
        """
        ms = MySet()

        ms.add(4)

        ans = 1
        val = len(ms)
        self.assertEquals(ans, val, f'Expected {ans}, but received {val}')

        self.assertFalse(2 in ms, '{4} hould not contain the value 2')
        self.assertTrue(4 in ms, '{4} should contain the value 4')
        self.assertFalse(0 in ms, '{4} should not contain the value 0')

    def test_set_with_two_elements(self):
        """
        #name(Test set after adding value 20 and 39)
        """
        ms = MySet()

        ms.add(20)
        ms.add(39)

        ans = 2
        val = len(ms)
        self.assertEquals(ans, val, f'Expected {ans}, but received {val}')

        self.assertFalse(2 in ms, '{20, 39} hould not contain the value 2')
        self.assertTrue(20 in ms, '{20, 39} should contain the value 20')
        self.assertTrue(39 in ms, '{20, 39} should contain the value 39')

    def test_set_with_duplicates(self):
        """
        #name(Test set after adding value 20, 14, 39, 14)
        """
        ms = MySet()

        ms.add(20)
        ms.add(14)
        ms.add(39)
        ms.add(14)

        ans = 3
        val = len(ms)
        self.assertEquals(ans, val, f'Expected {ans}, but received {val}')

        self.assertFalse(2 in ms, '{14, 20, 39} hould not contain the value 2')
        self.assertTrue(20 in ms, '{14, 20, 39} should contain the value 20')
        self.assertTrue(20 in ms, '{14, 20, 39} should contain the value 14')
        self.assertTrue(39 in ms, '{14, 20, 39} should contain the value 39')

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
        import my_set_client
        val = capture_output(my_set_client.main)
        ans = '''True
False
3'''
        self.assertEqual(ans.strip(), val.strip(), error_message(ans, val))

    def test_constant_time(self):
        """
        #name(MySet implements all methods in constant time)
        """
        self.assertFalse(has_loops('my_set.py'),
                         'MySet methods should all run in O(1) time')

    def test_no_special_methods(self):
        """
        #name(You shouldn't call special methods (e.g., __len__\) directly)
        """
        files = ['my_set.py', 'my_set_client.py']
        for f in files:
            self.assertFalse(has_special_calls(f),
                             'Should not call special methods directly')
