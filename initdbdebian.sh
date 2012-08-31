#!/usr/bin/env bash
TOPDIR=$(python -c "print '$PWD'.split('/')[-1]")
sudo -u postgres dropdb fixmystreet
sudo -u postgres createdb -T template_postgis -O fixmystreet fixmystreet
echo 'alter user fixmystreet with superuser' | sudo -u postgres psql
./bin/fixmystreet_manage syncdb --noinput
./bin/fixmystreet_manage createsuperuser --username=fixmystreet --email=foo@bar.com
./bin/fixmystreet_manage loaddata $PWD/makina.json
./bin/fixmystreet_manage loaddata $PWD/lemans.json
./bin/fixmystreet_manage loaddata $PWD/tunis.json
./bin/fixmystreet_manage loaddata $PWD/api.json
# vim:set et sts=4 ts=4 tw=80:
