#! /usr/bin/env bash
# run the given command as a background process and hide output
$* &>/dev/null &
# Capture the process id of the above process
pid="$!"
# quit this script if someone presses Ctrl+C
trap exit SIGINT
# print the top output including header info
top -b n1 -n1 -p "$pid"
# check if the program is still running
while test -d /proc/"$pid"/ ; do
    # get the top info for this process
    top -b n1 -n1 -p "$pid"  | tail -1
    # sleep for 0.2 seconds before the next output
    sleep 0.2
done
