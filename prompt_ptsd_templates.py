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

To ensure clarity and easy readability, format your output into a nested JSON. The first level should contain the key PTSD_Subfactor_Scores, and its value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
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

To ensure clarity and easy readability, format your output into a nested JSON. The first level should contain the key PTSD_Subfactor_Scores, and its value should be a JSON containing each subfactor (Re-experiencing, Avoidance, Dysphoria, Hyperarousal) as keys. For each subfactor, include:
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
"""

}