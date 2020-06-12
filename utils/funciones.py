from utils.IsMusicaError import *
import sys, traceback
import json
import os
import boto3
from boto3.dynamodb.conditions import Key, Attr

def obtenerCancion(jsonCancion):
    try:
        
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Musica')
        artista = jsonCancion['artista']
        titulo = jsonCancion['titulo']
        
        response = table.get_item(Key={'Artista': artista, 'Titulo': titulo})
        print(response)

        if 'Item' in response:
            body = response['Item']
        else:
            body = {
                "mensaje": "No existe"
            }

        return response
    
    except ServicioError as e:
        print("error de servicio")

        return -1

    except IsMutateError as e:
        print("error de negocio")

        return -1
        
    except Exception as e:
        print("error no esperado")
        print(traceback.format_exc())
        print (e)
        return -1

def insertCancion(jsonCancion):
    try:
        
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Musica')

        artista = jsonCancion['artista']
        titulo = jsonCancion['titulo']
        letra = jsonCancion['letra']
        disco = jsonCancion['disco']
        
        response = table.put_item(
           Item={
                'Artista': artista,
                'Titulo': titulo,
                'letra': letra,
                'disco': disco
            }
        )
        
        return response
    
    except ServicioError as e:
        print("error de servicio")

        return -1

    except IsMutateError as e:
        print("error de negocio")

        return -1
        
    except Exception as e:
        print("error no esperado")
        print(traceback.format_exc())
        print (e)
        return -1

def detalleArtista(jsonCancion):
    try:
        
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Musica')
        artista = jsonCancion['artista']
        
        response = table.query(
            KeyConditionExpression=Key('Artista').eq(artista)
        )

        return response
    
    except ServicioError as e:
        print("error de servicio")

        return -1

    except IsMutateError as e:
        print("error de negocio")

        return -1
        
    except Exception as e:
        print("error no esperado")
        print(traceback.format_exc())
        print (e)
        return -1

def actualizarCancion(jsonCancion):
    try:
        
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Musica')
        artista = jsonCancion['artista']
        titulo = jsonCancion['titulo']
        letra = jsonCancion['letra']
        disco = jsonCancion['disco']
        
        response = table.update_item(
            Key={
                'Artista': artista,
                'Titulo': titulo
            },
            UpdateExpression="set disco=:r, letra=:p",
            ExpressionAttributeValues={
                ':r': disco,
                ':p': letra
            },
            ReturnValues="UPDATED_NEW"
        )

        return response
    
    except ServicioError as e:
        print("error de servicio")

        return -1

    except IsMutateError as e:
        print("error de negocio")

        return -1
        
    except Exception as e:
        print("error no esperado")
        print(traceback.format_exc())
        print (e)
        return -1

def eliminandoCancion(jsonCancion):
    try:
        
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Musica')
        artista = jsonCancion['artista']
        titulo = jsonCancion['titulo']
        
        response = table.delete_item(
            Key={
                'Artista': artista,
                'Titulo': titulo
            }
        )

        return response
    
    except ServicioError as e:
        print("error de servicio")

        return -1

    except IsMutateError as e:
        print("error de negocio")

        return -1
        
    except Exception as e:
        print("error no esperado")
        print(traceback.format_exc())
        print (e)
        return -1