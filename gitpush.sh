#!/bin/bash

if [ -z "$1" ]; then
  echo "  使い方:"
  echo "  bash gitpush.sh contest_name num problem"
  echo " Example: $ bash gitpush.sh ABC ABC999 A" 
  exit 1
fi

git add "contests/$1/$2/$3/solution.rb" 
git add "contests/$1/$2/$3/input.txt"
git commit -m "$2 $3 solved"
git push -u origin main
 
