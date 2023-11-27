from django_components import component


@component.register("assigned-to")
class AssignedTo(component.Component):
    template_name = "forms/table/assigned_to/assigned_to.html"

    def get_context_data(self, **kwargs):
        return kwargs

    # class Media:
    #     js = "select_menu/assigned_to/assigned_to.js"
