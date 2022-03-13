from decimal import DivisionByZero
from math import factorial
import unittest
import calc

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(1_000_000_000, 1), 1_000_000_001)
        self.assertEqual(calc.add(1, 0.000_000_000_1), 1.000_000_000_1)

    def test_sub(self):
        self.assertEqual(calc.sub(1, 1), 0)
        self.assertEqual(calc.sub(1.0, 0.999_999_999_9), 0.000_000_000_1)
        self.assertEqual(calc.sub(0.999_999_999_9, 1.0), -0.000_000_000_1)

    def test_mul(self):
        self.assertEqual(calc.mul(0, 0), 0)
        self.assertEqual(calc.mul(2315523153, 0), 0)
        self.assertEqual(calc.mul(123489235, 0.53215231), 65_715_081.665)
        self.assertEqual(calc.mul(123489235, 0.523475), 64643527.292)
        self.assertEqual(calc.mul(123489235, 0.9), 111140311.5)
        self.assertEqual(calc.div(0.0000000001, 0.0000000001), 1)

    def test_div(self):
        self.assertRaises(Exception, calc.div(231, 0))
        self.assertEqual(calc.div(0, 3421), 0)
        self.assertEqual(calc.div(0.000000001, 0.0000000001), 10)
        self.assertEqual(calc.div(0.0000000001, 100), 0) 
        self.assertEqual(calc.div(0.0000000001, 10), 0) 
        self.assertEqual(calc.div(0.000000001, 123), 0) 
        self.assertEqual(calc.div(0.000000001, 5.1), 0.0000000002) 

    def test_fact(self):
        self.assertEqual(calc.fact(0), 1)
        self.assertEqual(calc.fact(1), 1)
        self.assertEqual(calc.fact(13), 6_227_020_800)
        self.assertRaises(TypeError, calc.fact(2.2))
        self.assertRaises(ValueError, calc.fact(2.2))
        self.assertRaises(TypeError, calc.fact(-2.2))

    def test_exp(self):
        self.assertEqual(calc.exp(0, 324234), 0)
        self.assertEqual(calc.exp(-1, 324234), -1)
        self.assertEqual(calc.exp(2.3, 3), 12.167)
        self.assertEqual(calc.exp(2.3, 6), 148.035889)
        self.assertEqual(calc.exp(2.3, 9), 1801.1526615)

    def test_root(self):
        # n = -10
        self.assertEqual(calc.root(0, -10), float('inf'))
        self.assertEqual(calc.root(100, -10), 0.630_957_344_5)
        self.assertRaises(Exception, calc.root(-100, -10))

        # n = -7
        self.assertEqual(calc.root(0, -7), float('inf'))
        self.assertEqual(calc.root(100, -7),  0.517_947_467_9)
        self.assertEqual(calc.root(-100, -7), -0.517_947_467_9)

        # n = -9.9
        self.assertEqual(calc.root(0, -9.9), float('inf'))
        self.assertEqual(calc.root(3, -9.9), 0.894_964_757_8) 
        self.assertEqual(calc.root(-3, -9.9), -0.517_947_467_9)

        # n = -9.8
        self.assertEqual(calc.root(0, -9.8), float('inf'))
        self.assertEqual(calc.root(3, -9.8), 0.893_951_912_2) 
        self.assertEqual(calc.root(-3, -9.8), -0.893_951_912_2)

        # n = -1
        self.assertEqual(calc.root(-1, -1), -1)
        self.assertEqual(calc.root(1, -1), 1)
        self.assertEqual(calc.root(3, -1), 0.333_333_333_3)
        self.assertEqual(calc.root(-3, -1), -0.333_333_333_3)

        # n = 0
        self.assertRaises(Exception, calc.root(1, 0))
        self.assertRaises(Exception, calc.root(0, 0))
        self.assertRaises(Exception, calc.root(-1, 0))

        # n = 0.1 ; x<0 => y>0
        self.assertEqual(calc.root(10, 0.1), 1_000_000_000_0)
        self.assertEqual(calc.root(-10, 0.1), 1_000_000_000_0)
        self.assertEqual(calc.root(0, 0.1),0 )
        self.assertEqual(calc.root(0.1, 0.1), 0.000_000_000_1)
        self.assertEqual(calc.root(-0.1, 0.1), 0.000_000_000_1)

        self.assertEqual(calc.root(0.3, 0.1), 0.000_005_904_9)

        # n = 0.2 ; x<0 => y<0
        self.assertEqual(calc.root(10, 0.2), 1_000_00) 
        self.assertEqual(calc.root(-10, 0.2), -1_000_00)
        self.assertEqual(calc.root(0, 0.2),0)
        self.assertEqual(calc.root(0.1, 0.2), 0.00001) 
        self.assertEqual(calc.root(-0.1, 0.2), -0.00001) 

        self.assertEqual(calc.root(-0.7, 0.2), -0.16807) 
        
        # n = 0.4 ; x<0 => y doesnt exist
        self.assertEqual(calc.root(0, 0.4),0)
        self.assertRaises(Exception, calc.root(-0.5, 0.4))
        self.assertRaises(Exception, calc.root(-25, 0.4))

        self.assertEqual(calc.root(1, 0.4), 1) 
        self.assertEqual(calc.root(4, 0.4), 32) 
        self.assertEqual(calc.root(4, 0.4), 32) 
        self.assertEqual(calc.root(8, 0.4), 181.01933598) 

    def test_mod(self):
        self.assertRaises(Exception, calc.mod(1, 0))
        self.assertRaises(Exception, calc.mod(0, 0))

        self.assertEqual(calc.mod(-5, 2), 1) 
        self.assertEqual(calc.mod(-5, 2), 1) 
        self.assertEqual(calc.mod(-5.6, 2), 0.4) 
        self.assertEqual(calc.mod(-5.23, 2), 0.76) 
        self.assertEqual(calc.mod(12353251, 52311235), 12353251) 

if __name__ == "__main__":
    unittest.main()
