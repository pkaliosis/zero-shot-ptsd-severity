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

"ptsd_w-reasoning_w-subscales_w-questions_phase-1_xml":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
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

To ensure clarity and easy readability, format your output into an XML structure. Each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) should be represented as an XML tag, containing a child tag for the severity score. Each subfactor should include:
Reason: A list containing the rationale for the assigned severity score, based on evidence explicitly or implicitly found in the transcription. This could be a direct quote, paraphrased text, or a context-based inference.
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

"ptsd_w-reasoning_w-subscales_w-questions_phase-2_xml":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
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

To ensure clarity and easy readability, format your output into an XML structure. Each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) should be represented as an XML tag, containing a child tag for the severity score. Each subfactor should include:
Reason: A list containing the rationale for the assigned severity score, based on evidence explicitly or implicitly found in the transcription. This could be a direct quote, paraphrased text, or a context-based inference.
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

"ptsd_w-reasoning_w-subscales_w-questions_phase-3_xml":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
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

To ensure clarity and easy readability, format your output into an XML structure. Each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) should be represented as an XML tag, containing a child tag for the severity score. Each subfactor should include:
Reason: A list containing the rationale for the assigned severity score, based on evidence explicitly or implicitly found in the transcription. This could be a direct quote, paraphrased text, or a context-based inference.
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

"ptsd_wo-reasoning_w-subscales_wo-questions_xml_alt_defs":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing: Individuals who experience re-experiencing symptoms tend to have intrusive thoughts, flashbacks, or nightmares related to the trauma. They may also react emotionally or physically to trauma-related cues, while individuals who do not experience re-experiencing symptoms tend to remain unaffected by such memories or reminders.
Avoidance: Individuals who experience avoidance symptoms tend to actively avoid thoughts, feelings, or external reminders of the trauma, while individuals who do not experience avoidance symptoms tend to face these thoughts and reminders without distress.
Dysphoria: Individuals who experience dysphoria tend to have persistent negative thoughts, emotional detachment, or a diminished sense of future. They may also struggle with recalling aspects of the trauma, experience a loss of interest in activities, or display restricted emotional expression. Individuals who do not experience dysphoria tend to maintain a stable emotional state and engagement in daily life.
Hyperarousal: Individuals who experience hyperarousal tend to be highly alert, easily startled, or struggle with sleep, irritability, and concentration. They may also exhibit hypervigilance and an exaggerated startle response, while individuals who do not experience hyperarousal tend to feel more at ease and relaxed in their daily lives.

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

"ptsd_wo-reasoning_w-subscales_wo-questions_base":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
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
PTSD Severity Scores:
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

Text: '{text}',

Assign a severity score for each subfactor (between 1 and 5).
PTSD Severity Scores:
""",

"ptsd_wo-reasoning_w-subscales_wo-questions_base_fs":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
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
PTSD Severity Scores:
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

Here are a few examples of text-scores pairs in order to introduce you to the task:

Text: 'Three things that I look forward to most spending time with my family. And Friends.
Exercising and playing golf. What are the three things you like that? What are the three biggest 
challenges you are managing in your life right now? That would be the biggest challenges. 
Obviously getting over the passing of my wife. Would be a one challenge. I'm sure we'll go on for. 
A while. With winter coming, just occupying myself since I won't be able to do as many outdoor activities. 
That would be a challenge. and, 3rd challenge. Watch store. 3rd challenge. Is managing a relationship 
with my current girlfriend? Where are the three places you turn to find support right now? And why? 
I know. I'm a pretty happy person. Replace the shifter night. I guess would be my three children if 
I have a problem, but so far everything is smooth sailing. I'm not dealing with any crisis, 
is at this point. Olympus ideas, what are the three nicest things? That happened to you and your family? 
3 nicest things. I have happened to me and my family. Well, my wife passed away, three and a half 
years ago. So the outpouring from the community. and, Friends. What is probably the nicest thing 
I've ever experienced? I guess, another nice thing would be my oldest daughter getting married. 
She still. Lives in my neighborhood, which is very convenient. My son getting engaged. 
And my middle daughter, having a boy or boyfriend. Now. Wow, can I keep on harping on my wife over 
the past five years? Were the three worst things that happened to you and your family? obviously, 
for me, it would be The death of again, my wife, I guess, my obviously my dad passed away about a 
year-and-a-half ago. So That was something that wasn't pleasant. And then I guess, the third thing 
would be just dealing with this covid and seeing, you know, how many people have passed away. 
Something, you know, and obviously acquaintances people. I used to work with it. The police department. 
Imagine you are 5 years old at, please tell us about the life. You're leading your interest, 
your own life and your work will, I will be working a little part-time security right now when I want to, 
But hopefully, they'll be some grandchildren in my future. And I'll still be going to the gym exercising 
and playing golf being active. Take care of my pool cut, my lawn, take care of the house. 
Are they free Reflections that you have had on This research experience or any parts? 
Particularly challenging or interesting. Do you have any recommendations for us continuing 
this research? Reflections, I don't know, make me thinking about passing of my wife and my father. 
but yeah, I'm fortunate to have a lot of Can children have people around me, their friends? And it's all good.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 1
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 1
    }}
  }},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 4
    }},
    "Avoidance": {{
      "Severity Score": 4
    }},
    "Dysphoria": {{
      "Severity Score": 2
    }},
    "Hyperarousal": {{
      "Severity Score": 4
    }}
  }},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 1
    }}
  }},


Text: '{text}',

Output:
""",

"ptsd_wo-reasoning_w-subscales_wo-questions_fs":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
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

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Three things that I look forward to most spending time with my family. And Friends.
Exercising and playing golf. What are the three things you like that? What are the three biggest 
challenges you are managing in your life right now? That would be the biggest challenges. 
Obviously getting over the passing of my wife. Would be a one challenge. I'm sure we'll go on for. 
A while. With winter coming, just occupying myself since I won't be able to do as many outdoor activities. 
That would be a challenge. and, 3rd challenge. Watch store. 3rd challenge. Is managing a relationship 
with my current girlfriend? Where are the three places you turn to find support right now? And why? 
I know. I'm a pretty happy person. Replace the shifter night. I guess would be my three children if 
I have a problem, but so far everything is smooth sailing. I'm not dealing with any crisis, 
is at this point. Olympus ideas, what are the three nicest things? That happened to you and your family? 
3 nicest things. I have happened to me and my family. Well, my wife passed away, three and a half 
years ago. So the outpouring from the community. and, Friends. What is probably the nicest thing 
I've ever experienced? I guess, another nice thing would be my oldest daughter getting married. 
She still. Lives in my neighborhood, which is very convenient. My son getting engaged. 
And my middle daughter, having a boy or boyfriend. Now. Wow, can I keep on harping on my wife over 
the past five years? Were the three worst things that happened to you and your family? obviously, 
for me, it would be The death of again, my wife, I guess, my obviously my dad passed away about a 
year-and-a-half ago. So That was something that wasn't pleasant. And then I guess, the third thing 
would be just dealing with this covid and seeing, you know, how many people have passed away. 
Something, you know, and obviously acquaintances people. I used to work with it. The police department. 
Imagine you are 5 years old at, please tell us about the life. You're leading your interest, 
your own life and your work will, I will be working a little part-time security right now when I want to, 
But hopefully, they'll be some grandchildren in my future. And I'll still be going to the gym exercising 
and playing golf being active. Take care of my pool cut, my lawn, take care of the house. 
Are they free Reflections that you have had on This research experience or any parts? 
Particularly challenging or interesting. Do you have any recommendations for us continuing 
this research? Reflections, I don't know, make me thinking about passing of my wife and my father. 
but yeah, I'm fortunate to have a lot of Can children have people around me, their friends? And it's all good.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 1
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 1
    }}
  }},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 4
    }},
    "Avoidance": {{
      "Severity Score": 4
    }},
    "Dysphoria": {{
      "Severity Score": 2
    }},
    "Hyperarousal": {{
      "Severity Score": 4
    }}
  }},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 1
    }}
  }},

Text: '{text}'

Output:
""",

"pcs_zs": """
Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the individual’s overall physical health based on their self-described experiences and limitations. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of health-related questions, designed to evaluate their physical functioning, pain levels, general health perception, and any limitations in work or daily activities.

Using the content of this transcript, you will predict a single PCS-12 (Physical Component Summary) score. This score should reflect the individual’s overall physical health status as captured by the SF-12 Health Survey framework.

Scoring System

The PCS-12 score is a standardized health score derived from the SF-12 questionnaire. It is reported on a norm-based T-score scale, where:

- The average score in the general population is 50
- The standard deviation is 10
- Scores typically range from ~10 to ~75, where higher scores indicate better physical health

