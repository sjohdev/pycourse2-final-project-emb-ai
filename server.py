'''Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # Get user text and call sentiment analyzer:
    text_to_analyze = str(request.args.get('textToAnalyze'))
    result_dict = emotion_detector(text_to_analyze)
    dom_emotion = result_dict['dominant_emotion']
    del result_dict['dominant_emotion']
    result_str = f"{result_dict}"

    # Make sure output is not invalid:
    if dom_emotion is None:
        output_str = "Invalid input! Try again."
    else:
        # format output:
        output_str = f"For the given statement, the system response is {result_str[1:-1]}."
        output_str = output_str + f" The dominant emotion is {dom_emotion}."
    return output_str

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
