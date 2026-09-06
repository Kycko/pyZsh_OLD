# функции инициализации globals, для создания глобальных переменных

from os  import environ
from sys import exit as SYSEXIT

def checkGUI():
  # проверяем 'echo $TERM'
  term    = environ.get('TERM','').lower()
  inTmux  = environ.get('TMUX') is not None
  guiterm = term != 'linux' and not inTmux
  return guiterm,inTmux

# защита от запуска модуля
if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
