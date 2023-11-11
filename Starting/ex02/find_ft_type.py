def all_thing_is_obj(object: any) -> int:
    _type = object.__class__.__name__.capitalize()

    if _type == 'Str':
        print(f"{object} is in the kitchen: {type(object)}")
    elif _type == 'Int':
        print("Type not found")
    else:
        print(f"{_type}: {type(object)}")

    return 42
