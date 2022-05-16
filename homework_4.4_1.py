nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]


class FlatIterator:

    def __init__(self, nested_list):
        self.item = sum(nested_list, [])

    def __iter__(self):
        return iter(self.item)

    def __next__(self):
        return self


for item in FlatIterator(nested_list):
        print(item)
