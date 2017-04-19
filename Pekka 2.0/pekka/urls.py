from django.conf.urls import url
from . import views

app_name = 'pekka'

urlpatterns = [
    # login and register
    url(r'^$', views.login_user, name='login_user'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    # main views
    url(r'^ask/$', views.ask, name='ask'),
    url(r'^answer/$', views.answer, name='answer'),
    url(r'^about/$', views.about, name='about'),
    # question and voting
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<answer_id>[0-9]+)/vote_answer/$', views.vote_answer, name='vote_answer'),
    url(r'^(?P<question_id>[0-9]+)/vote_question/$', views.vote_question, name='vote_question'),
    # courses
    url(r'^TDT4140_a/$', views.TDT4140_a, name='TDT4140_a'),
    url(r'^TDT4110_a/$', views.TDT4110_a, name='TDT4110_a'),
    url(r'^TDT4145_a/$', views.TDT4145_a, name='TDT4145_a'),
    url(r'^TDT4180_a/$', views.TDT4180_a, name='TDT4180_a'),
    url(r'^TTM4100_a/$', views.TTM4100_a, name='TTM4100_a'),

    url(r'^TDT4140_q/$', views.TDT4140_q, name='TDT4140_q'),
    url(r'^TDT4110_q/$', views.TDT4110_q, name='TDT4110_q'),
    url(r'^TDT4145_q/$', views.TDT4145_q, name='TDT4145_q'),
    url(r'^TDT4180_q/$', views.TDT4180_q, name='TDT4180_q'),
    url(r'^TTM4100_q/$', views.TTM4100_q, name='TTM4100_q'),

    url(r'^TTM4100_b/$', views.TTM4100_b, name='TTM4100_b')
]