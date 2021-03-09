from django.contrib import admin

from inventory.models import Device

class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'device', 'manufacturer','serial_number','purchased_date','employee_name','employee_mobile','handover_date']
    


admin.site.register(Device, DeviceAdmin)
