from setuptools import setup

setup(name='takeover',
      version='0.1',
      description='Sub-Domain TakeOver Vulnerability Scanner',
      url='https://github.com/m4ll0k/takeover',
      author='m4ll0k',
      author_email='m4ll0k@protonmail.com',
      license='MIT',
      scripts=['takeover.py'],
      install_requires=[
          'requests',
          'urllib3',
      ],
      entry_points={
          'console_scripts': ['takeover=takeover:main'],
      },
      zip_safe=False)
