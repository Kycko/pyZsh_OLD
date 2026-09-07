# общие функции обработки строк

from   sys import exit as SYSEXIT
import pzexec.globals  as G

# преобразование
def color       (string:str,colr:str,bold=False):
  colors          = G.colors['term']
  final           =   colors[colr]
  if bold: final +=   colors['bld']
  final          +=   str(string) # защита от TypeError
  final          +=   colors['rst']
  return final
def cutColors   (string:str): # вырезает из строки все цвета
  # можно использовать для правильного подсчёта длины строки
  for color in G.colors['term'].values():
    string = string.replace(color,'')
  return string
def alignColored(string:str,finalLen:int):
  # здесь ljust() не используем: он не учитывает цвета
  addLen = finalLen - len(cutColors(string))
  return string + ' '*addLen

# защита от запуска модуля
if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
