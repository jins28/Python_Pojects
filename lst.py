students = [("Alice", {"Math", "Science", "English"}),
            ("Bob", {"math", "History", "Art"}),
            ("Charlie", {"science", "Art", "English"}),
            ]
diana_subjects = set(["Math", "Math", "Science", "Science"])
students.append(("Diana", diana_subjects))

names = sorted([name for name, subjects in students])
print("All students (sorted):", names)
