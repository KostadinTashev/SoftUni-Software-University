import os
import django
from django.db.models import Q, Count, F

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Profile, Product, Order


def get_profiles(search_string: str = None) -> str:
    if search_string is None:
        return ''

    searched_profiles = Profile.objects.filter(
        Q(full_name__icontains=search_string)
        |
        Q(email__icontains=search_string)
        |
        Q(phone_number__icontains=search_string)
    ).order_by('full_name')

    if not searched_profiles:
        return ""

    result = []
    for profile in searched_profiles:
        result.append(f"Profile: {profile.full_name}, email: {profile.email}, "
                      f"phone number: {profile.phone_number}, orders: {profile.profile_orders.count()}")

    return '\n'.join(result)


def get_loyal_profiles() -> str:
    profiles = Profile.objects.get_regular_customers()

    if not profiles:
        return ""

    result = []

    for profile in profiles:
        result.append(f'Profile: {profile.full_name}, orders: {profile.num_orders}')

    return '\n'.join(result)


def get_last_sold_products() -> str:
    last_order = Order.objects.prefetch_related('products').last()

    if last_order is None or not last_order.products.exists():
        return ''

    product_names = [product.name for product in last_order.products.all()]

    return f"Last sold products: {', '.join(product_names)}"


def get_top_products() -> str:
    top_products = Product.objects.annotate(
        orders_count=Count('products_orders')
    ).filter(
        orders_count__gt=0
    ).order_by(
        '-orders_count',
        'name'
    )[:5]

    if not top_products:
        return ""

    product_lines = [f"{p.name}, sold {p.orders_count} times" for p in top_products]

    return f"Top products:\n" + "\n".join(product_lines)


def apply_discounts() -> str:
    updated_orders_count = Order.objects.annotate(
        products_count=Count('products')
    ).filter(
        products_count__gt=2,
        is_completed=False,
    ).update(
        total_price=F('total_price') * 0.90
    )

    return f"Discount applied to {updated_orders_count} orders."


def complete_order() -> str:
    order = Order.objects.prefetch_related('products') \
        .filter(is_completed=False) \
        .order_by('creation_date') \
        .first()

    if not order:
        return ''

    for product in order.products.all():
        product.in_stock -= 1

        if product.in_stock == 0:
            product.is_available = False

        product.save()

    order.is_completed = True
    order.save()

    return f'Order has been completed!'
