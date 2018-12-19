from django.contrib import admin
from .models import Doctor, Nurse, Patient, Floor, Setting, Division
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter



try:
    admin.site.site_header = Setting.objects.first().Hospital_Name
except:
    admin.site.site_header = 'The Nairobi South Hospital'
admin.site.site_title = 'Nairobi South'


class CustomUserAdmin(UserAdmin):
    list_display = ['username', ]
    pass


# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)


class PatientAdmin(admin.ModelAdmin):

    list_display = ['Name', 'Room', 'Floor', 'Doctor_Attending', 'Nurse_Attending', 'Division']
    # list_filter = [('Floor', RelatedDropdownFilter), ('Division', RelatedDropdownFilter), ('Doctor_Attending', RelatedDropdownFilter),
    #               ('Nurse_Attending', RelatedDropdownFilter), 'Discharged']
    list_filter = ['Floor', 'Division', 'Doctor_Attending', 'Nurse_Attending', 'Discharged']


    def get_queryset(self, request):
        qs = super(PatientAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(Floor=request.user.floor)


class DoctorAdmin(admin.ModelAdmin):

    list_display = ['Name', 'get_patient_count']


class NurseAdmin(admin.ModelAdmin):

    list_display = ['Name', 'get_patient_count']


class FloorAdmin(admin.ModelAdmin):

    list_display = ['Name', 'Shift_Leader', 'get_patient_count', 'get_division_count']


admin.site.register(Setting)
admin.site.register(Floor, FloorAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Nurse, NurseAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Division)