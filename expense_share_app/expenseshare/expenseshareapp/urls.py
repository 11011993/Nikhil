from django.urls import include, path
from expenseshareapp import views 



urlpatterns = [
    path('api/insert-amount-participants/', views.Amountandparticipants.as_view()),
    path('api/participants-payable-part/', views.expensecalculation.as_view()),
    path('api/user-register/', views.userregister.as_view()),
    path('api/flipcart-sale/', views.flipcartsaleowe.as_view()),
    path('api/third-installment/', views.thirdinstallmentowe.as_view()),
    ]