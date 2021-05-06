def get_distance(index1, index2):
    return abs(index1 - index2)


def apartment_hunting(blocks, requirements):
    """This function returns the minimum maximum distance needed to reach all the requirements given in a list of requirements,
     regarding a certain block given in a  a list of block that partially
    contain the requirements"""
    # Runtime:O(B^2*R), B for blocks, R for requirements
    # Space complexity:  O(B)
    maximum_distance = [float('-inf') for _ in blocks]
    for index1, block in enumerate(blocks):
        for requirement in requirements:
            closest_requirement_distance = float("inf")
            for index2 in range(len(blocks)):
                if blocks[index2][requirement]:
                    closest_requirement_distance = min(closest_requirement_distance, get_distance(index1, index2))
            maximum_distance[index1] = max(closest_requirement_distance, maximum_distance[index1])
    return maximum_distance.index(min(maximum_distance))


if __name__ == '__main__':
    blocks_table = {0: {'gym': False, "school": True, 'store': False},
                    1: {'gym': False, "school": True, 'store': False},
                    2: {'gym': True, "school": True, 'store': False},
                    3: {'gym': False, "school": True, 'store': True}}
    requirements_list = ["gym", "school", "store"]
    print(apartment_hunting(blocks=blocks_table, requirements=requirements_list))
