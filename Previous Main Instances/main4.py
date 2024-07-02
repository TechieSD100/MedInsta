import re
import time
import speech_recognition as sr
# import pygame

# pygame.init()

voice_input = ["voice", "voice input", "v", "2nd", "2", "second", "2nd option",
               "second option", "audio", "audio input", "voice recording", "record"]

positive_responses = ["yes", "yash", "y", "yeah",
                      "yea", "ya", "yup", "haa", "ha", "hai", "got it", "i have"]

extra_positive_responses = [
    "i have", "got it", "i am having", "yes", "maybe i am having", "maybe i have"]

disease_dict = {
    "diarrhea": {
        "symptom_terms": ["1abdomen pain", "1abdominal pain", "1pain in my abdomen", "1abdomen is paining", "2stomach ache", "2stomach pain", "2stomach is paining", "2pain in my stomach", "3nausea", "3uncomfortable", "5vomit", "5vomitting", "6fever", "6feverish", "6feeling cold", "6having cold", "7bloody & watery loose stools", "7bloody stools", "7watery stools", "7watery loose stools", "7loose stools", "8dehydration", "8dehydrated", "8dehydrating"],
        "cures": ["• We recommend you to consult a doctor regarding medications & antibiotics."],
        "avoid": ["• Avoid milk-based & sweet foods.", "• Avoid caffeine & alcohol.", "• Do not eat solid food.", "• Avoid high sugar drinks and clear liquids."],
        "remedies": ["• Drink plenty of liquids.", "• Consider taking probiotics.", "• Add semisolid and low-fiber foods gradually."]
    },
    "allergies": {
        "symptom_terms": ["1eye irritation", "1irritation in my eyes", "1eyes are irritating", "1eyes are itching", "1itchy eyes", "2runny nose", "2nose is runny", "2nose is running", "3stuffy nose", "3nose is stuffy", "4puffy eyes", "4eye is puffy", "5watery eyes", "5eyes are watery", "6sneeze", "6sneezing", "6sneezy", "7inflamed nose", "7nose is inflammed", "8itchy nose", "8nose is itchy", "8itching in nose", "9inflamed throat", "9throat is inflammed", "9itchy throat", "9throat is itchy", "9itching in throat"],
        "cures": ["• Medication may be necessary to lessen symptoms caused by allergens:", " - Antihistamines", " - Decongestants", " - Anti-inflammatory agents: Corticosteroid", " - Allergy Shots", "However, please consume the above only as & if prescribed by a specialist doctor."],
        "avoid": ["• Avoid outside activities and heavy rain and exposure to pollen.", "• Avoid exposure to outside air through window.", "• Have a knowledge of what you are eating or drinking, so as to avoid the allergic consumption.", "• Review product lables carefullly before buying."],
        "remedies": ["• Honey sometimes reduces your allergic reaction.", "• To stay cool, use air conditioners and dehumidifiers.", "• Consume Vitamin C foods like Oranges, Guavas, Broccoli, etc."]
    },
    "cold and flu": {
        "symptom_terms": ["1fever", "1feverish", "2headache", "2head pain", "2pain in my head", "2head is paining", "3pain and fatigue", "3severe pain", "3fatigue", "cough", "4dry cough", "5sinus", "6ear infections", "6infections in my ear", "7sore throat", "7throat is sore", "7throat sore", "8runny nose", "8nose is runny", "8nose is running", "8running nose", "9stuffy nose", "9nose is stuffy", "10sneeze", "10sneezing", "10sneezy", "11cough", "11coughing"],
        "cures": ["• Use salt water nasal sprays.", "• You could take the below medications as and if prescribed by a doctor:", " - Decongestants (e.g. pseudoephedrine)", " - Dextromethorphan, an effective cough suppressant", " - Acetaminophen, Aspirin & Ibuprofen"],
        "avoid": ["• Avoid exercise until symptoms are gone.", "• Avoid cigarette smoke.", "• Do not take antibiotics unless specifically prescribed.", "• Avoid drinking alcohol.", "• Avoid caffeine products like coffee, fizzy drinks, etc."],
        "remedies": ["• Rest more than usual.", "• Drink lots of clear fluids.", "• Eat a well-balanced diet including fruits vegetables and grains.", "• Stay hydrated.", "• Take humidifiers and hot showers.", "• Use Phenol for surroundings.", "• Gargling with warm saltwater (1 tsp. salt in one cup of warm water) every four hours.", "• Drink tea with lemon."]
    },
    "conjunctivitis (“pink eye“)": {
        "symptom_terms": ["1redness in eyes", "1red eye", "1red eyes", "1redness in eye", "1eye is red", "1eyes are red", "2eyes are itching", "2itching in my eyes", "2itchy eyes", "2eye is itching", "3teary eyes", "3eye tearing", "4burning eye sensation", "4eyes are burning", "4eye burn", "4burning sensation in my eyes", "5discharge of pus", "5pus like discharge", "pus discharge", "6crusting of eyelids", "6eyelids are crusting", "6eyelids crusting", "7unclear vision", "7no clear vision"],
        "cures": ["• Viral conjunctivitis clears up on its own", "• Consult a doctor for prescribing antibiotic eye drops for cure."],
        "avoid": ["• Avoid rubbing your eyes.", "• Avoid using make-up on or near eyes.", "• Avoid using unclean and unwashed objects near eyes.", "• Avoid wearing contact lenses.", "• Avoid touching the drop bottle's tip to the eyes."],
        "remedies": ["• Wash your hands frequently.", "• Use a cool wet washcloth to soak off any crusting.", "• Use a warm or cool compress to reduce discomfort.", "• Give as much rest possible to your eyes."]
    },
    "Hypertension": {
        "symptom_terms": ["1headache", "1headaches", "1pain in my head", "2increased blood pressure", "2increased b p", "2increased bp", "2high bp", "2high b p", "2high blood pressure", "3breathing problem", "3problems in breathing", "3breathing issues", "4sweating", "4sweat", "5bleeding nose", "5nose is bleeding", "6 tiredness", "6tired", "7edema", "7swelling", "8irregular heartbeats", "8irregular heart beats", "9chest pain", "10trouble in sleeping"],
        "cures": ["• We recommend you to consult a doctor regarding medications."],
        "avoid": ["• Avoid foods high in saturated fats, such as fatty meats and palm oil.", "• Avoid alcohol.", "• Avoid sugary foods, such as maple syrup, candy, and jelly.", "• Avoid high sugar drinks and clear liquids."],
        "remedies": ["• Drink plenty of liquids.", "• Eat fruits: such as apples, bananas, and strawberries.", "• Eat vegetables, such as broccoli, green beans, and carrots.", "• Perform physical exercises.", "• Avoid smoking."]
    },
    "Diabetes": {
        "symptom_terms": ["1thirst", "1thirsty", "2urinating", "2urination", "2toilet", "2continues urination", "2excessive urination", "2frequent urination", "3losing weight", "3weight loss", "3loss in weight", "4blurry vision", "4blurred vision", "4vision is blurry", "5slow healing", "5slow wound healing ", "5wound healing is slow", "5not healing fast", "6tiredness", "6tired", "6dizziness", "6dizzy", "6weakness", "6weak", "6week", "7tingling in foot", "7tingling foot", "7foot tingling", "7pricking foot", "7pricking in foot", "7foot pricking"],
        "cures": ["• No particular cure but we recommend you to consult a doctor immediately regarding medications."],
        "avoid": ["• Less intake of glucose.", "• Avoid carbohydrates such as rice, high fat meat (fatty cuts of pork, beef, and lamb, poultry skin, dark meat chicken).", "• Avoid high sugar drinks and sugar bevarages, sweets (candy, cookies, baked goods, ice cream, desserts), processed foods (chips, microwave popcorn, processed meat, convenience meals)."],
        "remedies": ["• Consume fruits (apples | oranges | berries | melons | pears | peaches).", " Vegetables (like broccoli | cauliflower | spinach | cucumbers | zucchini.", "  Beverages like (water | black coffee | unsweetened tea | vegetable juice."]}
}


