multi_lists = [1,2,3,[4,5,6,[7,8,[444,55,66]]],"a","b","c",[1,2,3,[4,5,6,[7,8,9]]]]

def iterate_multi_list(multi_list):
    for list_data in multi_list:
        if isinstance(list_data, list):
            iterate_multi_list(list_data)
        else:
            print(list_data)


iterate_multi_list(multi_lists)