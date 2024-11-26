# repo2mono/cli.py
import os
import click
from process import create_markdown_file, generate_tree, ProjectAnalyzer


@click.command()
@click.argument(
    "codebase_path",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    default=".",
)
@click.option(
    "--output",
    "-o",
    default="mono_output.md",
    help="Output markdown file path (default: mono_output.md)",
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
@click.option(
    "--force-type",
    type=click.Choice(["nextjs", "python", "django", "generic"]),
    help="Force a specific project type analysis",
)
@click.option(
    "--exclude",
    "-x",
    multiple=True,
    help="Directories or files to exclude. Supports wildcards (*). Can be used multiple times.",
)
def main(codebase_path, output, toc, print_output, force_type, exclude):
    """Convert a codebase into a single markdown file with smart project type detection."""

    # Convert exclusions to a set and normalize them
    custom_excludes = {x.strip(os.sep) for x in exclude}

    # Initialize project analyzer with custom exclusions
    project_analyzer = ProjectAnalyzer(codebase_path, custom_excludes=custom_excludes)
    if force_type:
        project_analyzer.project_type = force_type
        project_analyzer.config = project_analyzer.PROJECT_CONFIGS.get(force_type, {})

    click.echo(f"Detected project type: {project_analyzer.project_type}")
    if custom_excludes:
        click.echo("Custom exclusions:")
        for excl in sorted(custom_excludes):
            click.echo(f"  - {excl}")

    # Collect all files
    code_files = []
    excluded_files = []
    for root, _, files in os.walk(codebase_path):
        if any(
            ignore in root.split(os.sep) for ignore in ProjectAnalyzer.COMMON_IGNORE
        ):
            continue
        for file in files:
            file_path = os.path.join(root, file)
            if project_analyzer.should_include_file(file_path):
                code_files.append(file_path)
            else:
                rel_path = os.path.relpath(file_path, codebase_path)
                if project_analyzer._matches_exclude_pattern(file_path):
                    excluded_files.append(rel_path)

    if not code_files:
        click.echo("Warning: No relevant files found to process!")
        return

    # Generate tree and create markdown
    architecture_tree = generate_tree(codebase_path, project_analyzer)
    create_markdown_file(
        code_files, output, architecture_tree, project_analyzer, include_toc=toc
    )

    # Print summary
    click.echo(f"\nProcessing Summary:")
    click.echo(f"- Processed files: {len(code_files)}")
    click.echo(f"- Excluded files: {len(excluded_files)}")
    click.echo(f"- Output file: {output}")

    if excluded_files and print_output:
        click.echo("\nExcluded files:")
        for f in sorted(excluded_files)[:10]:  # Show first 10 excluded files
            click.echo(f"  - {f}")
        if len(excluded_files) > 10:
            click.echo(f"  ... and {len(excluded_files) - 10} more")

    if print_output:
        with open(output, "r", encoding="utf-8") as file:
            content = file.read()
            click.echo("\nGenerated Content:")
            click.echo(content)


if __name__ == "__main__":
    main()
