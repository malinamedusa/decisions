def bracket(entry):  # take pound in []

    entry = list(entry)
    for x in range(len(entry)):
        if entry[x] == '.':
            entry[x] = '[.]'

    return ''.join(entry)
