#!/usr/bin/env bash
TOPDIR=$(python -c "print '$PWD'.split('/')[-1]")
cd $(dirname $0)
if [[ ! -e sys/var/data/postgresql ]];then
    ../../bin/paster create -t minitage.instances.postgresql\
        $TOPDIR  \
        db_name=fixmystreet \
        db_user=fixmystreet \
        db_password=fixmystreet \
        db_host=127.0.0.1 \
        db_port=30007 \
        --no-interactive;
    sys/etc/init.d/makina.fixmystreet_postgresql.fixmystreet restart
    sleep 4
fixmystreet.createdb  -U $(whoami) template_postgis -O fixmystreet
    fixmystreet.psql  -U $(whoami) template_postgis < ../../dependencies/postgresql-9.1/parts/part/share/contrib/postgis-1.5/postgis.sql
    fixmystreet.psql  -U $(whoami) template_postgis < ../../dependencies/postgresql-9.1/parts/part/share/contrib/postgis-1.5/spatial_ref_sys.sql
fi
fixmystreet.dropdb -U $(whoami)   fixmystreet
fixmystreet.createdb -U $(whoami) fixmystreet -T template_postgis -O fixmystreet
echo 'alter user fixmystreet with superuser' | fixmystreet.psql  -U $(whoami)
./bin/fixmystreet_manage syncdb --noinput
./bin/fixmystreet_manage createsuperuser --username=k --email=mpa@makina-corpus.com
./bin/fixmystreet_manage loaddata $PWD/makina.json
./bin/fixmystreet_manage loaddata $PWD/lemans.json
# vim:set et sts=4 ts=4 tw=80:
