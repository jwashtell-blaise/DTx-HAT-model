from utils.mapping import expand_values

category_mapping = expand_values({
    "Symptoms.Anxiety|Behaviour|Avoidance - active|Actively avoiding anxiety-provoking situations": "Symptoms.anxiety|behaviour|avoidance",
    "Symptoms.Anxiety|Behaviour|Avoidance - active|Avoiding problems/everyday activities": "Symptoms.anxiety|behaviour|avoidance",
    "Symptoms.Anxiety|Behaviour|Avoidance - active|Avoiding specific places/people/things": "Symptoms.anxiety|behaviour|avoidance",
    "Symptoms.Anxiety|Behaviour|Avoidance - active|Other_CUSTOM_:struggling to leave the house": ["Symptoms.anxiety|behaviour|avoidance", "Symptoms.mood|physical|reduced_motivation", "Symptoms.mood|behaviour|avoidance|withdrawing"],
    "Symptoms.Anxiety|Behaviour|Safety behaviours|*": "Symptoms.anxiety|behaviour|safety_seeking",
    "Symptoms.Anxiety|Cognition|Thought distortions|Fearing the worst-case scenario of a situation or event": "Symptoms.anxiety|cognition|predicting_the_worst",
    "Symptoms.Anxiety|Cognition|Thought distortions|Other_CUSTOM_*": "Symptoms.mood|cognition|difficult_thoughts",
    "Symptoms.Anxiety|Cognition|Thought distortions|Worries about being unable to cope": "Symptoms.anxiety|cognition|worry",
    "Symptoms.Anxiety|Cognition|Uncertainty|Feelings of uncertainty about what is going to happen next": "Symptoms.anxiety|cognition|predicting_the_worst",
    "Symptoms.Anxiety|Cognition|Uncertainty|Worrying about the future 'what ifs'": "Symptoms.anxiety|cognition|worry",
    "Symptoms.Anxiety|Cognition|Uncertainty|Other_CUSTOM_:intrusive thoughts": "Symptoms.mood|cognition|difficult_thoughts",
    "Symptoms.Anxiety|Cognition|Uncertainty|Other_CUSTOM_:obsessive thoughts": "Symptoms.mood|cognition|difficult_thoughts",
    "Symptoms.Anxiety|Cognition|Uncertainty|Other_CUSTOM_:negative thoughts": "Symptoms.mood|cognition|difficult_thoughts",
    "Symptoms.Anxiety|Cognition|Uncertainty|Other_CUSTOM_*": "Symptoms.anxiety|cognition|worry",
    "Symptoms.Anxiety|Emotionals|Overwhelmed|Distressed and overwhelmed": ["Symptoms.anxiety|emotion|stress", "Symptoms.mood|emotion|overwhelmed"],
    "Symptoms.Anxiety|Emotionals|Overwhelmed|Other_CUSTOM_*": ["Symptoms.anxiety|emotion|stress", "Symptoms.mood|emotion|overwhelmed"],
    "Symptoms.Anxiety|Emotionals|Overwhelmed|'Panicky'": ["Symptoms.anxiety|emotion|stress", "Symptoms.anxiety|physical|sudden_attack_of_symptoms"],
    "Symptoms.Anxiety|Emotionals|Overwhelmed|Procrastinating": "Symptoms.anxiety|emotion|stress",
    "Symptoms.Anxiety|Emotionals|Overwhelmed|Trouble figuring out what to do next": "Symptoms.anxiety|emotion|stress",
    "Symptoms.Anxiety|Emotionals|Unease|Afraid": "Symptoms.anxiety|emotion|fearful",
    "Symptoms.Anxiety|Emotionals|Unease|Apprehensive": "Symptoms.anxiety|emotion|on_edge",
    "Symptoms.Anxiety|Emotionals|Unease|Dread": ["Symptoms.anxiety|emotion|on_edge", "Symptoms.anxiety|emotion|fearful"],
    "Symptoms.Anxiety|Emotionals|Unease|Feeling like something bad is going to happen": ["Symptoms.anxiety|emotion|fearful", "Symptoms.anxiety|cognition|predicting_the_worst"],
    "Symptoms.Anxiety|Emotionals|Unease|On edge": "Symptoms.anxiety|emotion|on_edge",
    "Symptoms.Anxiety|Emotionals|Unease|Other_CUSTOM_:fearful": "Symptoms.anxiety|emotion|fearful",
    "Symptoms.Anxiety|Emotionals|Unease|Other_CUSTOM_*": "Symptoms.anxiety|emotion|on_edge",
    "Symptoms.Anxiety|Physical symptoms|Cardiac|A fast, thumping or irregular heartbeat": "Symptoms.anxiety|physical|sudden_attack_of_symptoms",
    "Symptoms.Anxiety|Physical symptoms|Cardiac|Feeling nervous, restless or tense": "Symptoms.anxiety|emotion|on_edge",
    "Symptoms.Anxiety|Physical symptoms|Cardiac|Having a sense of impending danger, panic or doom": "Symptoms.anxiety|emotion|fearful",
    "Symptoms.Anxiety|Physical symptoms|Cardiac|Other_CUSTOM_*": "Symptoms.anxiety|physical|sudden_attack_of_symptoms",
    "Symptoms.Anxiety|Physical symptoms|Cardiac|Pins and needles": "Symptoms.anxiety|physical|sudden_attack_of_symptoms",
    "Symptoms.Anxiety|Physical symptoms|Cardiac|Shallow breathing, or breathing rapidly (hyperventilation)": "Symptoms.anxiety|physical|sudden_attack_of_symptoms",
    "Symptoms.Anxiety|Physical symptoms|Cardiac|Sweating or hot flushes": "Symptoms.anxiety|physical|sudden_attack_of_symptoms",
    "Symptoms.Anxiety|Physical symptoms|Gastrointestinal|IBS symptoms": "Symptoms.anxiety|physical|stomach_problems",
    "Symptoms.Anxiety|Physical symptoms|Gastrointestinal|Larger appetite e|g| Comfort eating": "Symptoms.general|physical|appetite",
    "Symptoms.Anxiety|Physical symptoms|Gastrointestinal|Poor appetite": "Symptoms.general|physical|appetite",
    "Symptoms.Anxiety|Physical symptoms|Gastrointestinal|Stomach problems": "Symptoms.anxiety|physical|stomach_problems",
    "Symptoms.Anxiety|Physical symptoms|Gastrointestinal|Weight gain/loss": "Symptoms.general|physical|appetite",
    "Symptoms.Anxiety|Physical symptoms|Gastrointestinal|*": "Symptoms.general|physical|appetite",
    "Symptoms.Anxiety|Physical symptoms|Intense attack of physical symptoms|*": "Symptoms.anxiety|physical|sudden_attack_of_symptoms",
    "Symptoms.Anxiety|Physical symptoms|Musculoskeletal|Aches/pains": "Symptoms.general|physical|aches_and_pains",
    "Symptoms.Anxiety|Physical symptoms|Musculoskeletal|Other_CUSTOM_:headaches": "Symptoms.general|physical|headaches",
    "Symptoms.Anxiety|Physical symptoms|Musculoskeletal|Other_CUSTOM_:migraines": "Symptoms.general|physical|headaches",
    "Symptoms.Anxiety|Physical symptoms|Neurological|Extreme focus on detail instead of big picture (hyperattention to detail)": ["Symptoms.general|physical|concentration", "Symptoms.anxiety|physical|sudden_attack_of_symptoms"],
    "Symptoms.Anxiety|Physical symptoms|Neurological|Feeling weak or tired": "Symptoms.general|physical|fatigue",
    "Symptoms.Anxiety|Physical symptoms|Neurological|Foggy headed": "Symptoms.mood|physical|foggy_head",
    "Symptoms.Anxiety|Physical symptoms|Neurological|Headaches": "Symptoms.general|physical|headaches",
    "Symptoms.Anxiety|Physical symptoms|Neurological|Jumpy, on edge": "Symptoms.anxiety|emotion|on_edge",
    "Symptoms.Anxiety|Physical symptoms|Neurological|Lack of energy": "Symptoms.general|physical|fatigue",
    "Symptoms.Anxiety|Physical symptoms|Neurological|Over-alertness (Hypervigilance)": "Symptoms.general|physical|restlessness",
    "Symptoms.Anxiety|Physical symptoms|Neurological|Restlessness": "Symptoms.general|physical|restlessness",
    "Symptoms.Anxiety|Physical symptoms|Neurological|Trouble concentrating": "Symptoms.general|physical|concentration",
    "Symptoms.Anxiety|Physical symptoms|Neurological|Other_CUSTOM_*": "Symptoms.anxiety|physical|sudden_attack_of_symptoms",
    "Symptoms.Anxiety|Physical symptoms|Respiratory|*": "Symptoms.anxiety|physical|sudden_attack_of_symptoms",
    "Symptoms.Anxiety|Physical symptoms|Sleep|Difficulties falling or staying asleep": "Symptoms.general|physical|disturbed_sleep",
    "Symptoms.Anxiety|Physical symptoms|Sleep|Fitful, broken sleep": "Symptoms.general|physical|disturbed_sleep",
    "Symptoms.Anxiety|Physical symptoms|Sleep|Insomnia": "Symptoms.anxiety|physical|insomnia",
    "Symptoms.Anxiety|Physical symptoms|Sleep|Nightmares/Night terrors": "Symptoms.anxiety|physical|nightmares",
    "Symptoms.Anxiety|Physical symptoms|Sleep|Other_CUSTOM_*": "Symptoms.general|physical|disturbed_sleep",
    "Symptoms.Anxiety|Physical symptoms|Sleep|Waking up abruptly": "Symptoms.general|physical|disturbed_sleep",
    "Symptoms.Mood|Behaviour|Active avoidance|Avoiding problems/everyday activities": "Symptoms.mood|behaviour|avoidance",
    "Symptoms.Mood|Behaviour|Active avoidance|Neglecting responsibilities": "Symptoms.mood|behaviour|avoidance",
    "Symptoms.Mood|Behaviour|Active avoidance|Not seeing friends": "Symptoms.mood|behaviour|avoidance|withdrawing",
    "Symptoms.Mood|Behaviour|Active avoidance|Not showering/washing hair etc": "Symptoms.mood|behaviour|avoidance|self_care",
    "Symptoms.Mood|Behaviour|Active avoidance|Poorer performance at work": "Symptoms.mood|behaviour|avoidance|work_problems",
    "Symptoms.Mood|Behaviour|Active avoidance|Putting things off": "Symptoms.mood|behaviour|putting_things_off",
    "Symptoms.Mood|Behaviour|Active avoidance|Reduced motivation to manage everyday tasks": ["Symptoms.mood|behaviour|avoidance", "Symptoms.mood|physical|reduced_motivation"],
    "Symptoms.Mood|Behaviour|Active avoidance|Withdrawing from social situations": "Symptoms.mood|behaviour|avoidance|withdrawing",
    "Symptoms.Mood|Behaviour|Active avoidance|Other_CUSTOM_*": ["Symptoms.mood|physical|reduced_motivation", "Symptoms.mood|behaviour|avoidance|withdrawing"],
    "Symptoms.Mood|Behaviour|Passive avoidance|Allowing other people to decide for you": "Symptoms.mood|behaviour|putting_others_first",
    "Symptoms.Mood|Behaviour|Passive avoidance|Drinking more alcohol than normal": "Symptoms.mood|behaviour|substance_use",
    "Symptoms.Mood|Behaviour|Passive avoidance|Putting other people’s needs before your own": "Symptoms.mood|behaviour|putting_others_first",
    "Symptoms.Mood|Behaviour|Passive avoidance|Substance use to try and manage symptoms": "Symptoms.mood|behaviour|substance_use",
    "Symptoms.Mood|Behaviour|Passive avoidance|Using over the counter medications": "Symptoms.mood|behaviour|substance_use",
    "Symptoms.Mood|Behaviour|Passive avoidance|Other_CUSTOM_:comfort eating": "Symptoms.general|physical|appetite",
    "Symptoms.Mood|Behaviour|Self-harm|*": "Symptoms.mood|cognition|thoughts_of_self-harm",
    "Symptoms.Mood|Cognition|Cognitive distortions|Comparing yourself unfairly to other people": "Symptoms.mood|cognition|difficult_thoughts|self_worth",
    "Symptoms.Mood|Cognition|Cognitive distortions|Feeling worthless, stupid, not good enough or not worthy": "Symptoms.mood|cognition|difficult_thoughts|self_worth",
    "Symptoms.Mood|Cognition|Cognitive distortions|Negative self-talk": "Symptoms.mood|cognition|difficult_thoughts|self_worth",
    "Symptoms.Mood|Cognition|Cognitive distortions|Negative thoughts about others": "Symptoms.mood|cognition|difficult_thoughts",
    "Symptoms.Mood|Cognition|Cognitive distortions|Negative thoughts about the future": "Symptoms.mood|cognition|difficult_thoughts|the_future_(negative_thoughts_about)",
    "Symptoms.Mood|Cognition|Cognitive distortions|Negative thoughts about the world": "Symptoms.mood|cognition|difficult_thoughts|the_world_(negative_thoughts_about)",
    "Symptoms.Mood|Cognition|Cognitive distortions|Remembering the bad more than the good": "Symptoms.mood|cognition|difficult_thoughts|the_past_(negative_thoughts_about)",
    "Symptoms.Mood|Cognition|Cognitive distortions|Self-criticism": "Symptoms.mood|cognition|difficult_thoughts|self_worth",
    "Symptoms.Mood|Cognition|Cognitive distortions|Thinking others are thinking negatively about you": "Symptoms.mood|difficult_thoughts|what_others_might_think",
    "Symptoms.Mood|Cognition|Cognitive distortions|Other_CUSTOM_:overthinking": ["Symptoms.mood|cognition|difficult_thoughts", "Symptoms.anxiety|cognition|worry"],
    "Symptoms.Mood|Cognition|Cognitive distortions|Other_CUSTOM_*": "Symptoms.mood|cognition|difficult_thoughts|self_worth",
    "Symptoms.Mood|Cognition|Rumination|*": "Symptoms.mood|cognition|difficult_thoughts|the_past_(negative_thoughts_about)",
    "Symptoms.Mood|Cognition|Self-harm|Other_CUSTOM_": "Symptoms.mood|cognition|thoughts_of_self-harm",
    "Symptoms.Mood|Cognition|Self-harm|Thoughts of self-harm": "Symptoms.mood|cognition|thoughts_of_self-harm",
    "Symptoms.Mood|Cognition|Self-harm|Urges to self-harm": "Symptoms.mood|cognition|thoughts_of_self-harm",
    "Symptoms.Mood|Cognition|Suicidal ideation|*": "Symptoms.mood|cognition|suicidal_ideation",
    "Symptoms.Mood|Emotionals|Feeling hopeless|Helpless": "Symptoms.mood|emotion|helpless",
    "Symptoms.Mood|Emotionals|Feeling hopeless|Hopeless": "Symptoms.mood|emotion|hopeless",
    "Symptoms.Mood|Emotionals|Feeling hopeless|Other_CUSTOM_:low self esteem": "Symptoms.mood|cognition|difficult_thoughts|self_worth",
    "Symptoms.Mood|Emotionals|Feeling overwhelmed/hyperarousal|Distressed": "Symptoms.mood|emotion|overwhelmed",
    "Symptoms.Mood|Emotionals|Feeling overwhelmed/hyperarousal|Dread": ["Symptoms.anxiety|emotion|on_edge", "Symptoms.anxiety|emotion|fearful"],
    "Symptoms.Mood|Emotionals|Feeling overwhelmed/hyperarousal|Irritable": "Symptoms.mood|emotion|irritable",
    "Symptoms.Mood|Emotionals|Feeling overwhelmed/hyperarousal|On edge": "Symptoms.anxiety|emotion|on_edge",
    "Symptoms.Mood|Emotionals|Feeling overwhelmed/hyperarousal|Stressed": "Symptoms.anxiety|emotion|stress",
    "Symptoms.Mood|Emotionals|Feeling overwhelmed/hyperarousal|Other_CUSTOM_:feeling angry": "Symptoms.mood|emotion|irritable",
    "Symptoms.Mood|Emotionals|Feeling overwhelmed/hyperarousal|Other_CUSTOM_:feeling angry and irritable": "Symptoms.mood|emotion|irritable",
    "Symptoms.Mood|Emotionals|Feeling overwhelmed/hyperarousal|Other_CUSTOM_:anger": "Symptoms.mood|emotion|irritable",
    "Symptoms.Mood|Emotionals|Feeling overwhelmed/hyperarousal|Other_CUSTOM_:angry": "Symptoms.mood|emotion|irritable",
    "Symptoms.Mood|Emotionals|Feeling overwhelmed/hyperarousal|Other_CUSTOM_:annoyed": "Symptoms.mood|emotion|irritable",
    "Symptoms.Mood|Emotionals|Feeling overwhelmed/hyperarousal|Other_CUSTOM_:feeling frustrated": ["Symptoms.mood|emotion|overwhelmed", "Symptoms.mood|emotion|irritable"],
    "Symptoms.Mood|Emotionals|Feeling overwhelmed/hyperarousal|Other_CUSTOM_:frustrated": ["Symptoms.mood|emotion|overwhelmed", "Symptoms.mood|emotion|irritable"],
    "Symptoms.Mood|Emotionals|Feeling overwhelmed/hyperarousal|Other_CUSTOM_:frustration": ["Symptoms.mood|emotion|overwhelmed", "Symptoms.mood|emotion|irritable"],
    "Symptoms.Mood|Emotionals|Feeling overwhelmed/hyperarousal|Other_CUSTOM_:feeling overwhelmed": "Symptoms.mood|emotion|overwhelmed",
    "Symptoms.Mood|Emotionals|Feeling sad|Feeling Sad": "Symptoms.mood|emotion|sad_or_low",
    "Symptoms.Mood|Emotionals|Feeling sad|Feelings of shame": "Symptoms.mood|emotion|shame_or_guilt",
    "Symptoms.Mood|Emotionals|Feeling sad|Lonely": "Symptoms.mood|emotion|lonely_or_isolated",
    "Symptoms.Mood|Emotionals|Feeling sad|Other_CUSTOM_:guilty": "Symptoms.mood|emotion|shame_or_guilt",
    "Symptoms.Mood|Emotionals|Feeling sad|Other_CUSTOM_:feeling guilty": "Symptoms.mood|emotion|shame_or_guilt",
    "Symptoms.Mood|Emotionals|Feeling sad|Tearful": "Symptoms.mood|emotion|sad_or_low",
    "Symptoms.Mood|Emotionals|Feeling sad|The world seems grey": "Symptoms.mood|emotion|numb_or_empty",
    "Symptoms.Mood|Emotionals|Feeling sad|Other_CUSTOM_*": ["Symptoms.mood|emotion|sad_or_low", "Symptoms.mood|emotion|numb_or_empty", "Symptoms.mood|physical|reduced_motivation"],
    "Symptoms.Mood|Physical symptoms|Female related hormonal changes|More irritability related to hormonal cycle": "Symptoms.mood|emotion|irritable",
    "Symptoms.Mood|Physical symptoms|Gastrointestinal|Comfort eating": "Symptoms.general|physical|appetite",
    "Symptoms.Mood|Physical symptoms|Gastrointestinal|Increased appetite": "Symptoms.general|physical|appetite",
    "Symptoms.Mood|Physical symptoms|Gastrointestinal|Nausea": "Symptoms.anxiety|physical|stomach_problems",
    "Symptoms.Mood|Physical symptoms|Gastrointestinal|Other_CUSTOM_*": "Symptoms.general|physical|appetite",
    "Symptoms.Mood|Physical symptoms|Gastrointestinal|Poorer appetite": "Symptoms.general|physical|appetite",
    "Symptoms.Mood|Physical symptoms|Gastrointestinal|Weight gain": "Symptoms.general|physical|appetite",
    "Symptoms.Mood|Physical symptoms|Gastrointestinal|Weight loss": "Symptoms.general|physical|appetite",
    "Symptoms.Mood|Physical symptoms|Low Libido|*": "Symptoms.mood|physical|low_libido",
    "Symptoms.Mood|Physical symptoms|Musculoskeletal|Aches and pains": "Symptoms.general|physical|aches_and_pains",
    "Symptoms.Mood|Physical symptoms|Musculoskeletal|Chronic pain": "Symptoms.general|physical|aches_and_pains",
    "Symptoms.Mood|Physical symptoms|Musculoskeletal|Fibromyalgia": "Symptoms.general|physical|aches_and_pains",
    "Symptoms.Mood|Physical symptoms|Musculoskeletal|Other_CUSTOM_:headaches": "Symptoms.general|physical|headaches",
    "Symptoms.Mood|Physical symptoms|Neurological|Fatigue": "Symptoms.general|physical|fatigue",
    "Symptoms.Mood|Physical symptoms|Neurological|Feeling heavy": "Symptoms.general|physical|fatigue",
    "Symptoms.Mood|Physical symptoms|Neurological|Foggy head": "Symptoms.mood|physical|foggy_head",
    "Symptoms.Mood|Physical symptoms|Neurological|Lost motivation": "Symptoms.mood|physical|reduced_motivation",
    "Symptoms.Mood|Physical symptoms|Neurological|Low energy": "Symptoms.general|physical|fatigue",
    "Symptoms.Mood|Physical symptoms|Neurological|Moving slowly": ["Symptoms.general|physical|fatigue", "Symptoms.mood|physical|reduced_motivation"],
    "Symptoms.Mood|Physical symptoms|Neurological|Other_CUSTOM_:upset stomach": "Symptoms.anxiety|physical|stomach_problems",
    "Symptoms.Mood|Physical symptoms|Neurological|Other_CUSTOM_*": ["Symptoms.mood|physical|reduced_motivation", "Symptoms.general|physical|fatigue"],
    "Symptoms.Mood|Physical symptoms|Neurological|Restlessness": "Symptoms.general|physical|restlessness",
    "Symptoms.Mood|Physical symptoms|Neurological|Struggling to concentrate": "Symptoms.general|physical|concentration",
    "Symptoms.Mood|Physical symptoms|Sleep|Fitful sleep": "Symptoms.general|physical|disturbed_sleep",
    "Symptoms.Mood|Physical symptoms|Sleep|Insomnia": "Symptoms.anxiety|physical|insomnia",
    "Symptoms.Mood|Physical symptoms|Sleep|Nightmares/Night terrors": "Symptoms.anxiety|physical|nightmares",
    "Symptoms.Mood|Physical symptoms|Sleep|Not being able to fall asleep": ["Symptoms.general|physical|disturbed_sleep", "Symptoms.anxiety|physical|insomnia"],
    "Symptoms.Mood|Physical symptoms|Sleep|Not being able to get out of bed in the morning": ["Symptoms.mood|behaviour|avoidance|self_care", "Symptoms.mood|physical|reduced_motivation"],
    "Symptoms.Mood|Physical symptoms|Sleep|Not sleeping enough": "Symptoms.general|physical|disturbed_sleep",
    "Symptoms.Mood|Physical symptoms|Sleep|Other_CUSTOM_*": "Symptoms.general|physical|disturbed_sleep",
    "Symptoms.Mood|Physical symptoms|Sleep|Sleeping too much": "Symptoms.general|physical|disturbed_sleep",
    "Symptoms.Mood|Physical symptoms|Sleep|Waking up in the night": "Symptoms.general|physical|disturbed_sleep",

    "PastExperiences.Feeling started recently|*": "PastExperiences.Feeling started recently",
    "PastExperiences.Feelings started a long time ago|*": "PastExperiences.Feelings started a long time ago",
    "PastExperiences.Have felt like this in the past|*": "PastExperiences.Have felt like this in the past",
    "PastExperiences.Therapies|Cognitive Behavioural Therapy|*": "PastExperiences.Therapies|Cognitive Behavioural Therapy",
    "PastExperiences.Therapies|Counselling|*": "PastExperiences.Therapies|Counselling",
    "PastExperiences.Therapies|Non-specified support|*": "PastExperiences.Therapies|Non-specified support",
    "PastExperiences.Therapies|Cognitive Behavioural Therapy|Helped|*": "PastExperiences.Treatment helped",
    "PastExperiences.Therapies|Counselling|Helped|*": "PastExperiences.Treatment helped",
    "PastExperiences.Therapies|Cognitive Behavioural Therapy|Didn*": "PastExperiences.Treatment didn't help",
    "PastExperiences.Therapies|Counselling|Didn*": "PastExperiences.Treatment didn't help",
    "PastExperiences.Situations|*": "PastExperiences.You have experienced traumatic of difficult life events(s)",
    "PastExperiences.Life-changing events|*": "PastExperiences.You have experienced traumatic of difficult life events(s)",
    
    "IsHighRisk": "IsHighRisk",
    "IsGpRecommended": "IsGpRecommended",

    "MainProblem.Low mood": "MainProblem.Low mood",
    "MainProblem.Anxiety": "MainProblem.Anxiety",
    "MainProblem.Worry": "MainProblem.Anxiety",
    "MainProblem.Health Anxiety": "MainProblem.Anxiety",
    "MainProblem.Social Anxiety": "MainProblem.Anxiety",
    "MainProblem.Stress": "MainProblem.Stress",
    "MainProblem.stress": "MainProblem.Stress",
    "MainProblem.Work-related stress": "MainProblem.Stress",
    "MainProblem.Work related stress": "MainProblem.Stress",
    "MainProblem.Work- related stress": "MainProblem.Stress",
    "MainProblem.work-related stress": "MainProblem.Stress",
    "MainProblem.Depression and Anxiety": "MainProblem.Anxiety and low mood",
    "MainProblem.Anxiety and Depression": "MainProblem.Anxiety and low mood",
    "MainProblem.Anxiety and low mood": "MainProblem.Anxiety and low mood",
    "MainProblem.anxiety and low mood": "MainProblem.Anxiety and low mood",
    "MainProblem.Anxiety and Low mood": "MainProblem.Anxiety and low mood",
    "MainProblem.Anxiety and associated low mood": "MainProblem.Anxiety and low mood",
    "MainProblem.low mood and worry": "MainProblem.Anxiety and low mood",
    "MainProblem.Low mood & Anxiety": "MainProblem.Anxiety and low mood",
    "MainProblem.low mood and anxiety": "MainProblem.Anxiety and low mood",
    "MainProblem.Low mood and anxiety": "MainProblem.Anxiety and low mood",
    "MainProblem.Low mood and Anxiety": "MainProblem.Anxiety and low mood",
    "MainProblem.Low Mood and Anxiety": "MainProblem.Anxiety and low mood",
    "MainProblem.Low mood and associated anxiety": "MainProblem.Anxiety and low mood",
    "MainProblem.Worry and low mood": "MainProblem.Anxiety and low mood",

    "MainProblem.a relationship break up": "OtherFactors.Relationship",
    "MainProblem.Marriage difficulties": "OtherFactors.Relationship",
    "MainProblem.Relationship difficulties": "OtherFactors.Relationship",
    "MainProblem.Relationship issues": "OtherFactors.Relationship",
    "MainProblem.Difficulties in relation to bereavement": "OtherFactors.Bereavement",
    "MainProblem.bereavement": "OtherFactors.Bereavement",
    "MainProblem.Insomnia": "Symptoms.anxiety|physical|insomnia",
    "MainProblem.Sleep difficulties": "Symptoms.general|physical|disturbed_sleep",
    "MainProblem.difficulty sleeping": "Symptoms.general|physical|disturbed_sleep",
    "MainProblem.difficulties relating to eating": "OtherFactors.Difficulties relating to food/body image",
    "MainProblem.Low self esteem": "Symptoms.mood|cognition|difficult_thoughts|self_worth",
    "MainProblem.Low self- esteem": "Symptoms.mood|cognition|difficult_thoughts|self_worth",
    "MainProblem.Low self-esteem": "Symptoms.mood|cognition|difficult_thoughts|self_worth",
    "MainProblem.Feeling overwhelmed": "Symptoms.mood|emotion|overwhelmed",
    "MainProblem.feeling overwhelmed": "Symptoms.mood|emotion|overwhelmed",
    "MainProblem.Anger": "Symptoms.mood|emotion|irritable",
    "MainProblem.Impatience": "Symptoms.mood|emotion|irritable",

    "TalkingTherapy.CBT": "TalkingTherapy.CBT",
    "TalkingTherapy.Counselling bereavement": "TalkingTherapy.Counselling bereavement",
    "TalkingTherapy.Counselling generic": "TalkingTherapy.Counselling generic",
    "TalkingTherapy.CBT - had before but further encouragement": "TalkingTherapy.CBT - had before but further encouragement",
    "TalkingTherapy.Counselling relationship": "TalkingTherapy.Counselling relationship",
    "TalkingTherapy.Need further exploration with GP": "TalkingTherapy.Need further exploration with GP",
    "TalkingTherapy.Doing ok": "TalkingTherapy.Doing ok",
    "TalkingTherapy.Watchful waiting": "TalkingTherapy.Watchful waiting",

    "SelfHelp.Automatic negative thoughts (ANTS)": "SelfHelp.Automatic negative thoughts (ANTS)",
    "SelfHelp.Worry tree": "SelfHelp.Worry tree",
    "SelfHelp.Square breathing": "SelfHelp.Square breathing",
    "SelfHelp.Stress bucket": "SelfHelp.Stress bucket",
    "SelfHelp.Worry 54321 grounding": "SelfHelp.Worry 54321 grounding",
    "SelfHelp.Sleep hygiene": "SelfHelp.Sleep hygiene",
    "SelfHelp.Gratitude journal for low mood": "SelfHelp.Gratitude journal for low mood",
    "SelfHelp.5 minute rule": "SelfHelp.5 minute rule",
    "SelfHelp.Goal setting": "SelfHelp.Goal setting",
    
    "OtherFactors.Gambling": "OtherFactors.Addiction",
    "OtherFactors.Drugs": "OtherFactors.Addiction",
    "OtherFactors.Alcohol": "OtherFactors.Addiction",
    "OtherFactors.Binge eating": "OtherFactors.Difficulties relating to food/body image",
    "OtherFactors.Eating difficulties": "OtherFactors.Difficulties relating to food/body image",
    "OtherFactors.Difficulties with eating": "OtherFactors.Difficulties relating to food/body image",
    "OtherFactors.Eating disorder/ Body image": "OtherFactors.Difficulties relating to food/body image",
    "OtherFactors.Difficulties relating to eating": "OtherFactors.Difficulties relating to food/body image",
    "OtherFactors.Bereavement": "OtherFactors.Bereavement",
    "OtherFactors.Medication": "OtherFactors.Medication",
    "OtherFactors.Domestic abuse": "OtherFactors.Risk from others",
    "OtherFactors.Risk from others*": "OtherFactors.Risk from others",
    "OtherFactors.Covid-19": "OtherFactors.Covid-19",
    "OtherFactors.Employment": "OtherFactors.Environmental, social, and economic factors",
    "OtherFactors.Housing": "OtherFactors.Environmental, social, and economic factors",
    "OtherFactors.Exams": "OtherFactors.Environmental, social, and economic factors",
    "OtherFactors.Finances": "OtherFactors.Environmental, social, and economic factors",
    "OtherFactors.Debt": "OtherFactors.Environmental, social, and economic factors",
    "OtherFactors.University": "OtherFactors.Environmental, social, and economic factors",
    "OtherFactors.Pregnancy": "OtherFactors.Pregnancy, baby under 12 months old, and parenting struggles",
    "OtherFactors.Parenting": "OtherFactors.Pregnancy, baby under 12 months old, and parenting struggles",
    "OtherFactors.New baby": "OtherFactors.Pregnancy, baby under 12 months old, and parenting struggles",
    "OtherFactors.Relationship": "OtherFactors.Relationships, family issues, ED/Sex",
    "OtherFactors.Family difficulties": "OtherFactors.Relationships, family issues, ED/Sex",
    "OtherFactors.Family relationships": "OtherFactors.Relationships, family issues, ED/Sex",
    "OtherFactors.Fertility difficulties": "OtherFactors.Relationships, family issues, ED/Sex",
    "OtherFactors.Physical health, or long term conditions": "OtherFactors.Health conditions",
    "OtherFactors.Severe mental health condition": "OtherFactors.Health conditions",
    "OtherFactors.Attention Deficit Hyperactivity Disorder (ADHD)": "OtherFactors.Health conditions",
    "OtherFactors.Sexuality": "OtherFactors.LGBTQ+",
    "OtherFactors.Menopause": "OtherFactors.Menopause",
    "OtherFactors.Retirement": "OtherFactors.Retirement",

    "OtherFactors.Self-harm": "Symptoms.mood|cognition|thoughts_of_self-harm",

    "Analysis.Low mood (severe)": "Analysis.Low mood (severe)",
    "Analysis.Low mood (mild)": "Analysis.Low mood (mild)",
    "Analysis.Anxiety (mild)": "Analysis.Anxiety (mild)",
    "Analysis.Low mood (moderate)": "Analysis.Low mood (moderate)",
    "Analysis.Anxiety (moderate)": "Analysis.Anxiety (moderate)",
    "Analysis.Low mood (moderately severe)": "Analysis.Low mood (moderately severe)",
    "Analysis.Anxiety (few symptoms)": "Analysis.Anxiety (few symptoms)",
    "Analysis.Low mood (few symptoms)": "Analysis.Low mood (few symptoms)",
    "Analysis.Anxiety (severe)": "Analysis.Anxiety (severe)",

    "PHQ9_0": "PHQ9_0",
    "PHQ9_1": "PHQ9_1",
    "PHQ9_2": "PHQ9_2",
    "PHQ9_3": "PHQ9_3",
    "PHQ9_4": "PHQ9_4",
    "PHQ9_5": "PHQ9_5",
    "PHQ9_6": "PHQ9_6",
    "PHQ9_7": "PHQ9_7",
    "PHQ9_8": "PHQ9_8",

    "GAD7_0": "GAD7_0",
    "GAD7_1": "GAD7_1",
    "GAD7_2": "GAD7_2",
    "GAD7_3": "GAD7_3",
    "GAD7_4": "GAD7_4",
    "GAD7_5": "GAD7_5",
    "GAD7_6": "GAD7_6"

})


