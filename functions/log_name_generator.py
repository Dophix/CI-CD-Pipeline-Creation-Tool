import time

def create_logfile_name(filename: str):
    secondsSinceEpoch = time.time()
    timeObj = time.localtime(secondsSinceEpoch)
    name = (filename + '_%d-%d-%d_%d_%d_%d.txt' % (timeObj.tm_year, timeObj.tm_mon, timeObj.tm_mday,
                                                    timeObj.tm_hour, timeObj.tm_min, timeObj.tm_sec))
    return name