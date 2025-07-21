from django.contrib import admin
from .models import ChaiVarites,ChaiReview,Store,ChaiCertificate

# Register your models here.

# class for review
class ChaiReviewInLine(admin.TabularInline):
    model = ChaiReview
    extra =2

class ChaiVaritesAdmin(admin.ModelAdmin):
    list_display = ('name','type','date_added',)
    inlines = [ChaiReviewInLine]
    
# class for store
class StoreAdmin(admin.ModelAdmin):
    list_display= ('name','location')
    filter_horizontal = ('chai_varities',)
    

# class for certificate 
class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display=('chai','certificate_number')
     


admin.site.register(ChaiVarites,ChaiVaritesAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)
