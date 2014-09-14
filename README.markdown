django-colorful
===============

**django-colorful** is an extension to the Django web framework that provides
database and form color fields (only RGB atm).

Written by Simon Charette
Inspired by http://djangosnippets.org/snippets/1261/
Built with https://github.com/laktek/really-simple-color-picker

Changes
-------------

1. Updated *jquery.colorPicker.js* to last version.
2. You can set options in ``attrs`` when defining ``ColorFieldWidget``. See usage below.

Install
-------------

The extension will take care of providing the custom widget, just make sure you include the static files and jQuery >= 1.2.

Install

    pip install git+https://github.com/proft/django-colorful.git#egg=django-colorful

Add ``'colorful'`` to project's ``INSTALLED_APPS``.

Usage
-------------
In order to use a color field you just have to add it to your model definition:

    from django.db import models
    from colorful.fields import RGBColorField

    class Tag(models.Model)
      color = RGBColorField()

Redefining options

    class BookForm(forms.ModelForm):
        class Meta:
            model = Book

        def __init__(self, *args, **kwargs):
            super(BookForm, self).__init__(*args, **kwargs)
            self.fields['color'].widget = ColorFieldWidget(
                attrs={'options': '{showHexField: false}'}
            )

    class BookAdmin(admin.ModelAdmin):
        form = BookForm

