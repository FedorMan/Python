import numpy as np
import unittest
import task3.task3


class Task1Test(unittest.TestCase):

    def testMy(self):
        self.assertEqual(task3.task3.myVersion(np.array([1,2,4,2]),np.array([4,2,1,2])), True)

    def testNumpy(self):
        self.assertEqual(task3.task3.numpyVersion(np.array([1, 2, 4, 2]), np.array([4, 2, 1, 2])), True)

if __name__ == '__main__':
    unittest.main()