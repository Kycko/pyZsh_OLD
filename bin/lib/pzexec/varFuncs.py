# разные глобальные функции, не подходящие для других модулей

from sys import exit as SYSEXIT

# прочие мелкие
def getIB(type:str,index:int):  # IB = index/boolean
  # служебная функция; возвращает сам index либо true/false
  return index if type == 'index' else index >= 0

# защита от запуска модуля
if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
