# k-means

***

## Algorithm
*k-means clustering* is a method of vector quantization, originally from signal processing, that aims to partition *n* observations into *k* clusters in which each observation belongs to the cluster with the nearest *mean* (cluster centers or cluster centroid), serving as a prototype of the cluster.

## How to use
    ./k_means_fcn.py -h

## Unit test
Run the command :

    python -m unittest unit_test.py

If you want to see line coverage, run :

    coverage run --source=. -m unittest unit_test.py

Then

    coverage report

***

### Dev
Ulysse Queritet-Diop