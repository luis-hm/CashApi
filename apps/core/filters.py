from django_filters import rest_framework as filters

class BaseFilterSet(filters.FilterSet):
    """
    Filtro base com suporte a intervalo de datas.
    Assume que o modelo tem o campo 'created_at' (do BaseModel).
    """
    de = filters.DateFilter(field_name="created_at", lookup_expr="gte")
    ate = filters.DateFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        abstract = True
