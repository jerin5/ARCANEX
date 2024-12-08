"""ARCANEXX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', views.index),
    path('loginn', views.loginn),
    path('addexpert_trainer', views.addexpert_trainer),
    path('viewexpert_trainer', views.viewexpert_trainer),
    path('add_batch', views.add_batch),
    path('view_batch', views.view_batch),
    path('view_registered_user', views.view_registered_user),
    path('allocate_user_to_batch/<id>', views.allocate_user_to_batch),
    path('batch_allocation_to_trainer/<id>', views.batch_allocation_to_trainer),
    path('change_password', views.change_password),
    path('month_wise_report', views.month_wise_report),
    path('fee_due', views.fee_due),
    path('send_alert', views.send_alert),
    path('login_post', views.login_post),
    path('add_batch_post', views.add_batch_post),
    path('add_expert_post', views.add_expert_post),
    path('change_password_post', views.change_password_post),
    path('monthly_wise_report_post', views.monthly_wise_report_post),
    path('view_expert_trainer_post', views.view_expert_trainer_post),
    path('allocate_user_batch_post/<id>', views.allocate_user_batch_post),
    path('admin_home', views.admin_home),
    path('view_expert', views.view_expert),
    path('delete_batch/<id>', views.delete_batch),
    path('delete_expert/<id>', views.delete_expert),
    path('delete_trainer/<id>', views.delete_trainer),
    path('update_expert/<id>', views.update_expert),
    path('update_trainer/<id>', views.update_trainer),
    path('update_expert_post/<id>', views.update_expert_post),
    path('update_trainer_post/<id>', views.update_trainer_post),
    path('batch_allocation_to_trainer_post/<id>', views.batch_allocation_to_trainer_post),
    path('add_event', views.add_event),
    path('view_event', views.view_event),
    path('add_event_post', views.add_event_post),
    path('delete_event/<id>', views.delete_event),

    # expert

    path('view_and_update_expert', views.view_and_update_expert),
    path('add_tips_expert', views.add_tips_expert),
    path('add_videos_expert', views.add_videos_expert),
    path('view_expert_expert', views.view_expert_expert),
    path('view_tips_expert', views.view_tips_expert),
    path('view_videos_expert', views.view_videos_expert),
    path('change_password_expert', views.change_password_expert),
    path('expert_home', views.expert_home),
    path('view_and_update_expert_post', views.view_and_update_expert_post),
    path('add_videos_post', views.add_videos_post),
    path('add_tips_post', views.add_tips_post),
    path('change_password_expert_post', views.change_password_expert_post),
    path('delete_health_tips/<id>', views.delete_health_tips),
    path('delete_video/<id>', views.delete_video),
    path('expert_chatt/<u>', views.expert_chatt),
    path('expert_chatsnd', views.expert_chatsnd),
    path('expert_chatrply', views.expert_chatrply),

    # trainer

    path('add_attendance_trainer/<id>', views.add_attendance_trainer),
    path('add_attendance_trainer_post/<id>', views.add_attendance_trainer_post),
    path('change_password_trainer', views.change_password_trainer),
    path('trainer_home', views.trainer_home),
    path('view_allocated_batch_trainer', views.view_allocated_batch_trainer),
    path('view_update_trainer', views.view_update_trainer),
    path('view_user_trainer/<id>', views.view_user_trainer),
    path('chatt/<u>', views.chatt),
    path('chatsnd', views.chatsnd),
    path('chatrply', views.chatrply),
    path('blog', views.blog),
    path('add_fee', views.add_fee),
    path('add_fee_post', views.add_fee_post),
    path('view_fee', views.view_fee),
    path('edit_fee/<id>', views.edit_fee),
    path('edit_fee_post/<id>', views.edit_fee_post),
    path('delete_fee/<id>', views.delete_fee),
    path('update_health_details/<id>', views.update_health_details),
    path('update_health_details_post/<id>', views.update_health_details_post),
    path('login_index', views.login_index),
    path('chat/<id>', views.chat),
    path('chat_post/<id>', views.chat_post),
    path('logout',views.logout),

    # User android

    path('and_login', views.and_login),
    path('add_user', views.add_user),
    path('change_password_user', views.change_password_user),
    path('and_view_profile', views.and_view_profile),
    path('and_view_allocate_trainer', views.and_view_allocate_trainer),
    path('and_view_expert', views.and_view_expert),
    path('and_health_tips', views.and_health_tips),
    path('and_event', views.and_event),
    path('and_health_details', views.and_health_details),
    path('and_attendance', views.and_attendance),
    path('and_video', views.and_video),
    path('and_pay_payment_alert', views.and_pay_payment_alert),
    path('add_chat', views.add_chat),
    path('view_chat', views.view_chat),
    path('expert_add_chat', views.expert_add_chat),
    path('expert_view_chat', views.expert_view_chat),
    path('and_view_fee', views.and_view_fee),
    path('android_online_payment', views.android_online_payment),
    path('android_view_payment_alerts', views.android_view_payment_alerts),
]
