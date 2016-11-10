import numpy as np
import unittest
import task4.task4


class Task1Test(unittest.TestCase):

    def testMy(self):
        self.assertEqual(task4.task4.myVersion(np.array([6,2,0,3,0,0,5,7,0])), 5)

    def testNumpy(self):
        self.assertEqual(task4.task4.numpyVersion(np.array([6,2,0,3,0,0,5,7,0])), 5)

if __name__ == '__main__':
    unittest.main()