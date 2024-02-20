from . import views
from django.urls import path

urlpatterns=[
    path("",views.home,name="home"),
    path("register/",views.register_account,name="register"),
    path("login/",views.login_account,name="login"),
    path("delete/<int:pk>/",views.delete_todo_obj,name="delete-todo"),
    path("delete/wish/<int:pk>/",views.delete_wish_obj,name="delete-wish"),
    path("logout/",views.logoutuser,name="logout"),
    path("updatelist/<int:pk>/",views.update_todo_list,name="update"),
    path("updatewish/<int:pk>/",views.update_wish_list,name="update-wish")
]