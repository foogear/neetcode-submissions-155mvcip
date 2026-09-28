class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        lenHand = len(hand)
        if lenHand % groupSize != 0:
            # print("exit")
            return False

        hand.sort()
        totalGroup = lenHand // groupSize
        cardWantedByGroup = {}
        groupRemainSlot = [groupSize] * totalGroup

        # print(f"totalGroup {totalGroup}") ####fhdjdjdjjdjdjdjdjd
        # print(groupRemainSlot) ####
        # print(cardWantedByGroup) ####

        groupId = None
        for card in hand:
            groupId = None
            # print("***********") ####
            # print(f"card {card}") ####

            if card not in cardWantedByGroup:
                if not totalGroup:
                    return False
                else:
                    totalGroup -= 1
                    groupId = totalGroup
            else:
                groupId = cardWantedByGroup[card].pop()
                if  not cardWantedByGroup[card]:
                    del cardWantedByGroup[card]

            groupRemainSlot[groupId] -= 1
            if groupRemainSlot[groupId]:
                if card + 1 not in cardWantedByGroup:
                    cardWantedByGroup[card + 1] = []
                cardWantedByGroup[card + 1].append(groupId)

            # print(f"totalGroup {totalGroup}") ####
            # print(groupRemainSlot) ####
            # print(cardWantedByGroup) ####

        if not cardWantedByGroup:
            return True

        return False