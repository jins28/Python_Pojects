math_students = {"Alice", "Bob", "Charlie"}
science_students = {"Bob", "Diana", "Eve"}
both = math_students.intersection(science_students)
uni = math_students.union(science_students)
# Task H: Find students taking math but NOT science (difference)
onl_math = math_students - science_students
print(both)
print(uni)
print(onl_math)
