# 2026-02-13T15:41:19.062998168
import vitis

client = vitis.create_client()
client.set_workspace(path="tp3_workspace")

platform = client.create_platform_component(name = "tp3_hw",hw_design = "$COMPONENT_LOCATION/../../../VivadoProjects/M1_Sorbonne_SysCom_UM4IN108-FPGA_TP3/project/TP3_wrapper.xsa",os = "standalone",cpu = "microblaze_0",domain_name = "standalone_microblaze_0",compiler = "gcc")

comp = client.create_app_component(name="tp3_sw",platform = "$COMPONENT_LOCATION/../tp3_hw/export/tp3_hw/tp3_hw.xpfm",domain = "standalone_microblaze_0")

platform = client.get_component(name="tp3_hw")
status = platform.build()

status = platform.build()

comp = client.get_component(name="tp3_sw")
comp.build()

status = platform.build()

status = comp.clean()

status = platform.build()

comp.build()

status = comp.clean()

status = platform.build()

comp.build()

status = comp.import_files(from_loc="$COMPONENT_LOCATION/../../../VivadoProjects/M1_Sorbonne_SysCom_UM4IN108-FPGA_TP3/ip_repo/my_led_1_0/drivers/my_led_v1_0/src", files=["my_led.c", "my_led.h"], dest_dir_in_cmp = "src", is_skip_copy_sources = False)

status = platform.build()

comp.build()

vitis.dispose()

