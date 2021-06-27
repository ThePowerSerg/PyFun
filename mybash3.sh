
#!/bin/bash

files=$(grep " jane " ../data/list.txt | cut -d' ' -f 3)

for file in $files; do
  newfile="~"$file
  echo $newfile
  if test -e $newfile; then echo "File exists"; else echo "File doesn't exist"; fi
  if test -e ~/data/jane_profile_07272018.doc; then echo "File exists"; else echo "File doesn't exist"; fi
  if [-d $newfile]
  then echo "yes"
done