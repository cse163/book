import ast
import os
import unittest

class NoLoops(ast.NodeVisitor):
    def __init__(self):
        self.has_loops = False

    def visit_For(self, node):
        self.has_loops = True

    def visit_While(self, node):
        self.has_loops = True

    def visit_ListComp(self, node):
        self.has_loops = True

    def visit_SetComp(self, node):
        self.has_loops = True

    def visit_DictComp(self, node):
        self.has_loops = True

    def visit_GeneratorExp(self, node):
        self.has_loops = True


def has_loops(file_name):
    with open(file_name) as f:
        source = ast.parse(f.read())
        nl = NoLoops()
        nl.visit(source)
        return nl.has_loops


class TestNoLoops(unittest.TestCase):
    def test_constant_time(self):
        """
        #name(Implemention does not use loops or comprehension)
        """
        for f in os.listdir('.'):
            if f.endswith('.py'):
                self.assertFalse(has_loops(f), f'{f} should not use loops or comprehensions')

