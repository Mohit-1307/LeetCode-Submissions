class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)

        for row in image:
            l, r = 0, n - 1

            while l <= r:
                row[l], row[r] = row[r] ^ 1, row[l] ^ 1
                l += 1
                r -= 1

        return image