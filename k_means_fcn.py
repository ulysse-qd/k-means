#!/usr/bin/python3
##
## EVIDENCEB, 2020
## k_means
## File description:
## k-means function
##

import numpy as np
import pandas as pds
import matplotlib.pyplot as plt
import math as m
import matplotlib
import random
import sys
import copy

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
    if len(argv) != 4:
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
    np.random.seed(1)

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
    return bary, smallest

def display_graph(clust_df, bary):
    fig = plt.figure(figsize=(8,8))
    axe = fig.add_subplot(1, 1, 1)
    axe.set_xlabel('X', fontsize=15)
    axe.set_ylabel('Y', fontsize=15)
    axe.set_title('2D Clustering Representation')
    clusts = [0, 1, 2]
    colors = ['r', 'g', 'b']
    for target, color, in zip(clusts, colors):
        indicesToKeep = clust_df['cluster'] == target
        axe.scatter(clust_df.loc[indicesToKeep, 'x'], clust_df.loc[indicesToKeep, 'y'],
                    c=color, s=50)
    for i in range(len(bary)):
        axe.scatter(bary[i][0], bary[i][1], c='black')
    axe.legend(clusts)
    axe.grid()
    plt.show()
    return

def main(argv):
    if usage(argv) != 0:
        exit(0)
    if check_error(argv) != 0:
        exit(84)
    points = int(argv[1])
    dim = int(argv[2])
    clusters = int(argv[3])
    points_coord, bary_coord = points_and_barycenter_generator(points, dim, clusters)
    bary_2 = copy.deepcopy(bary_coord)
    bary_1, pnt_clust = k_means_algorithm(points_coord, bary_coord, dim)
    for _ in range(300) :
        if (bary_2 == bary_1).all() :
            break
        else :
            bary_2 = copy.deepcopy(bary_1)
            bary_1, pnt_clust = k_means_algorithm(points_coord, bary_coord, dim)
    print("New barycenters :\n", bary_coord)
    clust_df = pds.DataFrame(pnt_clust, columns=['cluster'])
    points_df = pds.DataFrame(points_coord, columns=['x', 'y'])
    points_df = pds.concat([points_df, clust_df], axis=1).reindex(points_df.index)
    display_graph(points_df, bary_1)
    print(points_df)
    return 0

if __name__ == '__main__':
    main(sys.argv)