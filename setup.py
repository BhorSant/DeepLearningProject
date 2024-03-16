import os
import setuptools 

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "DeepLearningProject"
AUTHOR_USER_NAME = "BhorSant"
SRC_REPO = "Xray"
AUTHOR_EMAIL = "santoshbhor2001@gmail.com"
setuptools.setup(
    name="Xray",
    version="0.1.0",
    author="Santosh Bhor",
    author_email="santoshbhor2001@gmail.com",
    description="A Small Project of the Xray Dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SantBhor/DeepLearningProject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)