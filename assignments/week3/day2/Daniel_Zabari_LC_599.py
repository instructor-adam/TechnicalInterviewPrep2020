class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        rest_dict = {}
        for index, rest in enumerate(list2):
            rest_dict[rest] = index
        min_sum = float("inf")
        values = []
        for index, rest in enumerate(list1):
            if rest in rest_dict:
                temp_sum = rest_dict[rest] + index
                if temp_sum < min_sum:
                    values = [rest]
                    min_sum = temp_sum
                elif temp_sum == min_sum:
                    values.append(rest)
        return values
