#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
    echo "All Good"
else
    echo "Error"
fi