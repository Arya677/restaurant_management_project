from django.core.mail import send_mail, BadHeaderError
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.conf import settings
from datetime import datetime, time

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

def is_restaurant_open():
    now = datetime.now()
    currtent_day = now.weekday()
    current_time = now.time()

    opening_hours = {
        0: (time(9, 0), time(22, 0)),
        1: (time(9, 0), time(22, 0)),
        2: (time(9, 0), time(22, 0)),
        3: (time(9, 0), time(22, 0)),
        4: (time(9, 0), time(22, 0)),
        5: (time(9, 0), time(23, 0)),
        6: (time(9, 0), time(23, 0)),
    }

    open_time, close_time = opening_hours.get(current_day)

    if open_time <= current_time <-= close_time:
        return True
    else:
        return False
