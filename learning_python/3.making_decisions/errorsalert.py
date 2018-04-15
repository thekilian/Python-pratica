alert_system = 'console'
error_severity = 'critical'
error_message = 'OMG! Something terrible happend!'

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    send_email('admin@mail.com', error_message)
elif error_severity == 'medium':
    send_email('support1@mail.com', error_message)
else:
    send_email('support2@mail.com', error_message)