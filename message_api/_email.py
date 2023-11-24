import logging
import mimetypes
import traceback
from email.message import EmailMessage
from email.utils import make_msgid
from smtplib import SMTP

SMTP_HOST = 'sandbox.smtp.mailtrap.io'
SMTP_PORT = 2525


def send_email(from_addr, to_addrs, cc_addrs=[], bcc_addrs=[], subject='',
               content='', html_content='', files={}, attachments=True):
    msg = EmailMessage()

    if type(to_addrs) == str:
        to_addrs = [to_addrs]
    if type(cc_addrs) == str:
        cc_addrs = [cc_addrs]
    if type(bcc_addrs) == str:
        bcc_addrs = [bcc_addrs]

    # Add basic headers
    msg['From'] = from_addr
    msg['To'] = ', '.join(to_addrs)
    msg['Cc'] = ', '.join(cc_addrs)
    msg['Bcc'] = ', '.join(bcc_addrs)
    msg['Subject'] = subject

    # Add content
    msg.set_content(content)

    if html_content:
        cids = {}
        formatted_cids = {}
        for file in files.keys():
            cid = make_msgid()
            cids.update({files[file]: f'{cid}'})
            formatted_cids.update({f'{file.split(".")[0]}': cid[1:-1]})

        msg.add_alternative(html_content.format(
                content=content,
                **formatted_cids
            ),
            subtype='html'
        )

        for file, cid in cids.items():
            with open(file, 'rb') as img:
                msg.get_payload()[1].add_related(
                    img.read(), 'image', 'png', cid=cid
                )

    # Add attachments if exist
    if attachments:
        files_names = files.keys()
        i = 0
        for path in files.values():
            ctype, encoding = mimetypes.guess_type(path)
            if ctype is None or encoding is not None:
                # No guess could be made, or the file is encoded (compressed),
                # so use a generic bag-of-bits type.
                ctype = 'application/octet-stream'

            maintype, subtype = ctype.split('/', 1)
            with open(path, 'rb') as fp:
                msg.add_attachment(
                    fp.read(),
                    maintype=maintype,
                    subtype=subtype,
                    filename=path.split(
                        '\\')[-1] if not files_names else list(files_names)[i]
                    )  # Get the name of the file path

            i += 1

    try:
        # Send email using the configured SMTP server
        with SMTP(host=SMTP_HOST, port=SMTP_PORT) as smtp_conn:
            smtp_conn.login('','')
            smtp_conn.set_debuglevel(2)
            smtp_conn.send_message(msg)

        return True, ''
    except Exception:
        logging.error(traceback.format_exc())
        return False, traceback.format_exc()
