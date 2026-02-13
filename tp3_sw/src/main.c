#include "xparameters.h"
#include "xil_io.h"
#include "my_led.h"
#include "xgpio.h"

int main(void)
{
    u32 switch_state;
    u32 reg0_val;
    u32 reg1_val;

    XGpio gpio_sw;
    XGpio_Initialize(&gpio_sw, XPAR_XGPIO_0_BASEADDR);
    XGpio_SetDataDirection(&gpio_sw, 1, 0xF); // 4 switches en entrée

    while (1)
    {
        // Lire l'état des 4 interrupteurs
        switch_state = XGpio_DiscreteRead(&gpio_sw, 1);

        // sw_state(0) = bit 0 de slv_reg0 -> LED(3:0)
        // sw_state(1) = bit 1 de slv_reg0 -> LED(7:4)
        reg0_val = switch_state & 0x03; // bits 0 et 1

        // sw_state(2) = bit 0 de slv_reg1 -> LED(11:8)
        // sw_state(3) = bit 1 de slv_reg1 -> LED(15:12)
        reg1_val = (switch_state >> 2) & 0x03; // bits 2 et 3

        // Écrire dans les registres de l'IP my_led
        MY_LED_mWriteReg(XPAR_MY_LED_0_BASEADDR,
                         MY_LED_S00_AXI_SLV_REG0_OFFSET, reg0_val);

        MY_LED_mWriteReg(XPAR_MY_LED_0_BASEADDR,
                         MY_LED_S00_AXI_SLV_REG1_OFFSET, reg1_val);
    }

    return 0;
}
