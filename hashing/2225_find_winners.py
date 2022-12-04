class Solution(object):
    def findWinners(self, matches) -> List[List[int]]:

        losers = defaultdict(int)

        players = set()
        # to hold the players who have played matches

        for match in matches:
            losers[match[1]] += 1
            players.add(match[0])
            players.add(match[1])

        ans = [[], []]

        for player in players:
            if losers[player] == 0:
                ans[0].append(player)
            if losers[player] == 1:
                ans[1].append(player)

        return [sorted(ans[0]), sorted(ans[1])]