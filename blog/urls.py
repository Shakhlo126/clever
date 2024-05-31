from django.urls import path

from .views import (PagesAPIView,
                    Blog_categoryAPIView,
                    BlogAPIView,
                    Upcoming_eventsAPIView,
                    Course_categoryAPIView,
                    CourseAPIView,
                    CardsAPIView,
                    InstructorAPIView
)

urlpatterns =[
    path('pages/', PagesAPIView.as_view(), name='pages'),
    path('blog_category/', Blog_categoryAPIView.as_view(), name='blog_category'),
    path('blog/', BlogAPIView.as_view() , name='blog'),
    path('events/', Upcoming_eventsAPIView.as_view(), name='events'),
    path('course_catgory', Course_categoryAPIView.as_view(), name='course_category'),
    path('course/', CourseAPIView.as_view(), name='course'),
    path('cards/',CardsAPIView.as_view(), name='cards'),
    path('instructor/', InstructorAPIView.as_view(), name='instructor')
]