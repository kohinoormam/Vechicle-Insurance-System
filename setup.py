from setuptools import setup, find_packages

setup(
    name="src",
    version="0.0.1",
    author="Vikash Das",
    author_email="vikashdas770@gmail.com",
    packages=find_packages()
)

# Run python setup.py install or pip install . to install your project locally.
# from setuptools import setup, find_packages
# setuptools is the standard Python library for packaging and distributing Python projects.
# find_packages() automatically discovers all Python packages (directories with __init__.py) under your project.

# setup(...) → Main function that tells Python how to package your project. 
# version="0.0.1" → Version of your package.
# author & author_email → Metadata about the package author.