class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        if len(hand) % groupSize != 0:
            return False
        prev = hand[0]
        hand.pop(0)
        k = 1
        i = 0
        while len(hand):
            print(hand)
            if k == groupSize:
                prev = hand[0]
                hand.pop(0)
                k = 1
                i = 0
                continue
            
            if i >= len(hand):
                return False
            
            curr = hand[i]
            if curr != prev + 1:
                i = i + 1
            else:
                k += 1
                prev = curr
                hand.pop(i)

        return True
