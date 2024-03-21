from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

#final touch on automating profile creation second step
    def ready(self):
        import profiles.signals