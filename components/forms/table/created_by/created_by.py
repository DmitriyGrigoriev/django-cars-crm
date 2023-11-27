from django_components import component


@component.register("created-by")
class CreatedBy(component.Component):
    template_name = "forms/table/created_by/created_by.html"

    def get_context_data(self, **kwargs):
        return kwargs
