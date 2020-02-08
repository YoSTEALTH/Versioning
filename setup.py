from setuptools import setup, find_packages
from version import versioning


with open('README.rst', 'r') as file:
    long_description = file.read()

package = 'versioning'

setup(url='https://github.com/YoSTEALTH/versioning',
      name=package,
      author='STEALTH',
      version=versioning(package),  # version number is auto generated.
      packages=find_packages(),
      description=('Software versioning based on auto generated year.month.day format.'),
      python_requires='>=3.6',
      long_description=long_description,
      long_description_content_type="text/x-rst",
      classifiers=['License :: Public Domain',
                   'Intended Audience :: Developers',
                   # 'Development Status :: 1 - Planning',
                   'Development Status :: 2 - Pre-Alpha',
                   # 'Development Status :: 3 - Alpha',
                   # 'Development Status :: 4 - Beta',
                   # 'Development Status :: 5 - Production/Stable',
                   # 'Development Status :: 6 - Mature',
                   # 'Development Status :: 7 - Inactive',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Topic :: Software Development :: Libraries :: Python Modules'])
