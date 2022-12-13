from django.urls import path
from . import views
urlpatterns = [
 path('Info/', views.index, name='index'),
 path('skills/', views.skills, name='skills'),
 path('diploma/', views.iploma, name='diploma'),
 path('internships/', views.internship, name='internships'),
 path('change/', views.change, name='change'),
 path('change/del_s/<int:id>', views.del_s, name='del_s'),
 path('change/del_i/<int:id>', views.del_i, name='del_i'),
 path('change/del_d/<int:id>', views.del_d, name='del_d'),
 path('change/update_s/<int:id>', views.update_s, name='update_s'),
 path('change/update_s/update_s_action/<int:id>',views.update_s_action, name='update_s_action'),
 path('change/update_i/<int:id>', views.update_i, name='update_i'),
 path('change/update_i/update_i_action/<int:id>',views.update_i_action, name='update_i_action'),
 path('change/update_d/<int:id>', views.update_d, name='update_d'),
 path('change/update_d/update_d_action/<int:id>',views.update_d_action, name='update_d_action'),
 path('change/addS/', views.adds, name='adds'),
 path('change/addS/add_s/', views.add_s, name='add_s'),
 path('change/addI/', views.addi, name='addi'),
 path('change/addI/add_i/', views.add_i, name='add_i'),
 path('change/addD/', views.addd, name='addd'),
 path('change/addD/add_d/', views.add_d, name='add_d'),
]