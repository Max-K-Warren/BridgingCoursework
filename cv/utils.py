from .models import CV_Item, CV_Category

def CVStructureMaker():
    categories = list(CV_Category.objects.order_by('position'))
    template_dict = []
    for cat in categories:
        template_dict.append([cat, list(CV_Item.objects.filter(CV_Category__exact=cat.id).order_by('position'))])
    return template_dict

