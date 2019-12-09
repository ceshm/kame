# Kame

Async REST framework for tortoise-orm and starlette

## Requirements

- python>=3.6
- [starlette](https://www.github.com/encode/starlette)
- [tortoise-orm](https://www.github.com/tortoise/tortoise-orm)

## Installation
```
pip install kame
```

## Usage

Having the following tortoise model:
```python
from tortoise.models import Model
from tortoise import fields

class Tour(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    data = fields.JSONField(default=dict)

    def __str__(self):
        return self.name
```

1. Create a serializer
```python
from kame import serializers

class TourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tour
        fields = ['id', 'name', 'description', 'parent', 'active', 'image', 'descendant_ids']
```

2. Create a viewset
```python
from kame import viewsets

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.all
    serializer_class = TourSerializer

```

3. Register a route
```python
from kame import routers

router = routers.DefaultRouter()

router.register('/tours', TourViewSet, basename="tour")
```
