# всё важное, что должно выполняться в самом конце

from   sys import exit as SYSEXIT
import zshconf.globals as G

def _export(db:dict,key:str):
  for var,value in db.items(): print(f'{key} {var}="{value}"')

_export(G.exports,'export')
_export(G.aliases,'alias')

# clear в TTY обновляет цвета всего экрана
# в guiterm этого не делаем, чтобы не сбрасывать экран при подключении по SSH
if G.firstShell and not G.guiterm: print('clear')
print('fastfetch')

# защита от запуска модуля
if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
