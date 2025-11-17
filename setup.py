"""
Setup script for Voidinium
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="voidinium",
    version="0.1.0",
    author="Voidinium Team",
    author_email="team@voidinium.io",
    description="Build with Privacy, Powered by ZK Swarm Intelligence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/voidinium-lab/voidinium",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Security :: Cryptography",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "voidinium=scripts.run_orchestrator:main",
        ],
    },
)
