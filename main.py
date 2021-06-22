#import sys
import psutil, platform
import os, time
import systemInfo

REFRESH_SPEED = 1

clear = lambda: os.system('clear')
clear()

pymonitorLogo = (r"""
                                        _ _             
    _ __  _   _ _ __ ___   ___  _ __ (_| |_ ___  _ __ 
    | '_ \| | | | '_ ` _ \ / _ \| '_ \| | __/ _ \| '__|
    | |_) | |_| | | | | | | (_) | | | | | || (_) | |   
    | .__/ \__, |_| |_| |_|\___/|_| |_|_|\__\___/|_|   
    |_|    |___/
    """)

class textStyles:
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    BLUE = '\u001b[34m'
    YELLOW = '\u001b[33m'
    MAGENTA = '\u001b[35m'
    CYAN = '\u001b[36m'

coreTextColor = ''
systemInfoArt = systemInfo.getBasicSystemInfo()


def colorToUse(core):
    if core < 35:
        coreTextColor = textStyles.GREEN
        #print('checking green')
        return coreTextColor
    if core >= 35 and core <= 75:
        coreTextColor = textStyles.YELLOW
        #print('checking yellow')
        return coreTextColor
    if core > 75:
        coreTextColor = textStyles.RED
        #print('checking red')
        return coreTextColor
    else:
        coreTextColor = textStyles.GREEN
        return coreTextColor

while(True):
    
    print(textStyles.MAGENTA + '   [pymonitor]')
    print(textStyles.YELLOW + systemInfoArt)

    print(textStyles.CYAN + "   %-18s %-15s" % (f"Total cpu  usage: ", f"[{psutil.cpu_percent()}%]"))
    ramStats = psutil.virtual_memory()
    print(textStyles.BLUE + f"   RAM: [{round(ramStats.used / 1000000)}MB / {round(ramStats.total / 1000000)}MB] - [{ramStats.percent}% USED]")

    coreCount = 0
    cpuCores = psutil.cpu_percent(interval=0, percpu=True)
    for core in cpuCores:
        coreTextColor = colorToUse(core)

        #print(coreTextColor + f"core {coreCount} usage: [{core}%]")
        print(coreTextColor + "   %-10s %-5s %-15s" % (f"core {coreCount}", "usage: ", f"[{core}%]"))
        coreCount += 1


    time.sleep(REFRESH_SPEED)
    clear()
