from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    # 继承原始分页,设置自定义分页参数,已在settings中配置全局默认分页配置

    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 20
