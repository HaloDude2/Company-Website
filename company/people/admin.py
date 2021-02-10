from django.contrib import admin
from django.db import models
from django.forms.widgets import ClearableFileInput 

from company.people.models import Employee, Testimonial

class ImageWidget(ClearableFileInput):
    template_name = "image_widget.html"

class PersonAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ImageField: {'widget': ImageWidget},
    }

admin.site.register(Employee, PersonAdmin)
admin.site.register(Testimonial, PersonAdmin)
