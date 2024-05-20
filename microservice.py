from consultas import consulta

class microservice(consulta):
    
    def ejecucion(nit, mes, anio):
        json_file = consulta.consultar(nit, mes, anio)
        return json_file