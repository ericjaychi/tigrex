import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tigrex",
    version="1.0.0",
    author="Eric Chi",
    author_email="ericjaychi@gmail.com",
    description="A Magic the Gathering CLI Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "fire",
        "requests"
    ]
)