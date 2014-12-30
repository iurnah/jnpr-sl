#!/bin/sh 
# Linux users have to change $8 to $9

gawk 'BEGIN {FS = "[0-9]{1,2}:" } { print $2"\n"$3"\n"$4"\n"$5"\n"$6"\n"$7 } '
