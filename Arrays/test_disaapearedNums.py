import unittest

from disappeared_num import findDisappearedNumbers

class test_TestDisappearedNum(unittest.TestCase):
    def test_returns_valid_output(self):
        self.assertEqual(findDisappearedNumbers([4,3,2,7,8,2,3,1]), [5,6])

    def test_returns_valid_output_2(self):  
        self.assertEqual(findDisappearedNumbers([1,1]), [2])                                

    def test_returns_inavlid_output(self):
        self.assertNotEqual(findDisappearedNumbers([4,3,2,7,8,2,3,1]), [4,5,6])

    def test_returns_empty_list(self):
        self.assertEqual(findDisappearedNumbers([]), [])
    
if __name__ == '__main__':
    unittest.main()