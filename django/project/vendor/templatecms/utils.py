from django.core.cache import cache
from .models import Copy


def get_copy_dict(skip_cache=False):

    def get_copy_dict_from_db():
        copy_model, _ = Copy.objects.get_or_create(id=1)
        copy_dict = copy_model.copy if copy_model.copy else {}
        return copy_dict

    if skip_cache:
        return get_copy_dict_from_db()
    return cache.get_or_set("copy_dict", get_copy_dict_from_db)
