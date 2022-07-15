from iniheritance_folder.inheritance import job_class
alban = job_class('alban', 'data science', 'full stack', 30, 75, 75)
jerome = job_class('jerome', 'data science', 'full stack', 80, 75, 75)

alban.final_result()
print("\n")
alban.eligibility_check(alban)


jerome.final_result()
print("\n")
jerome.eligibility_check(jerome)


