from setuptools import setup, find_packages

requirements = []

setup_requirements = []

test_requirements = []


setup(
    name="mylib",
    version="0.0.1",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 0.0.1",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="my lib package",
    url="http://github//mylib",
    author="Rachid Benouini",
    keywords="mylib",
    author_email="benouini.rachid@gmail.com",
    license="",
    install_requires=requirements,
    setup_requires=setup_requirements,
    test_suite="tests",
    include_package_data=True,
    tests_require=test_requirements,
    packages=find_packages(),
    zip_safe=False,
)
