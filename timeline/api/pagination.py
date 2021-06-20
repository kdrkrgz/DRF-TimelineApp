from rest_framework import pagination


class SmallPagination(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = "sayfa"


class LargePagination(pagination.PageNumberPagination):
    page_size = 50
    page_query_param = "sayfa"