def speech2text():
    r = sr.Recognizer()
    # Set the microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        # Listen to the microphone and store the audio data
        audio_data = r.listen(source)

    # Convert the audio data to text
    text = r.recognize_google(audio_data, language='en-IN')
    print(f"You: {text}")
    return text


def remove_special_characters(string):
    removed = re.sub(r'[^\w\s]', '', string)
    return removed


def typing_animation(line):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(0.04)  # Delay for 0.04 seconds
    print()  # Move to a new line


def initial_convo():
    print()
    print("Bot:", end=' ')
    typing_animation("Welcome to VirtuoHealth!")


def extract_disease(combined):
    stop_char = ","
    stop_index = combined.index(stop_char)
    sub_string = combined[:stop_index]
    return sub_string


def present_in_string(list, sent):
    count = 0
    present_symp = ""
    s = ",".join(map(str, list))
    symps = s.split(",")
    for symp in symps:
        if symp in sent:
            count += 1
            present_symp = symp[1:] + "," + present_symp
    if present_symp != "":
        present_symp = present_symp + str(count)
        return present_symp
    else:
        return ""


def illness_working_main(sentence):
    possibilities = []
    for d_id, d_info in disease_dict.items():
        assumption = ""
        for key in d_info:
            if key == "symptom_terms":
                if (present_in_string(d_info[key], sentence)) != "":
                    assumption = d_id + "," + \
                        present_in_string(d_info[key], sentence)
        possibilities.append(assumption)
    if all(elem == '' for elem in possibilities):
        typing_animation(
            "Sorry, we failed to understand you, or we still aren't aware of what exactly you are facing!")
        raise SystemExit
    max = 0
    for i in range(len(possibilities)):
        if possibilities[i] != '':
            if int(possibilities[i][-1]) > max:
                max = int(possibilities[i][-1])
                possible_disease = extract_disease(possibilities[i])
                index = i
    mentioned = possibilities[index].split(',')
    mentioned_id = []
    for i in range(1, (len(mentioned)-1), 1):
        mentioned_id.append(mentioned[i][0])
    reply = "You might be having " + possible_disease + "."
    print("Bot:", end=' ')
    typing_animation(reply)
    print()
    print("Bot:", end=' ')
    typing_animation(
        "Please answer the following questions, and help us understand the illness better:")
    print("    ", end=' ')
    typing_animation(
        "Are you facing any of the following? (Answer with y or n for the following.)")
    c = 0
    answered_ids = []
    for d_id, d_info in disease_dict.items():
        if d_id == possible_disease:
            for key in d_info:
                if key == "symptom_terms":
                    temp = ",".join(map(str, d_info[key]))
                    parts = temp.split(',')
                    for p in parts:
                        if (p[0] not in mentioned_id) and (p[0] not in answered_ids):
                            print("    ", end=' ')
                            if input_format in voice_input:
                                print(f"• {p[1:]}? ")
                                response = speech2text()
                            else:
                                response = input(f"• {p[1:]}? ").lower()
                            if (response in positive_responses) or present(extra_positive_responses, response):
                                c = c + 1
                            answered_ids.append(p[0])
    print()
    print("Bot:", end=' ')
    if c != 0:
        print(f"You have {c} more symptoms of {possible_disease}.")
    else:
        print(
            f"You don't show any other symptoms of {possible_disease}, but we suspect it to be {possible_disease} itself.")
    print()
    print("Bot:", end=' ')
    avoidance(possible_disease)
    print()
    print("Bot:", end=' ')
    remedy(possible_disease)
    print()
    print("Bot:", end=' ')
    cure(possible_disease)


