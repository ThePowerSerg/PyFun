#!/bin/bash

for file in *.HTM; do
    name=$(basename "$file" .HTM)
    mv "$file" "$name.html"
    # this line can be used to test and make sure the script behaves as expected
    # echo mv "$file" "$name.html"
done