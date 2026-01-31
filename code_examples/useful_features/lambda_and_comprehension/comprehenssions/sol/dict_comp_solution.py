result = {
    name: [grade for grade in scores if grade >= 10]
    for name, scores in grades.items()
}