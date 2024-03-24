from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

import pprint
class ParentForm(forms.Form):
    def addError(self, message):
        self._errors[NON_FIELD_ERRORS] = self.error_class([message])

class SigninForm(ParentForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(render_value=False),
    )

    form_name = 'signin_form'
    ng_scope_prefix = 'signinform'

class UserForm(ParentForm):
    name = forms.CharField(required=True, min_length=3)
    email = forms.EmailField(required=True)
    password = forms.CharField(
        required=True,
        label=(u"Password"),
        widget=forms.PasswordInput(render_value=False),
        
    )
    ver_password = forms.CharField(
        required=True,
        label=(u"Password Verification"),
        widget=forms.PasswordInput(render_value=False),
    )
    
    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get("password")
        ver_password = cleaned_data.get("ver_password")
        if password != ver_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

    form_name = "user_form"
    ng_scope_prefix = "userform"

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            attrs = {"ng-model": "%s.%s" % (self.ng_scope_prefix, name)}

            if field.required:
                attrs.update({"required": "true"})
            if field.min_length:
                attrs.update({"min-length": field.min_length})
            field.widget.attrs.update(attrs)