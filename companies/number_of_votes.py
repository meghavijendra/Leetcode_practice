from typing import List

class RankTeams:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) == 0:
            return ''

        dict = {}
        for vote in votes:
            for i, char in enumerate(vote):
                if char not in dict:
                    dict[char] = [0] * len(vote)
                dict[char][i] += 1
        for key,value in dict.items():
            value.append(-ord(key))
        
        voted_names = sorted(dict.keys())
        return "".join(sorted(voted_names,key=lambda x: dict[x], reverse=True))

