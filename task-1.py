const_array = [1, 2, 3, 1, 2, 1, 2, 3]
n_value = 3
let_array = []


def task_1_fun(n):
    for value in const_array:
        if let_array.count(value) < n:
            let_array.append(value)
    return let_array


print("Array Value", task_1_fun(n_value))
print("N Value", n_value)
