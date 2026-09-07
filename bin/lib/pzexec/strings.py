# общие для нескольких скриптов строки

from   sys import exit    as SYSEXIT
import pzexec.stringFuncs as SF

separator     = '-'*25
cmdsAvailable = 'Доступные команды:'
addPkg        = 'Добавьте имя пакета'
ownHelp       =  SF.color('(есть HELP)','ylw',True)
userCancel    = '\nОтменено пользователем'

# защита от запуска модуля
if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
