from abstraction.abs import course_fee1

a = course_fee1("Fullstack","EWS")
# Here we are getting fee after discount, and we don't bother from where and how this value is coming.
print("Fee after all discount : ", a)
# 18% GST is applicable on fee.

payable = a + (a*.18)
print("Total fee including 18% GST : ", payable)