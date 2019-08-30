from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import ArticlesSerializer
from acticles.models import Articles


class ArticleListApi(ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer


class ArticleDetailApi(RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer

