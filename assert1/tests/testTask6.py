import numpy as np
import unittest
import task6.task6


class Task1Test(unittest.TestCase):

    def testMy(self):
        np.testing.assert_array_equal(task6.task6.myVersion(np.array([2,2,2,3,3,3,5])), np.array([[2,3,5],[3,3,1]]))

    def testNumpy(self):
        np.testing.assert_array_equal(task6.task6.numpyVersion(np.array([2, 2, 2, 3, 3, 3, 5])),
                                      np.array([[2, 3, 5], [3, 3, 1]]))

if __name__ == '__main__':
    unittest.main()