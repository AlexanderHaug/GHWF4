
def compute_hw_average(grades, numdrop):
    if len(grades) == 0:
        return 0
    for x in range(numdrop):
        grades.remove(min(grades))
    return sum(grades)/len(grades)
