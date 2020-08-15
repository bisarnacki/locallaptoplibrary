from django.contrib import admin

# Register your models here.

from .models import Manufacturer, Make, Language, Laptop, LaptopInstance

class LaptopsInstanceInline(admin.TabularInline):
    model = LaptopInstance
#    def get_extra(self, request, obj=None, **kwargs):
#    if obj.BookInstance.count() :
#        return 0
#    else:
#        return 1

class LaptopInline(admin.TabularInline):
    model = Laptop

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'display_make')
    inlines = [LaptopsInstanceInline]

# admin.site.register(Author)
# Define the admin class
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('last_name')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [LaptopInline]

# Register the admin class with the associated model
admin.site.register(Manufacturer, ManufacturerAdmin)

admin.site.register(Make)
admin.site.register(Language)
@admin.register(LaptopInstance)
class LaptopInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('laptop', 'status', 'due_back', 'id')

    fieldsets = (
        (None, {
            'fields': ('laptop', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )



