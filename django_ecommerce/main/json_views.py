from rest_framework import mixins, generics, permissions
from main.permissions import IsOwnerOrReadOnly
from main.serializers import StatusReportSerializer
from main.models import StatusReport
class StatusCollection(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

    queryset = StatusReport.objects.all()
    serializer_class = StatusReportSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class StatusMember(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):

    queryset = StatusReport.objects.all()
    serializer_class = StatusReportSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from main.serializers import StatusReportSerializer
# from main.models import StatusReport



# @api_view(['GET', 'POST'])
# def status_collection(request: HttpResponse):
#     """Get the collection of all status_reports
#     or create a new one"""
#     if request.method == 'GET':
#         status_report = StatusReport.objects.all()
#         serializer = StatusReportSerializer(status_report, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = StatusReportSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def status_member(request: HttpResponse, id):
#     """Get, update or delete a status_report instance"""
#     try:
#         status_report = StatusReport.objects.get(id=id)
#     except StatusReport.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = StatusReportSerializer(status_report)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = StatusReportSerializer(status_report, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         status_report.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)