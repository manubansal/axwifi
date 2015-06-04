#makefile for test binaries for individual blocks

#include $(top_srcdir)/Makefile.am.common

#CFLAGS+=-DENABLE_TIMING
#CFLAGS+=-I"$(top_srcdir)/oros/sfifos/lib/"

#Do not uncomment the following - these variable are intialized ONLY in the top level 
#automake file so that no included makefile ends up clearing these variables
#bin_PROGRAMS =
#EXTRA_DIST = 
#BUILT_SOURCES =


wifi54lcp:
	cd wifi54lcp && $(MAKE) $(AM_MAKEFLAGS) wifi54lcp

wifi54:
	cd wifi54 && $(MAKE) $(AM_MAKEFLAGS) wifi54

wifirx54mc:
	cd wifirx54mc && $(MAKE) $(AM_MAKEFLAGS) wifirx54mc

wifitx6m:
	cd wifitx6m && $(MAKE) $(AM_MAKEFLAGS) wifitx6m

.PHONY: wifi54lcp wifi54 wifirx54mc wifitx6m

all: wifi54 wifi54lcp
