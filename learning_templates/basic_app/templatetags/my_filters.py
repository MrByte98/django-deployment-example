from django import template


register = template.Library()


def cut (value,args):

    return value.replace(args,'')






register.filter('cut',cut)