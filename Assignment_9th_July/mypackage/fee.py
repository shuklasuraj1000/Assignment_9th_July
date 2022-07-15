import logging
logging.basicConfig(filename="fee1.log", level=logging.INFO)

def course_fee(course, category):

    logging.info("Course fee function initiated")

    """ This function will provide payable fee after discount as per your given details,
     To avail discount please enter your category EWS/HANDICAP/ALUMNI/NORMAL"""

    a = {"fullstack": 17700, "data analysis": 10000, "big data": 7800}
    b = {"EWS": 10, "HANDICAP": 15, "ALUMNI": 20, "NORMAL": 0, "ARMY": 35}
    c = str(course)
    d = str(category).upper()
    try:
        for i in a:
            if i == c:
                g = a[i]
                break
        for j in b:
            if j == d:
                f = b[j]
                break

        dis_fee = (g-(g*f/100))
        print("Selected program : {}.\nSelected category : {} ".format(c, d))
        if f != 0:
            print("Fee for {} program for others is {} INR.".format(c, g))
        else:
            pass

        print("Exclusive offer only for you, payable  : {} INR.".format(dis_fee))

    except Exception as e:
        logging.info(e)
        print("Please enter correct program and category details")
