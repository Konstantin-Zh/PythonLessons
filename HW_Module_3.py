
def calculate_structure_sum(data_structure):
    ncount = 0
    for el in data_structure:
        if isinstance(el, list) or isinstance(el, set) or isinstance(el, tuple):
            if len( list(el)) == 0:
                continue
            else:
                ncount += calculate_structure_sum(el)
        elif isinstance(el, dict):
            ncount += calculate_structure_sum(dict(el).keys())
            ncount += calculate_structure_sum(dict(el).values())
        elif isinstance(el, str):
            ncount += len( str(el))
        elif isinstance(el, int):
            ncount += int(el)
        elif isinstance(el, float):
            ncount += float(el)
        elif isinstance(el, bool) and bool(el):
            ncount += 1

    return ncount


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))