grades = {
    "Ann": [7, 10, 12],
    "Bob": [12, 5, 11],
    "Kate": [8, 10, 10],
    "Max": [4, 12, 6],
}
result = [(name, grade)
          for name, scores in grades.items()
          for grade in scores
          if grade >= 10]

print(result)