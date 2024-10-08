from setuptools import setup, find_packages

setup(
    name="sara",
    version="1.0",
    url="https://github.com/casterbyte/sara",
    author="Magama Bazarov",
    author_email="caster@exploit.org",
    scripts=['sara.py'],
    description="RouterOS Security Inspector",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license="Apache-2.0",
    keywords=['mikrotik', 'routeros', 'config analyzer'],
    packages=find_packages(),
    install_requires=[
        'colorama',
    ],
    entry_points={
        "console_scripts": ["sara = sara:main"],
    },
    python_requires='>=3.11',
)