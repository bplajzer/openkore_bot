#!/bin/bash
sleep ${2}
cd eng && ./openkore.pl --profile=${1} --logs=./logs/${1}
