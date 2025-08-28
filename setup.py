#!/usr/bin/env python3
"""
Setup script for PPT Translator package.
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ppt-translator",
    version="1.0.0",
    author="PPT Translator Team",
    author_email="your.email@example.com",
    description="A modern Streamlit web application for translating PowerPoint presentations into multiple languages",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ppt-translator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
        ],
    },
    entry_points={
        "console_scripts": [
            "ppt-translator=app:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="powerpoint, translation, streamlit, google-translate, pptx",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/ppt-translator/issues",
        "Source": "https://github.com/yourusername/ppt-translator",
        "Documentation": "https://github.com/yourusername/ppt-translator#readme",
    },
)
