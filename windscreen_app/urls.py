from django.urls import path
from windscreen_app.views import (
    CreateOrderAPIView, GetApprovedOrdersAPIView, GetOrderDetailsAPIView, GetQuotesAPIView, GetServicesAPIView, RegisterVehicleAPIView, GenerateQuoteAPIView,
    ApproveQuoteAPIView, SubmitServiceAPIView, SubmitWorkProgressAPIView, 
)
from windscreen_app import views

urlpatterns = [
    path('register-vehicle/', RegisterVehicleAPIView.as_view(), name='register-vehicle'),
    path('generate-quote/', GenerateQuoteAPIView.as_view(), name='generate-quote'),
    path('get-services/', GetServicesAPIView.as_view(), name='get-services'),
    path('vehicle-makes/', views.vehicle_makes, name='vehicle-makes'),
    path('vehicle-models/<int:make_id>/', views.vehicle_models, name='vehicle-models'),
    path('windscreen-types/', views.windscreen_types, name='windscreen-types'),
    path('windscreen-customizations/<int:type_id>/', views.windscreen_customizations, name='windscreen-customizations'),
    path('insurance-providers/', views.insurance_providers, name='insurance-providers'),
    path('submit-service/', SubmitServiceAPIView.as_view(), name='submit-service'),
    path('get-quotes/', GetQuotesAPIView.as_view(), name='get-quotes'),
    path('orders/', GetApprovedOrdersAPIView.as_view(), name='get-approved-orders'),
    path("quotes/<int:pk>/update-status/", ApproveQuoteAPIView.as_view(), name="update-quote-status"),
    path("orders/create/", CreateOrderAPIView.as_view(), name='create-order'),
    path('work-progress/submit/', SubmitWorkProgressAPIView.as_view(), name='submit-work-progress'),
    path('orders/<str:vehicle_reg_no>/', GetOrderDetailsAPIView.as_view(), name='get-order-details'),
]
