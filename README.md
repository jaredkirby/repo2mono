# repo2mono

repo2mono is a Python package that generates a single Markdown file containing the codebase architecture and file contents of a given directory.

## Features

- Generates a Markdown file with the codebase architecture and file contents
- Supports custom file extensions to include in the output
- Optionally includes a table of contents in the generated Markdown
- Prints the generated Markdown to the console if desired

## Installation

You can install repo2mono using pip:

```
pip install repo2mono
```

## Usage

To use repo2mono, run the following command in your terminal:

```
repo2mono [OPTIONS] [CODEBASE_PATH]
```

### Options

- `CODEBASE_PATH`: The path to the codebase directory (default: current directory)
- `-e, --extensions`: File extensions to include (default: .py, .toml, .md)
- `-o, --output`: Output Markdown file path (default: code_output.md)
- `--toc`: Include a table of contents in the generated Markdown
- `-p, --print`: Print the generated Markdown to the console

### Example

To generate a Markdown file for a codebase in the `my_project` directory, including only `.py` and `.md` files, and save it as `output.md`, run:

```
repo2mono my_project -e .py -e .md -o output.md
```

## Codebase Architecture

The package consists of the following files:

```
repo2mono
├── repo2mono.py
├── cli.py
```

- `repo2mono.py`: Contains the core functionality for generating the Markdown file
- `cli.py`: Provides the command-line interface for the package

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/yourusername/repo2mono).

## License

This project is licensed under the [MIT License](LICENSE).