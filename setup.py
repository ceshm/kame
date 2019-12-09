import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kame",
    version="0.0.1",
    author="ceshm",
    author_email="cesar.hernandez.mons@gmail.com",
    description="async REST framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ceshm/kame",
    packages=setuptools.find_packages(),
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
