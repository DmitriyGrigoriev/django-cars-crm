from django_components import component

@component.register("dropdown-item")
class root_navbar_item(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found.
    # To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "navbars/dropdown_navbar/dropdown_item/dropdown_item.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(self, item_ref: str, item_title: str):
        return {
            "href": item_ref,
            "title": item_title
        }