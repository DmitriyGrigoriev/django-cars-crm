from django_components import component

@component.register("progress")
class Progress(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found.
    # To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "progress/progress.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(self, **kwargs):
        return kwargs

    # class Media:
        # css = "progress/progress.css"
        # css = "progress/loader.css"
