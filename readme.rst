
cmpa (Comparison utility)
=========================

Compares the contents of two directories (folders) and reports if they are equal or not.

Usage
=====

cmpa can be used either as a command line application or as a Python library package.

Command Line
------------

Simple example:

    `cmpa <left_directory> <right_directory>`

Use `cmpa -h` for a complete list of options.

Python library package
----------------------

Simple example:

.. code:: python

    from cmpa import compare, Compare

    # For this simple example just compare directory with itself.
    compare(['.', '.'])
    print()

    # Use the class for finer grain observability
    c = Compare(['.', '.'], silent=True)
    print(c.get_total_files())
    print(c.get_file_counts())
    print(c.compare_ok_count)

