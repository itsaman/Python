import logging

# configure logging 
logging.basicConfig(level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s ')

#if we want to capture all the log messages into a file then
#logging.basicConfig(filename = 'demo.log',level = logging.DEBUG, filemode = 'w')

#to disable logging
#logging.disable()

def namecheck(name):
    logging.info(f'we will going to check the length of {name} and let you know if its correct or not')
    if len(name)<2:
        logging.debug('checking for the name length...')
        return 'Invalid Name'
    elif name.isspace():
        logging.debug('checking if the name has space...')
        return 'Invalid Name'
    elif name.isalpha():
        logging.debug('checking if the name is Alphabet...')
        return 'Name is Valid'
    else:
        logging.debug('Failled all checks...')
        return 'Invalid Name'


####################### To Change the root name ###########################

#root is a default logger we can specify our own as well
#to reate or own logger

logger = logging.getLogger('__name__')
#why we are using __name__ because if we are going to use this logger program in another program by using import than the logger get the name as file name 
#After defing the logger we need to set it so:
logger.setLevel(logging.DEBUG)

#to format this
f = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

#for file handler
fh = logging.FileHandler('savetofile.log')
fh.setFormatter(f)

#to set this file hadler to logger
logger.addHandler(fh)

#now
def namecheck2(name):
    logger.info(f'we will going to check the length of {name} and let you know if its correct or not')
    if len(name)<2:
        logger.debug('checking for the name length...')
        return 'Invalid Name'
    elif name.isspace():
        logger.debug('checking if the name has space...')
        return 'Invalid Name'
    elif name.isalpha():
        logger.debug('checking if the name is Alphabet...')
        return 'Name is Valid'
        
    else:
        logger.debug('Failled all checks...')
        return 'Invalid Name'

print(namecheck2('Qwerty'))
