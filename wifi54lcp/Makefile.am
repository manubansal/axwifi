#------------------------
# wifi54lcp
#------------------------

include $(top_srcdir)/Makefile.am.common

#bin_PROGRAMS = app_wifi54lcp
EXTRA_PROGRAMS = app_wifi54lcp


app_wifi54lcp_SOURCES = \
   main.c \
   setup.c \
   dstmacaddr.c


app_wifi54lcp_CFLAGS=-DENABLE_TIMING
TRACE_DIR=${APP_WIFI54LCP_OUT_BLDDIR}/trace
app_wifi54lcp_CFLAGS+=-DTRACE_DIR_MIXED=\\\"${TRACE_DIR}\\\"

include $(srcdir)/Makefile.am.traceconf

DSTMACADDR_ARRAY_NAME=trace_mac_addr
DSTMACADDR_N_SAMPLES_PER_SYMBOL=8
DSTMACADDR_N_SAMPLES=8
DSTMACADDR_N_WRAPAROUNDS=1
app_wifi54lcp_CFLAGS+=-DDSTMACADDR_ARRAY_NAME=${DSTMACADDR_ARRAY_NAME}
app_wifi54lcp_CFLAGS+=-DDSTMACADDR_N_SAMPLES_PER_SYMBOL=${DSTMACADDR_N_SAMPLES_PER_SYMBOL}
app_wifi54lcp_CFLAGS+=-DDSTMACADDR_N_SAMPLES=${DSTMACADDR_N_SAMPLES}
app_wifi54lcp_CFLAGS+=-DDSTMACADDR_N_WRAPAROUNDS=${DSTMACADDR_N_WRAPAROUNDS}



nodist_app_wifi54lcp_SOURCES = \
   __fifos__.h \
   __fifos__.c \
   __atoms__.h \
   __atoms__.c \
   __actions__.h \
   __actions__.c \
   __states__.h \
   __states__.c

app_wifi54lcp_CLEANFILES = \
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

app_wifi54lcp_LDADD = \
   $(top_builddir)/osl/lib.osl.a \
   $(top_builddir)/oros/sfifos/lib/edmadriver/lib.oros.sfifos.edmadriver.a \
   $(top_builddir)/oros/sfifos/lib/ipc/lib.oros.sfifos.ipc.a \
   $(top_builddir)/oros/sfifos/ilib/lib.oros.sfifos.ilib.a \
   $(top_builddir)/oros/sfifos/lib.oros.sfifos.a \
   $(top_builddir)/oros/sysilib/lib.oros.sysilib.a \
   $(top_builddir)/exilib/lib.exilib.a \
   $(top_builddir)/orilib/lib.orilib.a \
   $(top_builddir)/osl/lib.osl.vitdec.a \
   $(top_builddir)/osl/lib.osl.eth.a \
   $(top_builddir)/osl/lib.osl.platform.a
#   lib.oros.sfifos.test_blocks.a
#   oros/common/src/sfifos/lib.oros.common.sfifos.test_blocks.a
#   orlib/orlib_blocks/lib.orlib.blocks.a


app_wifi54lcp_CFLAGS += -I"`_cygpath -m $(top_srcdir)/app/wifi54lcp`"
#app_wifi54lcp_CFLAGS += -Iapp/wifi54lcp
app_wifi54lcp_CFLAGS += -I.
#app_wifi54lcp_CFLAGS += -I$(top_srcdir)/exilib
#app_wifi54lcp_CFLAGS += -I$(top_srcdir)/oros/sfifos/ilib
#app_wifi54lcp_CFLAGS += -I$(top_srcdir)/oros/sysilib

ILIB_INCLUDE_PATH  =
ILIB_INCLUDE_PATH += -I"`_cygpath -m $(top_srcdir)/exilib`"
ILIB_INCLUDE_PATH += -I"`_cygpath -m $(top_srcdir)/oros/sfifos/ilib`"
ILIB_INCLUDE_PATH += -I"`_cygpath -m $(top_srcdir)/oros/sysilib`"
ILIB_INCLUDE_PATH += -I"`_cygpath -m $(top_srcdir)/orilib`"

app_wifi54lcp_CFLAGS += ${ILIB_INCLUDE_PATH}

#app_wifi54lcp_LDFLAGS=\
#--LINKER_SCRIPT_FILE "`_cygpath -w \"$(top_srcdir)/memorymaps/$(MEMORYMAP_FILE)\"`" \
#-I"${CSL_ROOT}/ti/csl/lib"  \
#-I"${DSPLIB_ROOT}/lib" 

