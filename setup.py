import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="constant-variables-qqsongzi", # Replace with your own username
    version="0.0.1",
    author="qingswu",
    author_email="qqsongzi@gmail.com",
    description="Some useful constants for testing/development.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qingswu/constant_variables",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)