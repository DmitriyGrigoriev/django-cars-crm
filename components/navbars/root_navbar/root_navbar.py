from django_components import component

@component.register("root-navbar")
class root_navbar(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found.
    # To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "navbars/root_navbar/root_navbar.html"