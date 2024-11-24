import jinja2


def render_html(html_path: str, params: dict) -> str:
    template_loader = jinja2.FileSystemLoader(searchpath='./')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(html_path)
    output = template.render(params)
    return output
