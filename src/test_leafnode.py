import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_01(self):
        actual = LeafNode("p", "This is a paragraph of text.").to_html()
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(actual, expected)

    def test_to_html_02(self):
        actual = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(actual, expected)

    def test_repr_01(self):
        actual = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).__repr__()
        expected = "LeafNode(a, Click me!, {'href': 'https://www.google.com'})"
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