Use the following ranges as interpretive guidance:

| PCS-12 Score | Interpretation                      |
|--------------|-------------------------------------|
| 60–70+       | Excellent physical health           |
| 50–59        | Above-average physical health       |
| 40–49        | Below-average physical health       |
| 30–39        | Poor physical health                |
| <30          | Very poor or severely impaired      |

Instructions

The transcript should be carefully analyzed, and the following steps should be strictly followed:

STEP 1: Based on the individual’s description of their physical health, predict a single PCS-12 score, reflecting their overall physical health.

STEP 2: Format your output as a JSON object for clarity and ease of parsing:

{{
  "PCS-12 Score": 
}}

Text: '{text}'

""",

"pcs_zs_base": """
Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the individual’s overall physical health based on their self-described experiences and limitations. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of health-related questions, designed to evaluate their physical functioning, pain levels, general health perception, and any limitations in work or daily activities.

Using the content of this transcript, you will predict a single PCS-12 (Physical Component Summary) score. This score should reflect the individual’s overall physical health status as captured by the SF-12 Health Survey framework.

Scoring System

The PCS-12 score is a standardized health score derived from the SF-12 questionnaire. It is reported on a norm-based T-score scale, where:

- The average score in the general population is 50
- The standard deviation is 10
- Scores typically range from ~10 to ~75, where higher scores indicate better physical health

Use the following ranges as interpretive guidance:

| PCS-12 Score | Interpretation                      |
|--------------|-------------------------------------|
| 60–70+       | Excellent physical health           |
| 50–59        | Above-average physical health       |
| 40–49        | Below-average physical health       |
| 30–39        | Poor physical health                |
| <30          | Very poor or severely impaired      |

Instructions

The transcript should be carefully analyzed, and the following steps should be strictly followed:

STEP 1: Based on the individual’s description of their physical health, predict a single PCS-12 score, reflecting their overall physical health.

STEP 2: Format your output as a JSON object for clarity and ease of parsing:
PTSD Severity Scores:
{{
  "PCS-12 Score": <float from 10 to 75>
}}

Text: '{text}'

PTSD Severity Scores:
""",

"pcs_fs": """
Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the individual’s overall physical health based on their self-described experiences and limitations. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of health-related questions, designed to evaluate their physical functioning, pain levels, general health perception, and any limitations in work or daily activities.

Using the content of this transcript, you will predict a single PCS-12 (Physical Component Summary) score. This score should reflect the individual’s overall physical health status as captured by the SF-12 Health Survey framework.

Scoring System

The PCS-12 score is a standardized health score derived from the SF-12 questionnaire. It is reported on a norm-based T-score scale, where:

- The average score in the general population is 50
- The standard deviation is 10
- Scores typically range from ~10 to ~75, where higher scores indicate better physical health

Use the following ranges as interpretive guidance:

| PCS-12 Score | Interpretation                      |
|--------------|-------------------------------------|
| 60–70+       | Excellent physical health           |
| 50–59        | Above-average physical health       |
| 40–49        | Below-average physical health       |
| 30–39        | Poor physical health                |
| <30          | Very poor or severely impaired      |

Instructions

The transcript should be carefully analyzed, and the following steps should be strictly followed:

STEP 1: Based on the individual’s description of their physical health, predict a single PCS-12 score, reflecting their overall physical health.

STEP 2: Format your output as a JSON object for clarity and ease of parsing:

{{
  "PCS-12 Score": 
}}

To better understand the task, here are a few showcasing examples of input transcripts and their corresponding PCS-12 score predictions:

--- EXAMPLES ---

Example 1  
Text: "3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it."

Output:
{{
  "PCS-12 Score": 53
}}

Example 2  
Text: "How you lost family members? This happened to me. Cancer. Covid. If it's nothing too elaborate.
I know. They will be so happy. Life will be much easier for them. I don't work. If I'm making another 5 Years,
be so happy. I'm fighting for my three quarter disability. If I can get that, I would be so happy.
The wife, I know, my wife will be taken care of. And my children will be taken care of. Waking up in
the morning. Well. Just glad to be alive. Most of my friends. Not here. I need the people that most of
the people that, I work with no longer here. So I'm just glad to be here. The three biggest challenges.
Covid-19 is a big challenge. Go shopping. You have to put on the mask. Dealing with family members that
don't want to get vaccinated as a challenge. Staying healthy is a challenge. The only place I turn.
Support is. Every two weeks. I go see. World Trade Center. I see Jenny Wang. I like. Hi, Google.
I wake up every morning to my wife. Third person is every now and then my brother calls me.
Every so often my sister calls me. That's it. Staying alive, just thing. Stay healthy. He trying to deal with.
Family. That doesn't want to get vaccinated. Never coming around. Coast. Picking share your beliefs.
Three things. I look forward to most of my life. Waking up in the morning. Seen my granddaughter.
Going to bed. Get me some. Nothing too. Elaborate. Plus some family members to covid. That's it.
People, my family is. Have cancer. Bipolar. Have covid-19 won't get vaccinated. My granddaughter won't get vaccinated.
Tough things in my life. I can elaborate. I keep in touch with my cousin. Those are the only support.
Like an isthmus that I have. I'd be so lost. And guys, like, Richard Palma calls me. And every so often.
The PTC holds immense. Did I go to? That's it. Ultra Library. other than the fact that I've been helpful.
Wutc. You guys have done so so much. So many good things. Program has been so much for so many.
Can only go up from here. Thank you so much. have anything nice happened to me over the Fast Five,
because I guess. I've never had anything bad happened to me over the past 5 years. I guess. That's nice.
So, I can't complain. I've had some deaths in the family."

Output:
{{
  "PCS-12 Score": 34
}}

Example 3  
Text: "Please answer the phone questions out loud. Open to the camera.  Okay, I can do that. 
What are what are three things in your life that you look forward to most right now?  Going on vacation. 
What are the big three biggest challenge in managing your life right now? Don't have any 
What are three places you find support in right now?  Fishing.  Walking in the woods.  Being alone. 
in the past five years, when the nicest things that happened to you and your family in the past 5 years, 
I don't know what's good.  Over the past five years were the worst things, that happened my mother passed away. 
2018.  I need matching you look five years old. Please tell us about your life. Are you leaving? 
Has covid-19.  No, nothing.  Inconveniences with mass and not sense. But other than that, it's nothing. 
What is the most difficult part?  Nothing.  What do you look for tomorrow?  Getting rid of the stupid mask. 
Look-back law last two decades. What effect did 9/11 hit didn't have any effect on my life  It's just a job. 
Nothing, no effect at all.  What would you like to meet for dinner or should learn what happened there?  
What are three reflection? Can you have on this research experience? No reflections.  Does this job?  
What are what are parts of particular children? Non  you have any right now? I have no recommendations."

Output:
{{
  "PCS-12 Score": 62
}}

--- END OF EXAMPLES ---

Now process the following transcript accordingly:

Text: '{text}'

""",

"pcs_fs_tsbs": """
Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the individual’s overall physical health based on their self-described experiences and limitations. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of health-related questions, designed to evaluate their physical functioning, pain levels, general health perception, and any limitations in work or daily activities.

Using the content of this transcript, you will predict a single PCS-12 (Physical Component Summary) score. This score should reflect the individual’s overall physical health status as captured by the SF-12 Health Survey framework.

Scoring System

The PCS-12 score is a standardized health score derived from the SF-12 questionnaire. It is reported on a norm-based T-score scale, where:

- The average score in the general population is 50
- The standard deviation is 10
- Scores typically range from ~10 to ~75, where higher scores indicate better physical health

Use the following ranges as interpretive guidance:

| PCS-12 Score | Interpretation                      |
|--------------|-------------------------------------|
| 60–70+       | Excellent physical health           |
| 50–59        | Above-average physical health       |
| 40–49        | Below-average physical health       |
| 30–39        | Poor physical health                |
| <30          | Very poor or severely impaired      |

Instructions

Enclose all your thoughts within <think> and </think> before you generate your task response. The transcript should be carefully analyzed, and the following steps should be strictly followed:

STEP 1: Based on the individual’s description of their physical health, predict a single PCS-12 score, reflecting their overall physical health.

STEP 2: Format your output as a JSON object for clarity and ease of parsing:

<think> You should think step by step here </think>
{{
  "PCS-12 Score": 
}}

To better understand the task, here are a few showcasing examples of input transcripts and their corresponding PCS-12 score predictions:

--- EXAMPLES ---

Example 1  
Text: "3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it."

<think> You should think step by step here </think>
Output:
{{
  "PCS-12 Score": 53
}}

