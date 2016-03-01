from distutils.core import setup
import markdown
import re

setup(
    name='galfect',
    version='0.1.1',
    author='Lirian Su',
    author_email='liriansu@gmail.com',
    url='http://liriansu.com',
    py_modules=['bin/translate'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description='Converting drama text to html pages',
    long_description=tag_re.sub('', markdown.markdown(open('README.md').read())),
)
