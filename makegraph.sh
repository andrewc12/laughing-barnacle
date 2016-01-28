#!/bin/sh
for i in $(basename -s .dot *.dot)
do
dot -Tpng -o $i.png $i.dot
dot -Tsvg -o $i.svg $i.dot
done
#dot -Tpng -o flow.png flow.dot
#dot -Tsvg -o flow.svg flow.dot

