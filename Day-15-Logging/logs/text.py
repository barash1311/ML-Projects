from logger import logging
def add(a,b):
    logging.debug("the addition function is taking place")
    return a+b
logging.debug("the addition function is called ")

add(2,3)