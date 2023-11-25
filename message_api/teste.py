from base64 import b64encode
from requests import post

def send_email():
    data = {
            'from_addr': 'zaion.arruda@fatec.sp.gov.br',
            'to_addrs': ['zaion.arruda@fatec.sp.gov.br'],
            'cc_addrs': ['zaion.arruda@fatec.sp.gov.br'],
            'subject': 'Testando',
            'content': 'Conteúdo do teste',

            }

    # result = post('http://bpsaibptasks02:8081/send_email', json=data)
    result = post('http://localhost:8081/send_email', json=data)

send_email()