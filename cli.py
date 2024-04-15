# code2md/cli.py
import os
import click
from code2md import create_markdown_file, generate_tree


@click.command()
@click.argument(
    "codebase_path", type=click.Path(exists=True, file_okay=False, dir_okay=True)
)
@click.option(
    "--extensions",
    "-e",
    multiple=True,
    default=[".py"],
    help="File extensions to include (default: .py)",
)
@click.option(
    "--output",
    "-o",
    default="output.md",
    help="Output markdown file path (default: output.md)",
)
def main(codebase_path, extensions, output):
    # Get a list of code file paths in the codebase directory
    code_files = [
        os.path.join(root, file)
        for root, dirs, files in os.walk(codebase_path)
        for file in files
        if any(file.endswith(ext) for ext in extensions)
    ]

    # Generate the codebase architecture tree
    architecture_tree = generate_tree(codebase_path)

    # Create the markdown file with code content and architecture tree
    create_markdown_file(code_files, output, architecture_tree)

    click.echo(f"Markdown file generated: {output}")


if __name__ == "__main__":
    main()
