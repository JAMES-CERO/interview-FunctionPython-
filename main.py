'''
Problem 1: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.
'''
def flatten_dict(d):
    res = {}
    for k, value in d.items():
        if isinstance(value, dict):
            newDic = flatten_dict(value)
            for newKeys, newValues in newDic.items():
                res[f'{k}.{newKeys}'] = newValues
        else:
            res[k] = value
    return res



print(flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))


'''
Problem 2: Write a function unflatten_dict to do reverse of flatten_dict.

>>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
{'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
'''

def unflatten_dict(d):
    res ={}
    for k, value in d.items():
        parts = k.split('.')
        current = res
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = value
    return res


print(unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}))
'''
Problem 3: Write a function treemap to map a function over nested list.

>>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
[1, 4, [9, 16, [25]]]
'''


def treemap(func, nestedList):
    if isinstance(nestedList, list):
        return [treemap(func, x) for x in nestedList]
    else:
        return func(nestedList)

print(treemap(lambda x: x*x, [1, 2, [3, 4, [5]]]))