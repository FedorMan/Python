import numpy as np
import unittest
import task2.task2


class Task1Test(unittest.TestCase):

    def testMy(self):
        np.testing.assert_array_equal(task2.task2.myVersion(np.array(range(20)).reshape(4,5)+1,np.array([1,3,0,2]),np.array([0,2,3,1])), [6,18,4,12])

    def testNumpy(self):
        np.testing.assert_array_equal(
            task2.task2.numpyVersion(np.array(range(20)).reshape(4, 5) + 1, np.array([1, 3, 0, 2]),
                                  np.array([0, 2, 3, 1])), [6, 18, 4, 12])

if __name__ == '__main__':
    unittest.main()