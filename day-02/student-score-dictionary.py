#Exercise: Student Score Dictionary
#Student: Animesh Acharya
#Day: 2
#Exercise: 6

student_scores = {
    "Anisha": 78,
    "Ravi": 55,
    "Maya": 92,
    "Sagar": 61,
    "Nima": 48
}

# 1. Print every student and score
for student, score in student_scores.items():
    print(f"{student}: {score}")

# 2. Dictionary comprehension - students who scored at least 60
passing_students = {
    student: score for student, score in student_scores.items() if score >= 60
}
print("Passing students (>=60):", passing_students)

# 3. Student with the highest score
top_student = max(student_scores, key=student_scores.get)
print(f"Top student: {top_student} with score {student_scores[top_student]}")

# 4. Average score
average_score = sum(student_scores.values()) / len(student_scores)
print("Average score:", round(average_score, 2))

print()