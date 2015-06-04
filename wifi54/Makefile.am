#------------------------
# wifi54
#------------------------

include $(ATOMIX_ROOT_VAL)/Makefile.am.common

#bin_PROGRAMS = app_wifi54
EXTRA_PROGRAMS = app_wifi54


app_wifi54_SOURCES = \
   main.c \
   setup.c \
   dstmacaddr.c


app_wifi54_CFLAGS=-DENABLE_TIMING
TRACE_DIR=${APP_WIFI54_OUT_BLDDIR}/trace
app_wifi54_CFLAGS+=-DTRACE_DIR_MIXED=\\\"${TRACE_DIR}\\\"

include $(srcdir)/Makefile.am.traceconf

DSTMACADDR_ARRAY_NAME=trace_mac_addr
DSTMACADDR_N_SAMPLES_PER_SYMBOL=8
DSTMACADDR_N_SAMPLES=8
DSTMACADDR_N_WRAPAROUNDS=1
app_wifi54_CFLAGS+=-DDSTMACADDR_ARRAY_NAME=${DSTMACADDR_ARRAY_NAME}
app_wifi54_CFLAGS+=-DDSTMACADDR_N_SAMPLES_PER_SYMBOL=${DSTMACADDR_N_SAMPLES_PER_SYMBOL}
app_wifi54_CFLAGS+=-DDSTMACADDR_N_SAMPLES=${DSTMACADDR_N_SAMPLES}
app_wifi54_CFLAGS+=-DDSTMACADDR_N_WRAPAROUNDS=${DSTMACADDR_N_WRAPAROUNDS}



nodist_app_wifi54_SOURCES = \
   __fifos__.h \
   __fifos__.c \
   __atoms__.h \
   __atoms__.c \
   __actions__.h \
   __actions__.c \
   __states__.h \
   __states__.c

app_wifi54_CLEANFILES = \
   __fifos__.h \
   __fifos__.c \
   __atoms__.h \
   __atoms__.c \
   __actions__.h \
   __actions__.c \
   __states__.h \
   __states__.c

EXTRA_DIST = \
   fifos.or \
   atoms.or \
   states.or

app_wifi54_LDADD = \
   $(ATOMIX_INSTALL_DIR_VAL)/osl/lib.osl.a \
   $(ATOMIX_INSTALL_DIR_VAL)/oros/sfifos/lib/edmadriver/lib.oros.sfifos.edmadriver.a \
   $(ATOMIX_INSTALL_DIR_VAL)/oros/sfifos/lib/ipc/lib.oros.sfifos.ipc.a \
   $(ATOMIX_INSTALL_DIR_VAL)/oros/sfifos/ilib/lib.oros.sfifos.ilib.a \
   $(ATOMIX_INSTALL_DIR_VAL)/oros/sfifos/lib.oros.sfifos.a \
   $(ATOMIX_INSTALL_DIR_VAL)/oros/sysilib/lib.oros.sysilib.a \
   $(ATOMIX_INSTALL_DIR_VAL)/exilib/lib.exilib.a \
   $(ATOMIX_INSTALL_DIR_VAL)/osl/lib.osl.vitdec.a \
   $(ATOMIX_INSTALL_DIR_VAL)/osl/lib.osl.platform.a \
   ${ORILIB_INSTALL_DIR}/lib.orilib.a \
   ${IQMATH_ROOT}/lib/IQmath_c64x+e_elf.lib
if !DEVICE_IS_6638K2K
   app_wifi54_LDADD += $(ATOMIX_INSTALL_DIR_VAL)/osl/lib.osl.eth.a 
endif

#   lib.oros.sfifos.test_blocks.a
#   oros/common/src/sfifos/lib.oros.common.sfifos.test_blocks.a
#   orlib/orlib_blocks/lib.orlib.blocks.a


app_wifi54_CFLAGS += -I"`_cygpath -m $(top_srcdir)/wifi54`"
#app_wifi54_CFLAGS += -Iwifi54
app_wifi54_CFLAGS += -I.
#app_wifi54_CFLAGS += -I$(ATOMIX_ROOT_VAL)/exilib
#app_wifi54_CFLAGS += -I$(ATOMIX_ROOT_VAL)/oros/sfifos/ilib
#app_wifi54_CFLAGS += -I$(ATOMIX_ROOT_VAL)/oros/sysilib

ILIB_INCLUDE_PATH  =
ILIB_INCLUDE_PATH += -I"`_cygpath -m $(ATOMIX_ROOT_VAL)/exilib`"
ILIB_INCLUDE_PATH += -I"`_cygpath -m $(ATOMIX_ROOT_VAL)/oros/sfifos/ilib`"
ILIB_INCLUDE_PATH += -I"`_cygpath -m $(ATOMIX_ROOT_VAL)/oros/sysilib`"
ILIB_INCLUDE_PATH += -I"`_cygpath -m ${ORILIB_INC_DIR}`"

app_wifi54_CFLAGS += ${ILIB_INCLUDE_PATH}

#app_wifi54_LDFLAGS=\
#--LINKER_SCRIPT_FILE "`_cygpath -w \"$(ATOMIX_ROOT_VAL)/memorymaps/$(MEMORYMAP_FILE)\"`" \
#-I"${CSL_ROOT}/ti/csl/lib"  \
#-I"${DSPLIB_ROOT}/lib" 

