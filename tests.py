from progs import sumAandB
import unittest

class Test(unittest.TestCase):
    def testSum(self):
        self.assertEqual(sumAandB(1,2), 5)

if __name__=='__main__':
    unittest.main()