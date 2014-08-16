Adding some interactivity to R2D2
=================================

Project page: http://antontsv.github.io/r2d2

Hardware
========

![Raspberry Pi & sensors](https://antontsv.github.io/r2d2/img/all-sensors-setup.jpg "Looks nice!")

1. Raspberry PI Model B+
2. Edimax WiFi
3. 5V blinking red LED
4. DC 5V Power supply Micro USB, 2A
5. HC-SR50 PIR sensor
6. HC-SR04 ultrasonic sensor (with 1KΩ, or better have [voltage divider](http://en.wikipedia.org/wiki/Voltage_divider))
7. X-mini speaker

Pinout diagram
==============

![Raspberry Pi B+ pins](http://antontsv.github.io/r2d2/img/raspberry-pi-b-plus-pinout.png "Pins")

Image is taken from this blog post: [Raspberry Pi B+ GPIO Header Details And Pinout](http://www.raspberrypi-spy.co.uk/2014/07/raspberry-pi-b-gpio-header-details-and-pinout/)

Installation
============

Install necessary packages and install as daemon/startup process:

```sh
sudo ./install
```

Sensors & their demo run
========================

```sh
# Showcase help & options
./sensor_showcase.py --help

# All demos (you will have 30 seconds for each to see and test)
sudo ./sensor_showcase.py --all
```


## 5V blinking red LED

Usually LEDs are ~2.5V and will require resistor in a circuit
as Raspberry PI gives only 3.3V or 5V. So I was happy to find this little one at local radioshack, which also happens to blink automatically.

So your's might just give constant light, and most likely require an extra resistor (or you can watch your LED to burn in front of you).
Also keep in mind connection polarity: usually longer leg is connected to power (red wire) and shorter leg is connected to the ground

![5V LED](https://antontsv.github.io/r2d2/img/blinking-red-led-5v.jpg "Let it shine!")

**Connection pins for LED:**
 * Power: #12 aka "GPIO18"
 * Ground: #9


```sh
# Runs for 30 seconds (5 seconds on / 3 seconds off cycles)
sudo ./sensor_showcase.py --led
```

## HC-SR501 PIR sensor

[Passive infrared (PIR) sensor](http://en.wikipedia.org/wiki/Passive_infrared_sensor) with 2 controls on top:

  * Left: sensitivity
  * Right: time delay (sensor outputs a signal for a pediof of time after initial motion is detected)

Also for R2D2 I plan to narrow this sensor's field of vision by painting most of the fresnel lens of the sides (robot needs a black eye)

![HC-SR501-PIR](https://antontsv.github.io/r2d2/img/HC-SR501-PIR.jpg "Hey, you are moving")

**Connection pins for PIR sensor:**
* VCC: #4
* OUT: #26 aka "GPIO7"
* GND: #39

```sh
# Runs for 30 seconds (prints message if motion is detected)
sudo ./sensor_showcase.py --motion
```

## HC-SR04 ultra sonic sensor

Simple: emit sound pulse, and sense the echo. That it all boils down to simple equation as we know speed of sound in the air.

Also I hope you are not going to submerge the sensor in water or use it the moist environment.

**Important**: needs voltage divider, or some kind of resistor (I used 1kΩ 0.5W) to protect raspberry pi pin from echo's 5V output.
See that purple wire on the pictures.

![ultrasonic sensor](https://antontsv.github.io/r2d2/img/HC-SR04-ultrasonic-sensor.jpg "You are standing right here, I can hear you")

**Connection pins for ultrasonic sensor:**
* Gnd: #34
* Echo: #13 aka "GPIO27" (+ 1KΩ resistor)
* Trig: #11 aka "GPIO17"
* Vcc: #2

```sh
# Runs for 30 seconds (prints average distance over period of 3 seconds)
sudo ./sensor_showcase.py --distance
```
