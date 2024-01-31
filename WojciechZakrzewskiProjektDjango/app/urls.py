from django.urls import path
from .views import TodoList, CreateItem, UpdateItem, DeleteItem, Login, LogoutView, Register

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path("register/", Register.as_view(), name="register"),
    path("", TodoList.as_view(), name="todolist"),
    path("createitem/", CreateItem.as_view(), name="createitem"),
    path("updateitem/<int:pk>/", UpdateItem.as_view(), name="updateitem"),
    path("deleteitem/<int:pk>/", DeleteItem.as_view(), name="deleteitem"),
]   