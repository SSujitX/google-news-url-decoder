from setuptools import setup, find_packages

setup(
    name="googlenewsdecoder",
    version="0.1.4",
    description="A python package to decode Google News URLs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SSujitX/google-news-url-decoder",
    author="Sujit Biswas",
    author_email="ssujitxx@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
