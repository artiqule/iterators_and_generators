nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'h']
]


def flat_generator(d_list):
    for item in sum(d_list, []):
        yield item


for item in flat_generator(nested_list):
        print(item)
