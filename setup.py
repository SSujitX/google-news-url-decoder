from setuptools import setup, find_packages
import os


def get_version():
    version_file = os.path.join(
        os.path.dirname(__file__), "googlenewsdecoder", "__version__.py"
    )
    with open(version_file, "r") as f:
        version_vars = {}
        exec(f.read(), version_vars)
    return version_vars["__version__"]


setup(
    name="googlenewsdecoder",
    version=get_version(),
    description="A Python package to decode Google News URLs to their original sources.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SSujitX/google-news-url-decoder",
    author="Sujit Biswas",
    author_email="ssujitxx@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=["requests>=2.32.3", "selectolax>=0.3.27", "pysocks>=1.7.1"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    keywords="google news decoder",
    project_urls={
        "Bug Tracker": "https://github.com/SSujitX/google-news-url-decoder/issues",
        "Documentation": "https://github.com/SSujitX/google-news-url-decoder#readme",
        "Source Code": "https://github.com/SSujitX/google-news-url-decoder",
    },
    python_requires=">=3.9",
)
