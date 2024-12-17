from setuptools import setup, find_packages

setup(
    name="Last.fm-Music-Analytics",
    version="0.1.0",
    author="nose1317",
    description="A Python package for scraping, analyzing, and visualizing Last.fm music data.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nose1317/Last.fm-Music-Analytics",
    packages=find_packages(),
    install_requires=[
        "playwright",
        "pandas",
        "matplotlib",
        "seaborn",
        "ipywidgets",
        "ipython",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={
        '': ['config.json', 'interactive_data_aggregator.ipynb'],
    },
    include_package_data=True,
)
