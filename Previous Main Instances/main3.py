symptoms_dict = {
    "headache": {
        "illnesses": ["migraine", "tension headache"],
        "cures": ["painkillers", "ice pack"],
        "remedies": ["drinking plenty of water", "getting enough sleep"]
    },
    "nausea": {
        "illnesses": ["gastroenteritis", "morning sickness"],
        "cures": ["antibiotics", "anti-nausea medication"],
        "remedies": ["drinking ginger tea", "eating small, frequent meals"]
    },
    "fatigue": {
        "illnesses": ["mononucleosis", "anemia"],
        "cures": ["rest", "iron supplements"],
        "remedies": ["exercising regularly", "eating a healthy diet"]
    },
    "chest pain": {
        "illnesses": ["angina", "heart attack"],
        "cures": ["aspirin", "emergency medical treatment"],
        "remedies": ["quitting smoking", "managing stress"]
    },
    "fever": {
        "illnesses": ["influenza", "malaria"],
        "cures": ["antiviral medication", "antimalarial medication"],
        "remedies": ["getting plenty of rest", "drinking fluids"]
    },
}


def chatbot():
    print("Welcome to the symptom checker chatbot!")
    print("Please tell me your symptoms.")

    user_symptoms = []
    while True:
        symptom = input()
        if symptom == "done":
            break
        user_symptoms.append(symptom)

    print("Thanks for your input. Based on your symptoms, the most likely illnesses are:")
    for symptom in user_symptoms:
        if symptom in symptoms_dict:
            illness_info = symptoms_dict[symptom]
            illnesses = illness_info["illnesses"]
            cures = illness_info["cures"]
            remedies = illness_info["remedies"]
            print("Illnesses:", ", ".join(illnesses))
            print("Cures:", ", ".join(cures))
            print("Remedies:", ", ".join(remedies))
        else:
            print("Sorry, I'm not sure what could be causing that symptom.")


chatbot()
