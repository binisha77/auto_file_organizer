from setuptools import setup, find_packages

setup(
    name="auto_file_organizer",
    version="0.1.0",
    author="Sovitha kahadka",
    author_email="binisha123@gmail.com",
    description="Python package to automatically organize files by type",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/auto_file_organizer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)