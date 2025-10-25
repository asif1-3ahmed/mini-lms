# courses/views.py
from rest_framework import generics, permissions
from .models import Course
from .serializers import CourseSerializer

# List and Create Courses (accessible only by authenticated users)
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

# Retrieve, Update, Destroy a course (accessible only by authenticated users)
class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
