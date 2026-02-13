# 2026-02-13T16:05:40.453552593
import vitis

client = vitis.create_client()
client.set_workspace(path="tp3_workspace")

platform = client.get_component(name="tp3_hw")
status = platform.build()

comp = client.get_component(name="tp3_sw")
comp.build()

status = platform.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

