from setuptools import setup, find_packages

setup(
    name="Last.fm-Music-Analytics",  
    version="0.1.0",
    author="nose1317",
    description="A Python package for scraping, analyzing, and visualizing Last.fm music data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "playwright",
        "pandas",
        "matplotlib",
        "seaborn",
        "ipywidgets",
        "ipython"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
