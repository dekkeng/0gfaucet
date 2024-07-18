#! /bin/bash

while read -r line; do 
    printf "y\n$line\n" | 0gchaind keys add wallet1 --eth --recover
    printf "y\n" | 0gchaind tx staking delegate $1 999900ua0gi --from wallet1 --chain-id zgtendermint_16600-2 --gas=auto --gas-adjustment=1.7
done < seeds.txt