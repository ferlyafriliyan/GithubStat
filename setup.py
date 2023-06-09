from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as markdown:
    long_description = markdown.read()

setup(
    name = "GithubStat",
    version = "1.2",
    license = "MIT",
    author = "HTR-TECH",
    author_email = "tahmidrayat@gmail.com",
    url = "https://github.com/htr-tech/GithubStat",
    description = "A Simple Github User Statistics Meter based on Github-API.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    packages = find_packages(),
    zip_safe = True,
    install_requires = ["requests >= 2.25.0", "six >= 1.13.0"],
    entry_points = {
        'console_scripts': [
            'GithubStat=GithubStat.__init__:main',
            'githubstat=GithubStat.__init__:main',
            'Gitstat=GithubStat.__init__:main',
            'gitstat=GithubStat.__init__:main',
            ]
        }
)

