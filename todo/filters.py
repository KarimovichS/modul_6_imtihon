import django_filters
from .models import Todo


class TodoFilters(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    create_at = django_filters.DateTimeFilter(
        name="start_time",
        lookup_type="lte")
    due_date = django_filters.DateTimeFilter(
        name="start_time",
        lookup_type="gte")

    class Meta:
        model_ = Todo
        fields = ['title']
