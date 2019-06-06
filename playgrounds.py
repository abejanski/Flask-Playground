from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play', defaults={'integer':3,'color':'red'})
@app.route('/play/<integer>', defaults={'color':'blue'})
@app.route('/play/<integer>/<color>')
def play_number(integer,color):
    return render_template('playgroundlink.html',some_color=color,some_integer=int(integer))








if __name__=="__main__":
    app.run(debug=True)

