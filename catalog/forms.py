from django import forms

from catalog.models import Product, Version


class StyleForm:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] += ' form-select'


class ProductForm(StyleForm, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['creation_date', 'last_modified_date', 'owner']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        bad_names = ['казино', 'криптовалюта', 'крипта', 'биржа',
                     'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        check = False
        for bad in bad_names:
            if bad in name:
                check = True
                break

        if check:
            raise forms.ValidationError("<name> содержит запрещенные слова")

        return name


class VersionForm(StyleForm, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
