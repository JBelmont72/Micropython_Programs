'''
https://www.youtube.com/watch?v=wAt93JhSLoQ
'''
# +5v to pico vbus pin 40
# gnd to pico gnd pin 38
# din to pico gp0 pin 1
import array, time, sys, select

from machine import Pin
import rp2 
from rp2 import PIO, StateMachine, asm_pio
NUM_LEDS = 4
@asm_pio(sideset_init=PIO.OUT_LOW, out_shiftdir=PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():    
  T1 = 2    
  T2 = 5   
  T3 = 3    
  label("bitloop")   
  out(x, 1)             .side(0)    [T3 - 1]    
  jmp(not_x, "do_zero") .side(1)    [T1 - 1]   
  jmp("bitloop")        .side(1)    [T2 - 1]    
  label("do_zero")    nop()                 .side(0)    [T2 - 1]

  sm = StateMachine(0, ws2812, freq=8000000, sideset_base=Pin(0))
  sm.active(1)

ar = array.array("I", [0 for _ in range(NUM_LEDS)])
while True:    
     time.sleep(0.1)    
     while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:        
          ch = sys.stdin.read(1)        
              if (ch == 'r'):            
                for i in range(NUM_LEDS):                
                   ar[i] = 0x0000ff00        
               elif (ch == 'g'):            
                   for i in range(NUM_LEDS):                
                       ar[i] = 0x00ff0000       
                elif (ch == 'b'):            
                     for i in range(NUM_LEDS):                
                         ar[i] = 0x000000ff        
                sm.put(ar, 8)


# remember to run html replace %lt with less than symbol and %gt with greater than symbol

# // chrome://flags/#enable-experimental-web-platform-features 
# // tested on chrome 87&lt = less than symbol&gt = greater than symbol
# youtube don't like angle brackets


html:
&lt html &gt


&lt button onclick="test()" &gt connect &lt button &gt

&lt button id="r" type="button" &gt red &lt /button &gt
&lt button id="g" type="button" &gt green &lt /button &gt
&lt button id="b" type="button" &gt blue &lt /button &gt


&lt script &gt
var port;
function sendByte(b){  
     if (port && port.writable) {   
          const writer = port.writable.getWriter();   
          writer.write(b);    
          writer.releaseLock();   }}


document.getElementById ("r").addEventListener("click", function() {
         sendByte(new Uint8Array([114])); // ascii 'r'});


document.getElementById ("g").addEventListener("click", function() {
   sendByte(new Uint8Array([103])); // ascii 'g'
});


document.getElementById ("b").addEventListener("click", function() {
  sendByte(new Uint8Array([98])); // ascii 'b'
});


const test = async function () {    port = await navigator.serial.requestPort({});    await port.open({ baudRate: 115200 });}


&lt /script &gt
&lt /html &gt
