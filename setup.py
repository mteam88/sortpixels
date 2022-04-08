from distutils.core import setup

setup(
    name='Sort-Image',
    version='0.1.0',
    author='Matthew Edelen',
    packages=['sort-image', 'sort-image/test'],
    scripts=['main.py'],
    license='LICENSE.txt',
    description='Useful image sorter.',
    long_description=open('README.txt').read(),
    install_requires=[
        "Pillow >= 9.0",
        "numpy >= 1.22"
    ],
)