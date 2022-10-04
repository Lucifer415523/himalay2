from unicodedata import name
from flask import Flask,render_template
# creating object of class
abc=Flask(__name__)
#creating a scret key
abc.secret_key="@12345sedr"

@abc.route('/')
def xyz():
    return render_template('index.html')

if __name__=="__main__":
    abc.run(debug=True)