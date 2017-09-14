def to_bool(some_string):
    false_terms = {'False', 'false', '0', 0, False, None}
    true_terms = {'True', 'true', '1', 1, True}

    if some_string in false_terms:
        return False
    elif some_string in true_terms:
        return True
    else:
        raise ValueError('Value neither True or False')