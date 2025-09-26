from django.core.mail import send_mail, BadHeaderError
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.conf import settings

def send_mail(recipient, subject, message):
    try:
        validate_email(recipient)
        send_mail(
            subject=subject,
            messagep=message,
            form_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient],
            fail_silently=False,
        )
        return {'status':'success','message':f'Email sent to {recipient}'}

    except ValidationError:
        return {'status':'error','message':'Invalid email found'}
    except BadHeaderError:
        return {'status':'error','message':'Invalid header found'}
    except Exception as e:
        return {'status':'error','message':str(e)}
