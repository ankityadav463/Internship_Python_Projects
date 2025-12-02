from flask import Flask 
app = Flask(__name__)  

@app.route("/")
def home():
    return"""
    <h1> Radhe Radhe ji</h1>
    <h2> I am python developer</h2>
    """

@app.route("/about")
def about():  
    return"""
    <h1> Radhe Radhe ji....</h1>
    <h2> I am python developer</h2>
    """

if __name__=='__main__':
     app.run(debug=True)