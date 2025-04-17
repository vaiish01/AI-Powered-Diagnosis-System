from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    symptoms = request.form.get('symptoms')

    # Dummy logic
    predicted_disease = "Flu"
    dis_des = "Influenza is a viral infection that attacks your respiratory system."
    dis_pre = ["Rest", "Stay Hydrated", "Avoid contact with others"]
    dis_med = ["Paracetamol", "Cough Syrup"]
    dis_wrkout = ["Light stretching", "Breathing exercises"]
    dis_diet = ["Warm soup", "Fruits", "Fluids"]

    return render_template(
        'Alintern.html',
        predicted_disease=predicted_disease,
        dis_des=dis_des,
        dis_pre=dis_pre,
        dis_med=dis_med,
        dis_wrkout=dis_wrkout,
        dis_diet=dis_diet
    )

if __name__ == '__main__':
    app.run(debug=True)
