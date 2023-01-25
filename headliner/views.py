from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer

from .models import HeadlinerTable
from .serializers import HeadlinerSerializer


# class HeadlinerTemplateHTMLRender(TemplateHTMLRenderer):
#     def get_template_context(self, data, renderer_context):
#         response = renderer_context['response']
#         if response.exception:
#             data['status_code'] = response.status_code
#         return {'data': data}


class HeadlinerAPIList(generics.ListCreateAPIView):
    queryset = HeadlinerTable.objects.all()
    serializer_class = HeadlinerSerializer
    permission_classes = (IsAuthenticated, )

    # renderer_classes = [HeadlinerTemplateHTMLRender]
    # template_name = 'index.html'


class HeadlinerAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = HeadlinerTable.objects.all()
    serializer_class = HeadlinerSerializer
    permission_classes = (IsAuthenticated, )


class HeadlinerAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = HeadlinerTable.objects.all()
    serializer_class = HeadlinerSerializer
    permission_classes = (IsAuthenticated, )

