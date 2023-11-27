from django_components import component


@component.register("label")
class Input(component.Component):
    template_name = "input_group/label/label.html"

    def get_context_data(self, **kwargs):
        return kwargs

    class Media:
        css = "input_group/label/label.css"
