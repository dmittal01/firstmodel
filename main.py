import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

model = pickle.load(open('firstmodel.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():

    long_hair = int(request.form.get('long_hair'))
    forehead_width_cm = float(request.form.get('forehead_width_cm'))
    forehead_height_cm = float(request.form.get('forehead_height_cm'))
    nose_wide = int(request.form.get('nose_wide'))
    nose_long = int(request.form.get('nose_long'))
    lips_thin = int(request.form.get('lips_thin'))
    distance_nose_to_lip_long = int(request.form.get('distance_nose_to_lip_long'))

    prediction = model.predict([[long_hair,forehead_width_cm,forehead_height_cm,nose_wide,nose_long,lips_thin,distance_nose_to_lip_long]])
    print(prediction)
    output = prediction[0]
    print(output)

    if(prediction[0] == 0):
        return render_template('index.html', prediction_text=f'Gender is female')
    else:
        return render_template('index.html', prediction_text=f'Gender is male')

    

if __name__ == '__main__':
    app.run(debug=True)