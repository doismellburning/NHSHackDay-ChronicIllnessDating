from django.contrib import admin
from nhshd.models import Patient, Place, Interest, Symptom, Photo

admin.site.register(Patient)
admin.site.register(Place)
admin.site.register(Interest)
admin.site.register(Symptom)
admin.site.register(Photo)
