import unittest

from number_of_votes import RankTeams

class test_numberOfVotes(unittest.TestCase):
    def setUp(self):
        self.solution = RankTeams()

    def test_case1(self):
        votes = ["ABC","ACB","ABC","ACB","ACB"]
        self.assertEqual(self.solution.rankTeams(votes), "ACB")

    def test_case2(self):
        votes = ["WXYZ","XYZW"]
        self.assertEqual(self.solution.rankTeams(votes), "XWYZ")

    def test_case3(self):
        votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
        self.assertEqual(self.solution.rankTeams(votes), "ZMNAGUEDSJYLBOPHRQICWFXTVK")

    def test_case4(self):
        votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
        self.assertEqual(self.solution.rankTeams(votes), "ABC")

if __name__ == '__main__':
    unittest.main()