from django.http import response

# Create your views here.
from django.shortcuts import render

from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import mixins, status
from rest_framework import generics
from rest_framework import viewsets

class BaseAPI(viewsets.ViewSet):
  
     def list(self, request):
         timeline = Basetable(
             properties=Properties.objects.all(),
             dimensions=Dimensions.objects.all(),
             images=Images.objects.all(),
         )
         serializer = BasetableSerializers(timeline)
         #print(serializer)
         return Response(serializer.data)

# class PostApi(viewsets.ViewSet):
#      def list(self,request):
#         serializer=Basetable.objects.all()
#         base_list=BasetableSerializers(serializer, many=True)
#         return Response(base_list.data)

class PostAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = BasetableSerializers
    queryset = Basetable.objects.all()
    
    # querylist = [{'queryset': Properties.objects.all(), 'serializer_class': PropertiesSerializers},
    #              {'queryset': Images.objects.all(), 'serializer_class':ImagesSerializers},]
        
    # print(querylist)
    lookup_field = 'base_id'

    def get(self, request , base_id = None):
        # timeline = Basetable(
        #      #basetable=Basetable.objects.all(),
        #      properties=Properties.objects.all(),
        #      dimensions=Dimensions.objects.all(),
        #      images=Images.objects.all(),
        #  )
        # serializer = BasetableSerializers(timeline)
        #response(serializer.data)
        #print(serializer)
        if base_id:
            return self.retrieve(request)
        else:
            return self.list(request)
    

   
    def post(self, request ):
        return self.create(request)
    
    def put(self, request, base_id=None):
        return self.update(request, base_id)
    
    def delete(self, request, base_id):
        return self.destroy(request, base_id)

    


class PropertiesAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class =PropertiesSerializers
    queryset =Properties.objects.all()
   

    lookup_field = 'product_id'

    
    def get(self, request , product_id = None):
        if product_id:
            return self.retrieve(request)
        else:
            return self.list(request)
    


    def post(self, request ):
        return self.create(request)
    def put(self, request, product_id=None):
        return self.update(request, product_id)
    
    def delete(self, request, product_id):
        return self.destroy(request, product_id)

    
    
class DimensionsAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    
    serializer_class = DimensionsSerializers
    queryset = Dimensions.objects.all()

    lookup_field = 'id'

    def get(self, request , id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request ):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id)
    
    def delete(self, request, id):
        return self.destroy(request, id)

    


    
   
class ImagesAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    
    serializer_class = ImagesSerializers
    queryset = Images.objects.all()

    lookup_field = 'id'

    def get(self, request , id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request ):
        return self.create(request)
    

    def put(self, request, id=None):
        return self.update(request,id)
    
    def delete(self, request, id):
        return self.destroy(request, id)

    
# class ProductAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    
#     serializer_class = ProductSerializers
#     queryset = Product.objects.all()

#     lookup_field = 'product_id'

#     def get(self, request , product_id = None):
#         if product_id:
#             return self.retrieve(request)
#         else:
#             return self.list(request)
    
#     def post(self, request ):
#         return self.create(request)
    
    

  
