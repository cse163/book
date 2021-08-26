import io
import unittest

from contextlib import redirect_stdout

from test.grading_utils import error_message

def capture_output(fun, *args):
    buf = io.StringIO()
    with redirect_stdout(buf):
        fun(*args)
        return buf.getvalue()


class Test(unittest.TestCase):
    def setUp(self):
        try:
            from dog import Dog
            self.Dog = Dog
        except:
            self.Dog = None

        try:
            from dog_pack import DogPack
            self.DogPack = DogPack
        except:
            self.DogPack = None

    def assert_loaded(self, classes):
        attrs = self.__dict__
        for c in classes:
            self.assertTrue(attrs[c] is not None, f'Error importing {c}')

    def test_dog_fields(self):
        """
        #name(Problem 0: Has required field and they are private)
        """
        self.assert_loaded(['Dog'])

        dog = self.Dog('Chester')
        attrs = dog.__dict__
        self.assertTrue('_name' in attrs, 'Should have a private field named name')
        self.assertFalse('name' in attrs, 'Should not have a public field named name')
        self.assertEquals('Chester', dog._name, error_message('Chester', dog._name))

        try:
            dog.bark()
        except:
            raise AssertionError('Program crashed when we called bark')

    def test_dogpack_constructor(self):
        """
        #name(Problem 1: Test constructor)
        """
        self.assert_loaded(['Dog', 'DogPack'])

        dogpack = self.DogPack()

        attrs = dogpack.__dict__
        self.assertTrue('_dogs' in attrs, 'Should have a private field named dogs')

        self.assertEquals([], dogpack._dogs, error_message([], dogpack._dogs))

    def test_add_dog_(self):
        """
        #name(Problem 1: Test add_dog)
        """
        self.assert_loaded(['Dog', 'DogPack'])

        dogpack = self.DogPack()
        dogpack.add_dog(self.Dog('FirstDog'))
        dogpack.add_dog(self.Dog('SecondDog'))

        val = len(dogpack._dogs)
        self.assertEquals(2, val, error_message(2, val, 'Length of dogs field'))

        val = dogpack._dogs[0]._name
        self.assertEquals('FirstDog', val, error_message('FirstDog', val, "First Dog's Name"))

        val = dogpack._dogs[1]._name
        self.assertEquals('SecondDog', val, error_message('SecondDog', val, "Second Dog's Name"))

    def test_all_bark(self):
        """
        #name(Problem 1: Test all_bark)
        """
        self.assert_loaded(['Dog', 'DogPack'])

        dogpack = self.DogPack()
        dogpack.add_dog(self.Dog('FirstDog'))
        dogpack.add_dog(self.Dog('SecondDog'))
        dogpack.add_dog(self.Dog('ThirdDog'))


        val = capture_output(dogpack.all_bark)
        ans = """FirstDog: Woof
SecondDog: Woof
ThirdDog: Woof"""
        self.assertEqual(ans.strip(), val.strip(), error_message(ans, val))

        with open('dog_pack.py') as f:
            file_contents = f.read()
            self.assertFalse('._name' in file_contents, 'DogPack should not refer to the private fields of Dog')

