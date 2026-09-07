# запросы к базе DNF (и для репозиториев, и локальных пакетов)
# self.api = главный объект, из которого будем доставать инфу

from datetime import datetime
from dnf      import Base as dnfBase
from sys      import exit as SYSEXIT

class DNF():
  def __init__(self):
    # сюда больше ничего не добавляем
    # этот минимальный алгоритм используется для "прогрева" кеша
    try:
      self.api = dnfBase()
      self.api.read_all_repos()
      self.api.fill_sack()
      self.dbLoaded = True  # для проверки, что try выполнился
    except Exception: self.dbLoaded = False
  def query   (self,f={}):  # f = filter
    def _init(f:dict):  # чтобы не писать кучи проверок
      for  key in ['b','fn','pn']:
        if key not in f.keys(): f[key] = None
    ############################ инициализация
    _init(f)
    pkgs = self.api.sack.query()

    ############################ фильтры
    ###### здесь перечислены возможности фильтра f{} (ВСЕ ОПЦИОНАЛЬНЫ)
    ###### b (base) = l/r (локальные/в репозиториях)
    if   f['b'] == 'r': pkgs = pkgs.available()
    elif f['b'] == 'l': pkgs = pkgs.installed()
    ###### fn (full name) = поиск по точному совпадению имени пакета
    if f['fn']: pkgs = pkgs.filter(name=f['fn'])
    ###### pn (part name) = поиск по частичному совпадению имени пакета
    if f['pn']: pkgs = pkgs.filter(name__glob=f"*{f['pn']}*")

    ############################ возвращаем итог
    return [DNFpackage(pkg) for pkg in pkgs]
class DNFpackage():
  def __init__(self,pkgObj):
    # нельзя напрямую наследовать от класса пакета dnf, поэтому так
    self.api       = pkgObj

    self.name      = pkgObj.name
    self.nevra     = str(pkgObj)
    self.epoch     = pkgObj.epoch
    self.version   = pkgObj.version
    self.release   = pkgObj.release

    self.URL       = '' if pkgObj.url is None else pkgObj.url
    self.summary   = pkgObj.summary
    self.desc      = pkgObj.description

    self.arch      = pkgObj.arch
    self.buildtime = datetime.fromtimestamp(pkgObj.buildtime).strftime('%d.%m.%Y')

    self.EVR = f'{self.version}-{self.release}'
    if self.epoch is None: self.epoch = ''
    else:
      self.epoch = str(self.epoch)
      self.EVR   =  f'{self.epoch}:{self.EVR}'

# защита от запуска модуля
if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
