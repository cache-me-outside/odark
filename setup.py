import setuptools

setuptools.setup(
    name="Object Detection and Classification Kit (ODACK)",
    version="0.1.0",
    url="",

    author="Tyler Riedal",
    author_email="riedalsolutions@gmail.com",

    description="",
    long_description=open('README.rst').read(),
    include_package_data=True,
    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    entry_points={
        'console_scripts': []
    }
)
