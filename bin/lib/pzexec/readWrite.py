# функции чтения, записи и импорта библиотек

from sys import exit as SYSEXIT
from zshconf.readWrite import *

def write_toFile(lines,file:str,justAdd=False):
  # если justAdd=True, предыдущие данные останутся в файле
  if isinstance(lines,str): lines = [lines]
  mode = ('w','a')[justAdd]

  with open(file,mode,encoding='utf-8') as f:
    # один f.writelines() работает быстрее,
    # чем множество f.write() внутри цикла
    f.writelines(f'{line}\n' for line in lines)

# защита от запуска модуля
if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
