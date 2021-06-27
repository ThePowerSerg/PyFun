
#!/bin/bash

files=$(grep " jane " ../data/list.txt | cut -d '/data/' -f 3)

for file in "$files"; do
   if test -e "$file"; then echo "$file"; else echo "File doesn't exist"; fi
done