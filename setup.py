import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["requests<=2.21.0", "fire<=0.1.3"]

setuptools.setup(
    name="tigrex",
    version="1.1.0",
    author="Eric Chi",
    author_email="ericjaychi@gmail.com",
    description="A Magic the Gathering CLI Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    url="https://github.com/pypa/sampleproject",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)