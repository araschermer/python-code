def calculate_rewards(grades: [float]):
    """given a list of grades represented by positive integers
    returns rewards number that suits the students grades in the same given
    orders """
    # Runtime: O(n), space: O(n)
    # initializing the rewards with minimum of 1 for each grade
    rewards = [1 for _ in grades]
    # iterating forwards
    for index in range(1, len(grades)):
        # if the current grade greater than the previous grade:
        #  increase the corresponding reward by 1
        if grades[index] > grades[index - 1]:
            rewards[index] = 1 + rewards[index - 1]
        # if duplicates exist :
        # same rewards  for the same  grades
        elif grades[index] == grades[index - 1]:
            rewards[index] = rewards[index - 1]
        else:
            #  if the current grade is smaller then the previous grade:
            # reward for current grade=1
            continue
    # iterating backwards: handle the reward corresponding to grades in descending order
    for index in range(len(grades) - 2, -1, -1):
        # if the current grade is greater following grade
        if grades[index] > grades[index + 1]:
            #  the rewards  numbers is the maximum between the current assignment
            # and the reward of the following grade +1
            rewards[index] = max(rewards[index + 1] + 1, rewards[index])
        elif grades[index] <= grades[index + 1]:
            # otherwise, continue, these cases have been handled in the previous for loop
            continue

    return rewards


print(calculate_rewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))
print(calculate_rewards([0, 0, 0, 1, 0, 2]))
print(calculate_rewards([0, 0, 0, 0]))
print(calculate_rewards([0, 0, 0, 1, 0]))
