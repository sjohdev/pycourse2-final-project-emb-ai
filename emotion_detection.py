''' Emotion detection function using IBM's Watson AI API.'''
import requests
import json

def emotion_detector(text_to_analyze):
    url_base = 'https://sn-watson-emotion.labs.skills.network'
    url = url_base + '/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id":
              "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Sending a POST request to the emotion detector API:
    response = requests.post(url, json=myobj, headers=header)
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    emotions = list(formatted_response['emotionPredictions'][0]['emotion'].keys())
    scores = list(formatted_response['emotionPredictions'][0]['emotion'].values())
    output_dictionary = {emotions[0]: scores[0],
                         emotions[1]: scores[1],
                         emotions[2]: scores[2],
                         emotions[3]: scores[3],
                         emotions[4]: scores[4],
                         'dominant_emotion': emotions[scores.index(max(scores))]
                         }
    return output_dictionary


