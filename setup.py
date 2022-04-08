from distutils.core import setup

setup(
    name='sortpixels',
    version='0.1.3',
    author='Matthew Edelen',
    packages=['sortpixels', 'sortpixels/test'],
    scripts=['bin/example.py'],
    license='LICENSE.txt',
    description='Useful image sorter.',
    long_description=open('README.txt').read(),
    install_requires=[
        "Pillow >= 9.0",
        "numpy >= 1.22"
    ],
)