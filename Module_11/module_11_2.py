import inspect
from inspect import getmembers


def introspection_info(obj):
    result = {}

    typ_obj = type(obj)
    result['tipe'] = typ_obj.__name__

    anydir = dir(obj)
    atrib = [attr for attr in anydir  if not callable(getattr(obj, attr))]
    result['attributes'] = atrib

    meth = [method for method in anydir if callable(getattr(obj, method))]
    result['methods'] = meth

    obj_module = ('builtins' if inspect.getmodule(obj) is None else inspect.getmodule(obj))
    result['module'] = obj_module

    return(result)


number_info = introspection_info(42)
print(number_info)