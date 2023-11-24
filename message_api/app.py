import base64
import json
import logging
import os
from datetime import datetime
from pathlib import Path
from datetime import datetime

from flask import Flask, render_template, request
from waitress import serve

from _email import send_email



# POSTs responses
POST_RESP_SUCCESS = "OK"
POST_RESP_FAIL = "KO"
POST_RESP_SUCCESS_STATUS = 200
POST_RESP_WRONG_PARAM_STATUS = 400
POST_RESP_FAIL_STATUS = 500

TEMP_FOLDER = 'temp_folder'

app = Flask(__name__)

# Config log file
FORMAT = '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
logging.basicConfig(filename=r'app.log', level=logging.INFO, format=FORMAT)

# Create temp folder if not exists
temp_folder = Path(TEMP_FOLDER)
if not temp_folder.exists():
    os.mkdir(temp_folder)



@app.route('/', methods=['GET'])  # noqa
def hello():
    return render_template('hello.html')


@app.route('/send_email', methods=['POST'])
def _send_email():
    a = request.data.decode("utf-8")
    data = json.loads(a)

    from_addr = data.get('from_addr')
    to_addrs = data.get('to_addrs')
    cc_addrs = data.get('cc_addrs', [])
    bcc_addrs = data.get('bcc_addrs', [])
    subject = data.get('subject')
    content = data.get('content')
    files = data.get('files')
    html_content = data.get('html_content', '')
    attachments = data.get('attachments', True)

    # Save files to send
    files_temp_paths = []
    file_paths = {}
    if files:
        for file_name, file_b64_data in files.items():
            file_data = base64.b64decode(file_b64_data)
            file_path = (
                r'%s\%s_%s' % (TEMP_FOLDER, datetime.now().strftime(
                    '%d_%m_%Y_%H_%M_%S_%f'), file_name)
            )
            with open(file_path, 'wb') as f:
                f.write(file_data)

            files_temp_paths.append(file_path)
            file_paths.update({file_name: file_path})
    
    send_email(from_addr=from_addr,
                                to_addrs=to_addrs,
                                cc_addrs=cc_addrs,
                                bcc_addrs=bcc_addrs,
                                subject=subject,
                                content=content,
                                files=file_paths,
                                html_content=html_content,
                                attachments=attachments)
    
    return POST_RESP_SUCCESS, POST_RESP_SUCCESS_STATUS
if __name__ == "__main__":
    app.run(debug=True, port=8081)
    # serve(app, port=8081, threads=2)