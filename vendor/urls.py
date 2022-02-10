from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'vendor'


urlpatterns = [
    path('', views.vendors, name="vendors"),
    path('become-vendor/', views.become_vendor, name="become-vendor"),
    path('vendor-admin/', views.vendor_admin, name="vendor-admin"),
    path('vendor-admin/tanishq', views.vendor_admin_tanishq, name="vendor-admin-tanishq"),
    path('vendor-admin/roadster', views.vendor_admin_roadster, name="vendor-admin-roadster"),
    path('edit-vendor/', views.edit_vendor, name="edit-vendor"),
    # path('edit-vendor/tanishq', views.edit_vendor_tanishq, name="edit-vendor-tanishq"),
    path('add-product/', views.add_product, name="add-product"),
    # path('add-product/tanishq', views.add_product_tanishq, name="add-product-tanishq"),
    # path('add-product/roadster', views.add_product_roadster, name="add-product-roadster"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name="login"),

    path('<int:vendor_id>/', views.vendor, name="vendor"),
]
