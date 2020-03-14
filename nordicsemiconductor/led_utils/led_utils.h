#include "boards.h"

#ifdef BSP_LED_0
#define BSP_BOARD_LED_MASK_0  1
#endif
#ifdef BSP_LED_1
#define BSP_BOARD_LED_MASK_1  2
#endif
#ifdef BSP_LED_2
#define BSP_BOARD_LED_MASK_2  4
#endif
#ifdef BSP_LED_3
#define BSP_BOARD_LED_MASK_3  8
#endif
#ifdef BSP_LED_4
#define BSP_BOARD_LED_MASK_4  10
#endif
#ifdef BSP_LED_5
#define BSP_BOARD_LED_MASK_5  20
#endif
#ifdef BSP_LED_6
#define BSP_BOARD_LED_MASK_6  40
#endif
#ifdef BSP_LED_7
#define BSP_BOARD_LED_MASK_7  80
#endif

uint32_t led_is_on(uint32_t leds_mask);
void leds_on(uint32_t leds_mask);
void leds_off(uint32_t leds_mask);
