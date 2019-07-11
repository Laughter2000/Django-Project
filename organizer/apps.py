from django.apps import AppConfig


class OrganizerConfig(AppConfig):
    name = 'organizer'

    def ready(self):
        import organizer.signals