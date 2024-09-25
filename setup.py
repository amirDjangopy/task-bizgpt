from setuptools import setup, find_packages

setup(
    name='my_project',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
        'selenium',
        'beautifulsoup4',
        'markdownify',
        'sentence-transformers',
        'psycopg2',
    ],
)
