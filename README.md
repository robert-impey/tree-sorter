# tree-sorter

[![Build Status](https://travis-ci.org/robert-impey/tree-sorter.svg?branch=master)](https://travis-ci.org/robert-impey/tree-sorter)

Program for sorting indented text, treating blocks indented to the same level as groups.

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
