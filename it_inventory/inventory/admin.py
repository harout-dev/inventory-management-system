from django.contrib import admin

from inventory.models import Laptop , Mobile , Tab , Sim
from employees.models import Employee
from import_export.admin import ImportExportModelAdmin

class LaptopAdmin(admin.ModelAdmin):
    list_display = ['id', 'manufacturer','serial_number','ram','processor','purchased_date','employee_name','handover_date']
    search_fields = ('serial_number', 'employee_name',)
    
class MobileAdmin(admin.ModelAdmin):
    list_display = ['id', 'manufacturer','serial_number','purchased_date','employee_name','handover_date']

class TabAdmin(admin.ModelAdmin):
    list_display = ['id', 'manufacturer','serial_number','purchased_date','employee_name','handover_date']

class SimAdmin(admin.ModelAdmin):
    list_display = ['operator','sim_number','line_number','sim_type','sim_status']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','mobile','location','title','department','project','email']

class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )
        

admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Mobile, MobileAdmin)
admin.site.register(Tab, TabAdmin)
admin.site.register(Sim, SimAdmin)
admin.site.register(Employee, EmployeeAdmin)
