from django.db import models

# Create your models here.

# 省市区的模型
class Area(models.Model):
    """
    两个自关联关系
    """
    name = models.CharField(max_length=20, verbose_name='名称')

    # ForeignKey('self') 自关联,related_name 可以设置 反向关联的属性名 默认是关联模型类名小写_set
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='subs',null=True, blank=True, verbose_name='上级行政区划')

    class Meta:
        db_table = 'tb_areas'
        verbose_name = '行政区划'
        verbose_name_plural = '行政区划'

    def __str__(self):
        return self.name