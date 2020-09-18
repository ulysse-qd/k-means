#!/usr/bin/python3
##
## EVIDENCEB, 2020
## k_mean
## File description:
## unit_test
##

import unittest
from k_means_fcn import points_and_barycenter_generator
from k_means_fcn import usage
from k_means_fcn import check_error

class test_usage_error(unittest.TestCase):
    def test_usage(self):
        argv = ["./k_means_fcn.py", "-h"]
        retrn = usage(argv)
        self.assertEqual(retrn, 1)

    def test_error_1(self):
        argv = ["./k_means_fcn.py", "4", "4", "4", "10"]
        retrn = check_error(argv)
        self.assertEqual(retrn, 1)

    def test_error_2(self):
        argv = ["./k_means_fcn.py", "4", "oui", "4"]
        retrn = check_error(argv)
        self.assertEqual(retrn, 1)

    def test_error_3(self):
        argv = ["./k_means_fcn.py", "4", "0", "4"]
        retrn = check_error(argv)
        self.assertEqual(retrn, 1)

class test_generation(unittest.TestCase):
    def test_points(self):
        pts, cl = points_and_barycenter_generator(4, 4, 4)
        self.assertEqual(len(pts), 4)
        self.assertEqual(len(pts[0]), 4)

    def test_barycenter(self):
        pts, cl = points_and_barycenter_generator(4, 4, 4)
        self.assertEqual(len(cl), 4)
        self.assertEqual(len(cl[0]), 4)

if __name__ == '__main__':
    unittest.main(argv=3)
