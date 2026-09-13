import exceptions as e

def inspect_component(object):
    name = getattr(object, "__name__", None)
    doc = getattr(object, "__doc__", None)
    module = getattr(object, "__module__", None)
    qualname = getattr(object, "__qualname__", None)
    dicti = getattr(object, "__dict__", None)
    slots = getattr(object, "__slots__", None)
    print(f"{object}:\n -Name: {name}\n -Docstring: {doc}\n -Module: {module}\n -Qual Name: {qualname}\n -Dict: {dicti}\n -Slots: {slots}")


