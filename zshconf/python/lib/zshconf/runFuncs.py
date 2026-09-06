# функции запуска программ

from   sys import exit as SYSEXIT
import subprocess      as spr
import zshconf.globals as G

def run(cmd,args=''):
  # cmd может быть списком[] либо строкой
  # доступные args:
  #   s (sudo)
  #   h (shell) NOT recommended
  #   o (out to /dev/null)
  #   e (err to /dev/null)
  #   r (get return code)
  #   t (get txt output)
  # 't' нужен ТОЛЬКО для возврата вывода (например, для записи в переменную)
  # по умолчанию, при args='', вывод будет направлен, как обычно, в терминал
  def _sudo  (shell:bool):
    final = '' if G.isRoot else 'sudo '
    if   shell: return final
    elif final: return [final.strip()]
    else      : return []
  def _return(res  :spr.CompletedProcess):
    if 'r' in args: return res.returncode
    if 't' in args: return res.stdout.split('\n')

  sh  = True        if 'h' in args else None
  err = spr.DEVNULL if 'e' in args else None
  if   's' in args: cmd = _sudo(sh) + cmd
  if   't' in args: out = spr.PIPE
  elif 'o' in args: out = spr.DEVNULL
  else            : out = None

  res = spr.run(cmd,stdout=out,stderr=err,shell=sh,text=True)
  return _return(res)

# защита от запуска модуля
if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
