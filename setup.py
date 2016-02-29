from distutils.core import setup

setup(
    name='galfect',
    version='0.1.0',
    author='Lirian Su',
    author_email='liriansu@gmail.com',
    url='http://liriansu.com',
    py_modules=['bin/translate'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description='Converting drama text to html pages',
    long_description=open('README.md').read(),
)
