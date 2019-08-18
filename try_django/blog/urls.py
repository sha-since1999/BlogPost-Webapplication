from django.urls import path ,re_path  #url


from .views import(
                        blog_post_detail_page,
                        blog_post_list_view,
                        blog_post_update_view,
                        blog_post_delete_view,
                        registrationBlog,
                        loginBlog,
                        logoutBlog,

                       
                       )



urlpatterns = [ 
    path('',blog_post_list_view),
    path('<str:slug>/',blog_post_detail_page),

    path('<str:slug>/edit/',blog_post_update_view),
    path('<str:slug>/delete/',blog_post_delete_view),
    

    #e_path(r'^download/(?P<path>.*)$',download,{'document root': settings.MEDIA_ROOT}),
    path('register',registrationBlog,name='registration'),
    path('login',loginBlog,name='login'),
    path('logout',logoutBlog,name='logout'),
   
]