def avoidance(dis1):
    typing_animation("We'll suggest you to avoid the following:")
    for d_id, d_info in disease_dict.items():
        if d_id == dis1:
            for key in d_info:
                if key == "avoid":
                    temp1 = ",".join(map(str, d_info[key]))
                    avoid_instructions = temp1.split(',')
                    for phrases in avoid_instructions:
                        print("    ", end=' ')
                        typing_animation(phrases)


def remedy(dis2):
    typing_animation(
        "We'll also suggest you to consider the following remedies:")
    for d_id, d_info in disease_dict.items():
        if d_id == dis2:
            for key in d_info:
                if key == "remedies":
                    temp1 = ",".join(map(str, d_info[key]))
                    avoid_instructions = temp1.split(',')
                    for phrases in avoid_instructions:
                        print("    ", end=' ')
                        typing_animation(phrases)


def cure(dis3):
    typing_animation(
        "Also check if you could undergo the following treatments:")
    for d_id, d_info in disease_dict.items():
        if d_id == dis3:
            for key in d_info:
                if key == "cures":
                    temp1 = ",".join(map(str, d_info[key]))
                    avoid_instructions = temp1.split(',')
                    for phrases in avoid_instructions:
                        print("    ", end=' ')
                        typing_animation(phrases)


def present_in_string(list, sent):
    count = 0
    present_symp = ""
    s = ",".join(map(str, list))
    symps = s.split(",")
    for symp in symps:
        if symp[1:] in sent:
            count += 1
            present_symp = symp + "," + present_symp
    if present_symp != "":
        present_symp = present_symp + str(count)
        return present_symp
    else:
        return ""


def present(list1, sentence):
    for items in list1:
        if items in sentence:
            return True
    return False


def chatbot():
    print()
    print("Bot:", end=' ')
    typing_animation("Please brief me about your unusualness.")
    print("You:", end=' ')
    if input_format in voice_input:
        symptom_words = speech2text()
    else:
        symptom_words = input().lower()
    symptom_words = remove_special_characters(symptom_words)
    symptom_split = symptom_words.split(' ')
    illness_working_main(symptom_words)


initial_convo()
print("    ", end=' ')
typing_animation("How do you want to proceed?")
print("    ", end=' ')
typing_animation("• Text Input\t• Voice Input")
print("You:", end=' ')
input_format = input().lower().strip()
chatbot()
