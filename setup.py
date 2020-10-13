import setuptools
setuptools.setup(name='xtract',
      version='1.0',
      description='extracts text from broken docx files',
      url='',
      author='Bichwaa',
      author_email='morandevelopers@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=[
          'fire',
      ],
      classifiers=[
        "Programming Language :: Python :: 3",
    ],
      entry_points={
    'console_scripts': [
        'xtractor = xtractor:recover',
    ],}
    )
