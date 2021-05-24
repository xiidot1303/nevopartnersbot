from django.apps import AppConfig

class func(AppConfig):
    name = 'hello'
    #label = 'any_unique_name'
    def ready(self):
        from scheduled_job import updater
        updater.start()