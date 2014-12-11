from distutils.core import setup

setup(name='Warhammer 40k Army Builder', # the package/module name
      version='1.0', # the version (an arbitrary string)
      author='Michael Degan', # someone to blame
      author_email='michael.degan@tricity.wsu.edu', # where to flame
      py_modules=[ 'army', 'MyGui', 'squad', 'unit', 'vehicle', 'weapon'], # modules in the package 
      )
