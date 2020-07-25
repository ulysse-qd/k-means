#!/usr/bin/python3
##
## EVIDENCEB, 2020
## k_means
## File description:
## k-means function
##

import numpy as np
import math as m
import matplotlib
import sys

def usage():
    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            print("USAGE")
            print("    ./k_means_fcn.py pt cl")
            print("DESCRIPTION")
            print("    pt      Number of points")
            print("    cl      Number of clusters")
            exit(0)
    return

def check_error():
    if len(sys.argv) > 3 or len(sys.argv) == 1:
        print("Wrong number of arguments, try \"-h\" for more informations")
        exit(84)
    if sys.argv[1].isdigit() and sys.argv[2].isdigit():
        return
    else:
        print("Arguments have to be numerical characters.")
        exit(84)

def points_and_barycenter_generator(pts, cl):
    pts_xyd = np.zeros((pts, 2), dtype=int)
    bcenter = np.zeros((cl, 2), dtype=int)
    max_coord = pts * 2

    for i in range(len(bcenter)):
        for j in range(2):
            bcenter[i][j] = np.random.randint(0, max_coord)
    for i in range(len(pts_xyd)):
        for j in range(2):
            pts_xyd[i][j] = np.random.randint(0, max_coord)
    return pts_xyd, bcenter

def k_means_algorithm(points, bary):
    norm = np.zeros((len(points), len(bary)), dtype=int)

    print("First bary :\n", bary, "\n\n")
    for i in range(len(points)):
        for j in range(len(bary)):
            norm[i][j] = np.linalg.norm(points[i] - bary[j], axis=0)
    smallest = np.argmin(norm, axis=1)
    for i in range(len(bary)):
        mean = np.empty((0, 2), dtype=int)
        for j in range(len(smallest)):
            if i == smallest[j]:
                mean = np.append(mean, [points[j]], axis=0)
        if len(mean) != 0:
            bary[i] = np.mean(mean, axis=0)
    print("new bary :\n", bary)
    return bary

if __name__ == '__main__':
    usage()
    check_error()
    points = int(sys.argv[1])
    clusters = int(sys.argv[2])
    points_and_barycenter_generator(points, clusters)
    points_coord, bary_coord = points_and_barycenter_generator(points, clusters)
    for i in range(100):
        bary_coord = k_means_algorithm(points_coord, bary_coord)