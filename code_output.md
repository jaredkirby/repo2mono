## Codebase Architecture

```
repo2mono
├── repo2mono.py
├── cli.py
```

## File: repo2mono.py
### Path: <a id='repo2monorepo2monopy'></a>repo2mono/repo2mono.py

```python
# repo2mono/repo2mono.py
import os
import re

__all__ = ["create_markdown_file", "generate_tree"]


def create_markdown_file(file_paths, output_path, architecture_tree, include_toc=False):
    with open(output_path, "w") as output_file:
        if include_toc:
            output_file.write("## Table of Contents\n\n")
            for file_path in file_paths:
                file_name = os.path.basename(file_path)
                anchor_id = re.sub(r"[^a-zA-Z0-9_]", "", file_path)
                output_file.write(f"- [{file_name}](#{anchor_id})\n")
            output_file.write("\n")

        output_file.write("## Codebase Architecture\n\n")
        output_file.write("```\n")
        output_file.write(architecture_tree)
        output_file.write("```\n\n")

        for file_path in file_paths:
            with open(file_path, "r") as input_file:
                file_name = os.path.basename(file_path)
                file_content = input_file.read()
                anchor_id = re.sub(r"[^a-zA-Z0-9_]", "", file_path)
                output_file.write(f"## File: {file_name}\n")
                output_file.write(f"### Path: <a id='{anchor_id}'></a>{file_path}\n\n")
                output_file.write(f"```python\n{file_content}\n```\n\n")


def generate_tree(directory, level=0, indent_size=4):
    tree = ""
    indent = " " * (level * indent_size)

    if level == 0:
        tree += f"{os.path.basename(directory)}\n"

    for item in os.listdir(directory):
        if item.startswith("__"):
            continue

        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            tree += f"{indent}├── {item}\n"
            tree += generate_tree(item_path, level + 1, indent_size)
        elif not item.endswith(".pyc"):
            tree += f"{indent}├── {item}\n"

    return tree

```

## File: __init__.py
### Path: <a id='repo2mono__init__py'></a>repo2mono/__init__.py

```python
# repo2mono/__init__.py
from .repo2mono import create_markdown_file, generate_tree

__all__ = ["create_markdown_file", "generate_tree"]

```

## File: cli.py
### Path: <a id='repo2monoclipy'></a>repo2mono/cli.py

```python
import os
import click
from repo2mono import create_markdown_file, generate_tree

# repo2mono/cli.py


@click.command()
@click.argument(
    "codebase_path",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    default=".",
)
@click.option(
    "--extensions",
    "-e",
    multiple=True,
    default=[".py", ".toml", ".md"],
    help="File extensions to include (default: .py, .toml, .md)",
)
@click.option(
    "--output",
    "-o",
    default="code_output.md",
    help="Output markdown file path (default: code_output.md)",
)
@click.option(
    "--toc",
    is_flag=True,
    help="Include a table of contents in the generated markdown",
)
@click.option(
    "--print",
    "-p",
    "print_output",
    is_flag=True,
    help="Print the generated markdown to the console",
)
def main(codebase_path, extensions, output, toc, print_output):
    code_files = [
        os.path.join(root, file)
        for root, dirs, files in os.walk(codebase_path)
        if not any(dirname == "__pycache__" for dirname in root.split(os.sep))
        for file in files
        if any(file.endswith(ext) for ext in extensions) and not file.endswith(".pyc")
    ]

    architecture_tree = generate_tree(codebase_path)
    create_markdown_file(code_files, output, architecture_tree, include_toc=toc)
    click.echo(f"Markdown file generated: {output}")

    if print_output:
        with open(output, "r") as file:
            content = file.read()
            click.echo(content)


if __name__ == "__main__":
    main()

```

