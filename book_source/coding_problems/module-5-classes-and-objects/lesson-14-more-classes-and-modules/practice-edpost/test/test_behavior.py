import io
import unittest

from contextlib import redirect_stdout

from test.grading_utils import error_message

from ed_post import EdPost


class Test(unittest.TestCase):
    def test_fields(self):
        """
        #name(Has required fields and they are private)
        """
        post = EdPost('Name', 'Tag', ['Comment'])
        attrs = post.__dict__
        self.assertTrue('_title' in attrs, 'Should have a private field named title')
        self.assertTrue('_tag' in attrs, 'Should have a private field named tag')
        self.assertTrue('_comments' in attrs, 'Should have a private field named comments')

    def test_get_title(self):
        """
        #name(Test constructor and get_title)
        """
        post = EdPost('Name', 'Foo', [])

        val = post.get_title()
        ans = 'Name'
        self.assertEquals(ans, val, error_message(ans, val))

    def test_get_tag_default(self):
        """
        #name(Test constructor and get_tag (when default parameter\))
        """
        post = EdPost('Name')

        val = post.get_tag()
        ans = 'General'
        self.assertEquals(ans, val, error_message(ans, val))

    def test_get_tag_provide(self):
        """
        #name(Test constructor and get_tag (when parameter provided\))
        """
        post = EdPost('Name', 'SomeTag')

        val = post.get_tag()
        ans = 'SomeTag'
        self.assertEquals(ans, val, error_message(ans, val))

    def test_add_comment_default(self):
        """
        #name(Test add_comment when using default parameter)
        """
        post = EdPost('Name')
        post.add_comment('Comment 1')
        post.add_comment('Comment 2')

        ans = ['Comment 1', 'Comment 2']
        val = post._comments
        self.assertEquals(ans, val, error_message(ans, val))

    def test_add_comment(self):
        """
        #name(Test add_comment when comments initially specified)
        """
        post = EdPost('Name', 'Tag', ['First Comment'])
        post.add_comment('Second Comment')
        ans = ['First Comment', 'Second Comment']
        val = post._comments
        self.assertEquals(ans, val, error_message(ans, val))

    def test_multiple_posts(self):
        """
        #name(Test creating multiple posts)
        """
        post1 = EdPost('Name1', 'Tag1')
        post2 = EdPost('Name2')

        post1.add_comment('Comment 1')
        post2.add_comment('Comment 2')

        ans = ['Comment 1']
        val = post1._comments
        self.assertEquals(ans, val, error_message(ans, val))

        ans = ['Comment 2']
        val = post2._comments
        self.assertEquals(ans, val, error_message(ans, val))

    @staticmethod
    def capture_output(fun, *args):
        buf = io.StringIO()
        with redirect_stdout(buf):
            fun(*args)
        return buf.getvalue()


    def test_display(self):
        """
        #name(Test display for example from spec)
        """

        ed_post = EdPost('Typo in spec?', 'Assignment 1')
        ed_post.add_comment('There was a typo!')
        val = Test.capture_output(ed_post.display)
        ans = """Typo in spec? (Assignment 1)
Comments:
  There was a typo!"""
        self.assertEqual(ans.strip(), val.strip(), error_message(ans, val))

