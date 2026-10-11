import re

from blocktype import *
from parentnode import ParentNode
from textnode import *


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = [block.strip() for block in markdown.split("\n\n")]
    blocks = list(filter(None, blocks))
    return blocks

def markdown_to_html_node(markdown: str) -> ParentNode:
    root = ParentNode("div", [])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        type = block_to_block_type(block)
        children = []
        text_nodes = None
        if type == BlockType.PARAGRAPH:
            tag = "p"
            text_nodes = text_to_textnodes(block.replace("\n", " "))
            children = [text_node_to_html_node(text_node) for text_node in text_nodes]
        elif type == BlockType.HEADING:
            count = len(block) - len(block.lstrip("#"))
            tag = f"h{count}"
            header = block[count+1:]
            text_nodes = text_to_textnodes(header)
            children = [text_node_to_html_node(text_node) for text_node in text_nodes]
        elif type == BlockType.CODE:
            tag = "pre"
            code_text = re.findall(r"```\n([\s\S]*?)```", block)[0]
            children = [text_node_to_html_node(TextNode(code_text, TextType.CODE))]
        elif type == BlockType.QUOTE:
            tag = "blockquote"
            lines = [line[2:] for line in block.split("\n")]
            quote_block = "\n".join(lines)
            text_nodes = text_to_textnodes(quote_block)
            children = [text_node_to_html_node(text_node) for text_node in text_nodes]
        elif type == BlockType.UNORDERED_LIST:
            tag = "ul"
            lines = [line[2:] for line in block.split("\n") if line.strip()]
            for line in lines:
                text_nodes = text_to_textnodes(line)
                children.append(ParentNode("li", [text_node_to_html_node(node) for node in text_nodes]))
        elif type == BlockType.ORDERED_LIST:
            tag = "ol"
            lines = [line.split(". ")[1] for line in block.split("\n") if line.strip()]
            for line in lines:
                text_nodes = text_to_textnodes(line)
                children.append(ParentNode("li", [text_node_to_html_node(node) for node in text_nodes]))
        else:
            raise ValueError("invalid block type")

        block_node = ParentNode(tag, children)
        root.children.append(block_node)
    return root

def extract_title(markdown: str) -> str:
    match = re.search(r"^# (.+)$", markdown, flags=re.MULTILINE)
    if not match:
        raise ValueError("no h1 line found")
    return match.group(1).strip()
