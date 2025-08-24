def triste(i):
    if i == 1:
        return 1
    elif i == 2:
        return 1
    else:
        return triste(i - 1) + triste(i - 2)
