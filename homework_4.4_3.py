nested_list = [
	[
        ['a', 'b', 'c'],
        [1, 2, 3]
    ],
	[
        ['d', 'e', 'f'],
        [4, 5, 6]
    ],
	[
        ['g', 'h', 'i'],
        [7, 8, 9]
    ]
]

class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        new_list = []
        while self.nested_list:
            item = self.nested_list.pop(0)
            if isinstance(item, list):
                self.nested_list.extend(item)
            else:
                new_list.append(item)
        return iter(new_list)

    def __next__(self):
        return self

for item in FlatIterator(nested_list):
	print(item)
