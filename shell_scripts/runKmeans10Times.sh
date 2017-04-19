#!/bin/bash
#
#
# Run this script as follows:
#
# sh runKmeans10Times.sh 3 | grep ‘purity’
#
# Arg0 => $0 => File Name
# Arg1 => $1 => Next Arg, i.e., our K value
#
$
for i in {0..10}; do python asign2_bmconrad.py iris.txt $1; done
