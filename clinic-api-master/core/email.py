from djoser import email

class PasswordResetEmail(email.PasswordResetEmail):
    template_name = 'email/password_reset.html'
    html_template_name = 'email/password_reset.html'
    subject = 'Password Reset'
    body = 'password_reset.html'
    html_body = 'password_reset.html'
    context = {
        'site_name': 'Project Alpha',
        'domain': 'localhost:8000',
        'uid': '{uid}',
        'user': '{user}',
        'token': '{token}',
        'protocol': 'http',
    }
    send_email = True
    from_email = 'Project Alpha'