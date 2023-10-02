class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        Awins = 0
        Bwins = 0

        for x in range(1, len(colors)-1):
            if(colors[x] == 'A' and colors[x - 1] == colors[x] and colors[x + 1] == colors[x]):
                Awins += 1
            elif(colors[x] == 'B' and colors[x - 1] == colors[x] and colors[x + 1] == colors[x]):
                Bwins += 1

        if Awins > Bwins:
            return True
        else:
            return False
