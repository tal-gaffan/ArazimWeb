from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def HelloWorld():
    return render_template('helloworld.html')

app.run()