import unittest

class TestStringMethods(unittest.TestCase):
    # tests should always have prefix "test"
    def test_upper(self):
        # assertEqual checks for an expected result
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        #to verify the condition
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()