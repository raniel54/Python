from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/webhook/outlook', methods=['POST'])
def outlook_webhook():
    data = request.json
    # Verificar se é um evento de e-mail
    if data['resource'] == '/me/messages':
        email_data = requests.get(data['resource'], headers={'Authorization': 'a61fe9a6-d030-411b-afd3-01e3089b1319'}).json()
        # Verificar se o e-mail é de erro
        for email in email_data['value']:
            if 'error' in email['subject'].lower() or 'error' in email['bodyPreview'].lower():
                print("E-mail de Erro:")
                print("De: ", email['from']['emailAddress']['address'])
                print("Para: ", email['toRecipients'][0]['emailAddress']['address'])
                print("Assunto: ", email['subject'])
                print("Corpo: ", email['bodyPreview'])
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)