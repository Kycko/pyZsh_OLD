# глобальные переменные, влияющие на настройку zsh

from   os      import getuid,environ
from   pathlib import Path
from   shutil  import which
from   sys     import exit as SYSEXIT
import zshconf.varFuncs    as VF


########### каталоги
# home
dirs = {'home':Path('/home/kycko')}
# репозитории
dirs['repos'] = {'local':{'root':dirs['home']/'data/repos'}}
# рабочие
dirs['work'] = {'cloud':dirs['home']/'data/cloud/build'}
# промпт
dirs['prompt'] = {  # замены путей в промпте
  str(dirs['repos']['local']['root']):{
    'distro':['arch','red'],
    'subst' : 'data/repos'
    },
  str(dirs['work']['cloud'])         :{
    'distro':['red'],
    'subst' : 'work'
    }
  }

########### файлы
files = {
  'distro' :Path('/etc/os-release'),
  'plugins':{
    'arch' :[
      Path('/usr/share/doc/pkgfile/command-not-found.zsh'),
      Path('/usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh')
      ],
    '8'    :[Path('/usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh')]
    }
  }

########### горячие клавиши
hotkeys = {
  'up'           :{'code':'^[[A'   ,'action':'up-line-or-beginning-search'},
  'down'         :{'code':'^[[B'   ,'action':'down-line-or-beginning-search'},
  'delete'       :{'code':'^[[3~'  ,'action':'delete-char'},
  'ctrlRight'    :{'code':'^[[1;5C','action':'forward-word'},
  'ctrlLeft'     :{'code':'^[[1;5D','action':'backward-word'},
  'ctrlBackspace':{'code':'^H'     ,'action':'backward-kill-word'},
  # ↓ чтобы срабатывало даже если в строке что-то введено
  'ctrlD'        :{'code':'^D'     ,'action':'exit_zsh'}
  }

########### цвета
colors = {
  'prompt':{
    'lines'    :{
      'local'  :{'user' :VF.fColor('yellow',True),
                 'root' :VF.fColor('red'   ,True)},
      'ssh'    :{'user' :VF.fColor('cyan'  ,True),
                 'root' :VF.fColor('red'   ,True)}
      },
    'dirPrefix':VF.fColor('yellow',False)
    },
  'TTY'   :{
    # 0 = цвет фона
    '0':'0b0c0f',  # grey  (orig name: black)
    '1':'e78285',  # red
    '2':'87d18c',  # green
    '3':'e19d7b',  # brown (orig name: yellow)
    '4':'95baf4',  # blue
    '5':'ad8dd8',  # magenta
    '6':'87c9d3',  # cyan
    # 7 = основной текст
    '7':'d1d2da',  # white
    # 8 = цвет для zsh-autosuggestions
    '8':'494e5e',  # grey  (orig name: black)
    '9':'e78285',  # red
    'A':'87d18c',  # green
    'B':'d8d398',  # yellow
    'C':'9bc6ff',  # blue
    'D':'ad8dd8',  # magenta
    'E':'6feee6',  # cyan
    'F':'d1d2da'   # white
    }
  }

########### программы
# если программа не найдена, which выдаёт None
sysBins = {}
for bin in ['dircolors','git','python3','tmux']:
  sysBins[bin] = which(bin)


########### проверка окружения
isRoot = getuid() == 0

distro   = VF.getDistro(files['distro'])  # 'arch'/'7'/'8'
isArch   = distro == 'arch'
distType = ['red','arch'][isArch]

guiterm,inTmux = VF.checkGUI()
# если вдруг уровень оболочки не задан, задаём 1
firstShell = int(environ.get('SHLVL',1)) == 1

sshDistro = VF.checkSSH()
inSSH     = sshDistro is not None

########### модули/плагины
try   : sources_toLoad = files['plugins'][distro]
except: sources_toLoad = []

############# прочее
termSymbols = '╭╰>' if guiterm else '┌└>'

########### алиасы и экспорты
aliases = {
  ####### git
  'gs'  :f"{sysBins['git']} status",
  # в gd='git diff' не работает автодополнение
  'gdh' : 'git diff HEAD',  # в моём git есть разбивка по guiterm
  'gl'  :f"{sysBins['git']} log",
  'ga'  :f"{sysBins['git']} add --all && {sysBins['git']} status",
  'gc'  :f"{sysBins['git']} commit -m",
  ####### прочее
  'clr' :'clear && fastfetch',
  'diff':'diff --color=auto',
  'grep':'grep -i --color=auto',
  'less':'less_wrapper',
  'ls'  :'ls -lah --color=auto',
  'ping':'ping -c 3',
  'py'  : sysBins['python3'],
  'rg'  :'rg -i',
  'sctl':'systemctl'
  }

for al in ['mount','umount','visudo']: aliases[al] = VF.sudo(isRoot) + al
if not isArch: aliases['cdBuildCloud'] = f"cd {dirs['work']['cloud']}"

# экспорты = то что в .zshrc прописывается как 'export EDITOR=nano'
exports = {'EDITOR'        :'nano',
           'VISUAL'        :'nano', # важный аналог переменной EDITOR
           'HISTSIZE'      :'6505',
           'SAVEHIST'      :'6505',
           # ↓ здесь {HOME}, чтобы корректно работало у root'а
           'HISTFILE'      :'${HOME}/.zshHistory',
           # ↓ чтобы работало удаление в корзину в VS Code
           'ELECTRON_TRASH':'kioclient',
           '_pzIsArch'     :str(isArch)}  # нужно для подмены less


# защита от запуска модуля
if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
