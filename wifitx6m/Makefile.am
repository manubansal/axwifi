#------------------------
# wifitx6m
#------------------------

include $(top_srcdir)/Makefile.am.common

EXTRA_PROGRAMS = app_wifitx6m

wifitx6m: app_wifitx6m$(EXEEXT)
#	execute app_wifitx6m$(EXEEXT)

.PHONY: wifitx6m

app_wifitx6m_CFLAGS=-DENABLE_TIMING
app_wifitx6m_CFLAGS+=-DDEBUG_ATOMS
TRACE_DIR=${APP_WIFITX6M_OUT_BLDDIR}/trace
app_wifitx6m_CFLAGS+=-DTRACE_DIR_MIXED=\\\"${TRACE_DIR}\\\"

#for FileTraceReader
#app_wifitx6m_CFLAGS+=-DINPUT_TRACE_FILE=\\\"${WIFITX6M_TRACE_DIR}/txpkt.dat\\\"

#for TraceReader
INPUT_TRACE_ARRAY_NAME=trace_mac_addr
INPUT_TRACE_N_SAMPLES_PER_SYMBOL=8
INPUT_TRACE_N_SAMPLES=8
INPUT_TRACE_N_WRAPAROUNDS=1
app_wifitx6m_CFLAGS+=-DINPUT_TRACE_ARRAY_NAME=${INPUT_TRACE_ARRAY_NAME}
app_wifitx6m_CFLAGS+=-DINPUT_TRACE_N_SAMPLES_PER_SYMBOL=${INPUT_TRACE_N_SAMPLES_PER_SYMBOL}
app_wifitx6m_CFLAGS+=-DINPUT_TRACE_N_SAMPLES=${INPUT_TRACE_N_SAMPLES}
app_wifitx6m_CFLAGS+=-DINPUT_TRACE_N_WRAPAROUNDS=${INPUT_TRACE_N_WRAPAROUNDS}

app_wifitx6m_SOURCES = \
   main.c \
   setup.c \
   trace.c

#   trace/rate54.snrInf.nmsgs1.scale1.41.txpkt.dat_${INPUT_TRACE_ARRAY_NAME}.c

#   trace/trace_6mbps_skip_400000_ns_10000.c \
#   trace/trace_54mbps_skip_400000_ns_10000.c \
#   trace/txpkt_nmsgs2_rate_54_snr_35_scale_1.4142.dat_trace_skip_0_ns_6080.c

#   trace/trace_54mbps_skip_400000_ns_50000.c
#   trace/txpkt_nmsgs2_rate_54_snr_Inf_scale_1.4142.dat_trace_skip_0_ns_6080.c
#   trace/txpkt_nmsgs2_rate_54_snr_50_scale_1.4142.dat_trace_skip_0_ns_6080.c

nodist_app_wifitx6m_SOURCES = \
   __fifos__.h \
   __fifos__.c \
   __atoms__.h \
   __atoms__.c \
   __actions__.h \
   __actions__.c \
   __states__.h \
   __states__.c

app_wifitx6m_CLEANFILES = \
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

app_wifitx6m_LDADD = \
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


app_wifitx6m_CFLAGS += -I"`_cygpath -m $(top_srcdir)/app/wifitx6m`"
#app_wifitx6m_CFLAGS += -Iapp/wifitx6m
app_wifitx6m_CFLAGS += -I.
#app_wifitx6m_CFLAGS += -I$(top_srcdir)/exilib
#app_wifitx6m_CFLAGS += -I$(top_srcdir)/oros/sfifos/ilib
#app_wifitx6m_CFLAGS += -I$(top_srcdir)/oros/sysilib

ILIB_INCLUDE_PATH  =
ILIB_INCLUDE_PATH += -I"`_cygpath -m $(top_srcdir)/exilib`"
ILIB_INCLUDE_PATH += -I"`_cygpath -m $(top_srcdir)/oros/sfifos/ilib`"
ILIB_INCLUDE_PATH += -I"`_cygpath -m $(top_srcdir)/oros/sysilib`"
ILIB_INCLUDE_PATH += -I"`_cygpath -m $(top_srcdir)/orilib`"

