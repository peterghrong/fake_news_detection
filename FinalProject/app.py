from flask import Flask, render_template, request
from predictor import Predictor

app = Flask(__name__)

# initiating the predictor model

# initiate this
predictor = Predictor()
# initiate this


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        title = request.form["news_title"]
        body = request.form["news_body"]
        input = title + body
        output = predictor.predict(input)
        print(input)
        print(output)
        if output == 0:
            print("this")
            return render_template('fake.html')
        else:
            print("that")
            return render_template('real.html')
    else:
        return render_template('take_input.html')


if __name__ == "__main__":
    app.run(debug=True)
