from setuptools import setup, find_packages

setup(
    name="googlenewsdecoder",
    version="0.1.6",
    description="A Python package to decode Google News URLs to their original sources.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SSujitX/google-news-url-decoder",
    author="Sujit Biswas",
    author_email="ssujitxx@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=["requests>=2.32.3", "selectolax>=0.3.21"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="google news decoder",
    project_urls={
        "Bug Tracker": "https://github.com/SSujitX/google-news-url-decoder/issues",
        "Documentation": "https://github.com/SSujitX/google-news-url-decoder#readme",
        "Source Code": "https://github.com/SSujitX/google-news-url-decoder",
    },
    python_requires=">=3.9",
)