Example 2  
Text: "How you lost family members? This happened to me. Cancer. Covid. If it's nothing too elaborate.
I know. They will be so happy. Life will be much easier for them. I don't work. If I'm making another 5 Years,
be so happy. I'm fighting for my three quarter disability. If I can get that, I would be so happy.
The wife, I know, my wife will be taken care of. And my children will be taken care of. Waking up in
the morning. Well. Just glad to be alive. Most of my friends. Not here. I need the people that most of
the people that, I work with no longer here. So I'm just glad to be here. The three biggest challenges.
Covid-19 is a big challenge. Go shopping. You have to put on the mask. Dealing with family members that
don't want to get vaccinated as a challenge. Staying healthy is a challenge. The only place I turn.
Support is. Every two weeks. I go see. World Trade Center. I see Jenny Wang. I like. Hi, Google.
I wake up every morning to my wife. Third person is every now and then my brother calls me.
Every so often my sister calls me. That's it. Staying alive, just thing. Stay healthy. He trying to deal with.
Family. That doesn't want to get vaccinated. Never coming around. Coast. Picking share your beliefs.
Three things. I look forward to most of my life. Waking up in the morning. Seen my granddaughter.
Going to bed. Get me some. Nothing too. Elaborate. Plus some family members to covid. That's it.
People, my family is. Have cancer. Bipolar. Have covid-19 won't get vaccinated. My granddaughter won't get vaccinated.
Tough things in my life. I can elaborate. I keep in touch with my cousin. Those are the only support.
Like an isthmus that I have. I'd be so lost. And guys, like, Richard Palma calls me. And every so often.
The PTC holds immense. Did I go to? That's it. Ultra Library. other than the fact that I've been helpful.
Wutc. You guys have done so so much. So many good things. Program has been so much for so many.
Can only go up from here. Thank you so much. have anything nice happened to me over the Fast Five,
because I guess. I've never had anything bad happened to me over the past 5 years. I guess. That's nice.
So, I can't complain. I've had some deaths in the family."

<think> You should think step by step here </think>
Output:
{{
  "PCS-12 Score": 34
}}

Example 3  
Text: "Please answer the phone questions out loud. Open to the camera.  Okay, I can do that. 
What are what are three things in your life that you look forward to most right now?  Going on vacation. 
What are the big three biggest challenge in managing your life right now? Don't have any 
What are three places you find support in right now?  Fishing.  Walking in the woods.  Being alone. 
in the past five years, when the nicest things that happened to you and your family in the past 5 years, 
I don't know what's good.  Over the past five years were the worst things, that happened my mother passed away. 
2018.  I need matching you look five years old. Please tell us about your life. Are you leaving? 
Has covid-19.  No, nothing.  Inconveniences with mass and not sense. But other than that, it's nothing. 
What is the most difficult part?  Nothing.  What do you look for tomorrow?  Getting rid of the stupid mask. 
Look-back law last two decades. What effect did 9/11 hit didn't have any effect on my life  It's just a job. 
Nothing, no effect at all.  What would you like to meet for dinner or should learn what happened there?  
What are three reflection? Can you have on this research experience? No reflections.  Does this job?  
What are what are parts of particular children? Non  you have any right now? I have no recommendations."

<think> You should think step by step here </think>
Output:
{{
  "PCS-12 Score": 62
}}

--- END OF EXAMPLES ---

Now process the following transcript accordingly:

Text: '{text}'

""",

"mcs_zs": """Your task is to conduct an in-depth analysis of a provided transcript, with the goal of deriving the final Mental Component Summary (MCS) score according to the SF-12 methodology. The transcript contains the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. Based on the overall mental health information in the transcript, provide a final estimate of the MCS score, reflecting aspects such as vitality, social functioning, role limitations due to emotional problems, and general mental health perceptions.

Scoring:
Use the SF-12 transformation methodology to approximate the MCS score on a norm-based scale (where the general population has a mean of 50 and a standard deviation of 10). The final score should be a single numeric value representing the overall mental health status.

Steps:
STEP 1: Analyze the transcript to extract indicators related to mental health.
STEP 2: Use these indicators to estimate the overall MCS score.
STEP 3: Present the final score as a nested JSON.

Format your output into a nested JSON with the following structure:
{{
   "SF12_MCS": {{
       "Final Score": "<Numeric value>"
   }}
}}

Text: '{text}'
""",

"pcs_zs_tsbs": """
Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the individual’s overall physical health based on their self-described experiences and limitations. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of health-related questions, designed to evaluate their physical functioning, pain levels, general health perception, and any limitations in work or daily activities.

Using the content of this transcript, you will predict a single PCS-12 (Physical Component Summary) score. This score should reflect the individual’s overall physical health status as captured by the SF-12 Health Survey framework.

Scoring System

The PCS-12 score is a standardized health score derived from the SF-12 questionnaire. It is reported on a norm-based T-score scale, where:

- The average score in the general population is 50
- The standard deviation is 10
- Scores typically range from ~10 to ~75, where higher scores indicate better physical health

Use the following ranges as interpretive guidance:

| PCS-12 Score | Interpretation                      |
|--------------|-------------------------------------|
| 60–70+       | Excellent physical health           |
| 50–59        | Above-average physical health       |
| 40–49        | Below-average physical health       |
| 30–39        | Poor physical health                |
| <30          | Very poor or severely impaired      |

Instructions

Enclose all your thoughts within <think> and </think> before you generate your task response. The transcript should be carefully analyzed, and the following steps should be strictly followed:

STEP 1: Based on the individual’s description of their physical health, predict a single PCS-12 score, reflecting their overall physical health.

STEP 2: Format your output as a JSON object for clarity and ease of parsing:
<think> You should think step by step here </think>
{{
  "PCS-12 Score": 
}}

Text: '{text}'

""",

"mcs_zs_tsbs": """Your task is to conduct an in-depth analysis of a provided transcript, with the goal of deriving the final Mental Component Summary (MCS) score according to the SF-12 methodology. The transcript contains the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. Based on the overall mental health information in the transcript, provide a final estimate of the MCS score, reflecting aspects such as vitality, social functioning, role limitations due to emotional problems, and general mental health perceptions.

Scoring:
Use the SF-12 transformation methodology to approximate the MCS score on a norm-based scale (where the general population has a mean of 50 and a standard deviation of 10). The final score should be a single numeric value representing the overall mental health status.

Steps:
STEP 1: Analyze the transcript to extract indicators related to mental health.
STEP 2: Use these indicators to estimate the overall MCS score.
STEP 3: Present the final score as a nested JSON.

Enclose all your thoughts within <think> and </think> before you generate your task response. Format your output into a nested JSON with the following structure:
<think> You should think step by step here </think>.
{{
   "SF12_MCS": {{
       "Final Score": "<Numeric value>"
   }}
}}

Text: '{text}'
""",

"mcs_zs_base": """Your task is to conduct an in-depth analysis of a provided transcript, with the goal of deriving the final Mental Component Summary (MCS) score according to the SF-12 methodology. The transcript contains the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. Based on the overall mental health information in the transcript, provide a final estimate of the MCS score, reflecting aspects such as vitality, social functioning, role limitations due to emotional problems, and general mental health perceptions.

Scoring:
Use the SF-12 transformation methodology to approximate the MCS score on a norm-based scale (where the general population has a mean of 50 and a standard deviation of 10). The final score should be a single numeric value representing the overall mental health status.

Steps:
STEP 1: Analyze the transcript to extract indicators related to mental health.
STEP 2: Use these indicators to estimate the overall MCS score.
STEP 3: Present the final score as a nested JSON.

Format your output into a nested JSON with the following structure:
MCS Score:
{{
   "SF12_MCS": {{
       "Final Score": "<Float value between 0 and 100>"
   }}
}}

Text: '{text}'

