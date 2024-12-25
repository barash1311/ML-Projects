import logging
## basic logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler(),
    ]
)
logger=logging.getLogger("Arithematic app")

def add(a,b):
    result=a+b
    logger.debug(f"adding {a}+{b}",result)
    return result
def sub(a,b):
    result=a-b
    logger.debug(f"subract {a}-{b}",result)
    return result
def multiple(a,b):
    result=a*b
    logger.debug(f"adding {a}*{b}",result)
    return result
def div(a,b):
    try:
        result=a/b
        logger.debug(f"adding {a}/{b}",result)
        return result
    except ZeroDivisionError:
        logger.error("divide by zero")
        return None
    
add(2,3)
sub(15,10)
multiple(2,3)
div(4,10)