import setuptools

setuptools.setup(
    name="psycopg2_numpy_ext",
    version="0.1.0",
    url="https://github.com/musically-ut/psycopg2-numpy-ext",

    author="Utkarsh Upadhyay",
    author_email="musically.ut@gmail.com",

    description="Adapters for Numpy's types for Psycopg2.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=['numpy', 'psycopg2'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