MCS Score:
""",

"ptsd_wo-reasoning_w-subscales_wo-questions_fs_tsbs":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
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
<think> <The model thinks step by step and predicts a score for the given transcript> </think>.
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

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts. Finally predict the severity scores for the last example.

Text: 'Three things that I look forward to most spending time with my family. And Friends.
Exercising and playing golf. What are the three things you like that? What are the three biggest 
challenges you are managing in your life right now? That would be the biggest challenges. 
Obviously getting over the passing of my wife. Would be a one challenge. I'm sure we'll go on for. 
A while. With winter coming, just occupying myself since I won't be able to do as many outdoor activities. 
That would be a challenge. and, 3rd challenge. Watch store. 3rd challenge. Is managing a relationship 
with my current girlfriend? Where are the three places you turn to find support right now? And why? 
I know. I'm a pretty happy person. Replace the shifter night. I guess would be my three children if 
I have a problem, but so far everything is smooth sailing. I'm not dealing with any crisis, 
is at this point. Olympus ideas, what are the three nicest things? That happened to you and your family? 
3 nicest things. I have happened to me and my family. Well, my wife passed away, three and a half 
years ago. So the outpouring from the community. and, Friends. What is probably the nicest thing 
I've ever experienced? I guess, another nice thing would be my oldest daughter getting married. 
She still. Lives in my neighborhood, which is very convenient. My son getting engaged. 
And my middle daughter, having a boy or boyfriend. Now. Wow, can I keep on harping on my wife over 
the past five years? Were the three worst things that happened to you and your family? obviously, 
for me, it would be The death of again, my wife, I guess, my obviously my dad passed away about a 
year-and-a-half ago. So That was something that wasn't pleasant. And then I guess, the third thing 
would be just dealing with this covid and seeing, you know, how many people have passed away. 
Something, you know, and obviously acquaintances people. I used to work with it. The police department. 
Imagine you are 5 years old at, please tell us about the life. You're leading your interest, 
your own life and your work will, I will be working a little part-time security right now when I want to, 
But hopefully, they'll be some grandchildren in my future. And I'll still be going to the gym exercising 
and playing golf being active. Take care of my pool cut, my lawn, take care of the house. 
Are they free Reflections that you have had on This research experience or any parts? 
Particularly challenging or interesting. Do you have any recommendations for us continuing 
this research? Reflections, I don't know, make me thinking about passing of my wife and my father. 
but yeah, I'm fortunate to have a lot of Can children have people around me, their friends? And it's all good.'
<think> <The model thinks step by step and predicts a score for the given transcript> </think>.
Output: {{
    "Re-experiencing": {{
      "Severity Score": 1
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 1
    }}
  }},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'
<think> <The model thinks step by step and predicts a score for the given transcript> </think>.
Output: {{
    "Re-experiencing": {{
      "Severity Score": 4
    }},
    "Avoidance": {{
      "Severity Score": 4
    }},
    "Dysphoria": {{
      "Severity Score": 2
    }},
    "Hyperarousal": {{
      "Severity Score": 4
    }}
  }},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'
<think> <The model thinks step by step and predicts a score for the given transcript> </think>.
Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 1
    }}
  }},

Text: '{text}'

Provide score for the last transcript:
Output: <think>
""",

"ptsd_wo-reasoning_w-subscales_wo-questions_distr_info":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
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

According to domain experts, most individuals typically score 0 or 1 on each subscale. Scores of 2 occur in fewer cases, while 3 or 4 are relatively rare and typically indicate more severe or clinically significant symptom expression.
You should take this distribution into account when making your severity judgments. Use higher scores only when there is clear textual evidence of substantial psychological distress or impairment.

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

"ptsd_wo-reasoning_w-subscales_wo-questions_tsbs_distr_info":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
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

According to domain experts, most individuals typically score 0 or 1 on each subscale. Scores of 2 occur in fewer cases, while 3 or 4 are relatively rare and typically indicate more severe or clinically significant symptom expression.
You should take this distribution into account when making your severity judgments. Use higher scores only when there is clear textual evidence of substantial psychological distress or impairment.

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

"ptsd_wo-reasoning_w-subscales_wo-questions_fs_alt":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
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

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 0
    }}
  }},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 4
    }},
    "Avoidance": {{
      "Severity Score": 4
    }},
    "Dysphoria": {{
      "Severity Score": 2
    }},
    "Hyperarousal": {{
      "Severity Score": 4
    }}
  }},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 1
    }}
  }},

Text: '{text}'

Output:
""",

"ptsd_wo-reasoning_w-subscales_wo-questions_base_alt_fs":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
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
PTSD Severity Scores:
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

Here are a few examples of text-scores pairs in order to introduce you to the task:

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 0
    }}
  }},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 4
    }},
    "Avoidance": {{
      "Severity Score": 4
    }},
    "Dysphoria": {{
      "Severity Score": 2
    }},
    "Hyperarousal": {{
      "Severity Score": 4
    }}
  }},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 1
    }}
  }},


Text: '{text}',

Assign a severity score for each subfactor (between 0 and 4). Reply with the scores only.
Output:
""",


"ptsd_wo-reasoning_w-subscales_wo-questions_fs_alt_tsbs":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
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
<think> <The model thinks step by step and predicts a score for the given transcript> </think>.
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

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'
<think> <The model thinks step by step and predicts a score for the given transcript> </think>.
Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 0
    }}
  }},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'
<think> <The model thinks step by step and predicts a score for the given transcript> </think>.
Output: {{
    "Re-experiencing": {{
      "Severity Score": 4
    }},
    "Avoidance": {{
      "Severity Score": 4
    }},
    "Dysphoria": {{
      "Severity Score": 2
    }},
    "Hyperarousal": {{
      "Severity Score": 4
    }}
  }},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'
<think> <The model thinks step by step and predicts a score for the given transcript> </think>.
Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 1
    }}
  }},

Text: '{text}'

Provide score for the last transcript:
Output: <think>
""",

"ptsd_wo-reasoning_w-subscales_wo-questions_direct": """
Your task is to conduct an in-depth analysis of a provided transcript, with the goal of estimating the overall severity of post-traumatic stress disorder (PTSD) symptoms experienced by the individual.

The text you will analyze is a transcription of the patient's spoken answers to a set of 15 self-recorded questions. The patients are questioned about their lives after the World Trade Center disaster that happened on 9/11. These questions were designed to assess various aspects of psychological well-being, particularly symptoms associated with PTSD. The goal is to assess the overall PTSD severity related to World Trade Center disaster.

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
  "PTSD_Score": 
}}

Text: {text}
""",

"ptsd_w-reasoning_wo-subscales_wo-questions_fs_alt": """Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
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

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 0
    }}
  }},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 4
    }},
    "Avoidance": {{
      "Severity Score": 4
    }},
    "Dysphoria": {{
      "Severity Score": 2
    }},
    "Hyperarousal": {{
      "Severity Score": 4
    }}
  }},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 1
    }}
  }},

Text: '{text}'

Output:
""",

"ptsd_w-reasoning_w-subscales_w-questions_phase-1_fs_alt":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
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

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 0
    }}
  }},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 4
    }},
    "Avoidance": {{
      "Severity Score": 4
    }},
    "Dysphoria": {{
      "Severity Score": 2
    }},
    "Hyperarousal": {{
      "Severity Score": 4
    }}
  }},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 1
    }}
  }},

Text: '{text}'

Output:
""",

"ptsd_w-reasoning_w-subscales_w-questions_phase-2_fs_alt":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
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

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 0
    }}
  }},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 4
    }},
    "Avoidance": {{
      "Severity Score": 4
    }},
    "Dysphoria": {{
      "Severity Score": 2
    }},
    "Hyperarousal": {{
      "Severity Score": 4
    }}
  }},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 1
    }}
  }},

Text: '{text}'

Output:
""",

"ptsd_w-reasoning_w-subscales_w-questions_phase-3_fs_alt":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
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

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 0
    }}
  }},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 4
    }},
    "Avoidance": {{
      "Severity Score": 4
    }},
    "Dysphoria": {{
      "Severity Score": 2
    }},
    "Hyperarousal": {{
      "Severity Score": 4
    }}
  }},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 1
    }}
  }},

Text: '{text}'

Output:
""",

"ptsd_wo-reasoning_wo-subscales_wo-questions_fs_alt":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
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

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 0
    }}
  }},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 4
    }},
    "Avoidance": {{
      "Severity Score": 4
    }},
    "Dysphoria": {{
      "Severity Score": 2
    }},
    "Hyperarousal": {{
      "Severity Score": 4
    }}
  }},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 1
    }}
  }},

Text: '{text}'
""",

"ptsd_wo-reasoning_wo-subscales_w-questions_phase-1_fs_alt":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
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

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 0
    }}
  }},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 4
    }},
    "Avoidance": {{
      "Severity Score": 4
    }},
    "Dysphoria": {{
      "Severity Score": 2
    }},
    "Hyperarousal": {{
      "Severity Score": 4
    }}
  }},

Text: '{text}'
""",

"ptsd_wo-reasoning_wo-subscales_w-questions_phase-2_fs_alt":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
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

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 0
    }}
  }},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 4
    }},
    "Avoidance": {{
      "Severity Score": 4
    }},
    "Dysphoria": {{
      "Severity Score": 2
    }},
    "Hyperarousal": {{
      "Severity Score": 4
    }}
  }},

Text: '{text}'
""",

"ptsd_wo-reasoning_wo-subscales_w-questions_phase-3_fs_alt":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
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

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 0
    }}
  }},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 4
    }},
    "Avoidance": {{
      "Severity Score": 4
    }},
    "Dysphoria": {{
      "Severity Score": 2
    }},
    "Hyperarousal": {{
      "Severity Score": 4
    }}
  }},

Text: '{text}'
""",

