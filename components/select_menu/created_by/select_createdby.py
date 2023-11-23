from django_components import component


@component.register("select-created-by")
class CreatedBy(component.Component):
    template_name = "select_menu/created_by/select_createdby.html"

    def get_context_data(self, **kwargs):
        return kwargs
