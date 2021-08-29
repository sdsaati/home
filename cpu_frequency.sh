#!/usr/bin/env bash

function power_saving {

    # Set the governor to ondemand for all processors
    for cpu in /sys/devices/system/cpu/cpufreq/policy*; do
        echo powersave > ${cpu}/scaling_governor
    done
    # Reduce the boost threshold to 80%
    #echo 80 > /sys/devices/system/cpu/cpufreq/ondemand/up_threshold
    for x in /sys/devices/system/cpu/*/cpufreq/; do echo 2500000 | tee $x/scaling_max_freq; done
}
FUNC=$(declare -f power_saving)
THE_PASS=$(kdialog --password "sudo password required")
echo $THE_PASS | sudo -S bash -c "$FUNC; power_saving"
