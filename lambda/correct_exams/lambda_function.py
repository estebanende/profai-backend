import json

def lambda_handler(event, context):
    # Se hace correctamente el despliegue de la función lambda con el pipeline
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
