class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        hand.sort()
        c = Counter(hand)
        for i in hand:
            if c[i] == 0:
                continue
            for j in range(i, i + groupSize):
                if c[j] == 0:
                    return False
                c[j] -= 1
        return True