import numpy as np
import unittest
import task1.task1


class Task1Test(unittest.TestCase):

    def testMy(self):
        self.assertEqual(task1.task1.myVersion(np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]])), 3)

    def testNumpy(self):
        self.assertEqual(task1.task1.numpyVersion(np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]])), 3)

if __name__ == '__main__':
    unittest.main()