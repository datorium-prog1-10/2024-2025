import json

# Load data from JSON file
with open('JSON/students.json', 'r', encoding="utf-8") as file:
    data = json.load(file)

# Calculate average age of students
Ages = [int(student['Age']) for student in data['Students']]
average_age = sum(Ages) / len(Ages) if Ages else 0

# Print the average age
print(f"The average age of students is: {average_age}")

# Calculate average SAT scores by state
sat_scores_by_state = {}
for student in data['Students']:
    country = student['Country']
    sat_score = int(student['SAT'])
    if country not in sat_scores_by_state:
        sat_scores_by_state[country] = []
    sat_scores_by_state[country].append(sat_score)

# Calculate and print average SAT scores
for state, scores in sat_scores_by_state.items():
    average_sat = sum(scores) / len(scores) if scores else 0
    print(f"The average SAT score in {state} is: {average_sat:.2f}")