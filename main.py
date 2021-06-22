import psutil
import os, time

REFRESH_SPEED = 1

clear = lambda: os.system('clear')
clear()

class textStyles:
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    BLUE = '\u001b[34m'
    YELLOW = '\u001b[33m'
    MAGENTA = '\u001b[35m'

coreTextColor = ''


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
        return coreTextColor

while(True):
    print(textStyles.MAGENTA + """
                                        _ _             
    _ __  _   _ _ __ ___   ___  _ __ (_| |_ ___  _ __ 
    | '_ \| | | | '_ ` _ \ / _ \| '_ \| | __/ _ \| '__|
    | |_) | |_| | | | | | | (_) | | | | | || (_) | |   
    | .__/ \__, |_| |_| |_|\___/|_| |_|_|\__\___/|_|   
    |_|    |___/                                       
    """)


    coreCount = 0
    cpuCores = psutil.cpu_percent(interval=0, percpu=True)
    for core in cpuCores:
        coreTextColor = colorToUse(core)

        print(coreTextColor + f"   core {coreCount} usage: [{core}%]")

        coreCount += 1

    ramStats = psutil.virtual_memory()
    print(textStyles.BLUE + f"   RAM: [{round(ramStats.used / 1000000)}MB / {round(ramStats.total / 1000000)}MB]")

    time.sleep(REFRESH_SPEED)
    clear()
