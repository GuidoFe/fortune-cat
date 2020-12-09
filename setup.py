import setuptools

with open("README.md") as fh:
    long_description = fh.read()


setuptools.setup(
    name="fortune-cat",
    version="1.1",
    scripts=['fortune-cat'],
    author="Guido Ferri",
    author_email="guido.ferri@protonmail.com",
    description="A cat that will show a fortune message when piped to it.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GuidoFe/fortune-cat",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
