from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, *kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control w-25"

    class Meta:
        model = Vehicle
        exclude = ('user',)