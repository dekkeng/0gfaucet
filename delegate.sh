#! /bin/bash

while read -r line; do 
    printf "y\n$line\n" | 0gchaind keys add wallet1 --eth --recover
done < seeds.txt