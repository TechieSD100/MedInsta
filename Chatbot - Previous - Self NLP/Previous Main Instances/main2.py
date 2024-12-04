# Define a list of common symptoms
symptoms = ["cough", "fever", "fatigue", "body aches"]

# Define a dictionary of possible conditions for each symptom
conditions = {
    "cough": ["cold", "flu", "pneumonia"],
    "fever": ["cold", "flu", "pneumonia", "typhoid"],
    "fatigue": ["anaemia", "chronic fatigue syndrome"],
    "body aches": ["cold", "flu", "pneumonia"]
}

# Create a function to ask the user about their symptoms


def ask_symptoms():
    user_symptoms = []
    # Iterate through the list of symptoms and ask the user if they are experiencing each one
    for symptom in symptoms:
        response = input(f"Are you experiencing {symptom}? (y/n)")
        if response.lower() == "y":
            user_symptoms.append(symptom)
    return user_symptoms

# Create a function to check for possible conditions based on the user's symptoms


def check_conditions(symptoms):
    possible_conditions = []
    # Check the dictionary for each of the user's symptoms
    for symptom in symptoms:
        if symptom in conditions:
            # If the symptom is found, add the possible conditions to the list
            possible_conditions += conditions[symptom]
    return possible_conditions


# Ask the user about their symptoms
user_symptoms = ask_symptoms()

# Check for possible conditions based on the user's symptoms
possible_conditions = check_conditions(user_symptoms)

# Print the possible conditions
print("Based on your symptoms, you may have one of the following conditions:")
print(", ".join(possible_conditions))
