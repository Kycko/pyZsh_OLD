# функции чтения, записи и импорта библиотек

from importlib.util import module_from_spec,spec_from_file_location
from sys            import exit as SYSEXIT

# запуск файлов, аргументы
def importModule(file): # file = объект Path
  spec = spec_from_file_location(file.stem,file)
  mod  = module_from_spec(spec)
  spec.loader.exec_module(mod)
  return mod

# защита от запуска модуля
if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
