from setuptools import setup, find_packages

setup(name='centrale',
      version='0.1',
      description='Zonnescherm- & rolluikenbediening centrale',
      author='Mike Clarke',
      author_email='mikec655@gmail.com',
      url='https://github.com/mikec655/ProjectCS.git',
      packages=find_packages(exclude=['centrale']),
      install_requires=[
        "pyserial>=3.4",
        "matplotlib>=3.0.0"
        ],
      )