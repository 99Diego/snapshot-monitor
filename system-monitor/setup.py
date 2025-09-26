from setuptools import setup, find_packages

setup(
    name="snapshot",
    version="0.1.0",
    description="Utility to monitor system and save snapshots",
    author="Diego López Arango",
    packages=find_packages(),
    install_requires=["psutil"],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "snapshot=snapshot.monitor:main",
        ],
    },
)

