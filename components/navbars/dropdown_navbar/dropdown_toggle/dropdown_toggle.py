from django_components import component

@component.register("dropdown-toggle")
class root_navbar_item(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found.
    # To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "navbars/dropdown_navbar/dropdown_toggle/dropdown_toggle.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(self, item_ref):
        return {
            "href": item_ref
        }