# -*- coding:utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deepdata",
    version="0.1.0",
    license="Apache License",
    author="killf",
    author_email="killf@foxmail.com",
    description="A general toolkit for deep learning dataset.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/killf/deepdata",
    packages=setuptools.find_packages(),  # 指定需要安装的模块
    classifiers=[
        # How mature is this project? Common values are
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.2',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        "Operating System :: OS Independent",
    ],
)