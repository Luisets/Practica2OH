import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="group06", # Replace with your own username
    version="2.0.0",
    author="group06",
    author_email="luis.mlozada@alumnos.upm.es",
    description="Heuristic optimization 1st practical work, by Group 06.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
