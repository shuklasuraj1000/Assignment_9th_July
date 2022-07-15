import logging
logging.basicConfig(filename="inheritance.log", level=logging.INFO, format='%(asctime)s, %(massage)s')

from student_database_and_test.student_DB import ineuron

class job_class (ineuron):

    def eligibility_check(self,student):

        #logging.info("Eligibility_check function initiated")

        self.student = student

        try:
            a = str(self.student.final_status())
            if a == "PASS":
                print("Congratulations!! you are eligible to apply for job")
            else:
                print(" Sorry!! you are not eligible to apply for job. \n "
                "Since you have failed in examination, please try next time")

        except Exception as e:
            print(e)
            #logging.info(e)

