from setuptools import setup, find_packages

setup(
    name="Last.fm-Music-Analytics",  
    version="0.1.0",
    author="nose1317",
    description="A Python package for scraping, analyzing, and visualizing Last.fm music data.",
    long_description=open("README.md", encoding="utf-8").read(),  # Ensures correct encoding
    long_description_content_type="text/markdown",
    url="https://github.com/nose1317/Last.fm-Music-Analytics",  # Add the project URL for reference
    packages=find_packages(),  # This will automatically find all packages
    install_requires=[
        "playwright",
        "pandas",
        "matplotlib",
        "seaborn",
        "ipywidgets",
        "ipython",
    ],
    python_requires=">=3.7",  # Specifies that it requires Python 3.7 or higher
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",  # Specify the exact versions supported
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
