from typing import Type, TypeVar

T = TypeVar("T")


def convertTo(source: object, target: Type[T], default: any = None):
    """Convert the source object to target object based on name of class properties

    Params:
        - source: object
        - target: Type -> type of the object that's going to be created
        - default: any -> the default value that the target's not mapped fields are going to have
    """

    target: T = target()

    for key in target.__dict__:
        try:
            value = source.__getattribute__(key)
        except AttributeError:
            value = default
        target.__setattr__(key, value)

    return target


def mapBy(**kwargs):
    """Convert the source object to the target object and alters the mapping according to the args

    Params:
        - fields: dict -> (decorator param) a dict that contains in the key the name of the target's field name and the value is the name of the source field name
        - source: object
        - target: Type -> type of the object that's going to be created
        - default: any -> the default value that the target's not mapped fields are going to have
    """

    def wrapper(_):
        def func_wrapper(source: object, target: Type[T], default: any = None):
            fields = kwargs["fields"]
            target: T = target()

            for key in target.__dict__:
                try:
                    if key in fields:
                        value = source.__getattribute__(fields[key])
                    else:
                        value = source.__getattribute__(key)
                except AttributeError:
                    value = default

                target.__setattr__(key, value)

            return target

        return func_wrapper

    return wrapper
