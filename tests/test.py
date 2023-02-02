import PyUnikeyNT

succeed = PyUnikeyNT.initialize()
assert succeed, "initialize failed"

mode = PyUnikeyNT.get_current_mode()
print(mode)

mode = PyUnikeyNT.Mode(not mode.value)
PyUnikeyNT.set_current_mode(mode)

mode = PyUnikeyNT.get_current_mode()
print(mode)
