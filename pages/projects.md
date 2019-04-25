Projects
========

<table border="0" cellspacing="0" cellpadding="0">
    <tr>
        <td valign="top" align="left">
            <img height="200" src="images/branden_soldering_wrong.jpg">
        </td>
        <td width="25">&nbsp;&nbsp;&nbsp;&nbsp;</td>
        <td width="0" valign="top" align="left">

<p style="font-size:16px">
My research area is embedded systems. It is the kind of field where you debug
software with an oscilloscope. Particularly, I work on resource-constrained
embedded hardware, software, and networking. Of a particular interest to me are
networking protocols such as Bluetooth Low Energy, LoRaWAN, and LTE-M, which
are capable of supporting various Internet of Things communication needs. My
research covers several systems areas including networking and operating
systems.
</p>
<p style="font-size:16px">
An extremely important part of publicly funded research is making results
available to the public. I strongly believe in open-access to research and you
can find all my papers provided on this website and all of the software and 
hardware for my projects on <a href="https://github.com/lab11">Github</a>.
</p>

        </td>
    </tr>
</table>

---

Low-Power Wide Area Networking
------------------------------
The domain of low-power, wide-area networking is becoming increasingly
important to the Internet of Things. A number of unlicensed band protocols,
such as LoRaWAN, Sigfox, Weightless, and WiFi HaLow have been developed to
solve the needs of energy-constrained, low-bandwidth, widely-deployed devices.
These networks use a range of techniques at the physical and link layers to
provide communications. Meanwhile, cellular technologies are also entering this
space with LTE-M and NB-IoT rolling out globally. Our researcher focuses on how
well these technologies will support future application needs and how IoT
devices will need to adapt in order to make use of them.

This work so far has resulted in an overview of the existing technologies and
their applicability to various applications created in collaboration with a
project with Ford.

<p>
<tt>
<a href="https://docs.google.com/presentation/d/1kZ0rFL1Ra5rBfM7lkH7w5Um_281uoM94FR4VJqxXEBo/edit?usp=sharing">[LPWAN Overview Slides]</a>
</tt>
</p>

---

BLE Networking
--------------
Bluetooth Low Energy (BLE) is an ubiquitous low-power networking technology. It
is already available in consumer devices, including all smartphones, and is
frequently used in Internet of Things devices for simple communication
capabilities. However, when it comes to sensor networks, BLE has seen little
use. BLE advertisements—short, periodic, broadcast messages—seem to be a
potentially useful medium for data transport, however, especially for densely
deployed devices. We find that academic literature has not rigorously studied
BLE advertisement networks in theory or practice, and are currently exploring
its use.

This work has so far resulted in a related workshop paper on the potential for
smartphone data muling over BLE advertisements at HotMobile'19.

