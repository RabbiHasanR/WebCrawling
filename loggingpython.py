import logging

# logging.basicConfig(filename='test.log', filemode='w',level=logging.DEBUG) #save log message in file
logging.basicConfig(format='%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p') #print log message with time and date
logging.debug('This is debug log')
logging.info('this is info log')
logging.warning('This is warning log')
logging.error('This is error log')
logging.critical('This is critical log')