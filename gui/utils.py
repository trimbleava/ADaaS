from django.conf import settings
from django.core.cache import cache
import redis, os, re


from gui import models, forms


def get_globals(request):

    facets = cache.get("facets", None)

    if not facets:
        print("gui.utils - get_globals: accessing database to get facets\n")

        facets = {
            "selected": {
                "predtype": "Hindcast",
                "eventcat": "Hurricane",
                "event": "Isabel, 2003",
                "ccmodel": "DFlow 2D",
                "scenario": "Scenario G"
            },
            "categories": {
                "predtypes": models.PredictionType.objects.all(),
                "eventcats": models.EventCat.objects.all(),
                "ccmodels": models.CCModel.objects.all(),
            },
            "drive_nodes": models.Drive.objects.all()
        }


    # if user change selections on these, update the context (see gui_main.js)

    eventchoice = request.GET.get("eventchoice")
    if eventchoice:
        facets["selected"]["event"] = eventchoice
        facets["selected"]["eventcat"] = request.GET.get("grplabel")

    modelchoice = request.GET.get("modelchoice")
    if modelchoice:
        facets["selected"]["scenario"] = modelchoice
        print("model: ", request.GET.get("grplabel"))
        facets["selected"]["ccmodel"] = request.GET.get("grplabel")

    predchoice = request.GET.get("predchoice")
    if predchoice:
        facets["selected"]["predtype"] = predchoice

    cache.set("facets", facets)
    facets = cache.get("facets")

    if settings.DEBUG:
        from pprint import pprint
        pprint(facets)

    return facets
