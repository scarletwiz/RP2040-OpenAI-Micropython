from machine import Pin, SPI
import network
import utime

import chatGPT

# W5x00 init
def init_ethernet(timeout=10):
    spi = SPI(0, 2_000_000, mosi=Pin(19), miso=Pin(16), sck=Pin(18))
    nic = network.WIZNET5K(spi, Pin(17), Pin(20))   # spi, cs, reset pin
    #DHCP
    nic.active(True)
    
    start_time = utime.ticks_ms()
    while not nic.isconnected():
        utime.sleep(1)
        if utime.ticks_ms() - start_time > timeout * 1000:
            raise Exception("Ethernet connection timed out.")
        print('Connecting ethernet...')

    print(f'Ethernet connected. IP: {nic.ifconfig()}')


def main ():
    init_ethernet()
    response= chatGPT.send_prompt_to_chatGPT("hello")
    print("\r\nchatGPT: ", response)


if __name__ == "__main__":
    main()