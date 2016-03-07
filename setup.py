from setuptools import setup
import markdown
import re

tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')

setup(
    name='galfect',
    version='0.2.0',
    author='Lirian Su',
    author_email='liriansu@gmail.com',
    url='http://liriansu.com',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description='Converting drama text to html pages',
    long_description=tag_re.sub('', markdown.markdown(open('README.md').read())),
    entry_points={
        'console_scripts': ['galfect = galfect.cmdline:execute']
    },
    packages=['galfect'],
)
