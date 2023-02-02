import os, ctypes
from enum import Enum

__author__      = "Vic P."
__version__     = "1.0"
__unikey_nt_obj = None
__unikey_nt_pkg = "PyUnikeyNT"

class Mode(Enum):
  EN = 0
  VI = 1

def initialize(process_id=0) -> bool:
  global __unikey_nt_obj
  if __unikey_nt_obj is None:
    # get module file path
    file_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(file_path, ["Win32", "x64"][ctypes.sizeof(ctypes.c_void_p)//8])
    file_path = os.path.join(file_path, f"{__unikey_nt_pkg}.dll")
    assert os.path.exists(file_path), f"{__unikey_nt_pkg} module not found."
    # load the module into memory
    try:
      __unikey_nt_obj = ctypes.cdll.LoadLibrary(file_path)
    except OSError: pass
  assert __unikey_nt_obj is not None, f"{__unikey_nt_pkg} module loading failed."
  # initialize the module
  return __unikey_nt_obj.unikey_nt_initialize(process_id) == 0

def get_current_mode() -> Mode:
  global __unikey_nt_obj
  assert __unikey_nt_obj is not None, f"{__unikey_nt_pkg} module not yet initialized."
  return Mode(__unikey_nt_obj.unikey_nt_get_current_mode())

def set_current_mode(mode: Mode):
  global __unikey_nt_obj
  assert __unikey_nt_obj is not None, f"{__unikey_nt_pkg} module not yet initialized."
  __unikey_nt_obj.unikey_nt_set_current_mode(mode.value)
  return None
