from setuptools import find_packages, setup

setup(
    name="aws_credentials_watcher",
    version="0.0.1",
    license="MIT",
    url="https://github.com/landmaj/aws_credentials_watcher",
    description="Automatically update AWS credentials file.",
    author="Michał Wieluński",
    author_email="michal@w-ski.dev",
    packages=find_packages(),
    install_requires=["pyperclip==1.7.0"],
    entry_points={"console_scripts": ["aws_credentials_watcher=watcher.watcher:main"]},
)
