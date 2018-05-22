WORK IN PROGRESS
================

Simple app for [5BX](https://en.wikipedia.org/wiki/5BX)

Architecture
------------

This is a [Jekyll](https://jekyllrb.com/) website.

The data is stored in `_data/`.

The levels follow a template defined in `_layouts/levels.html`.

Each level is defined by an empty markdown file with a non-empty YAML
header in `frames/`. Those files are automatically created by
`generate.py`.
