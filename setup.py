from setuptools import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(name="mobs_redo",
      version="1.0.0",
      description="Mobs redo documentation",
      long_description=long_description,
      url="https://github.com/eschan145/mr_docs",
      author="Ethan Chan",
      author_email="esamuelchan@gmail.com",
      license="GPLv3",
      keywords=[],
      py_modules=["mobs_redo"])
