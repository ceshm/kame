# Kame

Async REST framework for tortoise-orm and starlette

## Installation
```
pip install kame
```

## Usage

Having the following tortoise model:
```python
class Tour(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    data = fields.JSONField(default=dict)

    def __str__(self):
        return self.name
```

1. Create a serializer:
```python
class TourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tour
        fields = ['id', 'name', 'description', 'parent', 'active', 'image', 'descendant_ids']
```

