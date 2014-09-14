# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms.widgets import TextInput
from django.utils.safestring import mark_safe


class ColorFieldWidget(TextInput):
    class Media:
        css = {
            'all': ("colorful/colorPicker.css",)
        }
        js = ("colorful/jquery.colorPicker.js",)

    input_type = 'text'

    def __init__(self, attrs={}):
        self.options = attrs.get('options', {})
        super(ColorFieldWidget, self).__init__(attrs)

    def render_script(self, id, options):
        return '''<script type="text/javascript">
                    (function($){
                        $(document).ready(function(){
                            $('#%s').colorPicker(%s);
                        });
                    })('django' in window ? django.jQuery: jQuery);
                </script>
                ''' % (id, options)

    def render(self, name, value, attrs={}):
        if 'id' not in attrs:
            attrs['id'] = "id_%s" % name
        render = super(ColorFieldWidget, self).render(name, value, attrs)
        return mark_safe("%s%s" % (render, self.render_script(attrs['id'], self.options)))
