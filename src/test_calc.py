##
# @file test_calc.py
# @brief Tests for mathematical library. 

import unittest
import math_lib 

"""! TestCase class """
class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(math_lib.add(2, 3), 5)
        self.assertEqual(math_lib.add(1_000_000_000, 1), 1_000_000_001)
        self.assertEqual(math_lib.add(1, 0.000_000_000_1), 1.000_000_000_1)

    def test_sub(self):
        self.assertEqual(math_lib.sub(1, 1), 0)
        self.assertEqual(math_lib.sub(1.0, 0.999_999_999_9), 0.000_000_000_1)
        self.assertEqual(math_lib.sub(0.999_999_999_9, 1.0), -0.000_000_000_1)

    def test_mul(self):   
        self.assertEqual(math_lib.mul(0, 0), 0)
        self.assertEqual(math_lib.mul(2315523153, 0), 0)
        self.assertEqual(math_lib.mul(123489235, 0.53215231), 65715081.66538285)
        self.assertEqual(math_lib.mul(123489235, 0.523475), 64643527.291625)
        self.assertEqual(math_lib.mul(123489235, 0.9), 111140311.5)
        self.assertEqual(math_lib.div(0.0000000001, 0.0000000001), 1)

    def test_div(self):
        self.assertRaises(Exception, math_lib.div(231, 0))
        self.assertEqual(math_lib.div(0, 3421), 0)
        self.assertEqual(math_lib.div(0.000000001, 0.0000000001), 10)
        self.assertEqual(math_lib.div(0.0000000001, 100), 0) 
        self.assertEqual(math_lib.div(0.0000000001, 10), 0) 
        self.assertEqual(math_lib.div(0.000000001, 123), 0) 
        self.assertEqual(math_lib.div(0.000000001, 5.1), 0.0000000002) 

    def test_fact(self):
        self.assertEqual(math_lib.fact(0), 1)
        self.assertEqual(math_lib.fact(1), 1)
        self.assertEqual(math_lib.fact(13), 6_227_020_800)
        self.assertRaises(Exception, math_lib.fact(2.2))
        self.assertRaises(Exception, math_lib.fact(2.2))
        self.assertRaises(Exception, math_lib.fact(-2.2))

    def test_exp(self): 
        self.assertEqual(math_lib.exp(0, 324234), 0)
        self.assertEqual(math_lib.exp(-1, 324234), 1)
        self.assertEqual(math_lib.exp(-1, 324235), -1)
        self.assertEqual(math_lib.exp(2.3, 3), 12.167)
        self.assertEqual(math_lib.exp(2.3, 6), 148.035889)
        self.assertEqual(math_lib.exp(2.3, 9), 1801.152661463)

    def test_root(self):
        # n = -10
        self.assertRaises(Exception, math_lib.root(0, -10))
        self.assertEqual(math_lib.root(100, -10), 0.630_957_344_5)
        self.assertRaises(Exception, math_lib.root(-100, -10))

        # n = -7
        self.assertRaises(Exception, math_lib.root(0, -7))
        self.assertRaises(Exception, math_lib.root(-100, -7))
        self.assertEqual(math_lib.root(100, -10), 0.630_957_344_5)
        self.assertEqual(math_lib.root(100, -7),  0.517_947_467_9)

        # n = -9.9
        self.assertRaises(Exception, math_lib.root(0, -9.9))
        self.assertEqual(math_lib.root(3, -9.9), 0.894_964_757_8) 
        self.assertRaises(Exception, math_lib.root(-3, -9.9))

        # n = -9.8
        self.assertRaises(Exception, math_lib.root(0, -9.8))
        self.assertRaises(Exception, math_lib.root(-3, -9.8))
        self.assertEqual(math_lib.root(3, -9.8), 0.893_951_912_2) 

        # n = -1
        self.assertEqual(math_lib.root(-1, -1), -1)
        self.assertEqual(math_lib.root(1, -1), 1)
        self.assertEqual(math_lib.root(3, -1), 0.333_333_333_3)
        self.assertEqual(math_lib.root(-3, -1), -0.333_333_333_3)

        # n = 0
        self.assertRaises(Exception, math_lib.root(1, 0))
        self.assertRaises(Exception, math_lib.root(0, 0))
        self.assertRaises(Exception, math_lib.root(-1, 0))

        # n = 0.1 ; x<0 => y>0
        self.assertEqual(math_lib.root(10, 0.1), 1_000_000_000_0)
        self.assertEqual(math_lib.root(-10, 0.1), 1_000_000_000_0)
        self.assertEqual(math_lib.root(0, 0.1),0 )
        self.assertEqual(math_lib.root(0.1, 0.1), 0.000_000_000_1)
        self.assertEqual(math_lib.root(-0.1, 0.1), 0.000_000_000_1)

        self.assertEqual(math_lib.root(0.3, 0.1), 0.000_005_904_9)

        # n = 0.2 ; x<0 => y<0
        self.assertEqual(math_lib.root(10, 0.2), 1_000_00) 
        self.assertEqual(math_lib.root(-10, 0.2), -1_000_00)
        self.assertEqual(math_lib.root(0, 0.2),0)
        self.assertEqual(math_lib.root(0.1, 0.2), 0.00001) 
        self.assertEqual(math_lib.root(-0.1, 0.2), -0.00001) 

        self.assertEqual(math_lib.root(-0.7, 0.2), -0.16807) 
        
        # n = 0.4 ; x<0 => y doesnt exist
        self.assertEqual(math_lib.root(0, 0.4),0)
        self.assertRaises(Exception, math_lib.root(-0.5, 0.4))
        self.assertRaises(Exception, math_lib.root(-25, 0.4))

        self.assertEqual(math_lib.root(1, 0.4), 1) 
        self.assertEqual(math_lib.root(4, 0.4), 32) 
        self.assertEqual(math_lib.root(4, 0.4), 32) 

    def test_mod(self):
        self.assertRaises(Exception, math_lib.mod(1, 0))
        self.assertRaises(Exception, math_lib.mod(0, 0))

        self.assertEqual(math_lib.mod(-5, 2), 1) 
        self.assertEqual(math_lib.mod(-5, 2), 1) 
        self.assertEqual(math_lib.mod(-5.6, 2), 0.4) 
        self.assertEqual(math_lib.mod(-5.23, 2), 0.77) 
        self.assertEqual(math_lib.mod(12353251, 52311235), 12353251) 

if __name__ == "__main__":
    unittest.main()
