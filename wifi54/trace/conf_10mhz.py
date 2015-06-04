conf = {\
	'ltf_proc_entry_state': '3', \
	'sample_consumption_starts_in_state': '2', \
	'sample_consumption_ends_in_state': '21', \
	'rx_pkt_init_state': '1', \
	'rx_data_finish_state': '20', \
	'ofdm_sym_dur_us': 8, \
	'clock_rate_mhz': 1250, \
	'prepad_dur_us': 18, \
	'postpad_dur_us': 10, \
	'n_ofdm_syms_in_pkt': 61, \
	'n_ofdm_syms_in_stf': 2, \
	'slack_us': 32, \
	'c_prepad': 'LightYellow', \
	'c_stf': 'LightSalmon', \
	'c_ltf': 'Orange', \
	'c_plcp': 'Olive', \
	'c_data': 'LightBlue', \
	'c_slack': 'PaleGreen', \
	'traceReaderInTSID': '1234', \
	'traceReaderOutTSID': '1235', \
	'tail_state': '14', \
	'fini_state': '15', \
	'figsize': (30, 30), \
	'stin': 'staRxLTFProc:0', \
	#'stout': 'staRxFinish:3', \
	'stout': 'staTxAckInit:0', \
	'pkt_entry_atom': 'bufAlignOffset0', \
	'pkt_exit_atom': 'atx_preambleTraceReaderInit', \
	#
	#used for aligning timestamps from different cores
	'syncState': 'staRxPLCPDecode', \
	#
	#the mininum one. the full set of fifo wait ts ids is 1111 to 1118.
	#'fifo_wait_ts_ids': ('1111', '1130'), \
	'fifo_wait_ts_ids': ('1131', '1142'), \
	#'fifo_wait_ts_ids_to_plot': ('1141', '1142'), \
	'fifo_wait_ts_ids_to_plot': ('1131', '1142'), \
	'WAIT_WIN_THRESHOLD': 100,\
	#
	#time stamping overhead in cycles
	'TS_OVERHEAD': 62, \
	#
	'more_atomids': "", \
	}
