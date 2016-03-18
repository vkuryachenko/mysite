from django.contrib import admin
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from cuser.models import CUser


class UserCreationForm(forms.ModelForm):

    class Meta:
        model = CUser
        fields = ('email',)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    class Meta:
        model = CUser
        fields = ('email', 'date_joined', 'is_active', 'is_admin')

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Personal info', {'fields': ('date_joined',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(CUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)