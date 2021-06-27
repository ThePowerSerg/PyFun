#!/usr/bin/env bash

#-----Variables
#myvar="Hello"
#echo "My variable's value is: $myvar"

#----Arrays
declare -a snacks=("apple" "banana" "orange")
#echo ${snacks[2]}

snacks[5]="grapes"
snacks+=("mango")

#echo ${snacks[@]}

for i in {0..10}; do 
    echo "$i: ${snacks[$i]}"; 
done

#---Associative Arrays
declare -A office
office[city]="San Fran"
echo $office[city]