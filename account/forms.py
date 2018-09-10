from django import forms
from .models import TenantProfile

from django.contrib.auth import get_user_model

User = get_user_model()


class TenantCreateForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class TenantProfileCreateForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        # fields = {'room_no','elec_unit','water_unit','misc_cost'}
        exclude = ['tenant', 'deduct', 'cum_ovd', 'elec_unit', 'water_unit', 'misc_cost']


class RM101A_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM102A_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM103A_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM104A_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM105A_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM106A_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM201A_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM202A_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM203A_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM204A_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM205A_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM206A_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM301A_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM302A_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM303A_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM304A_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM305A_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM306A_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM201B_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM202B_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM203B_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM204B_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM205B_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM301B_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM302B_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM303B_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM304B_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM305B_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM401B_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM402B_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM403B_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM404B_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }


class RM405B_BillForm(forms.ModelForm):
    class Meta:
        model = TenantProfile
        fields = {'elec_unit', 'water_unit', 'misc_cost'}
        widgets = {
            'elec_unit': forms.NumberInput({'class': 'eu', 'placeholder': 'elect-unit', 'min': 0}),
            'water_unit': forms.NumberInput(attrs={'class': 'wu', 'placeholder': 'water-unit', 'min': 0}),
            'misc_cost': forms.NumberInput(attrs={'class': 'mc', 'placeholder': 'misc_cost', 'min': 0})
        }
