from django.contrib import admin

# Register your models here.


from app.models import *



# class customize(admin.ModelAdmin):
#     list_display=['ename','mgr']
#     list_display_links=['ename']
#     list_editable=['mgr']


admin.site.register(Dept)

admin.site.register(Emp)

admin.site.register(Salgrade)


