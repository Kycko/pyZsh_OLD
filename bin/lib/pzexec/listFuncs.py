# общие функции обработки списков

from   sys import exit    as SYSEXIT
import pzexec.stringFuncs as SF

# проверка данных
def getMaxLen(list:list,rmColors=True):
  if rmColors: list = cutColors(list)
  return max(map(len,list),default=0)

# преобразование
def cutColors(list:list):
  return [SF.cutColors(item) for item in list]

# защита от запуска модуля
if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
