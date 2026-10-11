import unittest

from blocktype import *
from markdownfunctions import *


class TestBlockType(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        blocks = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
            "> first line of quote\n> second line of quote",
            "## heading",
            "```\nPretend this is some code\nthat continues onto a second line\n```",
            "1. first item\n2. second item\n3. third item",
        ]
        types = [
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
            BlockType.UNORDERED_LIST,
            BlockType.QUOTE,
            BlockType.HEADING,
            BlockType.CODE,
            BlockType.ORDERED_LIST,
        ]
        for block, type in zip(blocks, types, strict=True):
            self.assertEqual(block_to_block_type(block), type)
