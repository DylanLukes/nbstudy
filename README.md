# nbstudy - tools for studying notebooks

[![CI Testing](https://github.com/DylanLukes/nbstudy/actions/workflows/test.yml/badge.svg)](https://github.com/DylanLukes/nb-study-tools/actions/workflows/test.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/nbstudy.svg)](https://pypi.org/project/nbstudy)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nbstudy.svg)](https://pypi.org/project/nbstudy)

-----

**Table of Contents**

- [Overview](#overview)
- [Installation](#installation)
- [Tools](#tools)
- [License](#license)

## Overview

`nbstudy` is a collection of tools for studying notebooks, especially those published on GitHub. 

It generalizes the tooling used in 
[Exploration and Explanation in Computational Notebooks](https://dl.acm.org/doi/10.1145/3173574.3173606)
 by Adam Rule et al, with additions for 
[Refactoring in Computational Notebooks](https://dl.acm.org/doi/full/10.1145/3576036) 
 by the author of this tool (Dylan Lukes, Eric Liu, et al).

**The goal of this project is to codify the functionality used to support these studies and future
studies in a way that they can be used reproducibly by anyone else who wants to study notebooks
in the wild.**

> ⚠️️**Warning:** This tool is still in early development. The API is not stable, and the tool is 
> not yet feature-complete. Many features are still missing (have not been cleaned up and copied
> over from existing code used priorly for publications), and the documentation is incomplete.

## Requirements

`nbstudy` requires Python 3.12 or later, and a recent version of Git 2.43 with support for 
[sparse-checkout](https://git-scm.com/docs/git-sparse-checkout) and 
[partial-clone](https://git-scm.com/docs/partial-clone).

## Installation

To install globally from PyPI, from anywhere run:

```console
pip install nbstudy
nbstudy -h
```

To develop, clone the repository and then from the root of the repository run:

```console
hatch shell
nbstudy -h
```

## Introduction

### Workspaces

`nbstudy` works on the principle of a "workspace" in which notebooks are studied. A workspace is a Git repository
which contains a local cache of notebooks (as sparsely checked-out submodules) as well a database of metadata about 
those notebooks used to maintain the cache, supported by settings in a configuration file and environment variables.

While some tools work in isolation without a workspace, by using one you get the benefits of being able to automate 
the process of studying collections of notebooks, collecting results interactively as you go. For example: if you 
wanted to do [coding](https://en.wikipedia.org/wiki/Coding_(social_sciences)) of every commit of each notebook. 

A workspace looks like this:

```
my-nbstudy-workspace/
├── .gitignore
├── .gitmodules
├── nbstudy.config.json
├── nbstudy.config.env
├── nbstudy.db
└── nbcache/
    ├── localhost/
    │   └── my-repo/
    │
    ├── github.com/
    ┆   ├── user1/
        ┆   ├── repo1/
            ┆   ├── .../notebook1.ipynb
                └── .../notebook2.ipynb
```

#### Workspace Settings

The `nbstudy.config.json` file contains settings for the workspace. Settings may also be configured
using environment variables prefixed with `NBSTUDY_`, or read from the `nbstudy.config.env` file.

> ⚠️ The `nbstudy.config.json` file is intended to be shared with others, and should not contain any
> sensitive information. The `nbstudy.config.env` file is intended to be private, and should contain
> sensitive information such as API keys. It is by default included in the `.gitignore` file.

#### Workpace Database

The `nbstudy.db` file is a SQLite database containing metadata about the notebooks in the workspace,
and is managed by `nbstudy`. It is not intended to be edited manually, though it can be inspected.

#### Workspace Notebook Cache

The `nbcache/` directory contains the notebooks themselves, organized by the hostname of the Git
repository they came from, followed by the username and repository name of the repository.

There are two cases that are specially managed by `nbstudy`:

The `localhost/` directory is used for notebooks with no provenance (e.g. notebooks that are created
locally and not in a Git repository), and is managed by the `nbstudy local` subcommands. 

The `github.com/` directory is used for notebooks that are scraped from a Git repository hosted 
on GitHub and is managed by the `nbstudy github` subcommands.

> ⚠️ **Notebook caches can grow very large, as repositories that are _fully_ downloaded can include
> huge data files.** `nbstudy` does make a best faith effort to minimize bloat by using the 
> [sparse-checkout](https://git-scm.com/docs/git-sparse-checkout) and
> [partial-clone](https://git-scm.com/docs/partial-clone) features of Git to only download the
> minimum files that are needed (notebook files themselves) by default.

## Usage

The `nbstudy` tool provides a number of subcommands for working with notebooks.

> 🛠️ _TODO_

## Attribution

If you use `nbstudy` in your research, please cite it as follows:

```bibtex
@misc{nbstudy,
  author = {Lukes, Dylan},
  title = {nbstudy - tools for studying notebooks},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/DylanLukes/nbstudy}},
  commit = {<commit hash here>}
}
```

## License

`nbstudy` is distributed under the terms of the [BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html) license.
