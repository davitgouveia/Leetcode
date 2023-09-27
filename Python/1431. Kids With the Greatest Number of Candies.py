class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = []

        for _ in range(len(candies)):
            if candies[_] + extraCandies >= max(candies):
                results.append(True)
            else:
                results.append(False)
        
        return results
