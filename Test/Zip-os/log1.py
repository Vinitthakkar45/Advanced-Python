# import logging

# # for handler in logging.root.handlers[:]:
# #     logging.root.removeHandler(handler)

# logging.basicConfig(filename='logging.log',encoding="utf-8", level=logging.DEBUG,format='%(asctime)s  - %(levelname)s - %(message)s', )
# # logging.basicConfig(filename='logging.log',encoding="utf-8", level=logging.DEBUG,format='%(asctime)s ',datefmt='%H  %p          %Y-%m-%d %H:%M:%S')

# # logging.debug('This message should go to the log file')
# # logging.info('So should this')
# # logging.warning('And this, too')
# # logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
# # logging.critical('fatal error')


# try :
#     a = 10/0
# except ZeroDivisionError:
#     logging.exception("Exception occurred")



import logging
# 1. Create a logger
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)
# 2. Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('example.log')
# 3. Set levels for handlers
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.ERROR)
# 4. Create formatters and set them for handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
# 5. Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
# 6. Logging messages
logger.debug('This is a debug message')
logger.error('This is an error message')
logger.log(logging.NOTSET, 'This is an error message')