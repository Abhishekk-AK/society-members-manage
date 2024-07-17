from django.urls import path
from members.views import show_all_members, member_detail


urlpatterns = [
    path('all/', show_all_members, name = 'show_all_members'),
    path('<int:member_id>/', member_detail, name = 'member_deatil')
    #path('<string:username>/', member_detail, name = 'member_deatil')

]

