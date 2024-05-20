#Impostamos flask, request, jsonify
from flask import Flask, request, jsonify
from microservice import microservice

app = Flask(__name__)

#Se declara el End point
@app.route('/Microservice/', methods=['GET'])
def microservice_init():
    #Los argumentos se convierten en variables
    nit = request.args.get('nit')
    mes = request.args.get('mes')
    anio = request.args.get('anio')
    
    #Si las 3 variables no tienen valor retornameros el mensaje
    if nit is None and mes is None and anio is None:
        return jsonify({'error': 'Se requieren los tres parámetros: id, mes y año'}), 400
    
    print(nit, mes, anio)
    json_file = microservice.ejecucion(nit, mes, anio)
    return json_file

if __name__=="__main__":
    app.run(debug=True)

