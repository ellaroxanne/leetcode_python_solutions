class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        my_str = ''
        for i in digits:
            my_str += str(i)
        new_str = str(int(my_str) + 1)
        new_list = []
        for i in range(len(new_str)):
            new_list.append(int(new_str[i]))
        return new_list
