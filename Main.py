from flask import Flask, render_template
from Controller.Image_Classification import Image_Classification

app = Flask(__name__)

@app.route('/')
def main():

    IC = Image_Classification()
    Selection,Question = IC.Choice()
    Player = "Ahmad"

    return render_template('404.html', Name = Player, Selection = Selection, question = Question)

if __name__ == '__main__':
    app.run()  