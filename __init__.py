import requests

# Variáveis de autenticação
tenant_id = '3869542e-373a-46df-9fb6-3111751c9275'
client_id = '3b578b13-c9b7-49ea-b146-00bb01e4f386'
client_secret = 'CPL8Q~bQ1CaUaKaWOhgdrvS7gvGWPDfb9xhJtdCe'

# Obter token de acesso usando Client Credentials Grant Flow
token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
token_data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': 'https://graph.microsoft.com/.default'
}
token_response = requests.post(token_url, data=token_data).json()
access_token = token_response['access_token']

# Obter e-mails do usuário autenticado
emails_url = 'https://graph.microsoft.com/v1.0/me/messages'
emails_response = requests.get(emails_url, headers={'Authorization': 'Bearer ' + access_token}).json()

# Verificar se a resposta contém a chave 'value'
if 'value' in emails_response:
    
# Exibir os e-mails
    for email in emails_response['value']:
        print('Assunto:', email['subject'])
        print('De:', email['from']['emailAddress']['address'])
        print('---')

else:
    print('Erro ao obter e-mails:', emails_response.get('error', 'Erro desconhecido'))