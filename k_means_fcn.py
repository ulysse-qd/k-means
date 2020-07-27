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

def usage(argv):
    if len(argv) == 2:
        if argv[1] == "-h":
            print("USAGE")
            print("    ./k_means_fcn.py pt n cl")
            print("DESCRIPTION")
            print("    pt      Number of points")
            print("    n       Number of dimensions")
            print("    cl      Number of clusters")
            return 1
    return 0

def check_error(argv):
    if len(argv) > 4 or len(argv) == 1:
        print("Wrong number of arguments, try \"-h\" for more informations")
        return 1
    if argv[1].isdigit() != True or argv[2].isdigit() != True or argv[3].isdigit() != True:
        print("Arguments have to be numerical characters.")
        return 1
    if int(argv[1]) <= 0 or int(argv[2]) <= 0 or int(argv[3]) <= 0:
        print("Arguments can't be 0 or less.")
        return 1
    return 0

def points_and_barycenter_generator(pts, n, cl):
    pts_xyd = np.zeros((pts, n), dtype=int)
    bcenter = np.zeros((cl, n), dtype=int)
    max_coord = pts * 2

    for i in range(len(bcenter)):
        for j in range(n):
            bcenter[i][j] = np.random.randint(0, max_coord)
    for i in range(len(pts_xyd)):
        for j in range(n):
            pts_xyd[i][j] = np.random.randint(0, max_coord)
    print("First bary :\n", bcenter, "\n\n")
    return pts_xyd, bcenter

def k_means_algorithm(points, bary, dim):
    norm = np.zeros((len(points), len(bary)), dtype=int)

    for i in range(len(points)):
        for j in range(len(bary)):
            norm[i][j] = np.linalg.norm(points[i] - bary[j], axis=0)
    smallest = np.argmin(norm, axis=1)
    for i in range(len(bary)):
        mean = np.empty((0, dim), dtype=int)
        for j in range(len(smallest)):
            if i == smallest[j]:
                mean = np.append(mean, [points[j]], axis=0)
        if len(mean) != 0:
            bary[i] = np.mean(mean, axis=0)
    return bary

def main(argv):
    if usage(argv) != 0:
        exit(0)
    if check_error(argv) != 0:
        exit(84)
    points = int(argv[1])
    dim = int(argv[2])
    clusters = int(argv[3])
    points_coord, bary_coord = points_and_barycenter_generator(points, dim, clusters)
    for _ in range(100) :
        bary_coord = k_means_algorithm(points_coord, bary_coord, dim)
    print("New barycenters :\n", bary_coord)
    return 0

if __name__ == '__main__':
    main(sys.argv)