from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter, CharFilter
from django.forms import DateTimeInput
from .models import Post, Category

class PostsFilter(FilterSet):
    title = CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Headlines',
    )

    category = ModelChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        label='Category',
        empty_label='All category',
    )

    added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Date',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )


    # class Meta:
    #     model = Post
    #     fields = {
    #         'title': ['icontains'],
    #         # 'postCategory': ['exact'],
    #     }