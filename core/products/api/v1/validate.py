from products.models import Products

def is_valid_user_admin(user):
    if user.is_staff:
        return True
    return False

def is_valid_product_name(name):
    try:
        Products.objects.get(name=name)
        return False
    except:
        return True
