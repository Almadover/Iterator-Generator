class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_iter = iter(self.list_of_list)
        self.main_list = []
        self.nested_list = -1
        return self

    def __next__(self):

        self.nested_list += 1

        if len(self.main_list) == self.nested_list:
            self.main_list = None
            self.nested_list = 0
            if self.main_list is None:
                self.main_list = next(self.list_iter)
        return self.main_list[self.nested_list]

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()