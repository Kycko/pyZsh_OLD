# глобальные переменные, влияющие на настройку zsh

from   shutil import which
from   sys    import exit as SYSEXIT
import zshconf.varFuncs   as VF

############# проверка окружения
guiterm,inTmux = VF.checkGUI()

############# программы
# если программа не найдена, which выдаёт None
sysBins = {'tmux':which('tmux')}

# защита от запуска модуля
if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
