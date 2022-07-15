import logging
logging.basicConfig(filename="abs1.log", level=logging.INFO)
def course_fee1(course, category):
    logging.info("Course fee1 function initiated")
    """ This function will provide payable fee after discount as per your given details,
     To avail discount please enter your category EWS/HANDICAP/ALUMNI/NORMAL"""

    a = {"fullstack": 17700, "data analysis": 10000, "big data": 7800}
    b = {"EWS": 10, "HANDICAP": 15, "ALUMNI": 20, "NORMAL": 0, "ARMY": 35}
    c = str(course).lower()
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

        dis_fee1 = (g-(g*f/100))
        return dis_fee1

    except Exception as e:
        logging.info(e)
        print("Choose a and b value from here >> "
              "a : fullstack/data analysis/big data, b : EWS/HANDICAP/ALUMNI/NORMAL/ARMY")
