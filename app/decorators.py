from functools import wraps
from flask import abort
from flask_login import current_user

def role_required(role_name):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role != role_name:
                abort(403)  # Или перенаправьте на другую страницу или отобразите ошибку
            return func(*args, **kwargs)
        return decorated_function
    return decorator