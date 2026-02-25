# Student Grade Analyzer

# Step 1: Create data structures
student_records = []
stats = {}
print("=== GRADE ANALYZER ===\n")

# Step 2: Collect student data
for i in range(1, 7):
    # These lines must be indented to stay inside the loop
    name = input(f"Student {i} name: ")
    score = int(input(f"Student {i} score: "))
    student_records.append((name, score))
    print()

# Step 3: Extract scores and calculate statistics
scores = [score for name, score in student_records]
stats['highest'] = max(scores)
stats['lowest'] = min(scores)
stats['average'] = sum(scores) / len(scores)

# Step 4: Find unique scores
# Using a set automatically removes duplicates
unique_scores = set(scores)

# Step 5: Count grade distribution
grade_distribution = {}
for score in scores:
    # Indent the logic inside the loop
    grade_distribution[score] = grade_distribution.get(score, 0) + 1

# Step 6: Display results
print("\n" + "="*40)
print("=== STUDENT RECORDS ===")
print("="*40)
for i, (name, score) in enumerate(student_records, 1):
    # Indent to print each record
    print(f"{i}. {name}: {score}")

print("\n" + "="*40)
print("=== CLASS STATISTICS ===")
print("="*40)
print(f"Highest Score: {stats['highest']}")
print(f"Lowest Score: {stats['lowest']}")
print(f"Average Score: {stats['average']:.2f}")

print("\n" + "="*40)
print("=== UNIQUE SCORES ===")
print("="*40)
print(unique_scores)
print(f"Total unique scores: {len(unique_scores)}")

print("\n" + "="*40)
print("=== GRADE DISTRIBUTION ===")
print("="*40)
for score in sorted(grade_distribution.keys(), reverse=True):
    # Indent the distribution report logic
    count = grade_distribution[score]
    plural = "students" if count != 1 else "student"
    print(f"Score {score}: {count} {plural}")