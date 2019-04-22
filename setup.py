import setuptools

with open('README.rst') as f:
    long_description = f.read()

setuptools.setup(
    name='cmdfunctools',
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    description='make python functions usable from command line',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url='http://pypi.python.org/pypi/cmdfunctions',
    author='Mr-Io',
    author_email='macrigaud@gmail.com',
    packages=['cmdfunctools'],
    python_requires='>=3.7, <4',
    classifiers=['Development Status :: 3 - Alpha',
                 "Intended Audience :: Developers",
                 "Natural Language :: English",
                 "License :: OSI Approved :: MIT License",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.7",
                 "Programming Language :: Python :: Implementation :: CPython",
                 "Programming Language :: Python :: Implementation :: PyPy"],
)
