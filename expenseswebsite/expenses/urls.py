from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='expenses'),
    path('add-expense', views.add_expense, name='add-expenses'),
    path('edit-expense/<int:pk>', views.expense_edit, name='expense-edit'),
    path('expense-delete/<int:pk>', views.delete_expense, name='expense-delete'),
]
