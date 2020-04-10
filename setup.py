import os

from setuptools import find_packages, setup


def long_description():
    this_directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        return f.read()


def list_requirements(file):
    with open(file) as f:
        return [line.strip() for line in f.readlines() if "." not in line]


setup(
    name='Motor-ODM',
    url='https://github.com/Codello/Motor-ODM/',
    license='MIT',
    author='Kim Wittenburg',
    author_email='codello@wittenburg.kim',
    description='A MongoDB ODM based on Motor and Pydantic.',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    keywords="MongoDB AsyncIO ODM Pydantic",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'PyMongo',
        'Motor',
        'Pydantic',
        'Funcy'
    ],
    extras_require={
        'docs': list_requirements('docs/requirements.txt'),
        'dev': [
            'pytest',
            'flake8',
            'isort'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
