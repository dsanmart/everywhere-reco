from setuptools import setup, find_packages
from pathlib import Path

# version
here = Path(__file__).absolute().parent
version_data = {}
with open(here.joinpath("everywhere", "__init__.py"), "r") as f:
    exec(f.read(), version_data)
version = version_data.get("__version__", "0.0")

install_requires = [
    "numpy>=1.19",  # 1.19 required by tensorflow 2.6
    "pandas>1.0.3,<2",
    "ipykernel>=4.6.1,<7",
    "pytest>=3.6.4",
    "scikit-learn>=0.20.3",
    "imblearn",
]

setup(
    name="everywhere",
    version=version,
    install_requires=install_requires,
    package_dir={"everywhere": "everywhere"},
    python_requires=">=3.6, <3.11",
    packages=find_packages(where=".", exclude=["docs", "examples", "tests"])
)
