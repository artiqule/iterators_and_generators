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


def flat_generator(d_list):
    while d_list:
        item = d_list.pop(0)
        if isinstance(item, list):
            d_list.extend(item)
        else:
            yield item


for item in flat_generator(nested_list):
        print(item)
