import os,logging,time
def log():
    os.makedirs("loggings",exist_ok=True)
    
    logger=logging.getLogger("ApiInfo")
    handler=logging.FileHandler("loggings/log.log")
    formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger