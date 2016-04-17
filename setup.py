from setuptools import setup
import os.path

datafiles = [
    'bootstrap/css/bootstrap.min.css',
    'bootstrap/js/bootstrap.min.js',
    'css/main.css',
    'index.html',
]

setup(
    name='galfect',
    version='1.0.0',
    author='Lirian Su',
    author_email='liriansu@gmail.com',
    url='https://github.com/LKI/galfect',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description='Converting drama text to html pages',
    long_description=open('README.rst').read(),
    entry_points={
        'console_scripts': ['galfect = galfect.cmdline:execute']
    },
    packages=['galfect', 'galfect.initialize'],
    data_files=map(lambda (x): (os.path.dirname(x), [x]), datafiles),
)
