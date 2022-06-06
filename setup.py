from setuptools import setup
import os

def open_file(fname):
   return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
   name="snake",            # name of your package
   version="0.0.1",
   description="a terminal-based snake game",
   long_description=open_file("README.md"),  # only if you have a README.md
   author="Kristian and the Stationary Siracha cohort",
   author_email="kristian.rother@posteo.de",
   packages=["snake"],      # same as folder name
   url="https://github.com/krother/snake",
   license="MIT",
   classifiers=[
      "Programming Language :: Python :: 3.8",
   ]
)