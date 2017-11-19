from setuptools import setup

setup(
    name='meta',
    version='0.0.1',
    install_requires=[
            'click',
            'tqdm',
            'bokeh',
            'palettable',
            'numpy',
            'scipy',
            'pathos',
            'typing'
    ],
    extras_require={
        'dev': [
            'coverage',
            'flake8',
            'mypy',
            'pytest',
            'pytest-cov',
            'towncrier',
            'coverage-badge'
        ]
    },
    author='Daniel Suo',
    author_email='danielsuo@gmail.com',
    url='https//github.com/danielsuo/meta',
    license='MIT',
    keywords='meta',
    packages=['meta'],
    python_requires='>=3.4',
    entry_points='''
[console_scripts]
'''
)
