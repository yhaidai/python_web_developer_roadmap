from rest_framework.pagination import PageNumberPagination


class StandardPageNumberPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"  # allows the client to set the page size on a per-request basis
    max_page_size = 100
