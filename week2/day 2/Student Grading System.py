def student_grading_system(score, attendance, assignment_score):
    if score >= 70:
        print("Excellent, Grade: A")
    elif score >= 60:
        print("Very Good, Grade: B")
    elif score >= 50:
        print("Good, Grade: C")
    elif score >= 40:
        print("Fair, Grade: D")
    elif score >= 30:
        print("Poor, Grade: E") 
    else:
        print("Fail, Grade: F")

student_grading_system(25, 90, 80)