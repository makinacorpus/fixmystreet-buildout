#!/usr/bin/env bash
cd $(dirname $0)/..
PROJECT="makina.fixmystreet"
IMPORT_URL="ssh://gitorious-git@gitorious.makina-corpus.net/makinacorpusfixmystreet-buildout.git"
cd $(dirname $0)/..
[[ ! -d t ]] && mkdir t
rm -rf t/*
tar xzvf $(ls -1t ~/cgwb/$PROJECT*z|head -n1) -C t
files="
.gitignore
bootstrap.py
buildout-dev.cfg
buildout-prod.cfg
minitage.buildout-dev.cfg
minitage.buildout-prod.cfg
README.*
etc/
"
rsync -azv t/minilays/makina.fixmystreet/ minilays/makina.fixmystreet/
for f in $files;do
    rsync -aKzv t/$f $f
done
core="tests/base.py
configure.zcml
profiles/default/metadata.xml"
core_folder="src.mrdeveloper/$PROJECT.core"
if [[ ! -e $core_folder ]];then
    core_folder="src/$PROJECT.core"
fi
#for i in $core;do
#    rsync -azKv t/src/$PROJECT.core/src/$PROJECT/core/$i src.mrdeveloper/$PROJECT.core/src/$PROJECT/core/$i
#done
EGGS_IMPORT_URL="${IMPORT_URL//\/$PROJECT\.buildout}"
#sed -re "/\[sources\]/{
#        a $PROJECT.core =  git $EGGS_IMPORT_URL/$PROJECT.core
#}" -i  etc/project/sources.cfg
#sed -re "s:(src/)?$PROJECT\.((skin)|(tma)|(core)|(testing))::g" -i etc/project/$PROJECT.cfg
#sed -re "/auto-checkout \+=/{
#        a \    $PROJECT.core
#}"  -i etc/project/sources.cfg
#sed -re "/eggs \+=.*buildout:eggs/{
#        a \    $PROJECT.core
#}"  -i etc/project/$PROJECT.cfg
#sed -re "/zcml \+=/{
#        a \    $PROJECT.core
#}"  -i etc/project/$PROJECT.cfg
sed -re "s/.*:default/    ${PROJECT}.core:default/g" -i  etc/project/$PROJECT.cfg
sed -re "s/(extends=.*)/\1 etc\/sys\/settings-prod.cfg/g" -i buildout-prod.cfg
sed -re "/\[buildout\]/ {
aallow-hosts = \${mirrors:allow-hosts}
}" -i etc/base.cfg
sed -re "/\[mirrors\]/ {
aallow-hosts =
a\     *localhost*
a\     *willowrise.org*
a\     *plone.org*
a\     *zope.org*
a\     *effbot.org*
a\     *python.org*
a\     *initd.org*
a\     *googlecode.com*
a\     *plope.com*
a\     *bitbucket.org*
a\     *repoze.org*
a\     *crummy.com*
a\     *minitage.org*
a\     *bpython-interpreter.org*
a\     *stompstompstomp.com*
a\     *ftp.tummy.com*
a\     *pybrary.net*
a\     *www.tummy.com*
a\     *www.riverbankcomputing.com*
a\     *.selenic.com*
}" -i etc/sys/settings.cfg
sed  -re "s/dependencies=/dependencies=git-1.7 subversion-1.6 /g" -i minilays/*/*
# vim:set et sts=4 ts=4 tw=80:
