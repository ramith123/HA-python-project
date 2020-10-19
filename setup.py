from setuptools import setup

setup(
    name="HA controls",
    version="0.2",
    py_modules=["main"],
    install_requires=["Click", "requests"],
    entry_points={
        "console_scripts": ["bac=main:acControls", "blight=main:lightsControls"],
    },
)