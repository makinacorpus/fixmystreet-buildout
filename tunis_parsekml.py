#!/usr/bin/env python
# -*- coding: utf-8 -*-
__docformat__ = 'restructuredtext en'

from copy import deepcopy
from django.template.defaultfilters import slugify
from lxml import etree
from json import dumps

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_fixmystreet.settings'
INC = 50




def xpath(root, query):
    kwargs = {}
    ns = deepcopy(root.nsmap) 
    ns['default'] = ns[None]
    del ns[None]
    kwargs['namespaces'] = ns
    return root.xpath(query, **kwargs)

def filter_coord(ret):
    ret = ret.replace('0 0',  '0').strip()
    ret = ret.replace('0 -0', '-0').strip()
    ret = ret.replace('0 ', '').strip()
    if 'e-005' in ret:
        ret = '0.0000%s' % (ret[:-5].replace('.', '').strip())
    return ret

def get_json(data):
    results = [
        {
            "pk": 3,
            "model": "django_fixmystreet.city",
            "fields": {
                "name": "Tunis",
                "slug": "tunis",
                "email": "foo@bar.com",
                "province": 3
            }
        }, 
    ]
    for i, item in enumerate(data):
        results.append({
            'pk': INC+i,
            "model": "django_fixmystreet.ward",
            "fields": {
                "number": INC+1,
                "city": 3,
                "name": item['name'],
                "slug": slugify(item['name']),
                "councillor": 7,
                "geom": item['geom'],
            } 
        }
        )
    return results


