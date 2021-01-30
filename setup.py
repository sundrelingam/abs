import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="abs-sundrelingam",
    version="0.0.1",
    author="Vaakesan Sundrelingam",
    author_email="vaakesan.sundrelingam@gmail.com",
    description="Grab bag ab workout.",
    long_description="Uses a list of your favourite ab exercises in a randomized, timed workout.",
    long_description_content_type="text/markdown",
    url="https://github.com/sundrelingam/abs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)