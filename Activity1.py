import numpy as np
data_type = [('name','S15'),('class',int),('height',float)]
student_details = [('Shardul',12,186.12),('Sharali',7,161.5),('Sharol',6,154.5),('Siddhartha',6,144.5),('Shayna',7,160)]
students = np.array(student_details, dtype= data_type)
print("Orginal")
print(students)
print("Sort by height : ")
print(np.sort(students, order = "height"))
