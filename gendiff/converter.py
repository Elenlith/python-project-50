def normalize_elem(elem):
    if type(elem) is bool and elem is True:
        result = 'true'
    elif type(elem) is bool and elem is False:
        result = 'false'
    elif elem is None:
        result = 'null'
    else:
        result = elem
    return result
