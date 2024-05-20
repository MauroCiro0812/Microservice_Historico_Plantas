from conexionbd import conexion
import json

class consulta(conexion):

    def consultar(nit, mes, anio):
        #Nos traemos el cursor desde conexion
        cur = conexion.conectar()
        #Declaramos una lista
        datos = []
        #En el caso de que el campo se encuentre vacio lo pasamos a None
        if mes == 0 or mes == "":
                mes = None
    
        if anio == 0 or anio == "":
            anio = None
            
        if nit == 0 or nit == "":
            nit = None
        
        if nit and not mes and not anio:
        # Consultar basada solo en el NIT
            cur.execute(f"SELECT nombre, descripcion FROM empresas WHERE nit = {nit}")
            for nombre, descripcion in cur.fetchall():
                datos.append({'nombre': nombre, 'descripcion': descripcion})

        elif not nit and mes and anio:
            # Consultar basada solo en mes y anio
            cur.execute(f"SELECT nombre, descripcion FROM empresas WHERE mes = {mes} AND anio = {anio}")
            for nombre, descripcion in cur.fetchall():
                datos.append({'nombre': nombre, 'descripcion': descripcion})

        elif nit and mes and anio:
            # Consultar basada en todos los parámetros
            cur.execute(f"SELECT nombre, descripcion FROM empresas WHERE nit = {nit} AND mes = {mes} AND anio = {anio}")
            for nombre, descripcion in cur.fetchall():
                datos.append({'nombre': nombre, 'descripcion': descripcion})

        else:
            # Si no hay suficientes datos para la consulta
            print("No se proporcionaron suficientes datos para la consulta")
        
        #Retornamos la lista
        return json.dumps(datos)
