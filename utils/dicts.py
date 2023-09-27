def get_val(collection, key=None, default='git'):
    if collection == {} or key is None:
        return default
    else:
        return collection[key]