#new_mapping = {}
#for key in symptom_mapping.keys():
#    new_mapping[key] = "|".join(key.split("|")[0:-1])
#symptom_mapping = new_mapping


symptom_phrases = {
    "worry", "stress", "thinking|thought", "anxi", "pressure",
    "low", "mood", "sad|unhappy|tearful|cry", "depress(ed|ion)", "emotion", "feeling", "hurtful",
    "lonely", "guilt", "shame", "esteem", "loath",
    "desperat", "despair",
    "sleep", "insomnia", "wake", "get(ting)? up", "morning", "night",
    "panic", "butterflies", "palpitations", "heart", "breath", "sweat"
    "energy", "motivat", "letharg", "fatigue", "exhaust", "tir(ed|ing)", "interest",
    "concentrat", "cop(e|ing)", "effort", "struggl", "trying",
    "pleasur", "bother", "interest", "pointless", "worthless", "flat", "a failure"
    "died", "passed away", "lost (my|our)", "was killed", "deceased", "grief", "griev",
    "sore", "health", "pain", "ill", "unwell", "sick", "ache", "disease", "chronic", "acute", "suffer", "condition",
    "naus", "disorder", "hospital", "operation", "disab", "handicap", "wheelchair", "mobil", "blind", "deaf", "imped",
    "cancer", "autis", "asd", "adhd", "lung", "liver", "kidney", "hepatitis", "diabet", "brain", "blood",
    "transplant", "leukemia", "pancrea", "bladder", "reproduc", "std", "hiv", "alzheimer", "parkinson", "arthriti",
    "dementia|senile", "incontinen", "chondria", "phobia", "iac", "opath",
    "libido|sex drive", "appetite|eating", "food", "snack", "binge", "weight|bmi|fat|obese", "ugly|disgust",
    "son|daughter", "child", "baby", "pregnan", "partner|husband|wife|boyfriend|girlfriend", "mum|mother", "dad|father",
    "relationship",
    "car(er|ing)", "childcare", "midwife", "doctor", "nurse", "nursery|playgroup", "care worker", "social worker"
    "kids", "juvenile", "teen",
    "school", "church", "council", "club", "local",
    "friends", "social", "go(ing)? out", "leav(e|ing) (the|my) (house|(bed)?room)",
    "financ", "money|cash", "savings", "bill", "pay", "rent|mortgage", "income", "job|employ", "debt|overdraft|loan|borrow", "bank",
    "salary", "hungry|starving", "destitute", "reposess|bailiff", "ccj", "court", "criminal",
    "police", "prison", "parole", "probation", "officer", "legal", "law", "bail", "remand", "detention", "institut",
    "alcohol|wine|beer|vodka|g&t|lager", "drink",
    "cannabis|weed|marajuana|skunk|spliff", "smoke", "cig|fags|rollies|tobacco", "spice",
    "drug", "cocaine", "fentanyl|morphine|codeine|codamol|ket|amphetamine|methadone|opiate|opioid|tramadol|dydramol",
    "ssri|anti(-)?depressant|talopram|xetine|prozac|oxactin|xamine|aline",
    "sleeping (pill|tablet)", "tranquilizer|benzo|zepam|diaz|zolam|xanax",
    "hallucinat", "(see|hear)(ing)? (things|voices)", "(i'm|am|going) (insane|crazy|mad)", "paranoi", "schizo",
    "fight", "argue", "shout", "anger|angry|rage|fury|furious", "irrita", "(broke|break(ing)?)(-)?up",
    "hat(e|red)", "self-", "bitter", "loath", "disgust", "dirty",
    "scar(y|ed|ing)|frighten|terrif(y|ied)|afraid", "terror|horror", "dread", "doom",
    "shock", "trauma", "mental", "obsess", "compuls", "ocd",
    "night(mare| terror)", "dream", "flashback", "memory|remember", "happened|occurred", "forget",
    "accident", "crash", "incident|event", "attack",
    "sexual", "abus", "rape", "assault", "mugg(ed|ing)", "violen", "bully", "coercive", "domestic", "exploit",
    "inappropriate", "uncomfortable", "unwanted", "touch(ed|ing)", "private", "personal", "intru", "violat", "genital",
    "grope", "groom", "advances", "advantage",
    "cbt", "therap", "counsell", "help",
    "jitter", "jumpy", "heart", "breath", "nerv", "lonel", "miser", "lazy", "effort", "energ", "worth", "value", "future", "past"
}















































































































































































