import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node1 = TextNode("This is also a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is also a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node1, node2)

    def test_eq_url_none(self):
        node1 = TextNode("Yet more text", TextType.CODE, None)
        node2 = TextNode("Yet more text", TextType.CODE, None)
        self.assertEqual(node1, node2)

    def test_not_eq_text(self):
        node1 = TextNode("First text", TextType.TEXT)
        node2 = TextNode("Second text", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_not_eq_type(self):
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same test", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_eq_url(self):
        node1 = TextNode("Same text", TextType.CODE, "https://www.boot.dev")
        node2 = TextNode("Same test", TextType.CODE, "https://www.google.com")
        self.assertNotEqual(node1, node2)

    def test_text_to_html(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()
