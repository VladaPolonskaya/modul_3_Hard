def calculate_structure_sum(*args, **kwargs):
    summa = 0
    for data in args:
        if isinstance(data, int):
            summa += data
        elif isinstance(data, str):
            summa += len(data)
        elif isinstance(data, tuple):
            summa += calculate_structure_sum(*data)
        elif isinstance(data, list):
            summa += calculate_structure_sum(*data)
        elif isinstance(data, set):
            summa += calculate_structure_sum(*data)
        elif isinstance(data, dict):
            for value in data.values():
                if isinstance(value, int):
                    summa += value                          
                elif isinstance(value, str):
                    summa += len(value)
            for key in data.keys():
                if isinstance(key, str):
                    summa += len(key)
    return summa

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)