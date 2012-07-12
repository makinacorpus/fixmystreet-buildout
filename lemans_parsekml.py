#!/usr/bin/env python
# -*- coding: utf-8 -*-
__docformat__ = 'restructuredtext en'

from copy import deepcopy
from django.template.defaultfilters import slugify
from lxml import etree
from json import dumps

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_fixmystreet.settings'
INC = 20




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
            "pk": 2,
            "model": "django_fixmystreet.city",
            "fields": {
                "name": "Le Mans",
                "slug": "lemans",
                "email": "foo@bar.com",
                "province": 2
            }
        }, 
    ]
    for i, item in enumerate(data):
        results.append({
            'pk': INC+i,
            "model": "django_fixmystreet.ward",
            "fields": {
                "number": INC+1,
                "city": 2,
                "name": item['name'],
                "slug": slugify(item['name']),
                "councillor": 7,
                "geom": item['geom'],
            } 
        }
        )
    return results


def main():
    xml = open("CANTONS_72.kml").read()
    root = etree.fromstring(xml)
    docs = xpath(root, '//kml:Placemark')
    results = []
    for placemark  in docs:
        data = {}
        data['name'] = xpath(placemark, 'kml:name/text()')[0]
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
    jsonresults = get_json(results)
    f = open('lemans.json', "w")
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
