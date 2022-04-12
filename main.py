from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        height = request.form.get('height')
        weight = request.form.get('weight')
        category = calculateBMI(height, int(weight))
        return render_template('index.html', BMI=category)
    else:
        return render_template('index.html', BMI = 'Waiting on values')


def calculateBMI(height, weight):
    heights = str.split(height, "-")
    height = int(heights[0]) * 12 + int(heights[1])
    bmi = (weight*.45)/(height*0.025)**2
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal weight"
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
    elif 30 <= bmi:
        category = "Obese"
    print(height,"inches", weight,"pounds", bmi, category)
    return category

