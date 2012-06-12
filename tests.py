import unittest

from vector import *

class VectorTests(unittest.TestCase):
    def test_init(self):
        self.assertEqual(vector(), tuple())
        self.assertEqual(vector(()), tuple())
        self.assertEqual(vector([]), tuple())
        self.assertEqual(vector((1,)), (1,))
        self.assertEqual(vector([1]), (1,))

    def test_v(self):
        self.assertEqual(v(), vector())
        self.assertEqual(v(1), vector([1]))
        self.assertEqual(v(1,2), vector([1,2]))
        with self.assertRaises(TypeError):
            v(x=1)
        with self.assertRaises(TypeError):
            v(1, z=3)

    def test_eq(self):
        self.assertEqual(vector([1,2]), vector([1,2]))
        self.assertEqual(vector([1,2]), (1,2))
        self.assertTrue(vector([1,2]) == (1,2))
        self.assertFalse(vector([1,2]) == [1,2])

    def test_req(self):
        self.assertEqual((1,2), vector([1,2]))
        self.assertTrue((1,2) == vector([1,2]))
        self.assertFalse([1,2] == vector([1,2]))

    def test_pos(self):
        self.assertEqual(+vector([1,2]), vector([1,2]))

    def test_neg(self):
        self.assertEqual(-vector([1,2]), vector([-1,-2]))

    def test_add(self):
        self.assertEqual(vector([1,2]) + vector([3,4]), (4,6))
        self.assertEqual(vector([1,2,3]) + vector([4,5,6]), (5,7,9))
        self.assertEqual(vector([1,0]) + (0,-1), (1, -1))
        with self.assertRaises(TypeError):
            vector([0,-1]) + 1

    def test_radd(self):
        self.assertEqual((1,2) + vector([3,4]), vector([4, 6]))
        self.assertEqual([1,2,3] + vector([4,5,6]), vector([5,7,9]))
        with self.assertRaises(TypeError):
            1 + vector([0,-1])

    def test_iadd(self):
        x = vector([1,2])
        x += vector([3,4])
        self.assertEqual(x, vector([4,6]))
        x = vector([1,2])
        x += (3,4)
        self.assertEqual(x, vector([4,6]))
        with self.assertRaises(TypeError):
            x = vector([0,-1])
            x += 1

    def test_sub(self):
        self.assertEqual(vector([1,2]) - vector([3,4]), (-2, -2))
        self.assertEqual(vector([4,5,6]) - vector([1,2,3]), (3, 3, 3))
        self.assertEqual(vector([1,0]) - (0,-1), (1, 1))

    def test_rsub(self):
        self.assertEqual((1,2) - vector([3,4]), vector([-2, -2]))
        self.assertEqual([4,5,6] - vector([1,2,3]), vector([3, 3, 3]))
        with self.assertRaises(TypeError):
            1 - vector([0,-1])

    def test_isub(self):
        x = vector([1,2])
        x -= vector([3,4])
        self.assertEqual(x, vector([-2, -2]))
        x = vector([4,5,6])
        x -= (1,2,3)
        self.assertEqual(x, (3, 3, 3))
        with self.assertRaises(TypeError):
            x = vector([0,-1])
            x -= 1

    def test_mul(self):
        self.assertEqual(vector([1,2]) * 2, vector([2, 4]))
        self.assertEqual(vector([4,5,6]) * 2, vector([8, 10, 12]))
        self.assertEqual(vector([1,2]) * (3,4), 1*3 + 2*4)
        with self.assertRaises(ValueError):
            vector([1,2]) * vector([3,4,5])
        with self.assertRaises(ValueError):
            vector([1,2,3]) * vector([4,5])

    def test_rmul(self):
        self.assertEqual(2 * vector([1,2]), vector([2, 4]))
        self.assertEqual(2 * vector([4,5,6]), vector([8, 10, 12]))
        self.assertEqual((3,4) * vector([1,2]), 3*1 + 4*2)
        with self.assertRaises(ValueError):
            vector([1,2]) * vector([3,4,5])
        with self.assertRaises(ValueError):
            vector([1,2,3]) * vector([4,5])

    def test_repr(self):
        self.assertEqual(repr(vector()), "v()")
        self.assertEqual(repr(vector([1, 0, -1])), "v(1, 0, -1)")

    def test_str(self):
        self.assertEqual(str(vector()), "<>")
        self.assertEqual(str(vector([1, 0, -1])), "<1, 0, -1>")

