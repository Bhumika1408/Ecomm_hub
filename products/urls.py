from django.urls import path
from .views import register_seller,seller_add_product,individual_product,buy_prod,order_confirm,developer_options,update_product,delete_product
urlpatterns = [
    path('register-seller',register_seller,name="register_s"),
    path('seller-add-product',seller_add_product,name="sell_add_prod"),
    path('product/<int:product_id>-<str:product_name>/',individual_product,name="prod"),
    path('product/<int:product_id>/',buy_prod,name="buy_prod"),
    path('product/order/<int:order_id>/',order_confirm,name="order_con"),
    path('developer-options/',developer_options, name='developer_options'),
    path('update-product/<int:product_id>/',update_product, name='update_product'),
    path('delete-product/<int:product_id>/',delete_product, name='delete_product'),
]

# In urls.py
