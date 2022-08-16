from keras_estimator import KerasEstimator
from task_specific_resources.HAT_category_mapping import category_mapping
import logging
import json

def init():

    global categories
    global estimator

    categories = set()
    for source_category, target_category in category_mapping:
        categories.add(target_category)
    categories = sorted(list(categories))

    estimator = KerasEstimator("task_specific_resources/model_config.json")

    logging.info("Model loaded")

def run(request):

    logging.info("Request received")

    request = json.loads(request)

    probs = estimator.predict([request["input_text"]])[0]
    response = {
        "classes": [{"name": categories[i], "probability": probs[i]} for i in range(len(categories))]
    }

    return response

init()
response = run("{\"input_text\":\"I've been having difficult thoughts and sleepless nights ever since the attack. I don't know if I can go on like this.\"}")
for c in response["classes"]:
    print(str(c["probability"]) + "\t" + str(c["name"]))