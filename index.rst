
dircmpa (Directory Comparison)
==============================

Compares the contents of two directories (folders) and reports if they are equal or not.
If they are not equal, how the are not equal.

Usage
=====

dircmpa can be used either as a command line application or as a Python library package.

Command Line
------------

dircmpa <directory> <directory> [-s/--silent] [-v/--verbose]


Python library package
----------------------

.. code:: python
from dircmpa import compare_folders

compare_folders('a', 'b')
