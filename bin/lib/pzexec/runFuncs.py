# функции запуска и остановки программ

from sys import exit as SYSEXIT
from zshconf.runFuncs import *

# прочие мелкие
def raiseError(): raise ValueError('app forced ValueError!')

# защита от запуска модуля
if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
