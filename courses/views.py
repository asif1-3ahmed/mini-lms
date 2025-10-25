from rest_framework import generics, permissions
from .models import Course
from .serializers import CourseSerializer

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # anyone can view courses, but must be authenticated to create
    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        # ensure only instructor can edit their course
        course = self.get_object()
        if self.request.user == course.instructor or self.request.user.is_superuser:
            serializer.save()
        else:
            raise permissions.PermissionDenied("You do not have permission to edit this course.")
