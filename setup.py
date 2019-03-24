import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='theHarvester',
    version='3.0.6',
    author="Christian Martorella",
    author_email="cmartorella@edge-security.com",
    description="theHarvester is a very simple, yet effective tool designed to be used in the early stages of a penetration test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/laramies/theHarvester",
    packages=setuptools.find_packages(),
    scripts=['theHarvester.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    data_files=[
        ('share/dict/theHarvester', [
            'wordlists/general/common.txt',
            'wordlists/dns-big.txt',
            'wordlists/dns-names.txt',
            'wordlists/dorks.txt',
            'wordlists/names_small.txt'
        ]
         )
    ],
)