app_wifi54_LDFLAGS=\
  -I"${CSL_ROOT}/ti/csl/lib"  \
  -I"${DSPLIB_ROOT}/packages/ti/dsplib/lib"

if DEVICE_IS_6638K2K
  app_wifi54_LDFLAGS+=\
  -I"${CSL_ROOT}/ti/drv/qmss/lib/c66" \
  -I"${CSL_ROOT}/ti/drv/cppi/lib/c66" \
  -I"${CSL_ROOT}/ti/drv/pa/lib/c66" \
  -I"${CSL_ROOT}/ti/platform/evmk2h/platform_lib/lib/debug"
else
  app_wifi54_LDFLAGS+=\
  -I"${CSL_ROOT}/ti/drv/qmss/lib" \
  -I"${CSL_ROOT}/ti/drv/cppi/lib" \
  -I"${CSL_ROOT}/ti/drv/pa/lib" \
  -I"${CSL_ROOT}/ti/platform/evmc6670l/platform_lib/lib/debug"
endif

#overriding rule to avoid regenerating source code when no update occurs to source file
APP_WIFI54_OUT_GENERATED_FILES = fifos atoms actions states
APP_WIFI54_OUT_SRCDIR = $(top_srcdir)/wifi54
APP_WIFI54_OUT_BLDDIR = .


app_wifi54$(EXEEXT): ATOMS_TXT_PREPROCESS $(APP_WIFI54_OUT_GENERATED_FILES) $(app_wifi54_OBJECTS) $(app_wifi54_DEPENDENCIES) $(EXTRA_app_wifi54_DEPENDENCIES) 
	@rm -f app_wifi54$(EXEEXT)
	$(app_wifi54_LINK) $(app_wifi54_LDFLAGS) $(app_wifi54_OBJECTS) $(app_wifi54_LDADD) $(LIBS) $(wildcard __*_j_*.c)


#atoms.ethreader.or
#atoms.tracereader.or
ATOMS_TXT_PREPROCESS:
	cat \
		$(APP_WIFI54_OUT_SRCDIR)/atoms.${SAMPLE_SOURCE}reader.or \
		$(APP_WIFI54_OUT_SRCDIR)/atoms.or \
		> $(APP_WIFI54_OUT_BLDDIR)/__atoms__.or

$(APP_WIFI54_OUT_GENERATED_FILES): %: __%__.c

__%__.c: \
	$(APP_WIFI54_OUT_SRCDIR)/fifos.or \
	$(APP_WIFI54_OUT_SRCDIR)/atoms.or \
	$(APP_WIFI54_OUT_SRCDIR)/states.or \
	$(APP_WIFI54_OUT_SRCDIR)/debug.or
	_create_afs_i \
		$(APP_WIFI54_OUT_SRCDIR)/fifos.or \
		$(APP_WIFI54_OUT_BLDDIR)/__atoms__.or \
		$(APP_WIFI54_OUT_SRCDIR)/states.or \
		$(APP_WIFI54_OUT_BLDDIR)/__fifos__.h \
		$(APP_WIFI54_OUT_BLDDIR)/__fifos__.c \
		$(APP_WIFI54_OUT_BLDDIR)/__atoms__.h \
	        $(APP_WIFI54_OUT_BLDDIR)/__atoms__.c \
	        $(APP_WIFI54_OUT_BLDDIR)/__actions__.h \
	        $(APP_WIFI54_OUT_BLDDIR)/__actions__.c \
	        $(APP_WIFI54_OUT_BLDDIR)/__states__.h \
	        $(APP_WIFI54_OUT_BLDDIR)/__states__.c \
		$(APP_WIFI54_OUT_SRCDIR)/code_placement.or \
		$(APP_WIFI54_OUT_SRCDIR)/debug.or \
		$(ATOMIX_ROOT_VAL)/memorymaps/$(MEMORYMAP_FILE) \
		$(APP_WIFI54_OUT_BLDDIR)/__memorymap__.cmd \
		${ILIB_INCLUDE_PATH} ${CFLAGS} ${app_wifi54_CFLAGS}
	if [[ ! -d ${TRACE_DIR} ]]; then mkdir -p ${TRACE_DIR}; fi



app_wifi54_cptrace:
if INPTRACE_LC
	cp -v ${INP_TRACE_C} ${OUT_TRACE_C}
endif
if INPTRACE_S
	cp -v ${INP_TRACE_C} ${OUT_TRACE_C}
endif


wifi54: app_wifi54_cptrace app_wifi54$(EXEEXT)
#	execute app_wifi54$(EXEEXT)

.PHONY: wifi54


dist_doc_DATA = README


###########################################
#common to all binary builds
###########################################
if DEVICE_IS_6638K2K
  LDFLAGS+=--LINKER_FLAGS_FILE "`_cygpath -w \"$(ATOMIX_ROOT_VAL)/linkerflags_k2k.cmd\"`"
else
  LDFLAGS+=--LINKER_FLAGS_FILE "`_cygpath -w \"$(ATOMIX_ROOT_VAL)/linkerflags.cmd\"`"
endif
app_wifi54_LDFLAGS+=\
--LINKER_SCRIPT_FILE "`_cygpath -w \"__memorymap__.cmd\"`"

