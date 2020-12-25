from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationManual(PageNumberPagination):
    page_query_param = 'p'
    # 默认情况下每一页显示的条数为2
    page_size = 5
