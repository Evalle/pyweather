from distutils.core import setup

from glob import glob

def fread(path):
  with open(glob(path)[0]) as f:
    return f.read()

def version():
  return fread('VERSION').strip()
 
setup(
  name              = 'pyweather',
  version           = '1.0',
  author            = 'Evgeny Shmarnev',
  author_email      = 'some email',
  url               = 'https://github.com/Evalle/pyweather',
  description       = 'Pyweather is a python cli program which allows you to get accurate weather forecast',
  long_description  = fread('README.*'),
  classifiers       = fread('classification').splitlines(),
  keywords          = 'weather',
  license           = 'MIT',
  scripts           = ['scripts/pyweather'],
#  py_modules        = 'bcolors coordtocity apikey'.split(),
  packages          = ['pyweather'],
)

