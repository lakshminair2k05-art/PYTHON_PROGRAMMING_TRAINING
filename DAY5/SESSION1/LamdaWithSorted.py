
students=[("bheem",5),("chutki",4),("theresa mosi",50),("kirvada",6)]
sorted_students=sorted(
    students,
    key=lambda x:x[1]
)
print(sorted_students)