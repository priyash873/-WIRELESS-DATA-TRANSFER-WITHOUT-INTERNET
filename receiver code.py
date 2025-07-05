from machine import Pin, SPI
from nrf24l01 import NRF24L01
import utime

spi = SPI(0, sck=Pin(2), mosi=Pin(3), miso=Pin(4))
csn = Pin(5, Pin.OUT)
ce = Pin(17, Pin.OUT)

nrf = NRF24L01(spi, csn, ce, channel=100, payload_size=32)
nrf.open_tx_pipe(b'\xd2\xf0\xf0\xf0\xf0')
nrf.open_rx_pipe(1, b'\xe1\xf0\xf0\xf0\xf0')
nrf.start_listening()

print("Receiver Ready")

while True:
    if nrf.any():
        msg = nrf.recv()
        print("Received:", msg.decode('utf-8'))
    utime.sleep(0.5)
