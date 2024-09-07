from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='splint',
    version='0.1',
    author="Daniel Jeranko", 
    author_email="danieljeranko@skittle.cc", 
    description='Splint: A simple, easy-to-use Python linter designed for beginner developers.',
    long_description=long_description,
    long_description_content_type="text/markdown",  
    url="https://github.com/jerankda/splint", 
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Quality Assurance",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires='>=3.6',
    test_suite='tests',
)
