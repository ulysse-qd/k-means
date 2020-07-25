#!/usr/bin/python3
##
## EVIDENCEB, 2020
## k_mean
## File description:
## unit_test
##

import unittest
from k_means_fcn import points_and_barycenter_generator

class test_generation(unittest.TestCase):
    "Test case utilisé pour tester la génération de points dans les clusters"
    def test_point(self):
        "Test la generation aleatoire des points."
        pts,cl = points_and_barycenter_generator(100, 3)
        self.assertEqual(len(pts), 100)

    def test_cluster(self):
        'Test la generation aleatoire des barycentres'
        pts,cl = points_and_barycenter_generator(100, 3)
        self.assertEqual(len(cl), 3)

if __name__ == '__main__':
    unittest.main()


