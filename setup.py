from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

    config = {
    'install_requires': requirements,
    'packages': find_packages(),
    'scripts': [],
    'name': 'tagging-repo'
}

setup(**config)
