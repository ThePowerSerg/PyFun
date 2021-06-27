#!/bin/bash

declare -i a=3
if [[ $a -gt 10 ]]; then
    echo "$a is greater than 10."
else
    echo "$a is NOT greater than 10."
fi