def main():
    xml = open("Tunisia divisions. Level 2.kml").read()
    root = etree.fromstring(xml)
    docs = xpath(root, '//kml:Placemark')
    results = []
    wanted = [
        u"Agareb",
        u"Akouda",
        u"Alaa",
        u"Amdoun",
        u"Ariana Médina",
        u"Ayoun",
        u"Aïn Draham",
        u"Bab Bhar",
        u"Bab Souika",
        u"Balta Bou Aouane",
        u"Bardo",
        u"Bargou",
        u"Bekalta",
        u"Belkhir",
        u"Bembla",
        u"Ben Arous",
        u"Ben Guerdane",
        u"Beni Hassen",
        u"Beni Khalled",
        u"Beni Khedache",
        u"Beni Khiar",
        u"Berges du lac",
        u"Bir Ali Ben Khélifa",
        u"Bir El Hfay",
        u"Bir Lahmar",
        u"Bir Mchergua",
        u"Bizerte Nord",
        u"Bizerte Sud",
        u"Borj El Amri",
        u"Bou Argoub",
        u"Bouarada",
        u"Bouficha",
        u"Bouhaira",
        u"Bouhajla",
        u"Boumerdès",
        u"Boumhel",
        u"Bourouis",
        u"Bousalem",
        u"Béja Nord",
        u"Béja Sud",
        u"Carthage",
        u"Chebba",
        u"Chebika",
        u"Chorbane",
        u"Chrarda",
        u"Cité El Khadra",
        u"Dahmani",
        u"Dar Chaabane El Fehri",
        u"Degueche",
        u"Dhiba",
        u"Djerba Ajim",
        u"Djerba Midoun",
        u"Douar Hicher",
        u"Douz",
        u"El Alia",
        u"El Amra",
        u"El Battan",
        u"El Ghraiba",
        u"El Jem",
        u"El Krib",
        u"El Menzah",
        u"El Mida",
        u"El Mourouj",
        u"El Ouardia",
        u"El Tahrir",
        u"Enfidha",
        u"Es Sers",
        u"Ettadhamen",
        u"Ezzahra",
        u"Ezzouhour",
        u"Fahs",
        u"Faouar",
        u"Feriana",
        u"Fernana",
        u"Fouchana",
        u"Foussana",
        u"Gaafour",
        u"Gabès Médina",
        u"Gabès Ouest",
        u"Gabès Sud",
        u"Gafsa Nord",
        u"Gafsa Sud",
        u"Ghannouch",
        u"Ghar El Melh",
        u"Ghardimaou",
        u"Ghazala",
        u"Ghomrassen",
        u"Goubellat",
        u"Grombalia",
        u"Guetar",
        u"Haffouz",
        u"Hajeb El Ayoun",
        u"Hamma",
        u"Hammam Chott",
        u"Hammam Ghezaz",
        u"Hammam Lif",
        u"Hammam Sousse",
        u"Hammamet",
        u"Haouaria",
        u"Hassi El Ferid",
        u"Hazoua",
        u"Hbira",
        u"Hencha",
        u"Hergla",
        u"Hidra",
        u"Houmt Souk",
        u"Hrairia",
        u"Jammel",
        u"Jebel Jelloud",
        u"Jebeniana",
        u"Jedaida",
        u"Jedeliane",
        u"Jelma",
        u"Jendouba Nord",
        u"Jendouba Sud",
        u"Jerissa",
        u"Joumine",
        u"Kabaria",
        u"Kairouan Nord",
        u"Kairouan Sud",
        u"Kalaa Kebira",
        u"Kalaa Khesba",
        u"Kalaa Sghira",
        u"Kalaat El Andalous",
        u"Kalaat Senan",
        u"Kasserine Nord",
        u"Kasserine Sud",
        u"Kebili Nord",
        u"Kebili Sud",
        u"Kef Est",
        u"Kef Ouest",
        u"Kelibia",
        u"Kerkennah",
        u"Kesra",
        u"Kondar",
        u"Korba",
        u"Ksar",
        u"Ksar Hellal",
        u"Ksibet El Mediouni",
        u"Ksour",
        u"Ksour Essef",
        u"La Goulette",
        u"La Marsa",
        u"Lake Ichkeul",
        u"Laroussa",
        u"M'Hamdia",
        u"M'Saken",
        u"Mahdia",
        u"Mahres",
        u"Majel Belabbes",
        u"Makthar",
        u"Manouba",
        u"Mareth",
        u"Mateur",
        u"Matmata",
        u"Matmata Nouvelle",
        u"Mazzouna",
        u"Mdhilla",
        u"Mejez El Bab",
        u"Meknassi",
        u"Melloulech",
        u"Menzel Bourguiba",
        u"Menzel Bouzaiene",
        u"Menzel Bouzelfa",
        u"Menzel Chaker",
        u"Menzel Habib",
        u"Menzel Jemil",
        u"Menzel Temime",
        u"Metlaoui",
        u"Metouia",
        u"Mnihla",
        u"Moknine",
        u"Monastir",
        u"Mornag",
        u"Mornaguia",
        u"Médenine Nord",
        u"Médenine Sud",
        u"Médina",
        u"Mégrine",
        u"Nabeul",
        u"Nadhour",
        u"Nasrallah",
        u"Nebeur",
        u"Nefta",
        u"Nefza",
        u"Nouvelle Médina",
        u"Omrane",
        u"Omrane Supérieur",
        u"Oued Ellil",
        u"Oued Mliz",
        u"Ouerdanine",
        u"Oueslatia",
        u"Ouled Chamekh",
        u"Ouled Haffouz",
        u"Oum Larais",
        u"Radès",
        u"Raoued",
        u"Ras Jebel",
        u"Redeyef",
        u"Regueb",
        u"Remada",
        u"Rouhia",
        u"Sabalat Ouled Asker",
        u"Sabkhet Sijoumi",
        u"Sahline",
        u"Sakiet Eddaier",
        u"Sakiet Ezzit",
        u"Sakiet Sidi Youssef",
        u"Samar",
        u"Saouaf",
        u"Sayada-Lamta-Bou Hjar",
        u"Sbeitla",
        u"Sbiba",
        u"Sbikha",
        u"Sebkhat Sidi El Hani",
        u"Sebkhet Ariana",
        u"Sebkhet El Moknine",
        u"Sebkhit El Kabla",
        u"Sejnane",
        u"Sened",
        u"Sfax Médina",
        u"Sfax Ouest",
        u"Sfax Sud",
        u"Sidi Aich",
        u"Sidi Ali Ben Aoun",
        u"Sidi Alouane",
        u"Sidi Bou Ali",
        u"Sidi Bouzid Est",
        u"Sidi Bouzid Ouest",
        u"Sidi El Béchir",
        u"Sidi El Heni",
        u"Sidi Hassine",
        u"Sidi Makhlouf",
        u"Sidi Thabet",
        u"Sijoumi",
        u"Siliana Nord",
        u"Siliana Sud",
        u"Skhira",
        u"Soliman",
        u"Souassi",
        u"Souk El Ahed",
        u"Souk Jedid",
        u"Soukra",
        u"Sousse Jaouhara",
        u"Sousse Médina",
        u"Sousse Riadh",
        u"Sousse Sidi Abdelhamid",
        u"Tabarka",
        u"Tajerouine",
        u"Takelsa",
        u"Tamaghza",
        u"Tataouine Nord",
        u"Tataouine Sud",
        u"Teboulba",
        u"Tebourba",
        u"Testour",
        u"Thala",
        u"Thibar",
        u"Tinja",
        u"Tozeur",
        u"Téboursouk",
        u"Unknown",
        u"Unknown1",
        u"Utique",
        u"Zaghouan",
        u"Zarzis",
        u"Zeramdine",
        u"Zriba",        
    ]
    idx = {}
    done = []
    for placemark  in docs:
        name = xpath(placemark, 'kml:name/text()')[0] 
        if not name in wanted:
            continue
        done.append(name)
        for n in ['Ezzouhour']:
            if name == n:
                if not n in idx:
                    idx[n] = 0
                idx[n] += 1
                name = '%s-%s' % (n, idx[n])
        data = {}
        data['name'] = name
        print data['name']
        try:
            raw_polygons = [a.strip()
                            for a in xpath(placemark, './/kml:coordinates/text()')]
            pointsL, pointsS, polygons = [], [], []
            for polygon in raw_polygons:
                coords = polygon.split(',')
                if coords[-1] == '0':
                    coords = coords[:-1]

                points = [(float(filter_coord(coords[2*a])), 
                           float(filter_coord(coords[2*a+1])))
                          for a in range((len(coords))/2)]
                polygons.append(
                    ' (( %s ))' % (
                        ', '.join(['%s %s' % c for c in points])
                    )
                )
                pointsL.append(points)
            data['points'] = pointsL
            data['polygons'] = polygons
            data['geom'] =  'MULTIPOLYGON (%s)' % (', '.join(polygons))
        except Exception, e:
            import pdb;pdb.set_trace()  ## Breakpoint ##
            pass
        results.append(data)
    print "Done \n%s\n" % "\n".join(done)
    print "Not done \n%s\n" % "\n".join([a for a in wanted if not a in done])
    jsonresults = get_json(results)
    f = open('tunis.json', "w")
    f.write(dumps(jsonresults, sort_keys=True, indent=4))
    f.close()
    print "exported done"
    from django.contrib.gis.geos import Point, MultiPolygon, Polygon
    from django_fixmystreet.models import Ward
    from django.db import transaction
    from django.contrib.gis.geos import GEOSGeometry as Geometry
    for i, item in enumerate(results):
        geom = item['geom']
        try:
            toto = Geometry(geom)
        except Exception, e:
            import pdb;pdb.set_trace()  ## Breakpoint ##
            print "%s FAILED VALIDATION" % geom
            raise

if __name__ == '__main__':
    main()

# vim:set et sts=4 ts=4 tw=80:
