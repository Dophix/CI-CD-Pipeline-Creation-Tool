import time

def create_logfile_name():
    secondsSinceEpoch = time.time()
    timeObj = time.localtime(secondsSinceEpoch)
    name = ('creation_log_%d-%d-%d_%d_%d_%d.txt' % (timeObj.tm_mday, timeObj.tm_mon, timeObj.tm_year,
                                                    timeObj.tm_hour, timeObj.tm_min, timeObj.tm_sec))
    return name