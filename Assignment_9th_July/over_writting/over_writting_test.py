from student_database_and_test.student_DB import ineuron

sameer = ineuron('sameer','data science','full stack', 30, 75, 75)  # Input feed
print(sameer.final_status())                   # "FAIL" or "PASS" result will be displayed.

print(" \n ## After over_writing result of final_status function ## \n ")
class over_writing(ineuron):

    def final_status():                                # Over_writing final_status function from ineuron class
        print("**** You are intern, so not required")

if __name__ == "__main__":
    over_writing.final_status()









