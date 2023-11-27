from django_components import component

@component.register("btn-filter")
class ButtonFilter(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found.
    # To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "buttons/btn_filter/btn_filter.html"

    def get_context_data(self, **kwargs):
        return kwargs