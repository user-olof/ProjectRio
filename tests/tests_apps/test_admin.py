from django.test import TestCase
from django.apps import apps
from django.contrib import admin



class AdminTest(TestCase):
    def test_all_models_are_registered(self):
        models = apps.get_models()
        for m in models:
            s = str(m)
            i0 = s.find("\'") + 1
            i1 = s.rfind("\'")
            if i0 < i1:
                cls_name = s[i0:i1]
            else:
                raise Exception("Could not find single quote inside the string")
            
            if not cls_name.startswith('django'):
                self.assertIs(  True, 
                                admin.site.is_registered(m), 
                                msg=f'Did you forget to register the "{m.__name__}" in the django-admin?' )




