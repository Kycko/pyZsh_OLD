# запросы к базам DNF и RPM (для репозиториев и локальных пакетов)

# Функции и свойства в классах DNF/RPM ДОЛЖНЫ ИМЕТЬ ОДИНАКОВЫЕ ИМЕНА
# И ВОЗВРАЩАТЬ ОДИНАКОВЫЕ ОБЪЕКТЫ для удобства обработки
# self.api = главный объект, из которого будем доставать инфу

from dnf import Base as dnfBase
from sys import exit as SYSEXIT

class DNF():
  def __init__(self):
    try:
      self.api = dnfBase()
      self.api.read_all_repos()
      self.api.fill_sack()
      self.dbLoaded = True  # для проверки, что try выполнился
    except Exception: self.dbLoaded = False
  def getAll  (self,filter=''): # получить список всех пакетов
    pkgs = self.api.sack.query()
    if   'r' in filter: pkgs = pkgs.available() # только доступные в репах
    elif 'l' in filter: pkgs = pkgs.installed() # только локально установленные
    return pkgs

# защита от запуска модуля
if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
