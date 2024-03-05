#!/bin/bash
cd /home/radar_test/backends/

declare -A radars
declare -A radar
radar_codes=()

radar_name="han"
radar_codes+=($radar_name)
radar[addr]=143.210.44.18
radar[in_port]=9696
radar[out_port]=9000
for key in "${!radar[@]}"; do
  radars[$radar_name,$key]=${radar[$key]}
done


borealis_radars=( han )
for i in "${radar_codes[@]}"
do
    if [[ " ${borealis_radars[*]} " == *"$i"* ]];
    then
        screen -d -m -S $i python3 realtimedisplay_borealis.py ${radars[$i,addr]} ${radars[$i,in_port]} ${radars[$i,out_port]}
    else
        screen -d -m -S $i python3 realtimedisplay.py ${radars[$i,addr]} ${radars[$i,in_port]} ${radars[$i,out_port]}
    fi
done

