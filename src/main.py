import os
import shutil

from generatepage import generate_page, generate_pages_recursive


def copy_src_content_to_dest(src: str, dest: str) -> None:
    if not os.path.isdir(src):
        raise ValueError(f"source directory does not exist: {src}")
    print(f"     SOURCE: {os.path.abspath(src)}")
    print(f"DESTINATION: {os.path.abspath(dest)}")
    if os.path.isdir(dest):
        print(f"destination directory '{dest}' already exists, removing")
        shutil.rmtree(dest)
    os.mkdir(dest)
    print(f"created directory '{dest}'")
    copy_src_content_to_dest_recurse(src, dest)

def copy_src_content_to_dest_recurse(src: str, dest: str, prefix: str = "") -> None:
    for entry in os.listdir(os.path.join(src, prefix)):
        path = os.path.join(prefix, entry)
        path_src = os.path.join(src, path)
        if os.path.isfile(path_src):
            target_dir = os.path.join(dest, prefix)
            shutil.copy(path_src, target_dir)
            print(f"copied file '{path_src}' to '{os.path.join(target_dir, entry)}'")
        elif os.path.isdir(path_src):
            target_dir = os.path.join(dest, path)
            os.mkdir(target_dir)
            print(f"created directory '{target_dir}'")
            copy_src_content_to_dest_recurse(src, dest, path)

def main() -> None:
    copy_src_content_to_dest("static", "public")
    #generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()
