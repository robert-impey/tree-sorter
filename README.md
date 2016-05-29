# tree-sorter

[![Build Status](https://travis-ci.org/robert-impey/tree-sorter.svg?branch=master)](https://travis-ci.org/robert-impey/tree-sorter)

Program for sorting space indented text, treating blocks indented to the same level as groups.

e.g.

    II Animals
      2 Dogs
      3 Cats
      1 Fish
    I Plants
      b Nettles
      c Oak
      a Grass
  
becomes

    I Plants
      a Grass
      b Nettles
      c Oak
    II Animals
      1 Fish
      2 Dogs
      3 Cats
      
Trees of grouped data can be of arbitrary depth.

## Usage

    $ ./TreeSorter.py -h
    usage: Sort trees [-h] [--SeparateTopLevel] [--InPlace] TreeFile

    positional arguments:
      TreeFile            The file containing the tree.

    optional arguments:
      -h, --help          show this help message and exit
      --SeparateTopLevel  Separate top level trees with a blank line.
      --InPlace           Write the output on top of the input file.

### Examples

    $ ./TreeSorter.py ~/docs/todo.txt

Reads the contents of the text file and prints out the trees in order.

    $ ./TreeSorter.py ~/docs/todo.txt --SeparateTopLevel

Separates "top level" trees with a blank line. This is useful for fast navigation in vim.

    $ ./TreeSorter.py ~/docs/todo.txt --SeparateTopLevel --InPlace

Writes the sorted trees on top of the input file. The tool creates a back up file with the extension ".bak" first. Obviously, you've already got other back ups anyway. This is free software. I take no respobsibility for anything that happens to your files. See license.

## License

This software is released under the terms of the [MIT License](https://opensource.org/licenses/MIT).
