from setuptools import setup, find_packages

with open("README.rst", encoding = "utf-8") as f:
    long_description = f.read()

setup(
    name = "mekanismPy",
    license = "MIT",
    version = "1.0.0",
    packages = find_packages(),
    outhor = "hihimamu",
    outhor_email = "hihimamug14@gmail.com",
    url = "https://github.com/hihimamuLab/mekanismPy.git",
    description = "mekanism material calculator",
    long_description = long_description,
    long_description_content_type = "text/x-rst",
    keywords = ["mekanism", "minecraft", "hihimamu", "mekanismPy"]
    )
