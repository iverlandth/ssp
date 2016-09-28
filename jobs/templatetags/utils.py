from django import template
from datetime import datetime
register = template.Library()


@register.simple_tag
def get_verbose_field_name(instance, field_name):
    return instance._meta.get_field(field_name).verbose_name.title()


@register.simple_tag
def get_state_jobsite(status):
    return {
        'N': 'NUEVO',
        'P': 'EN PROCESO',
        'T': 'TERMINADO',
        'D': 'DETENIDO',
    }[status]


@register.simple_tag
def get_state_profile(status):
    return {
        'CLI': 'CLIENTE',
        'ADM': 'ADMINISTRADOR',
        'GER': 'GERENTE',
        'CAP': 'CAPATAZ',
        'SUP': 'SUPERVISOR',
        'STR': 'SECRETARIA',
    }[status]

@register.simple_tag
def get_state_gender(status):
    return {
        'M': 'MASCULINO',
        'F': 'FEMENINO',
    }[status]

@register.simple_tag
def get_marital(status):
    return {
        'SO': 'SOLTERO(A)',
        'CA': 'CASADO(A)',
        'VI': 'VIUDO(A)',
        'DI': 'DIVORCIADO(A)',
        'CO': 'CONCUBINO(A)',
        'SE': 'SEPARADO(A)',
        'FA': 'FALLECIDO(A)',
    }[status]

@register.simple_tag
def get_condition(status):
    return {
        'NUE': 'NUEVO',
        'ENM': 'EN MANTENIMIENTO',
        'REP': 'REPARADO',
        'NOU': 'NO USABLE',
    }[status]

@register.simple_tag
def get_category(status):
    return {
        'MOV': 'MOVILIDAD',
        'EDT': 'EQUIPO DE TRABAJO',
        'REP': 'REPARADO',
        'NOU': 'NO USABLE',
    }[status]

@register.filter()
def to_int(value):
    return int(value)

@register.filter
def index(List, i):
    count = len(List)
    if(int(i)>count-1):
        return "No registrado"
    return List[int(i)]

