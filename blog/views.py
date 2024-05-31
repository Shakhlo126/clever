from rest_framework import generics, viewsets
from .models import (Pages,
                     Blog_category,
                     Blog,
                     Upcoming_events,
                     Course_category,
                     Course,
                     Cards,
                     Instructor)
# Create your views here.
from .serializers import (Pages_serializer,
                          Blog_category_serializer,
                          Blog_serialzer,
                          Upcoming_events_serializer,
                          Cource_category_serializer,
                          Cource_serializer,
                          Instructor_serializer,
                          Cards_serializer)

class PagesAPIView(generics.ListAPIView):
    queryset = Pages.objects.all()
    serializer_class = Pages_serializer

class Blog_categoryAPIView(generics.ListAPIView):
    queryset = Blog_category.objects.all()
    serializer_class = Blog_category_serializer

class BlogAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blog_serialzer

class Upcoming_eventsAPIView(generics.ListAPIView):
    queryset = Upcoming_events.objects.all()
    serializer_class = Upcoming_events_serializer

class Course_categoryAPIView(generics.ListAPIView):
    queryset = Course_category.objects.all()
    serializer_class = Cource_category_serializer

class CourseAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = Cource_serializer

class CardsAPIView(generics.ListAPIView):
    queryset = Cards.objects.all()
    serializer_class = Cards_serializer

class InstructorAPIView(generics.ListAPIView):
    queryset = Instructor.objects.all
    serializer_class = Instructor_serializer
