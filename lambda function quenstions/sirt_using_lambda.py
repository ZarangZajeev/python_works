subject_marks=[("English",88),("Science",90),("Maths",97),("Social science",82)]
print(f"Before sorting the list  {subject_marks}")
subject_marks.sort(key=lambda n:n[1])
print("\n Sorting the list of tuples: ")
print(subject_marks)