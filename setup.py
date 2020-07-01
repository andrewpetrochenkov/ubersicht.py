import setuptools

setuptools.setup(
    name='ubersicht',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
