from flask import Flask, render_template,request,redirect,url_for
"""
It creates an instance of the flask class, 
which will be ur WSGI(Web server gateway interface) application

"""
app = Flask(__name__)

@app.route("/")
def welcome():
    return " <html><H1>Welcome to this Flask course</H1></html> "

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('aboutUs.html')

@app.route('/form',methods=['GET','POST'])
def  form():
    if request.method =='POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')
# Variable rule
@app.route('/success/<int:score>')
def success(score):
    if score>=50:
          res ="Passed"
    else:
           res ="failed"
    return  render_template('result.html',results =res)     
            
# Variable rule
@app.route('/successres/<int:score>')
def successres(score):
    if score>=50:
        res ="Passed"
    else:
        res ="failed"
    exp ={'score':score ,"res":res}       
    return  render_template('result1.html',results =exp)    

@app.route('/failed/<int:score>')
def fail(score):

 return  render_template('result.html',results =score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method =='POST':
        maths = float(request.form['maths'])
        chemistry = float(request.form['chemistry'])
        physics = float(request.form['physics'])
        #datascience = float(request.form['datascience'])

        total_score =(maths+chemistry+physics)/3
    else:
        return render_template('getresults.html')    
    return redirect(url_for('successres',score =total_score))

if __name__ == "__main__":
    app.run(debug = True)
