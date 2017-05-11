#!/bin/bash

#######################################################################################
### Author: Blake Conrad
### Purpose: Create a dataframe object for a .csv file input
###          Get hands on experience with shell scripting
### Usage: bash read-file.sh yourFile.csv
#######################################################################################

##########################################################
### Create and return a dataframe-like object
##########################################################
createDataFrame() {
    echo "*************************************"
    echo "******** Creating Data Frame ********"
    echo "*************************************"
    ##########################################################
    ### Get Command Line Arguments
    ##########################################################
    file=$1
    
    ##########################################################
    ### Get the number of samples
    ##########################################################
    num_samples=$(cat $file | wc -l)
    echo "Number of Samples: " $num_samples
    
    ##########################################################
    ### Store samples
    ##########################################################
    samples=($(cat $file))
    #echo "Test Line 1: " 
    #echo ${samples[0]} #row1
    #echo "Test Line 2: " 
    #echo ${samples[1]} #row2
    #echo
    
    ##########################################################
    ### Get dimensions of each sample
    ##########################################################
    IFS="," read -a sample_fields_chopped <<< "${samples[0]}"
    dims=$(expr ${#sample_fields_chopped[@]} - 1)
    echo "Number of Fields: " ${#sample_fields_chopped[@]}
    echo "Number of dimensions: " $dims
    echo 
    
    ##########################################################
    # Create containers to hold the dataframe
    ##########################################################
    row_container=() # has num_lines items
    row_count=0
    for sample in "${samples[@]}"
    do

        ###
        ### IFS works similarly to array.split(",") in Python
        ### you pass it an indiviudal line with a delimter
        ### then it will store it into the variable A_ROW
        ### which simply gets overwritten each itteration
        ### We then look through each dimension of that array
        ### 
        IFS="," read -ra A_ROW <<< "$sample"
        #echo ${A_ROW[@]}
        col_container=() # holds dims items
        col_count=0
        for dim_value in "${A_ROW[@]}"
        do
            #echo $i."~"
            col_container+=($dim_value)
            #echo ${list[$inner_count]} "~"
            col_count=$((col_count + 1))
        done
        #echo ${col_container[*]}
        row_container[$row_count]=${col_container[*]}
        #echo ${row_container[$row_count]}
        row_count=$((row_count + 1))
    done
    ######################################################################################
    ### PRO-TIP: Parameter Expansion
    ### This allows for you to slice like in Python
    ### http://stackoverflow.com/questions/1335815/how-to-slice-an-array-in-bash
    ######################################################################################
    echo ${row_container[*][1]}
}

DEFAULT=default                             # Default param value.

function main () {
   if [ -z "$1" ]                           # Is parameter #1 zero length?
   then
     echo "Error: You did not specify a file argument."  # Or no parameter passed.
   else 
        if [ "$2" ]
            then
            echo "Error: You've specified too many parameters."
        fi
     echo "Success: Filename: \"$1\"."
     echo "Creating Data Frame Object from \"$1\""
     createDataFrame $1
   fi

   return 0
}

main $1
