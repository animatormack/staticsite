import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading" # r"^#{1,6} .+\n?$"
    CODE = "code" # r"^```\n(?:.*\n?)*```\n?$"
    QUOTE = "quote" # r"^(?:> ?.*\n?)+$"
    UNORDERED_LIST = "unordered_list" # r"^(?:- .*\n?)+$"
    ORDERED_LIST = "ordered_list" # r"^(?:\d+\. .*\n?)+$"

def block_to_block_type(markdown: str) -> BlockType:
    if re.fullmatch(r"^#{1,6} .+\n?$", markdown):
        return BlockType.HEADING
    if re.fullmatch(r"^```\n(?:.*\n?)*```\n?$", markdown):
        return BlockType.CODE
    if re.fullmatch(r"^(?:> ?.*\n?)+$", markdown):
        return BlockType.QUOTE
    if re.fullmatch(r"^(?:- .*\n?)+$", markdown):
        return BlockType.UNORDERED_LIST
    if re.fullmatch(r"^(?:\d+\. .*\n?)+$", markdown):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