<p>
<tt>
<a href="projects/ble/adkins19freeloader.pdf">[HotMobile'19 Workshop Paper]</a>
</tt>
</p>

---

Signpost
--------

<table border="0" cellspacing="0" cellpadding="0">
    <tr>
        <td valign="top" align="left">
            <img height="200" src="images/signpost.jpg">
        </td>
        <td width="25">&nbsp;&nbsp;&nbsp;&nbsp;</td>
        <td width="0" valign="top" align="left">

The growing field of city-scale sensing hold exciting promise. We look forward
to the new insights into the health and activities of our cities and towns that
can be gained through wide-area deployed sensing efforts. A key challenge to
these efforts, however, is that the application idea isn't the hard part.
Instead, the challenge for researchers is often all the other things that go
into real-world deployments: power, networking, storage, and weatherproofing.
These engineering challenges take time away from the core research goal and
raise the level of effort required to perform even simple tests of city-scale
sensing ideas.

Signpost provides a solution this problem. It is a modular city-scale sensing
platform that provides resources to arbitrary sensors that can be attached to
it over a simple hardware and software interface. Signpost is energy-harvesting
through a solar panel, easily mountable on ubiquitous city sign poles,
waterproof, and supports applications by providing communications, storage,
location, time, and data processing capabilities. A key design challenge for
Signpost is the ability to support multiple sensor modules by developers with
unaligned, and possibly opposing desires. In response, Signpost provides robust
hardware isolation in terms of energy use and communication capability for
hosted application modules.

<p>
<tt>
<a href="https://github.com/lab11/signpost">[Hardware Source]</a>
<a href="https://github.com/lab11/signpost-software">[Software Source]</a>
</tt>
</p>

        </td>
    </tr>
</table>
<p></p>

This work has led to multiple workshop and demo papers, a magazine article, and
a conference paper at IPSN'18.

**Abstract:**  
City-scale sensing holds the promise of enabling a deeper understanding of our
urban environments. However, a city-scale deployment requires physical
installation, power management, and communications—all challenging tasks
standing between a good idea and a realized one. This indicates the need for a
platform that enables easy deployment and experimentation for applications
operating at city scale. To address these challenges, we present Signpost, a
modular, energy-harvesting platform for city-scale sensing. Signpost simplifies
deployment by eliminating the need for connection to wired infrastructure and
instead harvesting energy from an integrated solar panel. The platform
furnishes the key resources necessary to support multiple, pluggable sensor
modules while providing fair, safe, and reliable sharing in the face of dynamic
energy constraints. We deploy Signpost with several sensor modules, showing the
viability of an energy-harvesting, multi-tenant, sensing system, and evaluate
its ability to support sensing applications. We believe Signpost reduces the
difficulty inherent in city-scale deployments, enables new experimentation, and
provides improved insights into urban health.

<p>
<tt>
<a href="projects/signpost/adkins18signpost.pdf">[IPSN'18 Conference Paper]</a>
<a href="projects/signpost/adkins18signpost-getmobile.pdf">[GetMobile 2018 Magazine Article]</a>
<a href="projects/signpost/adkins18signpostdemo.pdf">[IPSN'18 Demo Paper]</a>
<a href="projects/signpost/adkins17energy.pdf">[ENSsys'17 Workshop Paper]</a>
<a href="projects/signpost/adkins16signpost-demo.pdf">[SenSys'16 Demo Paper]</a>
</tt>
</p>

---

Gateway
-------
The many Internet of Things devices we work on have a common need: the ability
to communicate with the internet. They need a gateway that will bridge their
low-power communication methods, such as Bluetooth Low-Energy, with services
either local or cloud-based. The gateway also acts as a natural host for
applications that want to directly interact with local devices. We developed a
gateway architecture for our own use in various projects that could collect
packets sent over a variety of low-power networks including BLE and 802.15.4,
translate those packets into a human-readable JSON format, host local
applications that interact with the sensor data, and upload the data to cloud
services.

The key idea of this gateway project is that devices should be automatically
supported by the gateway by providing their own translation code. In our
architecture, devices share a URL with the gateway that hosts a Javascript
parser capable of translating that device's packets into a JSON structure. The
gateway automatically downloads these parsers, runs them in a sandbox on the
incoming packets, and publishes the resulting data over a local MQTT service.
In this way, the gateway can exist agnostic to the devices it services, and
device manufacturers can ensure that their devices are supported entirely
through their own efforts. We have used this gateway design to successfully
collect data from several deployments of other lab projects, such as Triumvi
and PowerBlade.

<p>
<tt>
<a href="https://github.com/lab11/gateway">[Source]</a>
</tt>
</p>

**Abstract:** 
The gateway is a key component for sensor network deployments and the Internet
of Things. Sensor deployments often tend towards low-power communication
protocols such as Bluetooth Low Energy or IEEE 802.15.4. Gateways are essential
to connect these devices to the Internet at large. Over time though, gateways
have gained additional responsibilities as well. Sensors expect gateways to
handle device-specific data translation and local processing while also
providing services, such as time synchronization, to the low-power device. As a
centralized computing resource, the gateway is also an obvious location for
running local applications which interact with sensor data and control nearby
actuators. Today, vendors and researchers often create their own
device-specific gateways to handle these responsibilities.

We propose a generic gateway platform capable of supporting the needs of many
devices. In our architecture, devices provide a pointer, such as a URL, to
descriptions of their interfaces. The gateway can download the interface
descriptions and use them to determine how to interact with the device,
translating its data to a usable format and enabling local services to
communicate with it. The translated data is provided to services including user
applications, local logging, device status monitoring, and cloud applications.
By simultaneously supporting communication with many sensors, our gateway
architecture can simplify future sensor network deployments and enable
intelligent building applications.

<p>
<tt>
<a href="projects/gateway/campbell16gateway-demo.pdf">[BuildSys'16 Demo Paper]</a>
</tt>
</p>

---

Tock
----

<table border="0" cellspacing="0" cellpadding="0">
    <tr>
        <td valign="top" align="left">
            <img height="200" src="images/tock_process.png">
        </td>
        <td width="25">&nbsp;&nbsp;&nbsp;&nbsp;</td>
        <td width="0" valign="top" align="left">

Embedded operating systems have traditionally been limited to libraries that
abstract hardware and implement common utilities. These systems provide only
limited mechanisms, if any, to ensure the safety of drivers and isolate
applications. An answer to this need is Tock, a safe, multitasking operating
system for memory constrained devices. It is written in Rust, a type-safe
systems language which is used to enforce safety of of kernel components. Tock
allows applications, which can be written in any language, to be compiled and
loaded independently from the kernel.

Tock is an open source project in use by research groups at several
universities, multiple companies, and independent engineers all over the world.
The project is still under active development and we welcome anyone interested
to participate.

<p>
<tt>
<a href="https://github.com/tock/tock">[Source]</a>
<a href="https://tockos.org">[Tock-OS Website]</a>
</tt>
</p>

        </td>
    </tr>
</table>
<p></p>


This work has led to multiple workshop papers and a conference paper at SOSP'17.

**Abstract:**  
Low-power microcontrollers lack some of the hardware features and memory
resources that enable multiprogrammable systems. Accordingly,
microcontroller-based operating systems have not provided important features
like fault isolation, dynamic memory allocation, and flexible concurrency.
However, an emerging class of embedded applications are software platforms,
rather than single purpose devices, and need these multiprogramming features.
Tock, a new operating system for low-power platforms, takes advantage of
limited hardware-protection mechanisms as well as the type-safety features of
the Rust programming language to provide a multiprogramming environment for
microcontrollers. Tock isolates software faults, provides memory protection,
and efficiently manages memory for dynamic application workloads written in any
language. It achieves this while retaining the dependability requirements of
long-running applications.

<p>
<tt>
<a href="projects/tock/levy17multiprogramming.pdf">[SOSP'17 Conference Paper]</a>
<a href="projects/tock/levy17rustkernel.pdf">[APSys'17 Workshop Paper]</a>
<a href="projects/tock/levy15ownership.pdf">[PLOS'15 Workshop Paper]</a>
</tt>
</p>

---

PowerBlade
----------

<table border="0" cellspacing="0" cellpadding="0">
    <tr>
        <td valign="top" align="left">
            <img height="200" src="images/powerblade.jpg">
        </td>
        <td width="25">&nbsp;&nbsp;&nbsp;&nbsp;</td>
        <td width="0" valign="top" align="left">

With an increasing number of miscellaneous electrical loads used in residential
and commercial buildings, understanding electricity usage patterns requires
metering every load. Existing plug-load power meters are bulky, power-hungry,
and require manual user interaction to record energy use. PowerBlade is a new
take on power meter designs that has an essentially 2D form factor. Loads
literally plug-through it and into the outlet. This means PowerBlade can stay
attached to the load plug itself, truly monitoring an individual device, rather
than an outlet. Designing a functional power meter with extreme volume
constraints requires rethinking the traditional power meter design choices.
PowerBlade employs a simplified AC power supply design, a novel method for
noninvasively sensing current draw, and a Bluetooth Low-Energy radio to
transmit data to nearby smartphones. This work was published and demonstrated
at SenSys 2015.

<p>
<tt>
<a href="https://github.com/lab11/powerblade">[Source]</a>
<a href="https://youtu.be/oNUXhCDnHoE">[Video]</a>
</tt>
</p>

        </td>
    </tr>
</table>
<p></p>

**Abstract:**  
We present PowerBlade, the smallest, lowest cost, and lowest
power AC plug-load meter that measures real, reactive and apparent power, and
reports this data, along with cumulative energy consumption, over an
industry-standard Bluetooth Low Energy radio. Achieving this design point
requires revisiting every aspect of conventional power meters: a new method of
acquiring voltage; a non-invasive, planar method of current measurement; an
efficient and accurate method of computing power from the voltage and current
channels; a radio interface that leverages nearby smart phones to display data
and report it to the cloud; and a retro power supply re-imagined with vastly
lower current draw, allowing extreme miniaturization. PowerBlade occupies a
mere 1" × 1" footprint, offers a 1/16" profile, draws less than 180 mW itself,
offers 1.13% error on unity power factor loads in the 2-1200 W range and
slightly worse for non-linear and reactive loads, and costs $11 in modest
quantities of about 1,000 units. This new design point enables affordable
large-scale studies of plug-load energy usage—an area of growing national
importance.
<p>
<tt>
<a href="projects/powerblade/debruin15powerblade.pdf">[SenSys'15 Conference Paper]</a>
<a href="projects/powerblade/debruin15powerblade-demo.pdf">[SenSys'15 Demo Paper]</a>
</tt>
</p>

This work was also included in an IEEE Pervasive journal paper covering the
topic of perpetual sensing in the built environment.

<p>
<tt>
<a href="projects/powerblade/campbell16perpetual.pdf">[IEEE Pervasive 2016 Journal Paper]</a>
</tt>
</p>

---

Wearabouts
-----------
**"Who's in lab?"** This is a harder question to answer than it may seem.
Determining the location of individuals indoors remains an unsolved problem.

The goal of Wearabouts is to perform room-level localization of individuals.
The expected output would include each discovered individual and
which room they have been found in.
An important piece of the design is to not require individuals to carry any
extra devices. We want to use only things they already carry and
characteristics of who they are to discover them. Currently, the system uses
Bluetooth Low-Energy advertisements from devices like
[Fitbits](https://www.fitbit.com/) to discover people and adds information from
RFID door entry and smartphone WiFi connections to increase its accuracy.

<p>
<tt>
<a href="https://github.com/lab11/whereabouts">[Source]</a>
</tt>
</p>

<p>
Terraswarm Annual Meeting 2014:
<br>
<tt>
<a href="projects/whereabouts/wearabouts_terraswarmAnnual.pdf">[Poster]</a>
</tt>
</p>


<p>
Terraswarm Localization Workshop 2014:
<br>
<tt>
<a href="projects/whereabouts/whereabouts_terraswarmLocalization.pdf">[Poster]</a>
<a href="projects/whereabouts/whereabouts.pdf">[Presentation]</a>
</tt>
</p>

---

Thermes
-------
Taking the Monjolo Principle of energy-harvester as a sensor, we created a new
platform with a heat harvesting thermoelectric generator. This work was
published at ENSsys 2014.

**Abstract:**  
Fine-grained energy metering in homes and buildings provides a promising
technique for addressing the unmaintainable energy consumption levels of
worldwide buildings. Metering electricity, lighting, natural gas, HVAC,
occupancy, and water on a per appliance or room basis can provide invaluable insight
when trying to reduce a building's energy footprint. A myriad of sensor designs
and systems collect data on particular building aspects, but are often hampered
by installation difficulty or ongoing maintenance needs (like battery
replacement). We address these common pitfalls for water and heat metering by
developing a small, energy-harvesting sensor that meters using the same
thermoelectric generator with which it powers itself. In short, the rate at which
the harvester captures energy is proportional to the heat production of the
monitored appliance or pipe and this relationship allows us to estimate energy use
simply based on the sensor's ability to harvest. We prototype our sensor in a
bracelet shaped form-factor that can attach to a shower head pipe, faucet, or
appliance to provide local hot water or heat metering.

<p>
<tt>
<a href="projects/thermonjolo/campbell14thermes.pdf">[ENSsys'14 Workshop Paper]</a>
<a href="projects/thermonjolo/enssys14_thermes_presentation.pdf">[ENSsys'14 Presentation]</a>
</tt>
</p>

---

Green Lights Forever
-------------------
Starting as a course project in
[EECS 588](https://www.eecs.umich.edu/courses/eecs588/), a group of three other
students and I investigated the security of an intelligent traffic light system
in the United States. This work was published at WOOT'14 and received
widespread media attention.

**Abstract:**  
The safety critical nature of traffic infrastructure requires that it
be secure against computer-based attacks, but this is not always the case.
We investigate a networked traffic signal system currently deployed in the
United States and discover a number of security flaws that exist due to
systemic failures by the designers. We leverage these flaws to create attacks
which gain control of the system, and we successfully demonstrate them on the
deployment in coordination with authorities. Our attacks show that an
adversary can control traffic infrastructure to cause disruption, degrade
safety, or gain an unfair advantage. We make recommendations on how to improve
existing systems and discuss the lessons learned for embedded systems security
in general.

<p>
<tt>
<a href="projects/green_lights/ghena14green_lights.pdf">[WOOT'14 Workshop Paper]</a>
<a href="projects/green_lights/woot14_greenlights_presentation.pdf">[WOOT'14 Presentation]</a>
</tt>
</p>

<p>
Selected News Articles:
<br>
<tt>
<a href="https://www.technologyreview.com/s/530216/researchers-hack-into-michigans-traffic-lights/">[MIT Technology Review]</a>
<a href="https://www.newscientist.com/article/mg22329814-600-traffic-light-hackers-could-cause-jams-across-the-us/">[New Scientist]</a>
<a href="https://www.washingtonpost.com/local/could-a-hacker-gain-control-of-dcs-traffic-system/2015/08/08/7cb7cf94-201a-11e5-bf41-c23f5d3face1_story.html">[Washington Post]</a>
<a href="https://www.nbcchicago.com/investigations/series/inside-the-new-hacking-threat/New-Hacking-Threat-Could-Impact-Traffic-Systems-282235431.html">[NBC Chicago]</a>
</tt>
</p>


---

NSF Fellowship
--------------
In my 2013 I applied to the NSF Graduate Research
Fellowship Program and was lucky enough to be awarded a fellowship. This was
the first year with the new essay rules that reduce the application to two
essays, Background & Previous Research and Proposed Research, a total of five
pages. Below, I have provided my essays as well as the reviews I received as
examples for other students applying to the program.

<p>
<tt>
<a href="projects/fellowships/nsf_background_prevResearch.pdf">[Background and Previous Research]</a>
<a href="projects/fellowships/nsf_propResearch.pdf">[Proposed Research]</a>
<a href="projects/fellowships/nsf_reviews.pdf">[Reviews]</a>
</tt>
</p>

---

SensEye
-------
The eyes are the window to the soul. What could a computer do if it knew what
you were looking at?

SensEye is an attempt to start answering that question. Low-power real-time
gaze detection is finally within our grasp. Using a microcontroller running
uCLinux and an FPGA, we can pull real-time images from two small cameras, one
facing inwards towards the eye and one facing outwards towards the world. This
data can be used to determine which object in view you are observing. Imagine
a world where your car would warn you if you were not paying attention, where
your phone would have interesting information available on the item you were
just observing, and where you could track how you actually spend your time each
day.

In order to achieve this goal, our system has to be both energy efficient and 
low cost. We hope to create such a system and distribute it to software
developers in order to spur innovation.

<p>
<tt>
<a href="https://github.com/lab11/SensEye-2">[Source]</a>
</tt>
</p>

---

Oculus-ASR
----------

<table border="0" cellspacing="0" cellpadding="0">
    <tr>
        <td valign="top" align="left">
            <img height="200" src="images/oculusasr.png">
        </td>
        <td width="25">&nbsp;&nbsp;&nbsp;&nbsp;</td>
        <td width="0" valign="top" align="left">

<p>
During my undergraduate studies at Michigan Tech I was part of
<a href="https://www.aerospace.mtu.edu/">Areospace Enterpise</a>,
a group of students building a nanosatellite as part of the University
Nanosatellite Program. We won the 6th iteration of the competition and have
been finalizing flight hardware. The mission is set to launch using the Falcon
Heavy on mission
<a href="https://en.wikipedia.org/wiki/Space_Test_Program">STP-2</a>.
</p>
<p>
The purpose of the satellite is to help test United States' space situational
awareness capabilities. Using spectroscopy, the attitude and configuration of
a satellite can be determined if it is first characterized on the ground.
Oculus-ASR has been characterized and has the ability to control and observe
its orientation and configuration. The Air Force will use our satellite to 
calibrate their algorithms and enable new advances in space awareness. I
presented an overview of the project at the 2013 JPL cubesat symposium.
</p>
<p>
<tt>
<a href="projects/nanosat/jpl13_oculusASR_presentation.pdf">[Presentation]</a>
</tt>
</p>

        </td>
    </tr>
</table>

<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>

