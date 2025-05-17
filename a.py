from flask import Flask, request, make_response, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')     

def index():
   return " Hello 7 "

@app.route('/i')

def h():
   return " Hello 8 "

@app.route('/g/<name>', methods=['GET','POST','PUT','DELETE'])
def greet(name):
    if request.method == 'GET':
       return "YOU MADE GET\n"
    elif request.method == 'POST':
       return "YOU MADE POST\n"
    else:
       return f"hello {name}"
@app.route('/a/<int:n1>/<int:n2>')

def add(n1, n2):
    
    return f"{n1}+{n2}={n1+n2}"

@app.route('/ha')

def handle():
    if 'g' in request.args.keys() and 'n' in request.args.keys():
        greet = request.args['g']
        name = request.args.get('n')
    
        return f'{greet}, {name}'

    else:
        return f'data not available'
@app.route('/r')   
def hr():
   return " Hello 9 " , 202
@app.route('/cr')
def hcr():
   response = make_response('cust resp')
   response.status_code = 202
   response.headers['content']=' respo 202'
   return response

app = Flask(__name__, template_folder='temp')
@app.route('/t')
def hr():
      v = "Hai"
      v2 = 10 + 11
      l = [1,2,3]
      return render_template('index.html', v=v, v2=v2, l=l)
@app.template_filter('reverse_string')
def r(s):
    return s[::-1]
@app.route('/rd')
def rd():
    return redirect(url_for('hr'))

@app.route('/f', methods=['GET', 'POST'])
def rdf():
    if request.method == 'GET':
       return render_template('index.html')
    if request.method == 'POST':
       return ""
if __name__== '__main__':
     app.run(host='0.0.0.0', port=5556, debug=True)
