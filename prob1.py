class Solution:
    def rotate(self, arr: list[int]) -> list[int]:
        temp = arr[-1]
        arr[-1] = arr[0]
        for i in range(len(arr)-2, -1, -1):
            temp, arr[i] = arr[i], temp
        return arr
        
    def feedPeople(self, food: list[int], people: list[int]) -> int:
        if len(food) != len(people):
            return -1
        
        if food == people:
            return 0

        if len(food) == 1:
            return -1

        for i in range(2, len(food)+1):
            food = self.rotate(food)
            # print(food, people)
            if food == people:
                return i

        return -1