app_wifitx6m_CFLAGS += ${ILIB_INCLUDE_PATH}

#app_wifitx6m_LDFLAGS=\
#--LINKER_SCRIPT_FILE "`_cygpath -w \"$(top_srcdir)/memorymaps/$(MEMORYMAP_FILE)\"`" \
#-I"${CSL_ROOT}/ti/csl/lib"  \
#-I"${DSPLIB_ROOT}/lib" 

app_wifitx6m_LDFLAGS=\
-I"${CSL_ROOT}/ti/csl/lib"  \
-I"${DSPLIB_ROOT}/lib" 


#overriding rule to avoid regenerating source code when no update occurs to source file
APP_WIFITX6M_OUT_GENERATED_FILES = fifos atoms actions states
APP_WIFITX6M_OUT_SRCDIR = $(top_srcdir)/app/wifitx6m
APP_WIFITX6M_OUT_BLDDIR = .


app_wifitx6m$(EXEEXT): $(APP_WIFITX6M_OUT_GENERATED_FILES) $(app_wifitx6m_OBJECTS) $(app_wifitx6m_DEPENDENCIES) $(EXTRA_app_wifitx6m_DEPENDENCIES) 
	@rm -f app_wifitx6m$(EXEEXT)
	$(app_wifitx6m_LINK) $(app_wifitx6m_LDFLAGS) $(app_wifitx6m_OBJECTS) $(app_wifitx6m_LDADD) $(LIBS) $(wildcard __*_j_*.c)


$(APP_WIFITX6M_OUT_GENERATED_FILES): %: __%__.c

__%__.c: $(APP_WIFITX6M_OUT_SRCDIR)/fifos.txt $(APP_WIFITX6M_OUT_SRCDIR)/atoms.txt $(APP_WIFITX6M_OUT_SRCDIR)/states.txt
	_create_afs_i \
		$(APP_WIFITX6M_OUT_SRCDIR)/fifos.txt \
		$(APP_WIFITX6M_OUT_SRCDIR)/atoms.txt \
		$(APP_WIFITX6M_OUT_SRCDIR)/states.txt \
		$(APP_WIFITX6M_OUT_BLDDIR)/__fifos__.h \
		$(APP_WIFITX6M_OUT_BLDDIR)/__fifos__.c \
		$(APP_WIFITX6M_OUT_BLDDIR)/__atoms__.h \
	        $(APP_WIFITX6M_OUT_BLDDIR)/__atoms__.c \
	        $(APP_WIFITX6M_OUT_BLDDIR)/__actions__.h \
	        $(APP_WIFITX6M_OUT_BLDDIR)/__actions__.c \
	        $(APP_WIFITX6M_OUT_BLDDIR)/__states__.h \
	        $(APP_WIFITX6M_OUT_BLDDIR)/__states__.c \
		$(APP_WIFITX6M_OUT_SRCDIR)/code_placement.txt \
		$(APP_WIFITX6M_OUT_SRCDIR)/debug_atoms.txt \
		$(top_srcdir)/memorymaps/$(MEMORYMAP_FILE) \
		$(APP_WIFITX6M_OUT_BLDDIR)/__memorymap__.cmd \
		${ILIB_INCLUDE_PATH} ${CFLAGS} ${app_wifitx6m_CFLAGS}
	if [[ ! -d ${TRACE_DIR} ]]; then mkdir -p ${TRACE_DIR}; fi


dist_doc_DATA = README


###########################################
#common to all binary builds
###########################################
LDFLAGS+=--LINKER_FLAGS_FILE "`_cygpath -w \"$(top_srcdir)/linkerflags.cmd\"`"

app_wifitx6m_LDFLAGS+=\
--LINKER_SCRIPT_FILE "`_cygpath -w \"__memorymap__.cmd\"`" 
