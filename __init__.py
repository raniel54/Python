import logging
import azure.functions as func
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/webhook', methods=['POST'])
def webhook():
    data = request.json
    logging.info(f'Received webhook notification: {data}')
    # Aqui você pode processar os dados recebidos conforme necessário
    return '', 200

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.WsgiMiddleware(app).handle(req)