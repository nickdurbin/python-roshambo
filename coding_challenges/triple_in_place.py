def triple_list_in_place(int_list):
    for idx, item in enumerate(int_list):
        int_list[idx] *= 3

    # No return statement because we've modified the original list in place.
    # There is no need to return another reference to the same list.