"ptsd_direct": """Your task is to conduct an in-depth analysis of a provided transcript, with the goal of estimating the overall severity of post-traumatic stress disorder (PTSD) symptoms experienced by the individual.

The text you will analyze is a transcription of the patient's spoken answers to a predefined set of self-recorded questions. The patients are questioned about their lives after the World Trade Center disaster that happened on 9/11. These questions were designed to assess various aspects of psychological well-being, particularly symptoms associated with PTSD. The goal is to assess the overall PTSD severity related to World Trade Center disaster.

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual related to World Trade Center disaster.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Text: {text}

""",

"ptsd_direct_fs_alt": """Your task is to conduct an in-depth analysis of a provided transcript, with the goal of estimating the overall severity of post-traumatic stress disorder (PTSD) symptoms experienced by the individual.

The text you will analyze is a transcription of the patient's spoken answers to a predefined set of self-recorded questions. These questions were designed to assess various aspects of psychological well-being, particularly symptoms associated with PTSD.

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

{{
'PTSD_Score': 17
}},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

{{
'PTSD_Score': 75
}},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

{{
'PTSD_Score': 22
}},

Text: {text}

""",

"ptsd_wo-reasoning_w-subscales_wo-questions_distr_info_fs_alt":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
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

According to domain experts, most individuals typically score 0 or 1 on each subscale. Scores of 2 occur in fewer cases, while 3 or 4 are relatively rare and typically indicate more severe or clinically significant symptom expression.
You should take this distribution into account when making your severity judgments. Use higher scores only when there is clear textual evidence of substantial psychological distress or impairment.

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

  Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 0
    }}
  }},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 4
    }},
    "Avoidance": {{
      "Severity Score": 4
    }},
    "Dysphoria": {{
      "Severity Score": 2
    }},
    "Hyperarousal": {{
      "Severity Score": 4
    }}
  }},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 1
    }}
  }},

Text: '{text}'
""",

"ptsd_wo-reasoning_w-subscales_wo-questions_distr_info_fs":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
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

According to domain experts, most individuals typically score 0 or 1 on each subscale. Scores of 2 occur in fewer cases, while 3 or 4 are relatively rare and typically indicate more severe or clinically significant symptom expression.
You should take this distribution into account when making your severity judgments. Use higher scores only when there is clear textual evidence of substantial psychological distress or impairment.

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

  Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 0
    }}
  }},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 4
    }},
    "Avoidance": {{
      "Severity Score": 4
    }},
    "Dysphoria": {{
      "Severity Score": 2
    }},
    "Hyperarousal": {{
      "Severity Score": 4
    }}
  }},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 1
    }}
  }},

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 4
    }},
    "Avoidance": {{
      "Severity Score": 4
    }},
    "Dysphoria": {{
      "Severity Score": 2
    }},
    "Hyperarousal": {{
      "Severity Score": 4
    }}
  }},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 1
    }}
  }},

Text: '{text}'
""",

"ptsd_direct_w_17_items": """Your task is to conduct an in-depth analysis of a provided transcript, with the goal of estimating the overall severity of post-traumatic stress disorder (PTSD) symptoms experienced by the individual.

The text you will analyze is a transcription of the patient's spoken answers to a predefined set of self-recorded questions. These questions were designed to assess various aspects of psychological well-being, particularly symptoms associated with PTSD. The goal is to assess the overall PTSD severity.

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.
The PCL score is calculated based on 17 specific items, each representing a symptom commonly associated with PTSD. The total score ranges from 17 to 85.

The 17 items are:
	1.	Repeated, disturbing memories, thoughts, or images of a stressful experience from the past
	2.	Repeated, disturbing dreams of a stressful experience from the past
	3.	Suddenly acting or feeling as if a stressful experience were happening again (as if you were reliving it)
	4.	Feeling very upset when something reminded you of a stressful experience from the past
	5.	Having physical reactions (e.g., heart pounding, trouble breathing, or sweating) when something reminded you of a stressful experience from the past
	6.	Avoiding thinking about or talking about a stressful experience from the past, or avoiding having feelings related to it
	7.	Avoiding activities or situations because they reminded you of a stressful experience from the past
	8.	Trouble remembering important parts of a stressful experience from the past
	9.	Loss of interest in things that you used to enjoy
	10.	Feeling distant or cut off from other people
	11.	Feeling emotionally numb or being unable to have loving feelings for those close to you
	12.	Feeling as if your future will somehow be cut short
	13.	Trouble falling or staying asleep
	14.	Feeling irritable or having angry outbursts
	15.	Having difficulty concentrating
	16.	Being “super alert” or watchful on guard
	17.	Feeling jumpy or easily startled

When assigning a total PCL score, consider how the individual’s statements may implicitly or explicitly reflect the presence or severity of these symptoms.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.
Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Text: {text}

""",

"ptsd_direct_w_subscales": """Your task is to conduct an in-depth analysis of a provided transcript, with the goal of estimating the overall severity of post-traumatic stress disorder (PTSD) symptoms experienced by the individual.

The text you will analyze is a transcription of the patient's spoken answers to a predefined set of self-recorded questions. These questions were designed to assess various aspects of psychological well-being, particularly symptoms associated with PTSD. The goal is to assess the overall PTSD severity.

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity. The PCL score is calculated based on self-reported answers to questions revolving around 4 subscales:
Re-experiencing: Intrusive thoughts, flashbacks, nightmares, or distress when reminded of the trauma.
Avoidance: Efforts to avoid thoughts, feelings, or external reminders associated with the trauma.
Dysphoria: Persistent negative thoughts, feelings of guilt, emotional numbness, or loss of interest in activities.
Hyperarousal: Increased irritability, hypervigilance, being easily startled, or difficulty concentrating and sleeping.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Text: {text}

""",

"ptsd_direct_w_subscales": """Your task is to conduct an in-depth analysis of a provided transcript, with the goal of estimating the overall severity of post-traumatic stress disorder (PTSD) symptoms experienced by the individual.

The text you will analyze is a transcription of the patient's spoken answers to a predefined set of self-recorded questions. These questions were designed to assess various aspects of psychological well-being, particularly symptoms associated with PTSD. The goal is to assess the overall PTSD severity.

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity. The PCL score is calculated based on self-reported answers to questions revolving around 4 subscales:
Re-experiencing: Intrusive thoughts, flashbacks, nightmares, or distress when reminded of the trauma.
Avoidance: Efforts to avoid thoughts, feelings, or external reminders associated with the trauma.
Dysphoria: Persistent negative thoughts, feelings of guilt, emotional numbness, or loss of interest in activities.
Hyperarousal: Increased irritability, hypervigilance, being easily startled, or difficulty concentrating and sleeping.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Text: {text}

""",

"ptsd_direct_w_evidence": """Your task is to conduct an in-depth analysis of a provided transcript, with the goal of estimating the overall severity of post-traumatic stress disorder (PTSD) symptoms experienced by the individual.

The text you will analyze is a transcription of the patient's spoken answers to a predefined set of self-recorded questions. These questions were designed to assess various aspects of psychological well-being, particularly symptoms associated with PTSD. The goal is to assess the overall PTSD severity.

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual and provide a clear explanation about the score you assigned. Ensure that the explanation references relevant text spans or contextual inferences to justify the assigned score.

Output Format

Return your answer in the following structured JSON format:

{{
'Reason': ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
'PTSD_Score':
}}

Text: {text}

""",

"ptsd_direct_w-questions_phase-1":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. How are you? Can you elaborate?
2. How's the family? Can you elaborate?
3. What's new? Can you elaborate?
4. What else?
5. Over the past 5 years what are the three nicest things that happened to you and your family? Can you elaborate?
6. Over the past 5 years what are the three worst things that happened to you and your family? Can you elaborate?
7. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Text: '{text}'
""",

"ptsd_direct_w-questions_phase-2":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. What are the three things in your life that you look forward to the most right now? Can you elaborate?
2. What are the three biggest challenges that you are managing in your life right now? Can you elaborate?
3. Where are three places that you turn to find support right now and why? Can you elaborate?
4. Over the past 5 years, what are the three nicest things that happened to you and your family? Can you elaborate?
5. Over the past 5 years, what are the worst three things that have happened to you and your family? Can you elaborate?
6. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?
7. What are three reflections that you have on this research experience? Were any parts particularly challenging or interesting? Do you have any recommendations for us continuing this research?

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Text: '{text}'
""",

