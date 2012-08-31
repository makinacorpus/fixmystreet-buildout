==============================================================
MINITAGE.DJANGO BUILDOUT FOR makina.fixmystreet
==============================================================

WARNING ABOUT BUILOOUT BOOTSTRAP WARNING
--------------------------------------------

        !!!    Be sure to use zc.buildout >= 1.5.0 or you ll have errors or bugs.    !!!


INSTALLING THIS PROJECT VITH MINITAGE
--------------------------------------
::

    export MT=/minitage
    virtualenv --no-site-packages --distribute $MT
    source /minitage/bin/activate
    easy_install -U minitage.core minitage.paste
    git clone  git@github.com:makinacorpus/fixmystreet-minilay.git ~/minitage/minilays/fms
    minimerge -v makina.fixmystreet
    #minimerge -v makina.fixmystreet-prod
    $MT/bin/paster create -t minitage.instances.env makina.fixmystreet #(-prod)
    source $MT/zope/makina.fixmystreet/sys/share/minitage/minitage.env
    cd $INS #enjoy !



INSTALLING THIS PROJECT VITHOUT MINITAGE
-----------------------------------------
DEBIAN PACKAGES

::

    sudo apt-get install libgdal1-devlibxslt1-dev libxml2-dev libfreetype6-dev libcairo2-dev

::

    git clone ssh://git@github.com:makinacorpus/fixmystreet-buildout.git
    cd fixmystreet-buildout.git
    python bootstrap.py -dc buildout-dev.cfg
    bin/buidout -vvvvvvvvvvvvvNc buildout-dev.cfg





# vim:set ft=rst sts=4 ts=4 ai:
