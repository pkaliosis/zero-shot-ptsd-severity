templates={
    "ptsd_w-reasoning_w-subscales_wo-questions":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing: Intrusive thoughts, flashbacks, nightmares, or distress when reminded of the trauma.
Avoidance: Efforts to avoid thoughts, feelings, or external reminders associated with the trauma.
Dysphoria: Persistent negative thoughts, feelings of guilt, emotional numbness, or loss of interest in activities.
Hyperarousal: Increased irritability, hypervigilance, being easily startled, or difficulty concentrating and sleeping.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide an explanation on how each symptom was identified. Provide a score between 0 and 4 for each subfactor.
STEP 2: Present the results as a nested JSON, providing both the severity score and a clear explanation for each subfactor. Ensure that each explanation references relevant text spans or contextual inferences to justify the assigned score.

To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Reason: A list containing the rationale for the assigned severity score, based on evidence explicitly or implicitly found in the transcription. This could be a direct quote, paraphrased text, or a context-based inference.
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON, with elements inside angle brackets being placeholders for the actual values:
 {{
    "Re-experiencing": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Avoidance": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",
    
    "ptsd_w-reasoning_wo-subscales_wo-questions": """Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing, Avoidance, Dysphoria, Hyperarousal.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide an explanation on how each symptom was identified. Provide a score between 0 and 4 for each subfactor.
STEP 2: Present the results as a nested JSON, providing both the severity score and a clear explanation for each subfactor. Ensure that each explanation references relevant text spans or contextual inferences to justify the assigned score.

To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Reason: A list containing the rationale for the assigned severity score, based on evidence explicitly or implicitly found in the transcription. This could be a direct quote, paraphrased text, or a context-based inference.
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON, with elements inside angle brackets being placeholders for the actual values:
 {{
    "Re-experiencing": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Avoidance": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_wo-reasoning_w-subscales_wo-questions":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing: Intrusive thoughts, flashbacks, nightmares, or distress when reminded of the trauma.
Avoidance: Efforts to avoid thoughts, feelings, or external reminders associated with the trauma.
Dysphoria: Persistent negative thoughts, feelings of guilt, emotional numbness, or loss of interest in activities.
Hyperarousal: Increased irritability, hypervigilance, being easily startled, or difficulty concentrating and sleeping.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide a score between 0 and 4 for each subfactor.

To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON:
 {{
    "Re-experiencing": {{
      "Severity Score": 
    }},
    "Avoidance": {{
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_w-reasoning_w-subscales_w-questions_phase-1":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. How are you? Can you elaborate?
2. How's the family? Can you elaborate?
3. What's new? Can you elaborate?
4. What else?
5. Over the past 5 years what are the three nicest things that happened to you and your family? Can you elaborate?
6. Over the past 5 years what are the three worst things that happened to you and your family? Can you elaborate?
7. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?

Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing: Intrusive thoughts, flashbacks, nightmares, or distress when reminded of the trauma.
Avoidance: Efforts to avoid thoughts, feelings, or external reminders associated with the trauma.
Dysphoria: Persistent negative thoughts, feelings of guilt, emotional numbness, or loss of interest in activities.
Hyperarousal: Increased irritability, hypervigilance, being easily startled, or difficulty concentrating and sleeping.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide an explanation on how each symptom was identified. Provide a score between 0 and 4 for each subfactor.
STEP 2: Present the results as a nested JSON, providing both the severity score and a clear explanation for each subfactor. Ensure that each explanation references relevant text spans or contextual inferences to justify the assigned score.

To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Reason: A list containing the rationale for the assigned severity score, based on evidence explicitly or implicitly found in the transcription. This could be a direct quote, paraphrased text, or a context-based inference.
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON, with elements inside angle brackets being placeholders for the actual values:
 {{
    "Re-experiencing": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Avoidance": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_w-reasoning_w-subscales_w-questions_phase-2":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. What are the three things in your life that you look forward to the most right now? Can you elaborate?
2. What are the three biggest challenges that you are managing in your life right now? Can you elaborate?
3. Where are three places that you turn to find support right now and why? Can you elaborate?
4. Over the past 5 years, what are the three nicest things that happened to you and your family? Can you elaborate?
5. Over the past 5 years, what are the worst three things that have happened to you and your family? Can you elaborate?
6. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?
7. What are three reflections that you have on this research experience? Were any parts particularly challenging or interesting? Do you have any recommendations for us continuing this research?

Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing: Intrusive thoughts, flashbacks, nightmares, or distress when reminded of the trauma.
Avoidance: Efforts to avoid thoughts, feelings, or external reminders associated with the trauma.
Dysphoria: Persistent negative thoughts, feelings of guilt, emotional numbness, or loss of interest in activities.
Hyperarousal: Increased irritability, hypervigilance, being easily startled, or difficulty concentrating and sleeping.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide an explanation on how each symptom was identified. Provide a score between 0 and 4 for each subfactor.
STEP 2: Present the results as a nested JSON, providing both the severity score and a clear explanation for each subfactor. Ensure that each explanation references relevant text spans or contextual inferences to justify the assigned score.

To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Reason: A list containing the rationale for the assigned severity score, based on evidence explicitly or implicitly found in the transcription. This could be a direct quote, paraphrased text, or a context-based inference.
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON, with elements inside angle brackets being placeholders for the actual values:
 {{
    "Re-experiencing": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Avoidance": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_w-reasoning_w-subscales_w-questions_phase-3":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. What are the three things in your life that you look forward to the most right now? Can you elaborate?
2. What are the three biggest challenges that you are managing in your life right now? Can you elaborate?
3. Where are three places that you turn to find support right now and why? Can you elaborate?
4. Over the past 5 years, what are the three nicest things that happened to you and your family? Can you elaborate?
5. Over the past 5 years, what are the worst three things that have happened to you and your family? Can you elaborate?
6. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?
7. How has the COVID-19 pandemic changed your life? Can you elaborate?
8. What was most difficult for you about the COVID-19 pandemic? Can you elaborate?
9. What do you most look forward to doing after the COVID-19 pandemic is over? Can you elaborate?
10. Looking back at the last two decades, what effect did 9/11 have on your life? Can you elaborate?
11. How does 9/11 affect you now? Can you elaborate?
12. What would you like future generations to know about 9/11? Can you elaborate?
13. What are three reflections that you have on this research experience?
14. Were any parts particularly challenging or interesting?
15. Do you have any recommendations for us continuing this research?

Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing: Intrusive thoughts, flashbacks, nightmares, or distress when reminded of the trauma.
Avoidance: Efforts to avoid thoughts, feelings, or external reminders associated with the trauma.
Dysphoria: Persistent negative thoughts, feelings of guilt, emotional numbness, or loss of interest in activities.
Hyperarousal: Increased irritability, hypervigilance, being easily startled, or difficulty concentrating and sleeping.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide an explanation on how each symptom was identified. Provide a score between 0 and 4 for each subfactor.
STEP 2: Present the results as a nested JSON, providing both the severity score and a clear explanation for each subfactor. Ensure that each explanation references relevant text spans or contextual inferences to justify the assigned score.

To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Reason: A list containing the rationale for the assigned severity score, based on evidence explicitly or implicitly found in the transcription. This could be a direct quote, paraphrased text, or a context-based inference.
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON, with elements inside angle brackets being placeholders for the actual values:
 {{
    "Re-experiencing": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Avoidance": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_wo-reasoning_w-subscales_w-questions_phase-1":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. How are you? Can you elaborate?
2. How's the family? Can you elaborate?
3. What's new? Can you elaborate?
4. What else?
5. Over the past 5 years what are the three nicest things that happened to you and your family? Can you elaborate?
6. Over the past 5 years what are the three worst things that happened to you and your family? Can you elaborate?
7. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?

Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing: Intrusive thoughts, flashbacks, nightmares, or distress when reminded of the trauma.
Avoidance: Efforts to avoid thoughts, feelings, or external reminders associated with the trauma.
Dysphoria: Persistent negative thoughts, feelings of guilt, emotional numbness, or loss of interest in activities.
Hyperarousal: Increased irritability, hypervigilance, being easily startled, or difficulty concentrating and sleeping.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide a score between 0 and 4 for each subfactor.
STEP 2: Present the results as a nested JSON, providing both the severity score and a clear explanation for each subfactor. Ensure that each explanation references relevant text spans or contextual inferences to justify the assigned score.

To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON, with elements inside angle brackets being placeholders for the actual values:
 {{
    "Re-experiencing": {{
      "Severity Score": 
    }},
    "Avoidance": {{
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_wo-reasoning_w-subscales_w-questions_phase-2":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. What are the three things in your life that you look forward to the most right now? Can you elaborate?
2. What are the three biggest challenges that you are managing in your life right now? Can you elaborate?
3. Where are three places that you turn to find support right now and why? Can you elaborate?
4. Over the past 5 years, what are the three nicest things that happened to you and your family? Can you elaborate?
5. Over the past 5 years, what are the worst three things that have happened to you and your family? Can you elaborate?
6. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?
7. What are three reflections that you have on this research experience? Were any parts particularly challenging or interesting? Do you have any recommendations for us continuing this research?

Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing: Intrusive thoughts, flashbacks, nightmares, or distress when reminded of the trauma.
Avoidance: Efforts to avoid thoughts, feelings, or external reminders associated with the trauma.
Dysphoria: Persistent negative thoughts, feelings of guilt, emotional numbness, or loss of interest in activities.
Hyperarousal: Increased irritability, hypervigilance, being easily startled, or difficulty concentrating and sleeping.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide a score between 0 and 4 for each subfactor.
STEP 2: Present the results as a nested JSON, providing both the severity score and a clear explanation for each subfactor. Ensure that each explanation references relevant text spans or contextual inferences to justify the assigned score.

To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON, with elements inside angle brackets being placeholders for the actual values:
 {{
    "Re-experiencing": {{
      "Severity Score": 
    }},
    "Avoidance": {{
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_wo-reasoning_w-subscales_w-questions_phase-3":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. What are the three things in your life that you look forward to the most right now? Can you elaborate?
2. What are the three biggest challenges that you are managing in your life right now? Can you elaborate?
3. Where are three places that you turn to find support right now and why? Can you elaborate?
4. Over the past 5 years, what are the three nicest things that happened to you and your family? Can you elaborate?
5. Over the past 5 years, what are the worst three things that have happened to you and your family? Can you elaborate?
6. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?
7. How has the COVID-19 pandemic changed your life? Can you elaborate?
8. What was most difficult for you about the COVID-19 pandemic? Can you elaborate?
9. What do you most look forward to doing after the COVID-19 pandemic is over? Can you elaborate?
10. Looking back at the last two decades, what effect did 9/11 have on your life? Can you elaborate?
11. How does 9/11 affect you now? Can you elaborate?
12. What would you like future generations to know about 9/11? Can you elaborate?
13. What are three reflections that you have on this research experience?
14. Were any parts particularly challenging or interesting?
15. Do you have any recommendations for us continuing this research?

Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing: Intrusive thoughts, flashbacks, nightmares, or distress when reminded of the trauma.
Avoidance: Efforts to avoid thoughts, feelings, or external reminders associated with the trauma.
Dysphoria: Persistent negative thoughts, feelings of guilt, emotional numbness, or loss of interest in activities.
Hyperarousal: Increased irritability, hypervigilance, being easily startled, or difficulty concentrating and sleeping.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide a score between 0 and 4 for each subfactor.
STEP 2: Present the results as a nested JSON, providing both the severity score and a clear explanation for each subfactor. Ensure that each explanation references relevant text spans or contextual inferences to justify the assigned score.

To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON, with elements inside angle brackets being placeholders for the actual values:
 {{
    "Re-experiencing": {{
      "Severity Score": 
    }},
    "Avoidance": {{
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_w-reasoning_wo-subscales_w-questions_phase-1":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. How are you? Can you elaborate?
2. How's the family? Can you elaborate?
3. What's new? Can you elaborate?
4. What else?
5. Over the past 5 years what are the three nicest things that happened to you and your family? Can you elaborate?
6. Over the past 5 years what are the three worst things that happened to you and your family? Can you elaborate?
7. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?

Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing, Avoidance, Dysphoria, Hyperarousal.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide an explanation on how each symptom was identified. Provide a score between 0 and 4 for each subfactor.
STEP 2: Present the results as a nested JSON, providing both the severity score and a clear explanation for each subfactor. Ensure that each explanation references relevant text spans or contextual inferences to justify the assigned score.

To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Reason: A list containing the rationale for the assigned severity score, based on evidence explicitly or implicitly found in the transcription. This could be a direct quote, paraphrased text, or a context-based inference.
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON, with elements inside angle brackets being placeholders for the actual values:
 {{
    "Re-experiencing": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Avoidance": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_w-reasoning_wo-subscales_w-questions_phase-2":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. What are the three things in your life that you look forward to the most right now? Can you elaborate?
2. What are the three biggest challenges that you are managing in your life right now? Can you elaborate?
3. Where are three places that you turn to find support right now and why? Can you elaborate?
4. Over the past 5 years, what are the three nicest things that happened to you and your family? Can you elaborate?
5. Over the past 5 years, what are the worst three things that have happened to you and your family? Can you elaborate?
6. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?
7. What are three reflections that you have on this research experience? Were any parts particularly challenging or interesting? Do you have any recommendations for us continuing this research?

Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing, Avoidance, Dysphoria, Hyperarousal.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide an explanation on how each symptom was identified. Provide a score between 0 and 4 for each subfactor.
STEP 2: Present the results as a nested JSON, providing both the severity score and a clear explanation for each subfactor. Ensure that each explanation references relevant text spans or contextual inferences to justify the assigned score.

To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Reason: A list containing the rationale for the assigned severity score, based on evidence explicitly or implicitly found in the transcription. This could be a direct quote, paraphrased text, or a context-based inference.
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON, with elements inside angle brackets being placeholders for the actual values:
 {{
    "Re-experiencing": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Avoidance": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_w-reasoning_wo-subscales_w-questions_phase-3":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. What are the three things in your life that you look forward to the most right now? Can you elaborate?
2. What are the three biggest challenges that you are managing in your life right now? Can you elaborate?
3. Where are three places that you turn to find support right now and why? Can you elaborate?
4. Over the past 5 years, what are the three nicest things that happened to you and your family? Can you elaborate?
5. Over the past 5 years, what are the worst three things that have happened to you and your family? Can you elaborate?
6. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?
7. How has the COVID-19 pandemic changed your life? Can you elaborate?
8. What was most difficult for you about the COVID-19 pandemic? Can you elaborate?
9. What do you most look forward to doing after the COVID-19 pandemic is over? Can you elaborate?
10. Looking back at the last two decades, what effect did 9/11 have on your life? Can you elaborate?
11. How does 9/11 affect you now? Can you elaborate?
12. What would you like future generations to know about 9/11? Can you elaborate?
13. What are three reflections that you have on this research experience?
14. Were any parts particularly challenging or interesting?
15. Do you have any recommendations for us continuing this research?

Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing, Avoidance, Dysphoria, Hyperarousal.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide an explanation on how each symptom was identified. Provide a score between 0 and 4 for each subfactor.
STEP 2: Present the results as a nested JSON, providing both the severity score and a clear explanation for each subfactor. Ensure that each explanation references relevant text spans or contextual inferences to justify the assigned score.

To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Reason: A list containing the rationale for the assigned severity score, based on evidence explicitly or implicitly found in the transcription. This could be a direct quote, paraphrased text, or a context-based inference.
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON, with elements inside angle brackets being placeholders for the actual values:
 {{
    "Re-experiencing": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Avoidance": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_wo-reasoning_wo-subscales_w-questions_phase-1":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. How are you? Can you elaborate?
2. How's the family? Can you elaborate?
3. What's new? Can you elaborate?
4. What else?
5. Over the past 5 years what are the three nicest things that happened to you and your family? Can you elaborate?
6. Over the past 5 years what are the three worst things that happened to you and your family? Can you elaborate?
7. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?

Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing, Avoidance, Dysphoria, Hyperarousal.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide a score between 0 and 4 for each subfactor.
STEP 2: Present the results as a nested JSON, providing both the severity score and a clear explanation for each subfactor. Ensure that each explanation references relevant text spans or contextual inferences to justify the assigned score.

To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON, with elements inside angle brackets being placeholders for the actual values:
 {{
    "Re-experiencing": {{
      "Severity Score": 
    }},
    "Avoidance": {{
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_wo-reasoning_wo-subscales_w-questions_phase-2":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. What are the three things in your life that you look forward to the most right now? Can you elaborate?
2. What are the three biggest challenges that you are managing in your life right now? Can you elaborate?
3. Where are three places that you turn to find support right now and why? Can you elaborate?
4. Over the past 5 years, what are the three nicest things that happened to you and your family? Can you elaborate?
5. Over the past 5 years, what are the worst three things that have happened to you and your family? Can you elaborate?
6. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?
7. What are three reflections that you have on this research experience? Were any parts particularly challenging or interesting? Do you have any recommendations for us continuing this research?

Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing, Avoidance, Dysphoria, Hyperarousal.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide a score between 0 and 4 for each subfactor.
STEP 2: Present the results as a nested JSON, providing both the severity score and a clear explanation for each subfactor. Ensure that each explanation references relevant text spans or contextual inferences to justify the assigned score.

To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON, with elements inside angle brackets being placeholders for the actual values:
 {{
    "Re-experiencing": {{
      "Severity Score": 
    }},
    "Avoidance": {{
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_wo-reasoning_wo-subscales_w-questions_phase-3":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. What are the three things in your life that you look forward to the most right now? Can you elaborate?
2. What are the three biggest challenges that you are managing in your life right now? Can you elaborate?
3. Where are three places that you turn to find support right now and why? Can you elaborate?
4. Over the past 5 years, what are the three nicest things that happened to you and your family? Can you elaborate?
5. Over the past 5 years, what are the worst three things that have happened to you and your family? Can you elaborate?
6. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?
7. How has the COVID-19 pandemic changed your life? Can you elaborate?
8. What was most difficult for you about the COVID-19 pandemic? Can you elaborate?
9. What do you most look forward to doing after the COVID-19 pandemic is over? Can you elaborate?
10. Looking back at the last two decades, what effect did 9/11 have on your life? Can you elaborate?
11. How does 9/11 affect you now? Can you elaborate?
12. What would you like future generations to know about 9/11? Can you elaborate?
13. What are three reflections that you have on this research experience?
14. Were any parts particularly challenging or interesting?
15. Do you have any recommendations for us continuing this research?

Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing, Avoidance, Dysphoria, Hyperarousal.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide a score between 0 and 4 for each subfactor.
STEP 2: Present the results as a nested JSON, providing both the severity score and a clear explanation for each subfactor. Ensure that each explanation references relevant text spans or contextual inferences to justify the assigned score.

To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON, with elements inside angle brackets being placeholders for the actual values:
 {{
    "Re-experiencing": {{
      "Severity Score": 
    }},
    "Avoidance": {{
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_wo-reasoning_wo-subscales_wo-questions":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing, Avoidance, Dysphoria, Hyperarousal.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide a score between 0 and 4 for each subfactor.

To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON:
 {{
    "Re-experiencing": {{
      "Severity Score": 
    }},
    "Avoidance": {{
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_wo-reasoning_wo-subscales_wo-questions_tsbs":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing, Avoidance, Dysphoria, Hyperarousal.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide a score between 0 and 4 for each subfactor.

Enclose all your thoughts within <think> and </think> before you generate your task response. To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON:
<think> You should think step by step here </think>
 {{
    "Re-experiencing": {{
      "Severity Score": 
    }},
    "Avoidance": {{
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_w-reasoning_wo-subscales_wo-questions_tsbs": """Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing, Avoidance, Dysphoria, Hyperarousal.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide an explanation on how each symptom was identified. Provide a score between 0 and 4 for each subfactor.
STEP 2: Present the results as a nested JSON, providing both the severity score and a clear explanation for each subfactor. Ensure that each explanation references relevant text spans or contextual inferences to justify the assigned score.

Enclose all your thoughts within <think> and </think> before you generate your task response. To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Reason: A list containing the rationale for the assigned severity score, based on evidence explicitly or implicitly found in the transcription. This could be a direct quote, paraphrased text, or a context-based inference.
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON, with elements inside angle brackets being placeholders for the actual values:
<think> You should think step by step here </think>
 {{
    "Re-experiencing": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Avoidance": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Reason": ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_wo-reasoning_w-subscales_wo-questions_tsbs":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing: Intrusive thoughts, flashbacks, nightmares, or distress when reminded of the trauma.
Avoidance: Efforts to avoid thoughts, feelings, or external reminders associated with the trauma.
Dysphoria: Persistent negative thoughts, feelings of guilt, emotional numbness, or loss of interest in activities.
Hyperarousal: Increased irritability, hypervigilance, being easily startled, or difficulty concentrating and sleeping.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide a score between 0 and 4 for each subfactor.

Enclose all your thoughts within <think> and </think> before you generate your task response. To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON:
<think> You should think step by step here </think>
 {{
    "Re-experiencing": {{
      "Severity Score": 
    }},
    "Avoidance": {{
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_wo-reasoning_wo-subscales_w-questions_phase-1_tsbs":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. How are you? Can you elaborate?
2. How's the family? Can you elaborate?
3. What's new? Can you elaborate?
4. What else?
5. Over the past 5 years what are the three nicest things that happened to you and your family? Can you elaborate?
6. Over the past 5 years what are the three worst things that happened to you and your family? Can you elaborate?
7. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?

Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing, Avoidance, Dysphoria, Hyperarousal.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide a score between 0 and 4 for each subfactor.
STEP 2: Present the results as a nested JSON, providing both the severity score and a clear explanation for each subfactor. Ensure that each explanation references relevant text spans or contextual inferences to justify the assigned score.

Enclose all your thoughts within <think> and </think> before you generate your task response. To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON, with elements inside angle brackets being placeholders for the actual values:
<think> You should think step by step here </think>
 {{
    "Re-experiencing": {{
      "Severity Score": 
    }},
    "Avoidance": {{
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_wo-reasoning_wo-subscales_w-questions_phase-2_tsbs":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. What are the three things in your life that you look forward to the most right now? Can you elaborate?
2. What are the three biggest challenges that you are managing in your life right now? Can you elaborate?
3. Where are three places that you turn to find support right now and why? Can you elaborate?
4. Over the past 5 years, what are the three nicest things that happened to you and your family? Can you elaborate?
5. Over the past 5 years, what are the worst three things that have happened to you and your family? Can you elaborate?
6. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?
7. What are three reflections that you have on this research experience? Were any parts particularly challenging or interesting? Do you have any recommendations for us continuing this research?

Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing, Avoidance, Dysphoria, Hyperarousal.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide a score between 0 and 4 for each subfactor.
STEP 2: Present the results as a nested JSON, providing both the severity score and a clear explanation for each subfactor. Ensure that each explanation references relevant text spans or contextual inferences to justify the assigned score.

Enclose all your thoughts within <think> and </think> before you generate your task response. To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON, with elements inside angle brackets being placeholders for the actual values:
<think> You should think step by step here </think>.
 {{
    "Re-experiencing": {{
      "Severity Score": 
    }},
    "Avoidance": {{
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_wo-reasoning_wo-subscales_w-questions_phase-3_tsbs":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. What are the three things in your life that you look forward to the most right now? Can you elaborate?
2. What are the three biggest challenges that you are managing in your life right now? Can you elaborate?
3. Where are three places that you turn to find support right now and why? Can you elaborate?
4. Over the past 5 years, what are the three nicest things that happened to you and your family? Can you elaborate?
5. Over the past 5 years, what are the worst three things that have happened to you and your family? Can you elaborate?
6. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?
7. How has the COVID-19 pandemic changed your life? Can you elaborate?
8. What was most difficult for you about the COVID-19 pandemic? Can you elaborate?
9. What do you most look forward to doing after the COVID-19 pandemic is over? Can you elaborate?
10. Looking back at the last two decades, what effect did 9/11 have on your life? Can you elaborate?
11. How does 9/11 affect you now? Can you elaborate?
12. What would you like future generations to know about 9/11? Can you elaborate?
13. What are three reflections that you have on this research experience?
14. Were any parts particularly challenging or interesting?
15. Do you have any recommendations for us continuing this research?

Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing, Avoidance, Dysphoria, Hyperarousal.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide a score between 0 and 4 for each subfactor.
STEP 2: Present the results as a nested JSON, providing both the severity score and a clear explanation for each subfactor. Ensure that each explanation references relevant text spans or contextual inferences to justify the assigned score.

Enclose all your thoughts within <think> and </think> before you generate your task response. To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the abstracted format of the JSON, with elements inside angle brackets being placeholders for the actual values:
<think> You should think step by step here </think>.
 {{
    "Re-experiencing": {{
      "Severity Score": 
    }},
    "Avoidance": {{
      "Severity Score": 
    }},
    "Dysphoria": {{
      "Severity Score": 
    }},
    "Hyperarousal": {{
      "Severity Score": 
    }}
  }}

Text: '{text}'
""",

"ptsd_wo-reasoning_wo-subscales_wo-questions_xml":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing, Avoidance, Dysphoria, Hyperarousal.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide a score between 0 and 4 for each subfactor.

To ensure clarity and easy readability, format your output into an XML structure. Each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) should be represented as an XML tag, containing a child tag for the severity score.
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the required XML format:
 <assessment>
    <subscale>
        <name>re-experiencing</name>
        <score>score</score>
    </subscale>
    <subscale>
        <name>avoidance</name>
        <score>score</score>
    </subscale>
    <subscale>
        <name>dysphoria</name>
        <score>score</score>
    </subscale>
    <subscale>
        <name>hyperarousal</name>
        <score>score</score>
    </subscale>
    <subscale>
        <name>total</name>
        <score>score</score>
    </subscale>
</assessment>

Text: '{text}'
""",

"ptsd_wo-reasoning_w-subscales_wo-questions_xml":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing: Intrusive thoughts, flashbacks, nightmares, or distress when reminded of the trauma.
Avoidance: Efforts to avoid thoughts, feelings, or external reminders associated with the trauma.
Dysphoria: Persistent negative thoughts, feelings of guilt, emotional numbness, or loss of interest in activities.
Hyperarousal: Increased irritability, hypervigilance, being easily startled, or difficulty concentrating and sleeping.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

Steps
The text should be carefully analyzed, and the following steps should be strictly followed:
STEP 1: Detect the PTSD subfactors in the text and provide a score between 0 and 4 for each subfactor.

To ensure clarity and easy readability, format your output into an XML structure. Each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) should be represented as an XML tag, containing a child tag for the severity score.
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity).
Here’s the required XML format:
 <assessment>
    <subscale>
        <name>re-experiencing</name>
        <score>score</score>
    </subscale>
    <subscale>
        <name>avoidance</name>
        <score>score</score>
    </subscale>
    <subscale>
        <name>dysphoria</name>
        <score>score</score>
    </subscale>
    <subscale>
        <name>hyperarousal</name>
        <score>score</score>
    </subscale>
    <subscale>
        <name>total</name>
        <score>score</score>
    </subscale>
</assessment>

Text: '{text}'
""",
}