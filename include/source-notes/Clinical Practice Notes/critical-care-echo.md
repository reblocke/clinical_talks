# Critical Care Echo

## Physics

Parameters controlled by settings on the machine

- power output (higher = higher amplitude reflected signals. Limited by safety. Bone heats faster than fat)
- gain (displayed amplitude of received signals, analogous to turning up the volume)
- Time-gain compensation (differential adjustment of gain along length of ultrasound beam; allows for correction of loss to attenuation in certain tissues)
- Depth (how long the machine waits before sending the next signal; increase depth decreases frame rate and maximal display area)
- Dynamic range and compression (amplitude range; larger dynamic range = more shades of grey)

In addition to these settings, there are post processing and preprocessing settings to adjust the display.

## Artifacts

- suboptimal image quality - usually poor tissue penetration (either poor contact, habits, tissue char)
- Acoustic shadowing - decreased info behind specular reflector
- reverberations - between two strong parallel reflectors
- beam width  - superimposition of structures within the beam profile
- lateral resolution - the apparent width increases as depth of the object increases due to refractions in the tissue
- range ambiguoity - echo from the previous pulse reaches transducer on the next cycle (results in superimposed second, deeper image)

## Doppler 

Intercept angle = angle between US beam and direction of travel. Cos(theta) = amount understimate

PRF = pulse <what?> frequency - determines maximum velocity (get nyquist effect if things are moving faster = signal aliasing)

- Continuous wave doppler: continuous transmission, receive info from length of the beam so all you get is the distribution of velocities along the beam and no depth resolution. 
- Pulsed doppler - pulses are timed, so that the movement at a specific depth is recorded.

Spectral analysis = display doppler velocity data vs time (scale = amplitude). This is the usual presentation in e.g. as in M-mode. 

(Note: M-mode has much higher sampling rates - 1800 per second - so can image fast moving structures better)

Color Doppler Flow imaging: on 2d mode, doppler interspersed over the area of interest. This means that the frame rate has to drop (drops more for a larger area of color). Things to adjust on color doppler to optimize: 

- color scale (represent the range of velocities across the maximum number of colors)
- velocity range (within nyquist limit at that depth)
- zero the baseline position on the color scale and set variance. 

Tissue Doppler: compared to flow of fluids, all moves in the same direction (so spectral analysis does not have a filled waveform).


## Normal Anatomy

3 types of movement: 

- translation (movement of an aspect of the heart)
- rotation (circular motion around long axis)
- torsion (unequal rotational motion around Apex vs base.

Nomenclature: 

- windows = where the probe is placed on the body
- view = the image plane (either long axis, short axis, four chamber, or two chamber.





### Flows

#### LV Outflow

Obtained from apical view

#### RV Outflow

Parasternal short or "RV outflow view"

#### LV Inflow 

- E = early diastolic peak velocity
- A = late diastolic peak as a result of atrial kick.

Typically assessed from apical window.
