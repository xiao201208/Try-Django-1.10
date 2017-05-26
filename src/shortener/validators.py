from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
    url_validator = URLValidator()
    reg_val = value
    if "http" in reg_val:
        new_value = reg_val
    else:
        new_value = 'http://' + value
    try:
        url_validator(new_value)
    except:
        raise ValidationError("您输入的url不合法，请重新输入！")
    return new_value


def validate_dot_com(value):
    if not ".com" in value:
        raise ValidationError("请出入包含.com的url")
    return value