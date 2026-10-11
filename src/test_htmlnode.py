import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_01(self):
        node = HTMLNode("a", "text to be linked", None, {"href": "https://www.boot.dev", "target": "_blank"})
        actual = str(node)
        expected = "HTMLNode(a, text to be linked, None, {'href': 'https://www.boot.dev', 'target': '_blank'})"
        self.assertEqual(actual, expected)

    def test_props_to_html_02(self):
        node = HTMLNode("b", "bolded text", None, None)
        actual = str(node)
        expected = "HTMLNode(b, bolded text, None, None)"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
