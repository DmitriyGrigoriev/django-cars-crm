from django_components import component


@component.register("select-assigned-to")
class AssignedTo(component.Component):
    template_name = "select_menu/assigned_to/select_assigned_to.html"

    def get_context_data(self, **kwargs):
        return kwargs

    class Media:
        js = "select_menu/assigned_to/assigned_to.js"
