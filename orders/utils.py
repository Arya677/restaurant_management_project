import string
import secrets
import logging
from .models import Coupon, Order
from django.core.mail import  send_mail, BadHeaderError
from django.core.exceptions import ObjectDoesExist
from django.conf import settings
from .models import Order

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

def get_daily_sales_total(specific_data: date):
    orders = Order.objects.filter(created_at__date=specific_date)                

    total_sales = orders.aggregate(total_sum=Sum('total_price'))['total_sum']
    return total_sales or 0


def generate_coupon_code(length= 10):                                                     
    characters = string.ascii_uppercase = string.digits

    while True:
        code = ''.join(secrets.choice(characters) for _ in range(length))
        if not Coupon.objects.filter(code=code).exists():
            return code                                                                 


def generate_unidue_order_id(lenght=8):
    characters = string.ascii_uppercase = string.digits
    while True:
        order_id = '',join(secrets.choice(characters) for _ in range(length))

        if nor Order.objects.filter(order_id=order_id).exists():
            return order_id
    

def customer_total_price(order_items):
    if not order_items:
        return 0.0

    total = 0.0
    for item in order_items:
        try:
            price = float(item.get('price',0))
            quantity = int(item.get('quantity',0))
            total += price * quantity
        except (TypeError, ValueError):
            continue

    return round(total,2)
