/**
Atomix project, setup.c, TODO: insert summary here
Copyright (c) 2015 Stanford University
Released under the Apache License v2.0. See the LICENSE file for details.
Author(s): Manu Bansal
*/
void app_wifirx6m_setup() {
  WIFILIB_genDerotTable();			
  WIFILIB_genTwiddleFactors();

  vitdec_profile_init();
}

void app_wifirx6m_setup_once() {
  vcp2_initOnce();
  vcp2_initPerUse(0,0,0,0);
}
