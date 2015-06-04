/**
Atomix project, configurator.c, TODO: insert summary here
Copyright (c) 2015 Stanford University
Released under the Apache License v2.0. See the LICENSE file for details.
Author(s): Manu Bansal
*/

#include <stdio.h>
#include <arpa/inet.h>

int main() {
  unsigned int ns = 400000;
  unsigned int f_ns = htonl(ns);
  FILE *f = fopen("orsys.conf", "wb");
  printf("ns  =%08x\n", ns);
  printf("f_ns=%08x\n", f_ns);
  fwrite(&f_ns, 4, 1, f);
  fclose(f);
  return 0;
}
