# Code2MD

Code2MD is a command-line tool that generates a markdown file from a Python codebase. It creates a well-structured markdown file that includes the codebase architecture, file paths, and the contents of each Python file.

## Features

- Generates a markdown file from a Python codebase
- Includes the codebase architecture as a tree structure
- Provides file paths and contents of each Python file
- Supports optional table of contents for easy navigation
- Customizable file extensions to include in the generated markdown

## Installation

To install Code2MD, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/code2md.git
   ```

2. Navigate to the project directory:
   ```
   cd code2md
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To generate a markdown file from your Python codebase, use the following command:

```
python -m code2md.cli [OPTIONS] [CODEBASE_PATH]
```

Options:
- `--extensions` or `-e`: File extensions to include (default: .py)
- `--output` or `-o`: Output markdown file path (default: output.md)
- `--toc`: Include a table of contents in the generated markdown

Example:
```
python -m code2md.cli -e .py -e .js -o docs/codebase.md /path/to/codebase
```

## Project Structure

```
code2md/
├── __init__.py
├── code2md.py
└── cli.py
```

- `__init__.py`: Initializes the `code2md` package and exposes the public functions.
- `code2md.py`: Contains the core functionality for generating the markdown file.
- `cli.py`: Provides the command-line interface for running Code2MD.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The project uses the [Click](https://click.palletsprojects.com/) library for building the command-line interface.
- The markdown file generation is inspired by the need for better code documentation.