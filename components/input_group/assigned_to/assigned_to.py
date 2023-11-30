from django_components import component


@component.register("assigned-to-label")
class AssignedToLabel(component.Component):
    template_name = "input_group/assigned_to/assigned_to.html"

    def get_context_data(self, **kwargs):
        return kwargs

    class Media:
        css = "input_group/assigned_to/assigned_to.css"
