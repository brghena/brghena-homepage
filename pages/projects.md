Projects
========

My research focuses on embedded systems. It is the kind of field
where you debug programs with an oscilloscope. Of particular interest to me
are low-level architectures and system interfaces.

Feel free to contact me if you have any questions: brghena@umich.edu

---

Whereabouts
-----------
**"Who's in lab?"**

This is a harder question to answer than it may seem. Determining the location of
individuals indoors remains an unsolved problem.

The goal of Whereabouts is to perform Semantic Heuristic Localization, that is
determine the location of an individual at the room level, and use a little bit
of guessing. The expected output would include each discovered individual and
which room they have been found in.
An important piece of the design is to not require individuals to carry any
extra devices. We want to use only things they already carry and
characteristics of who they are to discover them. Currently, the system uses
RFID cards and [Fitbits](https://www.fitbit.com/) to discover people.

<p>
<tt>
<a href="http://inductor.eecs.umich.edu/whereabouts.html">[demo]</a>
<a href="https://github.com/lab11/whereabouts">[source]</a>
</tt>
</p>

<p>
Terraswarm Localization Workshop 2014:
<br>
<tt>
<a href="projects/whereabouts_terraswarmLocalization.pdf">[poster]</a>
<a href="projects/whereabouts.pptx">[presentation]</a>
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
<a href="projects/campbell14thermes.pdf">[paper]</a>
</tt>
</p>

---

Green Lights Forever
-------------------
Starting as a course project in
[EECS 588](https://www.eecs.umich.edu/courses/eecs588/), a group of three other
students and I investigated the security of an intelligent traffic light system
in the United States. This work was published at WOOT 2014.

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
<a href="projects/ghena14green_lights.pdf">[paper]</a>
<a href="projects/ghena14green_lights.pptx">[presentation]</a>
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
<a href="https://github.com/lab11/SensEye-2">[source]</a>
</tt>
</p>

---

Oculus-ASR
----------
During my undergraduate studies at Michigan Tech I was part of the
[Aerospace Enterprise](http://www.aerospace.mtu.edu/), a group of students 
building a nanosatellite as part of the University Nanosatellite Program. We
won the 6th iteration of the competition and have been finalizing flight
hardware. The mission is set to launch using the Falcon Heavy on mission STP-2.

The purpose of the satellite is to help test United States' space situational
awareness capabilities. Using spectroscopy, the attitude and configuration of
a satellite can be determined if it is first characterized on the ground.
Oculus-ASR has been characterized and has the ability to control and observe
its orientation and configuration. The Air Force will use our satellite to 
callibrate their algorithms and enable new advances in space awareness.

<p>
JPL Cubesat Symposium 2013:
<br>
<tt>
<a href="projects/Oculus_ASR_Nanosatellite_JPL.pptx">[presentation]</a>
</tt>
</p>


