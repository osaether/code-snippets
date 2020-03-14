#include "boards.h"
#include "led_utils.h"

uint32_t led_is_on(uint32_t leds_mask)
{
    uint32_t leds_on = 0;
    uint32_t mask = 1;
    for (int idx=0; idx<LEDS_NUMBER; idx++)
    {
        if ((mask & leds_mask) != 0)
            leds_on |= bsp_board_led_state_get(idx)? mask:0;
        mask <<= 1;
    }
    return leds_on;
}


void leds_on(uint32_t leds_mask)
{
    uint32_t mask = 1;
    for (int idx=0; idx<LEDS_NUMBER; idx++)
    {
        if ((mask & leds_mask) != 0)
            bsp_board_led_on(idx);
        mask <<= 1;
    }
}

void leds_off(uint32_t leds_mask)
{
    uint32_t mask = 1;
    for (int idx=0; idx<LEDS_NUMBER; idx++)
    {
        if ((mask & leds_mask) != 0)
            bsp_board_led_off(idx);
        mask <<= 1;
    }
}
