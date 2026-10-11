import os
from pathlib import Path

from markdownfunctions import extract_title, markdown_to_html_node


def generate_page(basepath: str, from_path: str, template_path: str, dest_path: str) -> None:
    if not os.path.isfile(from_path):
        raise ValueError(f"Error: path '{from_path}' doesn't exist or isn't a file")
    if not os.path.isfile(template_path):
        raise ValueError(f"Error: path '{template_path}' doesn't exist or isn't a file")

    print(f"Generating page from '{from_path}' to '{dest_path}' using '{template_path}'")

    with open(from_path) as md_file:
        markdown = md_file.read()
    with open(template_path) as template_file:
        template_string = template_file.read()

    page_title = extract_title(markdown)
    html_string = markdown_to_html_node(markdown).to_html()
    output_str = template_string.replace("{{ Title }}", page_title)
    output_str = output_str.replace("{{ Content }}", html_string)

    output_str = output_str.replace('href="/', f'href="{basepath}')
    output_str = output_str.replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w") as dest_file:
        dest_file.write(output_str)

def generate_pages_recursive(basepath: str, dir_path_content, template_path, dest_dir_path) -> None:
    dir_path_content = Path(dir_path_content)
    template_path = Path(template_path)
    dest_dir_path = Path(dest_dir_path)
    for entry in dir_path_content.iterdir():
        if entry.is_dir():
            generate_pages_recursive(basepath, entry, template_path, dest_dir_path)
        elif entry.is_file() and entry.suffix == ".md":
            target_path = (dest_dir_path / Path(*entry.parts[1:])).with_suffix(".html")
            generate_page(basepath, str(entry), str(template_path), str(target_path))
