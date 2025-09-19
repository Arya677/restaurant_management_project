import logging
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)

def is_valid_email(email:str) -> bool:
    try:
        validate_email(email)
        return True
    except ValidationError as e:
        logger.error(f"Invalid email '{email}': {e}")
        return False
    except Exception as e:
        logger.exception(f"Unexcepted error while validating email '{email}':{e}")
        return False