import unittest

from blocktype import *
from markdownfunctions import *


class TestMarkdownFunctions(unittest.TestCase):
    def test_to_html_node_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_to_html_node_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_extract_title(self):
        inputs = [
            "# title text",
            "leading text\n\n# title on third line",
            "# first title\n# second title",
        ]
        expected = [
            "title text",
            "title on third line",
            "first title"
        ]
        self.assertListEqual(expected, [extract_title(input) for input in inputs])

    def test_extract_title_valueerror(self):
        strings = [
            " # has a space in front, so not title",
            "## not a title header",
            "#single hash but no space",
        ]
        for string in strings:
            self.assertRaises(ValueError, extract_title, string)
