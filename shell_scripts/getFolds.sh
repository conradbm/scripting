# Author: Blake Conrad
# Purpose: HW3 CSCI 48100
# Objective: Take a training file iris-shuffled.txt and chop it up using 
#            K-fold cross validation. This file simple chops up 1 
#            training set into 3 different test sets, so we can run 66% 
#            of the data against the other held out 33%. The first fold 
#            is instances 1..50, the second fold is instances 51..100, and the third fold is 
#            101..150 each from the training set. We will be examining the different 
#            metrics of how well our model did based on this 3-fold cross validation 
#            technique.
sed -n 1,50p iris-shuffled.txt > 1stfold_heldout.txt
sed -n 51,150p iris-shuffled.txt > 1stfold_train.txt

sed -n 51,100p iris-shuffled.txt > 2stfold_heldout.txt
sed -n 1,50p iris-shuffled.txt >> 2stfold_train.txt
sed -n 101,150p iris-shuffled.txt >> 2stfold_train.txt

sed -n 101,150p iris-shuffled.txt > 3rdfold_heldout.txt
sed -n 1,100p iris-shuffled.txt > 3rdfold_train.txt

