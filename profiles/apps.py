from django.apps import AppConfig

"""
 After overriding ready method with signals go to init.py
 
"""


class ProfilesConfig(AppConfig):

    name = 'profiles'

    def ready(self):
        import profiles.signals
