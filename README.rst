psycopg2_numpy_ext
==================

Adapters for Numpy's types for Psycopg2.

``psycopg2`` does not ship with adapters for `numpy`'s types and is unable to interpolate them in queries naturally.

Using `numpy`'s values as parameters results in ``ProgrammingError: can't adapt type 'numpy.int32'`` and similar errors with other ``numpy`` types. Such errors are common while mixing ``numpy``, ``pandas`` and ``psycopg2``.

This package solves the problem by registering ``AsIs`` adapters for these types.

Usage
-----

::

    from psycopg2_numpy_ext import register_numpy_types
    register_numpy_types()


Installation
------------

::

    pip install git+git://github.com/musically-ut/psycopg2_numpy_ext.git@master#egg=psycopg2_numpy_ext

Requirements
^^^^^^^^^^^^

  - `numpy >= 1.9.2`
  - `psycopg2 >= 2.5`

Authors
-------

`psycopg2-numpy-ext` was written by `Utkarsh Upadhyay <musically.ut@gmail.com>`_.
