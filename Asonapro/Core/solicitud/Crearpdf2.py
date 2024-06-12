"""


import jinja2
import pdfkit
import os


def crear_pdf2(ruta_template, info={}):
    nombre_template = os.path.basename(ruta_template)
    ruta_template = ruta_template.replace(nombre_template, '')

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
    template = env.get_template(nombre_template)
    html = template.render(info)

    options = {
        "enable-local-file-access": "",
        "margin-top": "0in",
        "margin-right": "0in",
        "margin-bottom": "0in",
        "margin-left": "0in",
        "encoding": "UTF-8"}

    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    ruta_salida = '/home/linuxlite/Desktop/Master/Core/solicitud/templates/reportes/seguimiento.pdf'
    pdfkit.from_string(html, ruta_salida,
                       configuration=config, options=options, css="/home/linuxlite/Desktop/Master/Core/solicitud/templates/reportes_css/reportes.css")
"""