"ptsd_direct_w-questions_phase-3":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
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

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Text: '{text}'
""",

"ptsd_direct_all_phase-1":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. How are you? Can you elaborate?
2. How's the family? Can you elaborate?
3. What's new? Can you elaborate?
4. What else?
5. Over the past 5 years what are the three nicest things that happened to you and your family? Can you elaborate?
6. Over the past 5 years what are the three worst things that happened to you and your family? Can you elaborate?
7. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Text: '{text}'
""",

"ptsd_direct_all_phase-2":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. What are the three things in your life that you look forward to the most right now? Can you elaborate?
2. What are the three biggest challenges that you are managing in your life right now? Can you elaborate?
3. Where are three places that you turn to find support right now and why? Can you elaborate?
4. Over the past 5 years, what are the three nicest things that happened to you and your family? Can you elaborate?
5. Over the past 5 years, what are the worst three things that have happened to you and your family? Can you elaborate?
6. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?
7. What are three reflections that you have on this research experience? Were any parts particularly challenging or interesting? Do you have any recommendations for us continuing this research?

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Text: '{text}'
""",

"ptsd_direct_all_phase-3":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
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

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Text: '{text}'
""",

"ptsd_wo-reasoning_wo-subscales_wo-questions_w_911":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions. The patients are questioned about their lives after the World Trade Center disaster that happened on 9/11. These questions were designed to assess various aspects of psychological well-being, particularly symptoms associated with PTSD. The goal is to assess the overall PTSD severity related to World Trade Center disaster. 
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
STEP 1: Detect the PTSD subfactors in the text and provide a score between 0 and 4 for each subfactor reflecting the overall PTSD severity of the individual related to World Trade Center disaster.

To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity) that best reflects the overall PTSD severity of the individual related to World Trade Center disaster.
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

"ptsd_wo-reasoning_wo-subscales_wo-questions_w_17_items":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing, Avoidance, Dysphoria, Hyperarousal.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

The PCL score is calculated based on 17 specific items, each representing a symptom commonly associated with PTSD.

The 17 items are:
	1.	Repeated, disturbing memories, thoughts, or images of a stressful experience from the past
	2.	Repeated, disturbing dreams of a stressful experience from the past
	3.	Suddenly acting or feeling as if a stressful experience were happening again (as if you were reliving it)
	4.	Feeling very upset when something reminded you of a stressful experience from the past
	5.	Having physical reactions (e.g., heart pounding, trouble breathing, or sweating) when something reminded you of a stressful experience from the past
	6.	Avoiding thinking about or talking about a stressful experience from the past, or avoiding having feelings related to it
	7.	Avoiding activities or situations because they reminded you of a stressful experience from the past
	8.	Trouble remembering important parts of a stressful experience from the past
	9.	Loss of interest in things that you used to enjoy
	10.	Feeling distant or cut off from other people
	11.	Feeling emotionally numb or being unable to have loving feelings for those close to you
	12.	Feeling as if your future will somehow be cut short
	13.	Trouble falling or staying asleep
	14.	Feeling irritable or having angry outbursts
	15.	Having difficulty concentrating
	16.	Being “super alert” or watchful on guard
	17.	Feeling jumpy or easily startled

When assigning a severity score for each of the four subscales, consider how the individual’s statements may implicitly or explicitly reflect the presence or severity of these symptoms.

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

"ptsd_direct_fs_alt_w_911": """Your task is to conduct an in-depth analysis of a provided transcript, with the goal of estimating the overall severity of post-traumatic stress disorder (PTSD) symptoms experienced by the individual.

The text you will analyze is a transcription of the patient's spoken answers to a predefined set of self-recorded questions. The patients are questioned about their lives after the World Trade Center disaster that happened on 9/11. These questions were designed to assess various aspects of psychological well-being, particularly symptoms associated with PTSD. The goal is to assess the overall PTSD severity related to World Trade Center disaster.

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual related to World Trade Center disaster.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

{{
'PTSD_Score': 17
}},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

{{
'PTSD_Score': 75
}},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

{{
'PTSD_Score': 22
}},

Text: {text}

""",

"ptsd_direct_fs_alt_w_17_items": """Your task is to conduct an in-depth analysis of a provided transcript, with the goal of estimating the overall severity of post-traumatic stress disorder (PTSD) symptoms experienced by the individual.

The text you will analyze is a transcription of the patient's spoken answers to a predefined set of self-recorded questions. These questions were designed to assess various aspects of psychological well-being, particularly symptoms associated with PTSD.

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.
The PCL score is calculated based on 17 specific items, each representing a symptom commonly associated with PTSD. The total score ranges from 17 to 85.

The 17 items are:
	1.	Repeated, disturbing memories, thoughts, or images of a stressful experience from the past
	2.	Repeated, disturbing dreams of a stressful experience from the past
	3.	Suddenly acting or feeling as if a stressful experience were happening again (as if you were reliving it)
	4.	Feeling very upset when something reminded you of a stressful experience from the past
	5.	Having physical reactions (e.g., heart pounding, trouble breathing, or sweating) when something reminded you of a stressful experience from the past
	6.	Avoiding thinking about or talking about a stressful experience from the past, or avoiding having feelings related to it
	7.	Avoiding activities or situations because they reminded you of a stressful experience from the past
	8.	Trouble remembering important parts of a stressful experience from the past
	9.	Loss of interest in things that you used to enjoy
	10.	Feeling distant or cut off from other people
	11.	Feeling emotionally numb or being unable to have loving feelings for those close to you
	12.	Feeling as if your future will somehow be cut short
	13.	Trouble falling or staying asleep
	14.	Feeling irritable or having angry outbursts
	15.	Having difficulty concentrating
	16.	Being “super alert” or watchful on guard
	17.	Feeling jumpy or easily startled

When assigning a total PCL score, consider how the individual’s statements may implicitly or explicitly reflect the presence or severity of these symptoms.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

{{
'PTSD_Score': 17
}},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

{{
'PTSD_Score': 75
}},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

{{
'PTSD_Score': 22
}},

Analyze the following transcript.
Text: {text}

""",

"ptsd_direct_fs_alt_w_evidence": """Your task is to conduct an in-depth analysis of a provided transcript, with the goal of estimating the overall severity of post-traumatic stress disorder (PTSD) symptoms experienced by the individual.

The text you will analyze is a transcription of the patient's spoken answers to a predefined set of self-recorded questions. These questions were designed to assess various aspects of psychological well-being, particularly symptoms associated with PTSD. The goal is to assess the overall PTSD severity.

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual and provide a clear explanation about the score you assigned. Ensure that the explanation references relevant text spans or contextual inferences to justify the assigned score.

Output Format

Return your answer in the following structured JSON format:

{{
'Reason': ["<Reason(s) based on explicit or paraphrased evidence from the text>"],
'PTSD_Score':
}}

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

{{
'Reason': ["<Reason(s) based on explicit or paraphrased evidence from the text>"]
'PTSD_Score': 17
}},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

{{
'Reason': ["<Reason(s) based on explicit or paraphrased evidence from the text>"]
'PTSD_Score': 75
}},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

{{
'Reason': ["<Reason(s) based on explicit or paraphrased evidence from the text>"]
'PTSD_Score': 22
}},

Analyze the following transcript
Text: {text}

""",

"ptsd_direct_fs_alt_w_subscales": """Your task is to conduct an in-depth analysis of a provided transcript, with the goal of estimating the overall severity of post-traumatic stress disorder (PTSD) symptoms experienced by the individual.

The text you will analyze is a transcription of the patient's spoken answers to a predefined set of self-recorded questions. These questions were designed to assess various aspects of psychological well-being, particularly symptoms associated with PTSD.

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity. The PCL score is calculated based on self-reported answers to questions revolving around 4 subscales:
Re-experiencing: Intrusive thoughts, flashbacks, nightmares, or distress when reminded of the trauma.
Avoidance: Efforts to avoid thoughts, feelings, or external reminders associated with the trauma.
Dysphoria: Persistent negative thoughts, feelings of guilt, emotional numbness, or loss of interest in activities.
Hyperarousal: Increased irritability, hypervigilance, being easily startled, or difficulty concentrating and sleeping.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

{{
'PTSD_Score': 17
}},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

{{
'PTSD_Score': 75
}},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

{{
'PTSD_Score': 22
}},

Text: {text}

""",

"ptsd_direct_fs_alt_w-questions_phase-1":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. How are you? Can you elaborate?
2. How's the family? Can you elaborate?
3. What's new? Can you elaborate?
4. What else?
5. Over the past 5 years what are the three nicest things that happened to you and your family? Can you elaborate?
6. Over the past 5 years what are the three worst things that happened to you and your family? Can you elaborate?
7. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

{{
'PTSD_Score': 17
}},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

{{
'PTSD_Score': 75
}},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

{{
'PTSD_Score': 22
}}.

Analyze the following transcript.
Text: '{text}'
""",

"ptsd_direct_fs_alt_w-questions_phase-2":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. What are the three things in your life that you look forward to the most right now? Can you elaborate?
2. What are the three biggest challenges that you are managing in your life right now? Can you elaborate?
3. Where are three places that you turn to find support right now and why? Can you elaborate?
4. Over the past 5 years, what are the three nicest things that happened to you and your family? Can you elaborate?
5. Over the past 5 years, what are the worst three things that have happened to you and your family? Can you elaborate?
6. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?
7. What are three reflections that you have on this research experience? Were any parts particularly challenging or interesting? Do you have any recommendations for us continuing this research?

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

{{
'PTSD_Score': 17
}},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

{{
'PTSD_Score': 75
}},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

{{
'PTSD_Score': 22
}}.

Analyze the following transcript.

Text: '{text}'
""",

"ptsd_direct_fs_alt_w-questions_phase-3":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
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

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

{{
'PTSD_Score': 17
}},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

{{
'PTSD_Score': 75
}},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

{{
'PTSD_Score': 22
}}.

Analyze the following transcript.

Text: '{text}'
""",

"ptsd_wo-reasoning_wo-subscales_wo-questions_w_911_fs_alt":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions. The patients are questioned about their lives after the World Trade Center disaster that happened on 9/11. These questions were designed to assess various aspects of psychological well-being, particularly symptoms associated with PTSD. The goal is to assess the overall PTSD severity related to World Trade Center disaster. 
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
STEP 1: Detect the PTSD subfactors in the text and provide a score between 0 and 4 for each subfactor reflecting the overall PTSD severity of the individual related to World Trade Center disaster.

To ensure clarity and easy readability, format your output into a nested JSON. Each value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
Severity Score: The assigned severity score for the subfactor, ranging from 0 (not at all severe) to 4 (extreme severity) that best reflects the overall PTSD severity of the individual related to World Trade Center disaster.
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

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'
<think> <The model thinks step by step and predicts a score for the given transcript> </think>.
Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 0
    }}
  }},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'
<think> <The model thinks step by step and predicts a score for the given transcript> </think>.
Output: {{
    "Re-experiencing": {{
      "Severity Score": 4
    }},
    "Avoidance": {{
      "Severity Score": 4
    }},
    "Dysphoria": {{
      "Severity Score": 2
    }},
    "Hyperarousal": {{
      "Severity Score": 4
    }}
  }},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'
<think> <The model thinks step by step and predicts a score for the given transcript> </think>.
Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 1
    }}
  }},

Text: '{text}'
""",

"ptsd_wo-reasoning_wo-subscales_wo-questions_w_17_items_fs_alt":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms. 
Using the content of these transcriptions, you will predict a severity score for the following four PTSD subscales:
Re-experiencing, Avoidance, Dysphoria, Hyperarousal.

Scoring System
Assign a severity score for each subscale based on the intensity and impact of the symptoms described in the text:
0 (Not at all severe): The symptom is not present or negligible.
1 (Low severity): The symptom is present but slightly impacts the individual.
2 (Moderate severity): The symptom is noticeably present and moderately impacts the individual.
3 (High severity): The symptom is significantly present and strongly impacts the individual.
4 (Extreme severity): The symptom is overwhelmingly present and has a profound impact on the individual.

The PCL score is calculated based on 17 specific items, each representing a symptom commonly associated with PTSD.

The 17 items are:
	1.	Repeated, disturbing memories, thoughts, or images of a stressful experience from the past
	2.	Repeated, disturbing dreams of a stressful experience from the past
	3.	Suddenly acting or feeling as if a stressful experience were happening again (as if you were reliving it)
	4.	Feeling very upset when something reminded you of a stressful experience from the past
	5.	Having physical reactions (e.g., heart pounding, trouble breathing, or sweating) when something reminded you of a stressful experience from the past
	6.	Avoiding thinking about or talking about a stressful experience from the past, or avoiding having feelings related to it
	7.	Avoiding activities or situations because they reminded you of a stressful experience from the past
	8.	Trouble remembering important parts of a stressful experience from the past
	9.	Loss of interest in things that you used to enjoy
	10.	Feeling distant or cut off from other people
	11.	Feeling emotionally numb or being unable to have loving feelings for those close to you
	12.	Feeling as if your future will somehow be cut short
	13.	Trouble falling or staying asleep
	14.	Feeling irritable or having angry outbursts
	15.	Having difficulty concentrating
	16.	Being “super alert” or watchful on guard
	17.	Feeling jumpy or easily startled

When assigning a severity score for each of the four subscales, consider how the individual’s statements may implicitly or explicitly reflect the presence or severity of these symptoms.

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

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'
<think> <The model thinks step by step and predicts a score for the given transcript> </think>.
Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 0
    }}
  }},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'
<think> <The model thinks step by step and predicts a score for the given transcript> </think>.
Output: {{
    "Re-experiencing": {{
      "Severity Score": 4
    }},
    "Avoidance": {{
      "Severity Score": 4
    }},
    "Dysphoria": {{
      "Severity Score": 2
    }},
    "Hyperarousal": {{
      "Severity Score": 4
    }}
  }},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'
<think> <The model thinks step by step and predicts a score for the given transcript> </think>.
Output: {{
    "Re-experiencing": {{
      "Severity Score": 0
    }},
    "Avoidance": {{
      "Severity Score": 0
    }},
    "Dysphoria": {{
      "Severity Score": 0
    }},
    "Hyperarousal": {{
      "Severity Score": 1
    }}
  }},

Text: '{text}'
""",

"ptsd_direct_all_phase-1_fs_alt":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. How are you? Can you elaborate?
2. How's the family? Can you elaborate?
3. What's new? Can you elaborate?
4. What else?
5. Over the past 5 years what are the three nicest things that happened to you and your family? Can you elaborate?
6. Over the past 5 years what are the three worst things that happened to you and your family? Can you elaborate?
7. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

{{
'PTSD_Score': 17
}},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

{{
'PTSD_Score': 75
}},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

{{
'PTSD_Score': 22
}}.

Analyze the following transcript.

Text: '{text}'
""",

"ptsd_direct_all_phase-2_fs_alt":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 7 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
They answered the following set of questions:

1. What are the three things in your life that you look forward to the most right now? Can you elaborate?
2. What are the three biggest challenges that you are managing in your life right now? Can you elaborate?
3. Where are three places that you turn to find support right now and why? Can you elaborate?
4. Over the past 5 years, what are the three nicest things that happened to you and your family? Can you elaborate?
5. Over the past 5 years, what are the worst three things that have happened to you and your family? Can you elaborate?
6. Imagine you are 5 years older. Please tell us about the life you are leading, your interests, your home life, and your work. Can you elaborate?
7. What are three reflections that you have on this research experience? Were any parts particularly challenging or interesting? Do you have any recommendations for us continuing this research?

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

{{
'PTSD_Score': 17
}},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

{{
'PTSD_Score': 75
}},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

{{
'PTSD_Score': 22
}}.

Analyze the following transcript.

Text: '{text}'
""",

"ptsd_direct_all_phase-3_fs_alt":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of assessing the severity of PTSD symptoms based on its 4 subscales. The text you will analyze is the transcription of the patient’s self-recorded answers to a set of 15 questions, which were designed to assess various aspects of psychological well-being, including PTSD-related symptoms.
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

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

{{
'PTSD_Score': 17
}},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

{{
'PTSD_Score': 75
}},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

{{
'PTSD_Score': 22
}}.

Analyze the following transcript.

Text: '{text}'
""",

"ptsd_direct_distr_info":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of estimating the overall severity of post-traumatic stress disorder (PTSD) symptoms experienced by the individual.

The text you will analyze is a transcription of the patient's spoken answers to a predefined set of self-recorded questions. These questions were designed to assess various aspects of psychological well-being, particularly symptoms associated with PTSD.

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

According to domain experts, most individuals typically score between 17 and 30. Scores between 30 and 50 occur in fewer cases, while above 50 are relatively rare and typically indicate more severe or clinically significant symptom expression.
You should take this distribution into account when making your severity judgments. Use higher scores only when there is clear textual evidence of substantial psychological distress or impairment.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Text: '{text}'
""",

"ptsd_direct_distr_info_fs_alt":"""Your task is to conduct an in-depth analysis of a provided transcript, with the goal of estimating the overall severity of post-traumatic stress disorder (PTSD) symptoms experienced by the individual.

The text you will analyze is a transcription of the patient's spoken answers to a predefined set of self-recorded questions. These questions were designed to assess various aspects of psychological well-being, particularly symptoms associated with PTSD.

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

