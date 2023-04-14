from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.readlines()

setup(
    name='pyanitools',
    version='0.0.1',
    packages=find_packages(include=['pyanitools']),
    include_package_data=True,
    description='File I/O for ani hdf5 files',
    install_requires=install_requires,
    python_requires=">=3.8.*",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering"
    ],
    author="Roman Zubatyuk, Justin S. Smith, Michael Tynes",
    url="https://github.com/miketynes/pyanitools"
)