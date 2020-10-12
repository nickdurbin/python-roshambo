def triple_list_out_of_place(int_list):
    # Allocate a new list with enough room for all of the elements
    tripled_list = [None] * len(int_list)

    for idx, item in enumerate(int_list):
        tripled_list[idx] = item *= 3

    return tripled_list