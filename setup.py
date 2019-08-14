from setuptools import (
    setup,
    find_packages,
)

setup(
    name='aws_credentials_watcher',
    version='0.0.1',
    license='MIT',
    author='Michał Wieluński',
    author_email='michal@w-ski.dev',
    packages=find_packages(),
    install_requires=["pyperclip==1.7.0"]
)
