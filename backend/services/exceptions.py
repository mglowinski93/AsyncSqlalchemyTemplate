class FailedToSaveTemplate(Exception):
    def __init__(self, message="Failed to save template"):
        self.message = message
        super().__init__(self.message)


class TemplateDoesntExist(Exception):
    def __init__(self, template_id):
        self.template_id = template_id
