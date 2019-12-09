

class ModelSerializer:

    def __init__(self, initial_queryset):
        self.initial_queryset = initial_queryset

    def get_data(self):
        data = []
        for q_obj in self.initial_queryset:
            obj_dict = {}
            for field in self.meta.fields:
                try:
                    obj_dict[field] = getattr(q_obj, field)
                except AttributeError:
                    pass
            data.append(obj_dict)
        return data


    def get_model_name(self):
        return self.meta.model.__name__

    def decode(self):
        pass

    def encode(self):
        pass
