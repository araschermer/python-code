row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? please enter two numbers  for the positions you  want, "
                 "such as 23 for the position of the second column and the  third row ")
# placing user input on the map
horizontal = int(position[0]) # first character of the input is for the horizontal position
vertical = int(position[1]) # second is for the vertical position
treasure_map[vertical - 1][horizontal - 1] = "X"  # to address the right indices of the map
print(f"{row1}\n{row2}\n{row3}")