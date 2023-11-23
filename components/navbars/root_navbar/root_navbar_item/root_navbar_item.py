from django_components import component

@component.register("root-navbar-item")
class root_navbar_item(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found.
    # To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "navbars/root_navbar/root_navbar_item/root_navbar_item.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(self, item_id, item_ref, item_title):
        return {
            "id": item_id,
            "href": item_ref,
            "title": item_title
        }