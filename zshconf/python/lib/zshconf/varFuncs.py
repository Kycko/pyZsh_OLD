# функции инициализации globals, для создания глобальных переменных

from   os  import environ
from   sys import exit   as SYSEXIT
import zshconf.readWrite as RW

def getDistro(file):  # file = объект Path
  def _errExit(file):
    RW.confError(f'файл {file} не найден или недоступен')
  try:
    for line in RW.readFile(file):
      if 'Arch Linux' in line: return 'arch'
      else:
        res = line.split('VERSION_ID="')
        if len(res) > 1:
          return res[1][0]  # второй элемент, первый символ
    _errExit(file)  # если не нашли нужную инфу
  except: _errExit(file)
def checkGUI ():
  # проверяем 'echo $TERM'
  term    = environ.get('TERM','').lower()
  inTmux  = environ.get('TMUX') is not None
  guiterm = term != 'linux' and not inTmux
  return guiterm,inTmux

# защита от запуска модуля
if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
