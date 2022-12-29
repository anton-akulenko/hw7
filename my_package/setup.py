from setuptools import setup, find_packages


setup(name='Folder_sorting',
      version='0.0.1',
      description='Use it for sort files ib required directory',
      url='https://github.com/anton-akulenko/GoIT_hw6/blob/main/HW6.py',
      author='Anton',
      author_email='anton_random@egmail.com',
      license='MIT',
      classifiers= [
            "Programming language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"],
      packages=find_packages(),
      entry_points={'console_scripts': 'clean-folder=HW6:__main__'
      })