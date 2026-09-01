from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'




##special method Django automatically calls once, when the app is fully loaded and ready to go. Inside it, you import your signals.py file (the act of importing it is what causes the @receiver decorator to actually run and register itself):
##ready() is a hook Django calls automatically during startup — you don't call it yourself anywhere
    def ready(self):
        import accounts.signals
