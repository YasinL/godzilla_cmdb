import logging
import datetime
import  os

module_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
logfile = "/logs/py_cmdb.log"
logfilename = module_path + logfile


if logfilename is False:
    file = open(logfilename,'w+')
    file.close()
else:
    pass

logging.basicConfig(filename=logfilename, level=logging.DEBUG, format='[%(asctime)s %(levelname)s %(process)d %(filename)s %(lineno)d] - %(message)s')
logger = logging.getLogger()   #日志


if __name__ == '__main__':
    logger.info(logfilename)
    print(logfilename)