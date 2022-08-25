from flask import Flask, jsonify, render_template, request, make_response, redirect, url_for
import montecarlo2
import Persona

app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# Index page and Rendering Basic Templates
@app.route('/index')
@app.route('/')
def index():
  return render_template('index.html')



# HTTP Methods
@app.route('/run_simulation', methods=['GET'])
def run_simulation():
  if request.method == 'GET':
    
    #result = [{ 'id': 0, 'entryTime':1205, 'outTime': 1300 }, 
    #          { 'id': 1, 'entryTime':1206, 'outTime': 1316 }, 
    #          { 'id': 2, 'entryTime':1210, 'outTime': 1338 }, 
    #          { 'id': 3, 'entryTime':1410, 'outTime': 1585 },
    #          { 'id': 4, 'entryTime':1600, 'outTime': 1700 }]
    
    lista = montecarlo2.correr()
    lst = []
    if not lst:
      print("Empty")
    else:
      print("Not Empty")
    result = []

    #dict = { 'id': lista[0].id, 'entryTime': lista[0].t_llegada, 'outTime': lista[0].t_salida }
    #result.append(dict)

    for i in lista:
      dict = { 'id': i.id, 'entryTime':i.t_llegada, 'outTime': i.t_salida }
      result.append(dict)
      #result[{'id','entryTime', 'outTime'}] = i , i.entryTime, i.outTime

    return make_response(jsonify(result), 200)

if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0', debug=True, port=8080)
