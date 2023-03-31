def get_query(cmd, val, file):
    if cmd == 'filter':
        res = list(filter(lambda x: val in x, file))
    if cmd == 'map':
        res = '\n'.join([x.split()[int(val)] for x in file])

    if cmd == 'unique':
        res = list(set(file))

    if cmd == 'sort':
        is_reverse = val == 'desc'
        res = sorted(file, reverse=is_reverse)

    if cmd == 'limit':
        res = list(file)[:int(val)]

    return res