# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "")
  file(REMOVE_RECURSE
  "/home/mathias8dev/VitisProjects/tp3_workspace/tp3_hw/microblaze_0/standalone_microblaze_0/bsp/include/sleep.h"
  "/home/mathias8dev/VitisProjects/tp3_workspace/tp3_hw/microblaze_0/standalone_microblaze_0/bsp/include/xiltimer.h"
  "/home/mathias8dev/VitisProjects/tp3_workspace/tp3_hw/microblaze_0/standalone_microblaze_0/bsp/include/xtimer_config.h"
  "/home/mathias8dev/VitisProjects/tp3_workspace/tp3_hw/microblaze_0/standalone_microblaze_0/bsp/lib/libxiltimer.a"
  )
endif()
