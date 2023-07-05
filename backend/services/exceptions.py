class TemplateDoesntExist(Exception):
    def __init__(self, template_id):
        self.template_id = template_id
