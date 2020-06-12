from utils.IsMusicaError import *
from utils.funciones import *
import time, json
import sys, traceback
import boto3
from boto3.dynamodb.conditions import Key, Attr

def obtener_cancion(event, context):
    try:
        # se carga body
        jsonCancion = json.loads(event['body'])
        
        response = obtenerCancion(jsonCancion)
        
        if 'Item' in response:
            body = response['Item']
        else:
            body = {
                "mensaje": "No existe"
            }
        
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        # return response
    except Exception as e:
        print("error no esperado")
        print(traceback.format_exc())

        print (e)
        body = {
            "mensaje": "Error al realizar la consulta",
            "ex": str(e)
        }

        response = {
            "statusCode": 500,
            "body": json.dumps(body)
        }
    
    return response

def obtener_artista(event, context):
    try:
        # se carga body
        jsonCancion = json.loads(event['body'])
        
        response = detalleArtista(jsonCancion)
        
        if 'Items' in response:
            body = response['Items']
        else:
            body = {
                "mensaje": "No existe"
            }
        
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        # return response
    except Exception as e:
        print("error no esperado")
        print(traceback.format_exc())

        print (e)
        body = {
            "mensaje": "Error al realizar la consulta",
            "ex": str(e)
        }

        response = {
            "statusCode": 500,
            "body": json.dumps(body)
        }
    
    return response

def borra_cancion(event, context):
    try:
        # se carga body
        jsonCancion = json.loads(event['body'])
        
        response = eliminandoCancion(jsonCancion)

        if 'ResponseMetadata' in response:
            if 'HTTPStatusCode' in response['ResponseMetadata']:
                body = response['ResponseMetadata']['HTTPStatusCode']
            else:
                body = {
                    "mensaje": "No existe"
                }
        else:
            body = {
                "mensaje": "No existe"
            }
        
        response = {
            
            
            
            "statusCode": 200,


            "body": json.dumps(body)
        }

        # return response
    except Exception as e:
        print("error no esperado")
        print(traceback.format_exc())

        print (e)
        body = {
            "mensaje": "Error al realizar la consulta",
            "ex": str(e)
        }

        response = {
            "statusCode": 500,
            "body": json.dumps(body)
        }
    
    return response

def inserta_cancion(event, context):
    try:
        # se carga body
        jsonCancion = json.loads(event['body'])
        
        response = insertCancion(jsonCancion)

        if 'ResponseMetadata' in response:
            if 'HTTPStatusCode' in response['ResponseMetadata']:
                body = response['ResponseMetadata']['HTTPStatusCode']
            else:
                body = {
                    "mensaje": "No existe"
                }
        else:
            body = {
                "mensaje": "No existe"
            }
        
        response = {
            
            
            
            "statusCode": 200,


            "body": json.dumps(body)
        }

        # return response
    except Exception as e:
        print("error no esperado")
        print(traceback.format_exc())

        print (e)
        body = {
            "mensaje": "Error al realizar la consulta",
            "ex": str(e)
        }

        response = {
            "statusCode": 500,
            "body": json.dumps(body)
        }
    
    return response

def actualiza_cancion(event, context):
    try:
        # se carga body
        jsonCancion = json.loads(event['body'])
        
        response = actualizarCancion(jsonCancion)

        if 'ResponseMetadata' in response:
            if 'HTTPStatusCode' in response['ResponseMetadata']:
                body = response['ResponseMetadata']['HTTPStatusCode']
            else:
                body = {
                    "mensaje": "No existe"
                }
        else:
            body = {
                "mensaje": "No existe"
            }
        
        response = {
            
            
            
            "statusCode": 200,


            "body": json.dumps(body)
        }

        # return response
    except Exception as e:
        print("error no esperado")
        print(traceback.format_exc())

        print (e)
        body = {
            "mensaje": "Error al realizar la consulta",
            "ex": str(e)
        }

        response = {
            "statusCode": 500,
            "body": json.dumps(body)
        }
    
    return response