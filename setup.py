from setuptools import setup

setup(
    name='gist-dl',
    version='0.0.1',
    py_modules=['gist_dl'],
    install_requires=[
        'click',
        'requests',
        'pygithub'
    ],
    entry_points='''
        [console_scripts]
        gist-dl=gist_dl:dl
    ''',
)
