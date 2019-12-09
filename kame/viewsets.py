from starlette.endpoints import HTTPEndpoint

from kame.routers import templates


class GenericView(HTTPEndpoint):

    async def get(self, request):
        return templates.TemplateResponse("base.html", {'request': request, "path" :"path", "basename": "basename"})


class ModelViewSet(GenericView):

    async def get(self, request):
        #print(self.queryset)

        instance_id = request.path_params.get('id', None)
        if instance_id:
            print("INSTANCE ID FOUND!!!")
            objects = await self.queryset().filter(id=int(instance_id))
        else:
            objects = await self.queryset()

        serializer = self.serializer_class(objects)
        serializer_meta = self.serializer_class.Meta()
        serializer.meta = serializer_meta

        return templates.TemplateResponse("generic.html", {'request': request, "serializer": serializer})
