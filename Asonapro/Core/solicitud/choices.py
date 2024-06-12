# estado de aprobacion por la administracion
aprobado_choices = (
    ('APROBADA', 'APROBADA'),
    ('ESPERA', 'ESPERA'),
)

# Tipo de Documento (V, E, P, T)  Venezolano (V), Pasaporte (P) o Extranjero (E)
tipo_documento = (
    ('VENEZOLANO', 'V'),
    ('EXTRANJERO', 'E'),
    ('PASAPORTE', 'P'),
)

sexo = (
    ('M', 'MASCULINO'),
    ('F', 'FEMENINO'),
)


municipios = (
    ('Agua Blanca', 'AGUA BLANCA'),
    ('ARAURE', 'ARAURE'),
    ('ESTELLER', 'ESTELLER'),
    ('GUANARE', 'GUANARE'),
    ('GUANARITO', 'GUANARITO'),
    ('JOSÉ VICENTE DE UNDA', 'JOSÉ VICENTE DE UNDA'),
    ('OSPINO', 'OSPINO'),
    ('PAPELÓN', 'PAPELÓN'),
    ('SAN GENARO DE BOCONOÍTO', 'SAN GENARO DE BOCONOÍTO'),
    ('SAN RAFAEL DE ONOTO', 'SAN RAFAEL DE ONOTO'),
    ('SANTA ROSALÍA', 'SANTA ROSALÍA'),
    ('SUCRE', 'SUCRE'),
    ('TURÉN', 'TURÉN'),



)


MUNICIPIOS_PORTUGUESA = (
    ('Agua Blanca', 'AGUA BLANCA'),
    ('ARAURE', 'ARAURE'),
    ('ESTELLER', 'ESTELLER'),
    ('GUANARE', 'GUANARE'),
    ('GUANARITO', 'GUANARITO'),
    ('JOSÉ VICENTE DE UNDA', 'JOSÉ VICENTE DE UNDA'),
    ('OSPINO', 'OSPINO'),
    ('PAPELÓN', 'PAPELÓN'),
    ('SAN GENARO DE BOCONOÍTO', 'SAN GENARO DE BOCONOÍTO'),
    ('SAN RAFAEL DE ONOTO', 'SAN RAFAEL DE ONOTO'),
    ('SANTA ROSALÍA', 'SANTA ROSALÍA'),
    ('SUCRE', 'SUCRE'),
    ('TURÉN', 'TURÉN'),
)


# Lista de estados de Venezuela
ESTADOS_VENEZUELA = (
    ('Amazonas', 'Amazonas'),
    ('Anzoátegui', 'Anzoátegui'),
    ('Apure', 'Apure'),
    ('Aragua', 'Aragua'),
    ('Barinas', 'Barinas'),
    ('Bolívar', 'Bolívar'),
    ('Carabobo', 'Carabobo'),
    ('Cojedes', 'Cojedes'),
    ('Delta Amacuro', 'Delta Amacuro'),
    ('Falcón', 'Falcón'),
    ('Guárico', 'Guárico'),
    ('Lara', 'Lara'),
    ('Mérida', 'Mérida'),
    ('Miranda', 'Miranda'),
    ('Monagas', 'Monagas'),
    ('Nueva Esparta', 'Nueva Esparta'),
    ('Portuguesa', 'Portuguesa'),
    ('Sucre', 'Sucre'),
    ('Táchira', 'Táchira'),
    ('Trujillo', 'Trujillo'),
    ('Vargas', 'Vargas'),
    ('Yaracuy', 'Yaracuy'),
    ('Zulia', 'Zulia'),
)
FUENTES_AGUA = (
    ('laguna', 'Laguna'),
    ('rio', 'Rio'),
    ('manantial', 'Manantial'),
    ('quebrada', 'Quebrada'),
    ('morichal', 'Morichal'),
)

MOTIVO_CHOICES = [
    ('urgente', 'Urgente'),
    ('rutina', 'Rutina'),
]

RECOMENDACION = [
    ('si', 'Si'),
    ('no',   'No'),
]
