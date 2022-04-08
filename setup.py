from distutils.core import setup

setup(
    name='SortImage',
    version='0.1.0',
    author='Matthew Edelen',
    packages=['sortimage', 'sortimage/test'],
    scripts=['main.py'],
    license='LICENSE.txt',
    description='Useful image sorter.',
    long_description=open('README.txt').read(),
    install_requires=[
        "Pillow >= 9.0",
        "numpy >= 1.22"
    ],
)