from rest_framework import viewsets
from .models import Essay
from .serializers import EssaySerializer
from rest_framework.filters import SearchFilter

class PostViewSet(viewsets.ModelViewSet):
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer

    # SearchFilter
    filter_backends = [SearchFilter]
    search_fields = ('title', 'body')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # 현재 request를 보낸 유저
    # == self.request.user

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_authenticated:
            qs = qs.filter(author = self.request.user)
        else : 
            qs = qs.none()
        return qs