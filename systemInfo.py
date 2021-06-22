import platform, os, re, psutil, time, subprocess


def getBasicSystemInfo():
    if platform.system() == 'Linux':
        command = 'cat /proc/cpuinfo' 
        systemCPUallInfo = os.popen(command).read().strip() 
        for line in systemCPUallInfo.split("\n"):
            if "model name" in line:
                systemCPU = re.sub(".*model name.*:", "", line, 1)
            else:
                systemCPU = 'unknown'
            if "cpu cores" in line:
                systemCPUcores = re.sub(".*cpu cores.*:", "", line, 1)
                break
            else:
                systemCPUcores = str(psutil.cpu_count(logical=False))
            if "siblings" in line:
                systemCPUthreads = re.sub(".*siblings.*:", "", line, 1)
            else:
                systemCPUthreads = str(psutil.cpu_count())
        command = 'cat /etc/os-release'
        systemNameAll = os.popen(command).read().strip()
        for line in systemNameAll.split("\n"):
            if "PRETTY_NAME" in line:
                systemName = re.sub(".*PRETTY_NAME.*=", "", line, 1)

        systemArt = (r"""
       .--.
      |o_o |     System:  {systemName}
      |:_/ |     CPU: {systemCPU}
     //   \ \    Cores/Threads: {coresThreadInfo}
    (|     | )   RAM: {systemRAM}
   /'|_   _/'\   UPTIME: {systemUPTIME}
   \___)=(___/
    """).format(systemName = f"{platform.system()} - {systemName} {platform.machine()}",
                systemCPU = f"{systemCPU.strip()} ({psutil.cpu_freq().max / 1000}GHz)",
                coresThreadInfo = f"{systemCPUcores.strip()}/{systemCPUthreads.strip()}",
                systemRAM = f"{round(psutil.virtual_memory().total / 1000000)}MB",
                systemUPTIME = f"{round((time.time() - psutil.boot_time()) / 60 / 60, 1)} hours")

    elif platform.system() == 'Windows':
        systemCPU = subprocess.check_output(["wmic","cpu","get", "name"]).decode('utf-8')
        systemCPU = systemCPU.replace('Name', '')
        systemCPU = systemCPU.strip()
        systemCPUcores = str(psutil.cpu_count(logical=False))
        systemCPUthreads = str(psutil.cpu_count())
        systemArt = (r"""
           _.-;;-._     System: {systemName}
    '-..-'|   ||   |    CPU: {systemCPU}
    '-..-'|_.-;;-._|    Cores/Threads: {coresThreadInfo}
    '-..-'|   ||   |    RAM: {systemRAM}
    '-..-'|_.-''-._|    UPTIME: {systemUPTIME}
        """).format(systemName = f"{platform.uname().system} {platform.uname().release} ({platform.uname().version})",
                    systemCPU = systemCPU,
                    coresThreadInfo = f"{systemCPUcores}/{systemCPUthreads}",
                    systemRAM = f"{round(psutil.virtual_memory().total / 1000000)}MB",
                    systemUPTIME = f"{round((time.time() - psutil.boot_time()) / 60 / 60, 1)} hours")

    return systemArt