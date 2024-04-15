# code2md/code2md.py
import os


def create_markdown_file(file_paths, output_path, architecture_tree):
    with open(output_path, "w") as output_file:
        # Write the architecture tree to the markdown file
        output_file.write("## Codebase Architecture\n\n")
        output_file.write("```\n")
        output_file.write(architecture_tree)
        output_file.write("```\n\n")

        for file_path in file_paths:
            with open(file_path, "r") as input_file:
                file_name = os.path.basename(file_path)
                file_content = input_file.read()

                # Format the file information in markdown
                markdown_content = f"## File: {file_name}\n"
                markdown_content += f"### Path: {file_path}\n\n"
                markdown_content += f"```python\n{file_content}\n```\n\n"

                output_file.write(markdown_content)


def generate_tree(directory, level=0):
    tree = ""
    indent = "    " * level

    if level == 0:
        tree += f"{os.path.basename(directory)}\n"

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        if os.path.isdir(item_path):
            tree += f"{indent}├── {item}\n"
            tree += generate_tree(item_path, level + 1)
        else:
            tree += f"{indent}├── {item}\n"

    return tree
