import setuptools

setuptools.setup(
    name='django-meta-tag-view',
    version='2020.7.1',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