app_wifi54lcp_LDFLAGS=\
-I"${CSL_ROOT}/ti/csl/lib"  \
-I"${DSPLIB_ROOT}/packages/ti/dsplib/lib" \
-I"${CSL_ROOT}/ti/drv/qmss/lib" \
-I"${CSL_ROOT}/ti/drv/cppi/lib" \
-I"${CSL_ROOT}/ti/drv/pa/lib" \
-I"${CSL_ROOT}/ti/platform/evmc6670l/platform_lib/lib/debug"

#overriding rule to avoid regenerating source code when no update occurs to source file
APP_WIFI54LCP_OUT_GENERATED_FILES = fifos atoms actions states
APP_WIFI54LCP_OUT_SRCDIR = $(top_srcdir)/app/wifi54lcp
APP_WIFI54LCP_OUT_BLDDIR = .


app_wifi54lcp$(EXEEXT): ATOMS_TXT_PREPROCESS $(APP_WIFI54LCP_OUT_GENERATED_FILES) $(app_wifi54lcp_OBJECTS) $(app_wifi54lcp_DEPENDENCIES) $(EXTRA_app_wifi54lcp_DEPENDENCIES) 
	@rm -f app_wifi54lcp$(EXEEXT)
	$(app_wifi54lcp_LINK) $(app_wifi54lcp_LDFLAGS) $(app_wifi54lcp_OBJECTS) $(app_wifi54lcp_LDADD) $(LIBS) $(wildcard __*_j_*.c)


#atoms.ethreader.txt
#atoms.tracereader.txt
ATOMS_TXT_PREPROCESS:
	cat \
		$(APP_WIFI54LCP_OUT_SRCDIR)/atoms.${SAMPLE_SOURCE}reader.txt \
		$(APP_WIFI54LCP_OUT_SRCDIR)/atoms.txt \
		> $(APP_WIFI54LCP_OUT_BLDDIR)/__atoms__.txt

$(APP_WIFI54LCP_OUT_GENERATED_FILES): %: __%__.c

__%__.c: \
	$(APP_WIFI54LCP_OUT_SRCDIR)/fifos.txt \
	$(APP_WIFI54LCP_OUT_SRCDIR)/atoms.txt \
	$(APP_WIFI54LCP_OUT_SRCDIR)/states.txt \
	$(APP_WIFI54LCP_OUT_SRCDIR)/debug.txt
	_create_afs_i \
		$(APP_WIFI54LCP_OUT_SRCDIR)/fifos.txt \
		$(APP_WIFI54LCP_OUT_BLDDIR)/__atoms__.txt \
		$(APP_WIFI54LCP_OUT_SRCDIR)/states.txt \
		$(APP_WIFI54LCP_OUT_BLDDIR)/__fifos__.h \
		$(APP_WIFI54LCP_OUT_BLDDIR)/__fifos__.c \
		$(APP_WIFI54LCP_OUT_BLDDIR)/__atoms__.h \
	        $(APP_WIFI54LCP_OUT_BLDDIR)/__atoms__.c \
	        $(APP_WIFI54LCP_OUT_BLDDIR)/__actions__.h \
	        $(APP_WIFI54LCP_OUT_BLDDIR)/__actions__.c \
	        $(APP_WIFI54LCP_OUT_BLDDIR)/__states__.h \
	        $(APP_WIFI54LCP_OUT_BLDDIR)/__states__.c \
		$(APP_WIFI54LCP_OUT_SRCDIR)/code_placement.txt \
		$(APP_WIFI54LCP_OUT_SRCDIR)/debug.txt \
		$(top_srcdir)/memorymaps/$(MEMORYMAP_FILE) \
		$(APP_WIFI54LCP_OUT_BLDDIR)/__memorymap__.cmd \
		${ILIB_INCLUDE_PATH} ${CFLAGS} ${app_wifi54lcp_CFLAGS}
	if [[ ! -d ${TRACE_DIR} ]]; then mkdir -p ${TRACE_DIR}; fi



app_wifi54lcp_cptrace:
if INPTRACE_LC
	cp -v ${INP_TRACE_C} ${OUT_TRACE_C}
endif
if INPTRACE_S
	cp -v ${INP_TRACE_C} ${OUT_TRACE_C}
endif


wifi54lcp: app_wifi54lcp_cptrace app_wifi54lcp$(EXEEXT)
#	execute app_wifi54lcp$(EXEEXT)

.PHONY: wifi54lcp


dist_doc_DATA = README


###########################################
#common to all binary builds
###########################################
LDFLAGS+=--LINKER_FLAGS_FILE "`_cygpath -w \"$(top_srcdir)/linkerflags.cmd\"`"

app_wifi54lcp_LDFLAGS+=\
--LINKER_SCRIPT_FILE "`_cygpath -w \"__memorymap__.cmd\"`"