According to domain experts, most individuals typically score between 17 and 30. Scores between 30 and 50 occur in fewer cases, while above 50 are relatively rare and typically indicate more severe or clinically significant symptom expression.
You should take this distribution into account when making your severity judgments. Use higher scores only when there is clear textual evidence of substantial psychological distress or impairment.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Below are illustrative input-output pairs demonstrating how to analyze and score PTSD severity across different levels: low, moderate, and high. These examples are provided to help guide your reasoning process and calibrate your scoring decisions.
Before generating severity scores for the provided transcript, carefully study the semantics and structure of each example. Pay close attention to how specific language patterns, symptom descriptions, and narrative cues are mapped to subscale scores.
Use these examples as reference points to ensure consistency, accuracy, and alignment with the intended scoring guidelines when evaluating new transcripts.

Text: 'Spending time with my children. Time off from work.  And enjoying boating.  3 biggest challenges in my life.  Would be.  figuring out when  would be a good time to retire. 
ensuring that I have enough money saved, for retirement, and ensuring I'm able to  Secure my children's future financially.  I tend to turn to my wife for support, as well as other friends and family members. 
Nicest things, that happened to myself and my family are our annual vacations.  My son's graduation and my daughter starting College.  The worst things that happened over the past five years,
are the death of my father-in-law just about a year-and-a-half ago.  other than that,  I can't say the word, any of the other things that were that bad  in five years, I anticipate to be retired. 
My interest would be spending time with my wife. Perhaps I taking up Golf and fulfilling other hobbies that I weren't wasn't able to do. While I was working  all the covid pandemic has  Changed my life in the,
in the way that I had to be concerned. For my wife's Health, she had covid 3 times. So I was really basically concerned about her and when my father-in-law had been sick, I was in the hospital.
We were unable to see him when he passed away.  The most difficult thing about the covid. Pandemic is just ensuring that my family is healthy and caring for my wife when she had been sick with covid. 
After covid, pandemic, the kelp, the covid can they make is over, I would look be. Looking forward to just returning to normal normal life situations.  911 head.  An immediate impact on my life. But over the past, 
Two decades. Cannot say it impacted my life directly.  911 does not really affect me now.  I guess I would like to Generations, just not to forget.  The occurrences.  Other things that happened on 9/11. 
Not really.  I don't have any recommendations. I don't have any recommendations.'

{{
'PTSD_Score': 17
}},

Text: '3 biggest things. I managed today is stress. And stress and stress. The three things. I turned to right now,
places you turn to support it is right now, is I deal with through 911. They helped me a lot. I deal with this guy dr.jay,
who's just put on 101 and brings me back to Earth and helps me close. My Pandora boxes. The other thing is family.
I use family for support group and they helped guide me. And then the last thing is, I find exercising reduces stress and helps me.
Come back to reality. You know, five years. I'll be 65. That's a million-dollar question. Hopefully, I'll be retired
and I pray every time. Why the type A personality? Can I shut down? I don't. Yes, three big things to manage his stress.
I have a high. Profile job. I managed to borough of Queens and it's trash. 24/7. I managed the 9/11 what I saw in that
keeps opening up Pandora's Box, and then the last thing is what happened to me in my childhood. Oh shit. I got a around,
someone else operate again. So the three things that his Doctor Dre, helps me deal with stuff and he helps me close Pandora's Box,
because I have a high-profile job and I type A personality. My stress level is high. I also had a rough life growing up and you
put all that into a Melting Pot and it spoils over and what helps me. Also, his family. I have a strong support family,
that is very crucial to my life. And then, the third thing is, I Fitness, I find Fitness helps me cope. Over the past five years.
Family, is, I am now a grandfather like kids have a grandchild, grandpa. I see the baby. She lives 4 miles from the house.
I helped her with the house, and they are always over the house. And that grandchild has now become an intricate part of our family,
My kids are successful. They're doing well and they have part of it in my wife we could and it's just definitely bonded together
and a close family. We do we spend all our time together. Health. Family. And the Bible. Yes, three things that I'm looking.
Elaborate is my help, my family, that they been good. And that's spiritually. I'm in a good place.
The three worst things over the past five years, would be when you lose someone close to you, that dies.
The biggest impact would be my wife's mother and father. They were very close to us. We looked after them and we were very intricate.
The other thing I'm fining, you know, I'll be 60 years old this year, and I'm seeing a lot of 911 guys, die. Can't talk about it.'

{{
'PTSD_Score': 75
}},

Text: '3 things that I look forward to the most right now or be with my son. Providing for my family and, Fun activities with my family and friends.
the three biggest challenges that I'm managing in my life right now, or Like my job in my career. My son and his school work. And just regular family obligations.
Free places that I turn to find support right now or my family. My friends. Maybe a trusted co-worker. 3 nicest, things that have happened to me and my family over the past five years. We moved into a brand new house.
We started a family of chickens and maybe going on some nice vacations. 3, worst things that happened. One of the worst things was getting stuck in between houses.
Due to delays in the new house, being built and then combined with slow down from covid. That's probably the worst thing that has happened. I don't know that there's been three.
I'm craving a question. 3 reflections. I don't know that any of its particularly challenging other than the will to want to. Share, intimate detail.
I think this is interesting. I don't think I've ever been asked to do a test like this before where I wouldn't just respond via typing that
someone would record my reactions and how he speak.'

{{
'PTSD_Score': 22
}}.

Analyze the following transcript.

Text: '{text}'
""",

"ptsd_direct_w_subscales_and_evidence_and_phq9": """Your task is to conduct an in-depth analysis of a provided transcript, with the goal of estimating the overall severity of post-traumatic stress disorder (PTSD) symptoms experienced by the individual.

The text you will analyze is a transcription of the patient's spoken answers to a predefined set of self-recorded questions. These questions were designed to assess various aspects of psychological well-being, particularly symptoms associated with PTSD. The goal is to assess the overall PTSD severity.

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity. The PCL score is calculated based on self-reported answers to questions revolving around 4 subscales:
Re-experiencing: Intrusive thoughts, flashbacks, nightmares, or distress when reminded of the trauma.
Avoidance: Efforts to avoid thoughts, feelings, or external reminders associated with the trauma.
Dysphoria: Persistent negative thoughts, feelings of guilt, emotional numbness, or loss of interest in activities.
Hyperarousal: Increased irritability, hypervigilance, being easily startled, or difficulty concentrating and sleeping.

Moreover, the second task is to predict speaker's depression severity (it includes symptoms of low interest or pleasure, depression or hopelessness, insomnia or hypersomnia, fatigue or low energy, poor appetite or overeating, feelings of guilt trouble concentrating, moving/speaking slowly or agitation, and thoughts of death or suicide) rated between 0 and 27, where 0 is no symptoms and 27 is extreme symptoms.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual. Then assign a single integer between 0 and 27, where 0 is no symptoms and 27 is extreme symptoms, that best reflects the depression severity of the individual.

Every field that has a numeric estimate must include a confidence in [0,1,2,3].

Do not add or omit keys. If uncertain, still output a numeric estimate and a lower confidence.

Provide evidence. Evidence should be a short phrase citing the transcript that led you into your prediction.


Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score': {{
      "score": ,
      "confidence": ,
      "evidence":
  }},
  "Depression": {{
      "score": ,
      "confidence": ,
      "evidence":
  }},
}}


Text: {text}

""",

"ptsd_direct_w_911": """Your task is to conduct an in-depth analysis of a provided transcript, with the goal of estimating the overall severity of post-traumatic stress disorder (PTSD) symptoms experienced by the individual.

The text you will analyze is a transcription of the patient's spoken answers to a predefined set of self-recorded questions. The patients are questioned about their lives after the World Trade Center disaster that happened on 9/11. These questions were designed to assess various aspects of psychological well-being, particularly symptoms associated with PTSD. The goal is to assess the overall PTSD severity related to World Trade Center disaster.

Scoring Objective
Based on the content of the transcript, predict a single scalar PTSD severity score in the range 17 to 85, where:

- 17 represents minimal or no PTSD-related symptoms.
- 85 represents extreme PTSD symptom severity across multiple domains of functioning.

This score should directly estimate the patient’s PCL score, a widely used self-report measure of PTSD symptom severity.

Instructions
Carefully analyze the transcript, considering the emotional tone, content, and any references to trauma-related symptoms or functional impairments. Then assign a single integer score between 17 and 85 that best reflects the overall PTSD severity of the individual related to World Trade Center disaster.

Output Format

Return your answer in the following structured JSON format:

{{
'PTSD_Score':
}}

Text: {text}

""",

}

