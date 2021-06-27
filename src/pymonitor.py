import psutil, platform, os
import time
#(•‿•)
import systemInfo
from textColors import textStyles, colorToUse

REFRESH_SPEED = 1.5
SYSTEM_INFO_ART = textStyles.YELLOW + systemInfo.getBasicSystemInfo()
TITLE = textStyles.MAGENTA + '   [ｐｙｍｏｎｉｔｏｒ - (•‿•)]'
clearCommand = ''



def clear():
    os.system(clearCommand)

def getRamUsage():
    ramStats = psutil.virtual_memory()
    return textStyles.BLUE + f"   RAM: [{round(ramStats.used / 1000000)}MB / {round(ramStats.total / 1000000)}MB] - [{ramStats.percent}%]"

def getCoreUsage():
    cpuCores = psutil.cpu_percent(interval=0, percpu=True)
    return cpuCores

def pymonitorMainLoop():
    while(True):
        print(TITLE)
        print(SYSTEM_INFO_ART)
        print(textStyles.CYAN + "   %-18s %-15s" % (f"Total cpu  usage: ", f"[{psutil.cpu_percent()}%]"))
        print(getRamUsage())

        print(textStyles.BLUE + '   <------------------------->')
        coreCount = 0
        cpuCores = getCoreUsage()
        for core in cpuCores:
            coreTextColor = colorToUse(core)
            print(coreTextColor + "   %-10s %-5s %-15s" % (f"core {coreCount}", "usage: ", f"[{core}%]"))
            coreCount += 1
        print(textStyles.BLUE + '   <------------------------->')

        time.sleep(REFRESH_SPEED)
        clear()



if __name__ == "__main__":
    if platform.system() == 'Windows':
        clearCommand = 'cls'
    else:
        clearCommand = 'clear'
    clear()
    pymonitorMainLoop()