import logging
logging.basicConfig(filename="pol.log", level=logging.INFO)
class test1():

    def status(self):
        logging.info("test1 class status function initiated")
        try:
            print("You are intern, so test is not required")

        except Exception as e:
            logging.info(e)

class test2():

    def status(self):
        logging.info("test2 class status function initiated")
        try:
            print("You need to clear exam before appearing in interview")

        except Exception as e:
            logging.info(e)
