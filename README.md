# Code2MD

Code2MD is a Python package that generates markdown documentation from code files and the codebase architecture tree. It provides an easy way to create a comprehensive documentation file that includes the structure of your codebase along with the content of selected code files.

## Features

- Generates a markdown file with the codebase architecture tree and code file contents
- Supports multiple programming languages (Python, JavaScript, Java, etc.)
- Customizable file extensions for code file selection
- Easy integration into your project using Poetry package manager

## Installation

To install Code2MD, you need to have [Poetry](https://python-poetry.org/) installed. If you don't have Poetry installed, you can install it by following the instructions in the [Poetry documentation](https://python-poetry.org/docs/#installation).

Once you have Poetry installed, follow these steps:

1. Create a new directory for your project and navigate to it:

   ```bash
   mkdir my-project
   cd my-project
   ```

2. Initialize a new Poetry project:

   ```bash
   poetry init
   ```

   Follow the prompts to provide the necessary information about your project.

3. Add Code2MD as a dependency to your project:

   ```bash
   poetry add code2md
   ```

   This will install Code2MD and its dependencies in your project's virtual environment.

## Usage

To use Code2MD, follow these steps:

1. Update the `codebase_path` variable in the `code2md/cli.py` file to point to the directory containing your code files:

   ```python
   codebase_path = "path/to/your/codebase"
   ```

2. Customize the file extensions for code file selection in the `code2md/cli.py` file:

   ```python
   code_files = [os.path.join(root, file)
                 for root, dirs, files in os.walk(codebase_path)
                 for file in files
                 if file.endswith((".py", ".js", ".java"))]  # Add more file extensions as needed
   ```

   Add or remove file extensions based on the programming languages used in your codebase.

3. Run the package using Poetry:

   ```bash
   poetry run python code2md/cli.py
   ```

   This will generate a markdown file named `output.md` in the current directory. The markdown file will contain the codebase architecture tree followed by the contents of the selected code files.

## Customization

You can customize the behavior of Code2MD by modifying the `code2md/code2md.py` file:

- Adjust the markdown formatting of the code file information by modifying the `markdown_content` variable in the `create_markdown_file` function.
- Customize the indentation and styling of the codebase architecture tree by modifying the `generate_tree` function.

## Contributing

Contributions to Code2MD are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/your-username/code2md).

## License

Code2MD is open-source software licensed under the [MIT License](https://opensource.org/licenses/MIT).