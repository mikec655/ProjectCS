from setuptools import setup, find_packages

setup(name='centrale',
      version='0.1',
      description='Zonnescherm- & rolluikenbediening centrale',
      author='Mike Clarke',
      author_email='mikec655@gmail.com',
      url='https://github.com/mikec655/ProjectCS.git',
      packages=['centrale'],
      install_requires=[
        "serial"
        ],
      )