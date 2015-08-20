"""psycopg2-numpy-ext - Adapters for Numpy's types for Psycopg2."""

__version__ = '0.1.0'
__author__ = 'Utkarsh Upadhyay <musically.ut@gmail.com>'
__all__ = ['__version__', 'register_numpy_types']

from psycopg2.extensions import register_adapter, AsIs
import numpy as np

def register_numpy_types():
    """Register the AsIs adapter for following types from numpy:
      - numpy.int8
      - numpy.int16
      - numpy.int32
      - numpy.int64

      - numpy.float16
      - numpy.float32
      - numpy.float64
      - numpy.float128
    """
    for typ in ['int8', 'int16', 'int32', 'int64',
                'float16', 'float32', 'float64', 'float128']:
        register_adapter(np.__getattribute__(typ), AsIs)
