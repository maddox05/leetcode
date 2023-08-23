class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowers_placed = 0
        for index, i in enumerate(flowerbed):
            if flowerbed.__len__() == 1:
                if flowerbed[index] ==0:
                    flowers_placed+=1
                    break
                else:
                    break
            if 1 <= index < flowerbed.__len__() - 1:
                if flowerbed[index - 1] == 0 and flowerbed[index] == 0 and flowerbed[index + 1] == 0:
                    flowerbed[index] = 1
                    flowers_placed += 1
            elif index == 0:
                if flowerbed[index] == 0 and flowerbed[index + 1] == 0:
                    flowerbed[index] = 1
                    flowers_placed += 1
            elif index == flowerbed.__len__() - 1:
                if flowerbed[index] == 0 and flowerbed[index - 1] == 0:
                    flowerbed[index] = 1
                    flowers_placed += 1

        if flowers_placed >= n:
            return True
        else:
            return False
