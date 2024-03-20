class reversePyramid:
    @staticmethod
    def reversepyramid():
        print('---')
        temp = 0
        op = ""
        character_to_add = "*"
        character_to_add_S = " "
        for i in range(9, 1, -1):
            temp = ((9 - i) * 2)
            if temp >= 9:
                break
            # print(int(temp/2))
            print(9 - i)
            op = op + "\n" + character_to_add_S * (9 - i) + (
                    9 - ((9 - i) + (9 - i))) * character_to_add + character_to_add_S * (9 - i)
            # print(op)

            # print(temp)
        print(op)

    reversepyramid()
# *********
#  *******
#   *****
#    ***
#     *

# for j in range
