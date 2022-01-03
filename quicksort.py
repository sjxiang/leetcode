def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot_index = 0
        pivot = array[pivot_index]
        less_part = [
                n for n in array[pivot_index+1:] if n <= pivot
                ]

        great_part = [
                n for n in array[pivot_index+1:] if pivot < n
                ]

        return quicksort(less_part) + [pivot] + quicksort(great_part)

    return -1


def test_quicksort():
    import random
    ll = list(range(20))
    random.shuffle(ll)  # 打乱后
    print(ll)

    assert quicksort(ll) == sorted(ll)


if __name__ == "__main__":
    test_quicksort()
