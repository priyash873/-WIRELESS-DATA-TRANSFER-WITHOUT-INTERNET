from machine import Pin, SPI
from nrf24l01 import NRF24L01
import utime

spi = SPI(0, sck=Pin(2), mosi=Pin(3), miso=Pin(4))
csn = Pin(5, Pin.OUT)
ce = Pin(17, Pin.OUT)

nrf = NRF24L01(spi, csn, ce, channel=100, payload_size=32)
nrf.open_tx_pipe(b'\xe1\xf0\xf0\xf0\xf0')
nrf.open_rx_pipe(1, b'\xd2\xf0\xf0\xf0\xf0')

print("Transmitter Ready")

while True:
    msg = b"Hello World from Pico"
    try:
        nrf.send(msg)
        print("Sent:", msg)
    except OSError:
        print("Send failed")
    utime.sleep(1)
