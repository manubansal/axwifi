#------------------------
# wifirx54m
#------------------------

include $(top_srcdir)/Makefile.am.common

bin_PROGRAMS = app_wifirx54m.out

app_wifirx54m_out_SOURCES = \
   main.c \
   setup.c \
   samples/trace_6mbps_skip_400000_ns_10000.c \
   samples/trace_54mbps_skip_400000_ns_10000.c

nodist_app_wifirx54m_out_SOURCES = \
   __fifos__.h \
   __fifos__.c \
   __atoms__.h \
   __atoms__.c \
   __actions__.h \
   __actions__.c \
   __states__.h \
   __states__.c

app_wifirx54m_out_CLEANFILES = \
   __fifos__.h \
   __fifos__.c \
   __atoms__.h \
   __atoms__.c \
   __actions__.h \
   __actions__.c \
   __states__.h \
   __states__.c

EXTRA_DIST = \
   fifos.txt \
   atoms.txt \
   states.txt

app_wifirx54m_out_LDADD = \
   $(top_builddir)/osl/lib.osl.a \
   $(top_builddir)/oros/sfifos/lib/edmadriver/lib.oros.sfifos.edmadriver.a \
   $(top_builddir)/oros/sfifos/lib/ipc/lib.oros.sfifos.ipc.a \
   $(top_builddir)/oros/sfifos/ilib/lib.oros.sfifos.ilib.a \
   $(top_builddir)/oros/sfifos/lib.oros.sfifos.a \
   $(top_builddir)/oros/sysilib/lib.oros.sysilib.a \
   $(top_builddir)/exilib/lib.exilib.a \
   $(top_builddir)/orilib/lib.orilib.a \
   $(top_builddir)/osl/lib.osl.vitdec.a
#   lib.oros.sfifos.test_blocks.a
#   oros/common/src/sfifos/lib.oros.common.sfifos.test_blocks.a
#   orlib/orlib_blocks/lib.orlib.blocks.a

app_wifirx54m_out_CFLAGS=-DENABLE_TIMING

app_wifirx54m_out_CFLAGS += -I$(top_srcdir)/app/wifirx54m
#app_wifirx54m_out_CFLAGS += -Iapp/wifirx54m
app_wifirx54m_out_CFLAGS += -I.
#app_wifirx54m_out_CFLAGS += -I$(top_srcdir)/exilib
#app_wifirx54m_out_CFLAGS += -I$(top_srcdir)/oros/sfifos/ilib
#app_wifirx54m_out_CFLAGS += -I$(top_srcdir)/oros/sysilib

ILIB_INCLUDE_PATH  =
ILIB_INCLUDE_PATH += -I$(top_srcdir)/exilib
ILIB_INCLUDE_PATH += -I$(top_srcdir)/oros/sfifos/ilib
ILIB_INCLUDE_PATH += -I$(top_srcdir)/oros/sysilib
ILIB_INCLUDE_PATH += -I$(top_srcdir)/orilib

app_wifirx54m_out_CFLAGS += ${ILIB_INCLUDE_PATH}

app_wifirx54m_out_LDFLAGS=\
--LINKER_SCRIPT_FILE "`_cygpath -w \"$(top_srcdir)/memorymaps/$(MEMORYMAP_FILE)\"`" \
-I"${CSL_ROOT}/ti/csl/lib"  \
-I"${DSPLIB_ROOT}/lib" 


#BUILT_SOURCES += af
#
#af:
#	_create_afs_i$(EXEEXT) \
#		$(top_srcdir)/app/wifirx54m/fifos.txt \
#		$(top_srcdir)/app/wifirx54m/atoms.txt \
#		$(top_srcdir)/app/wifirx54m/states.txt \
#		app/wifirx54m/__fifos__.h \
#		app/wifirx54m/__fifos__.c \
#		app/wifirx54m/__atoms__.h \
#	        app/wifirx54m/__atoms__.c \
#	        app/wifirx54m/__actions__.h \
#	        app/wifirx54m/__actions__.c \
#	        app/wifirx54m/__states__.h \
#	        app/wifirx54m/__states__.c \
#		${ILIB_INCLUDE_PATH}

#		"${app_wifirx54m_out_CFLAGS}"



#version 2
#overriding rule to avoid regenerating source code when no update occurs to source file
APP_WIFIRX54M_OUT_GENERATED_FILES = fifos atoms actions states
APP_WIFIRX54M_OUT_SRCDIR = $(top_srcdir)/app/wifirx54m
#APP_WIFIRX54M_OUT_BLDDIR = app/wifirx54m
APP_WIFIRX54M_OUT_BLDDIR = .

app_wifirx54m.out$(EXEEXT): $(APP_WIFIRX54M_OUT_GENERATED_FILES) $(app_wifirx54m_out_OBJECTS) $(app_wifirx54m_out_DEPENDENCIES) $(EXTRA_app_wifirx54m_out_DEPENDENCIES) 
	@rm -f app_wifirx54m.out$(EXEEXT)
	$(app_wifirx54m_out_LINK) $(app_wifirx54m_out_LDFLAGS) $(app_wifirx54m_out_OBJECTS) $(app_wifirx54m_out_LDADD) $(LIBS) $(wildcard __*_j_*.c)

#	$(app_wifirx54m_out_LINK) $(app_wifirx54m_out_OBJECTS) $(app_wifirx54m_out_LDADD) $(LIBS) $(wildcard app/app_wifirx54m/__*_j_*.c)

$(APP_WIFIRX54M_OUT_GENERATED_FILES): %: __%__.c

__%__.c: $(APP_WIFIRX54M_OUT_SRCDIR)/fifos.txt $(APP_WIFIRX54M_OUT_SRCDIR)/atoms.txt $(APP_WIFIRX54M_OUT_SRCDIR)/states.txt
	_create_afs_i$(EXEEXT) \
		$(APP_WIFIRX54M_OUT_SRCDIR)/fifos.txt \
		$(APP_WIFIRX54M_OUT_SRCDIR)/atoms.txt \
		$(APP_WIFIRX54M_OUT_SRCDIR)/states.txt \
		$(APP_WIFIRX54M_OUT_BLDDIR)/__fifos__.h \
		$(APP_WIFIRX54M_OUT_BLDDIR)/__fifos__.c \
		$(APP_WIFIRX54M_OUT_BLDDIR)/__atoms__.h \
	        $(APP_WIFIRX54M_OUT_BLDDIR)/__atoms__.c \
	        $(APP_WIFIRX54M_OUT_BLDDIR)/__actions__.h \
	        $(APP_WIFIRX54M_OUT_BLDDIR)/__actions__.c \
	        $(APP_WIFIRX54M_OUT_BLDDIR)/__states__.h \
	        $(APP_WIFIRX54M_OUT_BLDDIR)/__states__.c \
		${ILIB_INCLUDE_PATH} ${CFLAGS}
	



dist_doc_DATA = README


###########################################
#common to all binary builds
###########################################
#LDFLAGS=--LINKER_FLAGS_FILE "`cygpath -w -a \"$(top_srcdir)/linkerflags.cmd\"`"
LDFLAGS=--LINKER_FLAGS_FILE "`_cygpath -w \"$(top_srcdir)/linkerflags.cmd\"`"

