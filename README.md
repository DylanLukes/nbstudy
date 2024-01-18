# nbstudy - tools for studying notebooks

[![CI Testing](https://github.com/DylanLukes/nbstudy/actions/workflows/test.yml/badge.svg)](https://github.com/DylanLukes/nb-study-tools/actions/workflows/test.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/nb-study-tools.svg)](https://pypi.org/project/nbstudy)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nb-study-tools.svg)](https://pypi.org/project/nbstudy)

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

There are two broad classes of functionality:

- Inspecting and studying existing local notebooks in Git repositories.
  - Stepping through notebooks (wrapping around `nbdime`).
  - Extracting various kinds of statistics from notebooks.
- Studying notebooks published on GitHub.
  - Scraping notebooks from GitHub.
  - Maintaining a local database/cache of notebooks.

> ⚠️️**Warning:** This tool is still in early development. The API is not stable, and the tool is 
> not yet feature-complete. Many features are still missing (have not been cleaned up and copied
> over from existing code used priorly for publications), and the documentation is incomplete.

## Installation

To install globally, from anywhere:

```console
pip install nbstudy
nbstudy -h
```

For development, from inside a clone of this repository:

```console
hatch shell
nbstudy -h
```

## Tools

The `nbstudy` tool provides a number of subcommands for working with notebooks.

### `nbstudy github`


## License

`nbstudy` is distributed under the terms of the [BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html) license.
