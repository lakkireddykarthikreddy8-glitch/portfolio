# Site

name: Karthik Reddy Lakkireddy
email: karthik743004@gmail.com
site_url: https://YOUR-USERNAME.github.io/portfolio/
page_title: Karthik Reddy Lakkireddy — Power electronics, from the grid to the battery
page_description: Portfolio of Karthik Reddy Lakkireddy: grid, charger, vehicle battery and home storage, with studies, projects and certifications.
share_title: Karthik Reddy Lakkireddy: power electronics for EVs and energy storage
share_description: A 3D tour from the grid to the battery: converters, battery management and 350 kW fast-charging simulation, with studies, projects and certificates.
share_image: og-image.png

<!--
HOW TO EDIT THIS FILE
- Each "## " heading is one block of the page. Do not rename the headings or the section keys
  (grid, pv, obc, battery, charger, house): the 3D scene uses them.
- A line "key: value" sets one value. Use the same key twice (for example "text:") to add a second paragraph.
- Lines starting with "- " under "facts:" are rows written as "bold part | grey part".
- After editing, run:  python3 build.py   and upload the new index.html.
- Anything between the arrows like this is a comment and is ignored.
-->

## Intro

availability: Available immediately · Aachen, Germany
headline: From the grid to the battery, and back again.
lead: I am an electrical engineer working on power electronics for electric vehicles and energy storage: converters, battery management and the charging chain that joins them.
note: Every object in the scene is a piece of my work: the solar field and its inverter, the car’s charger and battery, the charging post and the house. Click one, or scroll on.

## Section: grid

eyebrow: 2018 to 2022 · B.E. Electrical and Electronics Engineering, Osmania University
title: Foundations
text: My bachelor’s degree is the grid everything else connects to: power systems, renewable energy and the power electronics that join them. Power electronics and electric vehicles were the subjects that pulled me in, and I chose every elective I could in that direction.
facts:
- Power electronics | with laboratory
- Electrical machines | I and II, with laboratories
- Control of electric drives | and linear control systems
- DSP and microcontrollers | theory and laboratory
- Power systems | smart grids, renewable energy, switchgear, high voltage
small: CGPA 7.87 out of 10, First Class with Distinction.

## Section: pv

eyebrow: 2020 · Internship at my college, MVSR Engineering College
title: Two-stage grid-tied inverter
text: An inverter that feeds power from a PV array into the grid in two stages, the cabinet beside the solar field in the scene. This is where I first worked at the grid connection itself, and where comparing two kinds of switch for their losses gave me an early taste of the efficiency problems I enjoy.
facts:
- dq0 | current control for grid synchronisation
- about 95 % | MPPT tracking efficiency, perturb and observe
- 50 to 100 ms | settling time
- MOSFET vs IGBT | switching strategies compared for losses and control response

## Section: obc

eyebrow: 2022 · Bachelor thesis, MVSR Engineering College
title: Bridgeless Landsman converter
text: A power factor correction converter, redesigned against international harmonic limits. In an electric car this kind of stage sits at the front of the on-board charger. Changing the topology and slowing the switching cut the losses, and by design it also means less electromagnetic interference, although I did not measure that physically.
facts:
- 25 % to under 5 % | total harmonic distortion
- 0.80 to 0.98 | power factor
- Fewer switches, slower switching | lower switching losses, less interference by design
chips: MATLAB, Simulink

## Section: battery

eyebrow: 2023 to 2026 · M.Sc. Elektro- und Mikrosystemtechnik, OTH Regensburg
title: Master’s studies and my own battery protection board
text: During my master’s I learned KiCad and used it to build a battery protection board of my own: protection against overcharge, deep discharge and short circuit, taken from schematic to a working board that I built and debugged on the bench.
facts:
- KiCad | learned during the master’s, used for schematic and high-current PCB layout
- Built and commissioned | on the bench, 2024
- Fault finding | faults traced to their cause on the real board
small: Grade 2.4.

## Section: charger

eyebrow: 2025 to 2026 · Master’s thesis, FEV GmbH, Aachen
title: 350 kW fast charging, as fast as the battery safely allows
text: A simulation model of 350 kW fast charging, from the AC grid through the converters and a liquid-cooled cable into the battery. The BMS code charges as fast as the pack allows and then derates the current against temperature, state of charge and the cell manufacturer’s own limits, with thermal management keeping the pack in range. The goal is the shortest charge that stays inside safe limits and protects the life of the battery, with state-of-health logic in the code.
facts:
- 350 kW | fast charging simulated
- 720 A | peak charging current, derated from there
- Derating inputs | temperature, state of charge, and the cell manufacturer’s limits
- Thermal management | pack held in its safe range while charging
- State of health | logic in the BMS code to protect battery life
- 97 % and 96 % | AC/DC and DC/DC efficiency, validated
- −20 °C to 50 °C | temperature extremes modelled
- MATLAB GUI | Parameters, Graphs and Sankey tabs
chips: MATLAB, Simulink, PLECS
button: Try the simulator | simulator.html
button_note: An illustrative recreation of my GUI with assumed parameters, not thesis data.

## Section: house

eyebrow: Next
title: Energy storage and EV R&D
text: The same electronics that charge a car also run a house, send power back to the grid and fill a grid-scale store. I want to work on energy storage systems and their management, and on power electronics research, development or testing at EV makers and their suppliers. Doctoral positions in this area interest me too.
facts:
- Learning plan | battery state estimation, Python, embedded C and CAN
- Then | motor control and grid integration
- Available | immediately
button: Get in touch | mailto:karthik743004@gmail.com

## Certificates

eyebrow: Certifications
title: Courses and certificates
text: Taken alongside my master’s, out of interest in batteries and electric vehicles, to go further than the degree itself covered.
items:
- Mastering Advanced Battery Management for Electric Vehicle | Udemy, instructor Ritul Shah · 9 hours · completed 28 December 2024
- Electric Vehicle Battery Management System | Udemy, E-Vehicle Design · 9 hours · completed 6 November 2026
- Electric Vehicle Technology, a Beginner’s Course | Udemy, instructor Er. Prasanthkumar Palani · 9.5 hours · completed 10 November 2026
- Electric Vehicle Battery, Charging, Motor Components: Basics | Udemy, instructor Ritul Shah · 5.5 hours · completed 10 November 2026
small: Each certificate carries a Udemy verification link, which I can share on request.

## Tools

eyebrow: Tools and methods
title: What I work with
chips: MATLAB, Simulink, Stateflow, PLECS, LTspice, KiCad
text: Battery modelling and BMS control, converter design and loss analysis, thermal-electrical modelling.
text: Test campaigns and validation against measurements, requirements and technical documentation.
small: Languages: English C1, German B1 and improving. Next on my list: Python, embedded C and CAN.

## Contact

eyebrow: Contact
title: Let’s talk
text: Aachen, Germany. Available immediately for energy storage and battery management work, and for power electronics research, development or testing at EV makers and their suppliers, as well as doctoral positions in the same area.
year: 2026
