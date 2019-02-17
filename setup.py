import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyvfx.menus",
    version="0.0.1",
    author="Zachary Cole",
    author_email="zcole@nzaneproductions.com",
    description="A package to find & import menu.py files -"
                "in all packages colocated with this package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nzanepro/pyvfx.menus",
    py_modules=["init", "userSetup"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
