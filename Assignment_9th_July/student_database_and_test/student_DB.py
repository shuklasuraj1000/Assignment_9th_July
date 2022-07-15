import logging
logging.basicConfig(filename="SDB.log", level=logging.INFO)

class ineuron:
    def __init__(self, student_name, class_name, class_type, marks_python, marks_SQL, mark_ML ):
        self.__student = student_name                    # Private variable
        self.class_name = class_name                     # Public  variable
        self.class_type = class_type                     # Public  variable
        self._marks_python = marks_python                # Protected variable
        self._marks_SQL = marks_SQL                      # Protected variable
        self._mark_ML = mark_ML                          # Protected variable


    def final_result(self):
        logging.info("final result function initiated")
        """ This function will show status of final result of student"""
        a1 = self._marks_python
        a2 = self._marks_SQL
        a3 = self._mark_ML
        A = a1+a2+a3

        try:
            l = [["Subject", "Max marks", "Scored marks"],
                 ["Python", 100, a1],
                 ["SQL", 100, a2],
                 ["ML", 100, a3],
                 ["Total", 100, A]
                 ]
            if a1 >= 40 and a2 >= 40 and a3 >= 40 and A >= 120:
                for i in l:
                    for j in i:
                        print(j, end=(" "*5))
                    print("\n")

                print("{} cleared examination ".format(self.__student))


            else:
                for i in l:
                    for j in i:
                        print(j, end=(" "*5))
                    print("\n")
                print("{} failed in examination ".format(self.__student))


        except Exception as e:
            logging.info(e)

    def final_status(self):
        logging.info("final status function initiated")
        """ This function will show final status for student"""
        a1 = self._marks_python
        a2 = self._marks_SQL
        a3 = self._mark_ML
        A = a1+a2+a3

        try:

            if a1 >= 40 and a2 >= 40 and a3 >= 40 and A >= 120:

                return "PASS"

            else:
                 return "FAIL"

        except Exception as e:
            logging.info(e)

