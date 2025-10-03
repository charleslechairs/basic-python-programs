def mean_eshan(list):
    if len(list) == 0:
        return 0
    return sum(list) / len(list)

def mode_eshan(list):
    if len(list) == 0:
        return 0
    f = {}
    for i in list:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    max_count = max(f.values())
    modes = [k for k, v in f.items() if v == max_count]
    if len(modes) == len(f):
        return 0  
    return modes 

def median_eshan(list):
    if len(list) == 0:
        return 0
    l = len(list)
    m = l // 2
    if l % 2 == 0:
        return (list[m - 1] + list[m]) / 2
    else:
        return list[m]

def stdvar_eshan(list):
    if len(list) == 0 or len(list) == 1:
        return 0
    mean = mean_eshan(list)
    var = sum((x - mean) ** 2 for x in list) / (len(list) - 1)
    return var

def stddev_eshan(list):
    var = stdvar_eshan(list)
    return var ** 0.5
    