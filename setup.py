import os
from setuptools import setup, find_packages

_ROOT = os.path.dirname(os.path.realpath(__file__))


def readme():
    with open(os.path.join(_ROOT, 'README.rst')) as f:
        return '\n' + f.read()


def find_requirements(testing=False):
    filename = 'requirements_test.txt' if testing else 'requirements.txt'
    requirements = []

    with open(os.path.join(_ROOT, filename), 'r') as f:
        for line in (l.strip() for l in f):
            if not line or line[0] in ('#', '-'):
                continue
            requirements.append(line)

    return requirements


setup(
    name="pylogrus",
    version="0.3.2",
    description="PyLogrus is a structured logger for Python which is inspired by Logrus Golang library",
    long_description=readme(),
    author="Vitalii Myhal",
    author_email="xmig.mir@gmail.com",
    url="https://github.com/vmig/pylogrus",
    license="MIT License",
    keywords="logger logging colorize output json extra fields",
    packages=find_packages(exclude=['examples']),
    include_package_data=True,
    install_requires=find_requirements(),

    # List additional groups of dependencies here. You can install these using the following syntax:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': [],
        'test': find_requirements(testing=True)
    },

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Customer Service',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Logging',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
    ]
)
