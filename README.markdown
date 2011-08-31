# Moonfire Games' Tools for Python

This library contains common functionality for creating command-line
utilities in Python. Most of them are other mfgames- packages (e.g.,
mfgames-writing, mfgames-media), but it can be used for anything that
needs an easily expandable command-line tool framework.

To simplify creation, the utility functions all use the subparser
component of argparse. In short, the tools are always in the format
of: script-name action argument(s)

## Example

The `example.py` file is an example command-line tool that uses the
tools to show how they are used.

## Inclusion

Since this is a low-profile and relatively immature library, it is not
intended to be installed as a system- or even site-wide Python
module. Instead, it can be included in other projects directly and
installed as part of that source.

Because of this, there is a branch (master-src or <version>-src) which
is just the Python code while the master (or <version>) branch
contains documentation, tests, and help files. When using Git with
submodules (or the subtree module), the master-src branch is a better
branch to include since it doesn't have extra files.

To keep the two branches in sync, the [subtree](https://github.com/apenwarr/git-subtree) module is used.

* `git subtree pull --prefix=src . master-src`
* `git subtree push --prefix=src . master-src`