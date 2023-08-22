from setuptools import find_packages, setup

setup(
    name="recsystools",
    versions="0.0.1",
    description="An usesfull tool for recsys",
    package_dir={"recsystools": "recsystools"},
    packages=find_packages(where="recsystools"),
    author="tanlocnguyen296",
    author_email="tanlocnguyen296@gmail.com",
    license="MIT",
)
