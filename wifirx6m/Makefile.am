#------------------------
# wifirx6m
#------------------------

bin_PROGRAMS += app_wifirx6m.out

app_wifirx6m_out_SOURCES = \
   app/wifirx6m/main.c \
   app/wifirx6m/setup.c \
   app/wifirx6m/samples/trace_6mbps_skip_400000_ns_10000.c

nodist_app_wifirx6m_out_SOURCES = \
   app/wifirx6m/__fifos__.h \
   app/wifirx6m/__fifos__.c \
   app/wifirx6m/__atoms__.h \
   app/wifirx6m/__atoms__.c \
   app/wifirx6m/__actions__.h \
   app/wifirx6m/__actions__.c \
   app/wifirx6m/__states__.h \
   app/wifirx6m/__states__.c

app_wifirx6m_out_CLEANFILES = \
   __fifos__.h \
   __fifos__.c \
   __atoms__.h \
   __atoms__.c \
   __actions__.h \
   __actions__.c \
   __states__.h \
   __states__.c

EXTRA_DIST += \
   app/wifirx6m/fifos.txt \
   app/wifirx6m/atoms.txt \
   app/wifirx6m/states.txt

app_wifirx6m_out_LDADD = \
   osl/lib.osl.a \
   oros/sfifos/lib/edmadriver/lib.oros.sfifos.edmadriver.a \
   oros/sfifos/lib/ipc/lib.oros.sfifos.ipc.a \
   oros/sfifos/ilib/lib.oros.sfifos.ilib.a \
   oros/sfifos/lib.oros.sfifos.a \
   oros/sysilib/lib.oros.sysilib.a \
   exilib/lib.exilib.a \
   orilib/lib.orilib.a \
   osl/lib.osl.vitdec.a
#   lib.oros.sfifos.test_blocks.a
#   oros/common/src/sfifos/lib.oros.common.sfifos.test_blocks.a
#   orlib/orlib_blocks/lib.orlib.blocks.a

app_wifirx6m_out_CFLAGS=-DENABLE_TIMING

#app_wifirx6m_out_CFLAGS = -I"$(top_srcdir)/oros/sfifos/test_blocks"
app_wifirx6m_out_CFLAGS += -Iapp/wifirx6m
app_wifirx6m_out_CFLAGS += -I$(top_srcdir)/app/wifirx6m
#app_wifirx6m_out_CFLAGS += -I$(top_srcdir)/exilib
#app_wifirx6m_out_CFLAGS += -I$(top_srcdir)/oros/sfifos/ilib
#app_wifirx6m_out_CFLAGS += -I$(top_srcdir)/oros/sysilib

ILIB_INCLUDE_PATH  =
ILIB_INCLUDE_PATH += -I$(top_srcdir)/exilib
ILIB_INCLUDE_PATH += -I$(top_srcdir)/oros/sfifos/ilib
ILIB_INCLUDE_PATH += -I$(top_srcdir)/oros/sysilib
ILIB_INCLUDE_PATH += -I$(top_srcdir)/orilib

app_wifirx6m_out_CFLAGS += ${ILIB_INCLUDE_PATH}

app_wifirx6m_out_LDFLAGS=\
--LINKER_SCRIPT_FILE "`_cygpath -w \"$(top_srcdir)/memorymaps/$(MEMORYMAP_FILE)\"`"


BUILT_SOURCES += af

af:
	_create_afs_i$(EXEEXT) \
		$(top_srcdir)/app/wifirx6m/fifos.txt \
		$(top_srcdir)/app/wifirx6m/atoms.txt \
		$(top_srcdir)/app/wifirx6m/states.txt \
		app/wifirx6m/__fifos__.h \
		app/wifirx6m/__fifos__.c \
		app/wifirx6m/__atoms__.h \
	        app/wifirx6m/__atoms__.c \
	        app/wifirx6m/__actions__.h \
	        app/wifirx6m/__actions__.c \
	        app/wifirx6m/__states__.h \
	        app/wifirx6m/__states__.c \
		${ILIB_INCLUDE_PATH} ${CFLAGS}

#		"${app_wifirx6m_out_CFLAGS}"

