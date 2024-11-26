# repo2mono/process.py
import os
import re
import json
from typing import Dict, List, Set


class ProjectAnalyzer:
    # Common directories and files to ignore across all project types
    COMMON_IGNORE = {
        "node_modules",
        "__pycache__",
        ".git",
        ".idea",
        ".vscode",
        "venv",
        "env",
        ".env",
        "build",
        "dist",
        ".next",
        "out",
        "coverage",
        ".coverage",
        ".pytest_cache",
        ".mypy_cache",
    }

    # Project type specific configurations
    PROJECT_CONFIGS = {
        "nextjs": {
            "indicators": ["next.config.js", "package.json"],
            "extensions": [".js", ".jsx", ".ts", ".tsx", ".css", ".scss", ".md"],
            "important_dirs": ["pages", "components", "styles", "public", "lib"],
            "ignore_dirs": ["node_modules", ".next", "out"],
            "config_files": ["next.config.js", "package.json", "tsconfig.json"],
        },
        "python": {
            "indicators": ["requirements.txt", "setup.py", "pyproject.toml"],
            "extensions": [".py", ".pyi", ".pyx", ".pxd", ".md"],
            "important_dirs": ["src", "tests", "docs"],
            "ignore_dirs": [
                "__pycache__",
                ".pytest_cache",
                "build",
                "dist",
                "*.egg-info",
            ],
            "config_files": ["setup.py", "pyproject.toml", "requirements.txt"],
        },
        "django": {
            "indicators": ["manage.py", "wsgi.py"],
            "extensions": [".py", ".html", ".css", ".js", ".md"],
            "important_dirs": ["templates", "static", "media", "apps"],
            "ignore_dirs": ["__pycache__", "migrations", "static_root", "media_root"],
            "config_files": ["manage.py", "requirements.txt", "settings.py"],
        },
        # Add more project types as needed
    }

    def __init__(self, directory: str, custom_excludes: Set[str] = None):
        self.directory = directory
        self.project_type = self._detect_project_type()
        self.config = self.PROJECT_CONFIGS.get(self.project_type, {})
        self.custom_excludes = custom_excludes or set()

    def _detect_project_type(self) -> str:
        """Detect the type of project based on key files and directory structure."""
        for project_type, config in self.PROJECT_CONFIGS.items():
            indicators = config["indicators"]
            for indicator in indicators:
                if os.path.exists(os.path.join(self.directory, indicator)):
                    return project_type
        return "generic"

    def _matches_exclude_pattern(self, path: str) -> bool:
        """Check if a path matches any exclusion pattern."""
        rel_path = os.path.relpath(path, self.directory)
        path_parts = rel_path.split(os.sep)

        for exclude in self.custom_excludes:
            # Handle wildcards in exclusion patterns
            if exclude.startswith("*") and exclude.endswith("*"):
                pattern = exclude.strip("*")
                if any(pattern in part for part in path_parts):
                    return True
            elif exclude.startswith("*"):
                if any(part.endswith(exclude.strip("*")) for part in path_parts):
                    return True
            elif exclude.endswith("*"):
                if any(part.startswith(exclude.strip("*")) for part in path_parts):
                    return True
            else:
                if exclude in path_parts:
                    return True
        return False

    def should_include_file(self, file_path: str) -> bool:
        """Determine if a file should be included in the documentation."""
        # Check custom exclusions first
        if self._matches_exclude_pattern(file_path):
            return False

        if self.project_type == "generic":
            return True

        # Get file extension and relative path
        _, ext = os.path.splitext(file_path)
        rel_path = os.path.relpath(file_path, self.directory)

        # Check if file is in ignored directories
        for ignore_dir in self.config.get("ignore_dirs", []):
            if ignore_dir in rel_path.split(os.sep):
                return False

        # Include if it's a config file
        for config_file in self.config.get("config_files", []):
            if rel_path.endswith(config_file):
                return True

        # Check if extension is allowed
        return ext in self.config.get("extensions", [])

    def get_project_summary(self) -> str:
        """Generate a summary of the project structure and configuration."""
        summary = [
            f"# Project Analysis\n",
            f"Project Type: {self.project_type}\n",
            "\n## Project Configuration:\n",
            "### Custom Exclusions:\n",
        ]

        if self.custom_excludes:
            for exclude in sorted(self.custom_excludes):
                summary.append(f"- {exclude}\n")
        else:
            summary.append("- None specified\n")

        summary.append("\n## Key Directories:\n")

        if self.project_type != "generic":
            summary.append("Important directories for this project type:\n")
            for dir_name in self.config.get("important_dirs", []):
                dir_path = os.path.join(self.directory, dir_name)
                if os.path.exists(dir_path):
                    summary.append(f"- {dir_name}/\n")

            summary.append("\n## Configuration Files:\n")
            for config_file in self.config.get("config_files", []):
                if os.path.exists(os.path.join(self.directory, config_file)):
                    summary.append(f"- {config_file}\n")

        return "".join(summary)


