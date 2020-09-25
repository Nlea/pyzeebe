import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyzeebe",
    version="1.2.0",
    author="Jonatan Martens",
    author_email="jonatanmartenstav@gmail.com",
    description="Zeebe client api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JonatanMartens/pyzeebe",
    packages=setuptools.find_packages(exclude=("tests",)),
    install_requires=["grpcio~=1.31.0", "protobuf~=3.13.0", "oauthlib~=3.1.0", "requests-oauthlib~=1.3.0"],
    exclude=["*test.py", "tests", "*.bpmn"],
    keywords="zeebe workflow workflow-engine",
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
