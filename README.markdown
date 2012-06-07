# Moonfire Games' Tools for Python

This library wraps around `argparse` and creates a framework for creating an object-oriented set of tools. Tools are typically combined into a single command-line client. The general format for calling a tool is `command-name operation [parameters]`. An command example is `git` which does operations based on the sub-command (the second parameter). In this library, a tool would correspond to both `git clone` and `git push`.

This library contains common functionality for creating command-line utilities in Python. Most of them are other mfgames- packages (e.g., mfgames-writing, mfgames-media), but it can be used for anything that needs an easily expandable command-line tool framework.

To simplify creation, the utility functions all use the subparser component of argparse. In short, the tools are always in the format of: script-name action argument(s)

## Example

The `example.py` file is an example command-line tool that uses the tools to show how they are used.
