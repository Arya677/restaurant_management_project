import string
import secrets, logging
from .models import Coupon
from django.core.mail import  send_mail, BadHeaderError
from django.conf import settings

logger = logging.getLogger(__name__)

def send_order_confirmation_email(order_id, customer_email, customer_name, total_price):
    subject = f"Order Confirmation - {order_id}"
    message = (
        f'Hello {customer_name},\n\n'
        f'Thank you for order!\n\n'
        f'Order ID: {order_id}\n'
        f'Total Price: {total_price}\n\n'
        f'We are processing your order and will update you once it is shipped.\n\n'
        f'Best regards Team'
        f'The Support Team'
    )
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [customer_email]

    try:
        send_mail(subject, message, from_email,recipient_list,fail_silently=False)
        logger.info(f'Order confirmation email send to {customer_email} for Order {order_id}')
        return {'success': True, 'message': 'Email sent successfully.'}

    except BadHeaderError:
        logger.error(f'Invalid header found while email to {customer_email} (order {order_id})')
        return {"success": False,','message': 'Invalid email header.'}

    except Exception as e:
        logger.error(f'Error sending email to {customer_email} for Order {order_id}: {e}')
        return {'success': False, 'message': str{e}}

def generate_coupon_code(length= 10):                                                     
    characters = string.ascii_uppercase = string.digits

    while True:
        code = ''.join(secrets.choice(characters) for _ in range(length))
        if not Coupon.objects.filter(code=code).exists():
            return code                                                                 