def create_markdown_file(
    file_paths: List[str],
    output_path: str,
    architecture_tree: str,
    project_analyzer: ProjectAnalyzer,
    include_toc: bool = False,
):
    """Create a markdown file with filtered project content."""
    with open(output_path, "w", encoding="utf-8") as output_file:
        # Write project summary
        output_file.write(project_analyzer.get_project_summary())
        output_file.write("\n")

        if include_toc:
            output_file.write("## Table of Contents\n\n")
            for file_path in file_paths:
                if project_analyzer.should_include_file(file_path):
                    file_name = os.path.basename(file_path)
                    anchor_id = re.sub(r"[^a-zA-Z0-9_]", "", file_path)
                    output_file.write(f"- [{file_name}](#{anchor_id})\n")
            output_file.write("\n")

        output_file.write("## Codebase Architecture\n\n")
        output_file.write("```\n")
        output_file.write(architecture_tree)
        output_file.write("```\n\n")

        for file_path in file_paths:
            if project_analyzer.should_include_file(file_path):
                try:
                    with open(file_path, "r", encoding="utf-8") as input_file:
                        file_name = os.path.basename(file_path)
                        file_content = input_file.read()
                        anchor_id = re.sub(r"[^a-zA-Z0-9_]", "", file_path)

                        # Determine file type for syntax highlighting
                        _, ext = os.path.splitext(file_name)
                        lang = {
                            ".py": "python",
                            ".js": "javascript",
                            ".jsx": "jsx",
                            ".ts": "typescript",
                            ".tsx": "tsx",
                            ".css": "css",
                            ".html": "html",
                            ".md": "markdown",
                            ".json": "json",
                        }.get(ext, "")

                        output_file.write(f"## File: {file_name}\n")
                        output_file.write(
                            f"### Path: <a id='{anchor_id}'></a>{file_path}\n\n"
                        )
                        output_file.write(f"```{lang}\n{file_content}\n```\n\n")
                except UnicodeDecodeError:
                    print(f"Warning: Skipping binary file: {file_path}")


def generate_tree(
    directory: str,
    project_analyzer: ProjectAnalyzer,
    level: int = 0,
    indent_size: int = 4,
) -> str:
    """Generate a tree structure of the project, respecting project-specific filters."""
    tree = ""
    indent = " " * (level * indent_size)

    if level == 0:
        tree += f"{os.path.basename(directory)}\n"

    try:
        items = sorted(os.listdir(directory))
        for item in items:
            if item in ProjectAnalyzer.COMMON_IGNORE:
                continue

            item_path = os.path.join(directory, item)

            if os.path.isdir(item_path):
                if project_analyzer.project_type != "generic":
                    # Skip ignored directories for specific project types
                    if item in project_analyzer.config.get("ignore_dirs", []):
                        continue
                tree += f"{indent}├── {item}/\n"
                tree += generate_tree(
                    item_path, project_analyzer, level + 1, indent_size
                )
            elif project_analyzer.should_include_file(item_path):
                tree += f"{indent}├── {item}\n"
    except PermissionError:
        print(f"Warning: Permission denied accessing {directory}")
    except Exception as e:
        print(f"Warning: Error processing {directory}: {str(e)}")

    return tree
