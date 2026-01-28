# Ventilator Management

## History

Invention of Ventilation: Vesalius in 16th century (animals). Then, iron long. Modern positive pressure ventilation: Ibsen did tracheostomy (+1500 medical students bagging for 165000 hours) to lower mortality in paralytic polio from 87% to 40%. Incidentally, this is also the invention of the ICU.

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1918826/pdf/procrsmed00411-0124.pdf

Last fifty years in mechanical ventilation: 

https://journals.lww.com/ccmjournal/fulltext/2021/04000/fifty_years_of_mechanical_ventilation_1970s_to.2.aspx

##Hyperacute Decompensation in a ventilated patient

DOPES Mnemonic

- Displacement of the tube
- Obstruction 
- Patient * ( PE, Pulm Edema, PTX, Abd Compartment Synd)
- Equipment (oxygen, tubing)
- Stacking (breaths) 

## Physiology: 
Airway pressure = Initial alveolar Pressure + (R _to_flow * flow) + (Vt * Elastance of resp system).

- note: you can control 1 side of the equation - called the equation of motion - either the Pressure or flow+Vt (just called volume control because it sounds better) depending if you are doing a pressure or volume mode. The other is dependent variable.

PPlat: take out flow term, leaving 1/Elastance = Compliance = Vt / (Pplat - initial pressure)

![alt](https://photos.collectednotes.com/photos/5187/41cc47fe-512d-4ffd-916a-66a160c78459)

Driving pressure = PPlat - PEEP =  Vt / Crs = 'Vt normalized to the respiratory systems compliance'. Hope to keep below 15.

Patient ventilator dyssynchrony: mismatch between inspiratory and expiratory times of the patient and the vent

![alt](https://photos.collectednotes.com/photos/5187/4c9a7124-44e3-4644-baee-289b5ee86ed7)
![alt](https://photos.collectednotes.com/photos/5187/9e5c8c03-b877-4252-a3da-4a2849c7853e)

## Modes:

Ventilator has a different inflow arm and outflow arm (always goes in 1 direction) to make the circuit.  
 
Phases: 

- Trigger = starts the breath (either a time in a controlled mode/breath, or an event in an assistant mode/breath)
- Target / Control  = criteria vent uses to adjust control variable while giving the breath
- Cycling = what stops the breath

Mandatory breath (triggered OR cycled by machine) vs Spontaneous (triggered and cycled by patient). 

Mode types: 

- CMV = all mandatory

- IMV = some mandatory

- CSV = all spontaneous

Pressure vs Volume control: neither proven superior. Need to monitor dependent variable in either. 

![alt](https://photos.collectednotes.com/photos/5187/70e0bf1d-d6a4-4bbe-83c9-7e970bb6fff0)


### AC-VC vs AC-VC+

[ ] what is the difference

Worry: do you have to work harder on the mode? Like SIMV
RTs like it because patient looks comfortable. 

##Adjusting Oxygenation
Goal: 

- PEEP (high PEEP table if P:F < 200 ARDS. Pro: better oxygenation, avoid atelectatrauma. Con: baroatrauma and reduced preload. If O2 increases = patient had recruitable lung. If not, the rest of lung will see more baro-stress.)

- FiO2 - ideally reduce to <60% to avoid oxygen toxicity. 

- I time - more of respiratory 
![alt](https://photos.collectednotes.com/photos/5187/416f4b65-d4ec-4763-a542-41b7a8bd60ff)

##Adjusting ventilation:
Goal is to maintain an acceptable (not normal) blood gas, in general tolerating some abnormality of blood gas to avoid VILI (this is permissive hypercapnia, thought based on no evidence to be OK to pH 7.2).
- Tidal Volume
- Respiratory Rate

##Peak and Plateau Pressure
Peak = reflects airway plus alveoli pressure

Plateau = reflects alveoli pressure  at lung inflation to total lung capacity. Try to keep below 30-35 mmHg. (or driving pressure in obesity). This is the sum of the transpulmonary (or transpleural) pressure and the pressure from the chest wall in a static setting. **How could you isolate these two relative components? (such as in a situation where there is chest wall restriction that you want to differentiate from increased lung compliance**

Via an esophageal pressure balloon = equilibrates with the pleural pressure. 

High peak + normal plateau pressure localizes to airway or tubing

High peak + high plateau pressure localizes to high alveolar pressure (low lung compliance, pneumothorax, abd process, mainstem bronchus). Note: obesity causes this pattern without add'n stress (because pleural pressure is similarly elevated = same driving pressure. Pleural pressure can be estimated by esophageal probe. Transpleural pressure correlates with barotrauma (note: does high pressure from chest wall lead to damage? presumably not). Generally, need higher PEEP to recruit)

Is it possible to have a higher plateau pressure than peak pressure? [Yes](https://www.atsjournals.org/doi/full/10.1513/AnnalsATS.201707-553CC). Patients must be completely passive for accurate plat measurement (inh = falsely low, exh = falsely high). if the patient is inhaling on a pressure regulated mode, pleural pressure is negative, transpulmonary pressure is larger = larger tidal volumes = higher pressure than alveolar/plateau pressure. This is the rationale for P-SILI

Why all the fuss about peak pressure? 

https://criticalcarenow.com/2021/01/11/peak-airway-pressure-why-the-fuss/

https://pubmed.ncbi.nlm.nih.gov/8275740/

Essentially: it's only because it's convenient to measure. The peak inspiratory pressure itself is not correlated with damage to the lung, only the plateau. 

## Obesity, Driving Pressure, and Stress Index

Transmural pressure = pressure between the inside of a n elastic chamber to the outside aka the 'distending pressure'

For alveoli: the transmural pressure estimated by the transpulmonary pressure = airway pressure - pleural pressure. When flow is 0 (e.g. end exp or end insp), airway pressure estimates alveolar pressure, so this value approximates the alveolar stress.

With obesity (esp if laying flat): pleural pressure increases. This means that a given PEEP will result in less transmural pressure on the alveoli, and also possible under-recruitment of lung (thus, increased compliance due to ventilating a smaller section of lung). 

One approach: increase the PEEP so as to minimize the driving pressure, with the knowledge that the Plateau doesn't likely reflect the true transmural pressure if pleural pressure is elevated (can be proven with an esophageal probe, though this has shown to not be helpful in all comers:  EP-Vent1 and EP-Vent2 trials)

https://criticalcarenow.com/2021/02/15/basics-of-transpulmonary-pressure-towards-a-better-surrogate-of-lung-stress/

Driving pressure improvements are more predictive of survival than P:F improvements - https://www.atsjournals.org/doi/abs/10.1513/AnnalsATS.202007-862OC

A step further, optimization of the driving pressure can be further improved by the concept of stress index( = the bend in the curve of the Paw to time curve - corresponding to at maximum volume of a breath, is the compliance increasing or decreasing?). If stress index > 1, this suggests that more pressure (PEEP) could decrease the driving pressure required to get a certain Vt

![alt](https://photos.collectednotes.com/photos/5187/2c96fa85-56bf-40f6-8a84-f7e61a152fe1)


### Pes

Insert 33-40cm; want to see oscillations from the cardiac beats to confirm.

Adjust PEEP 0 Ptp ~0 at end-expiration.  Double check your work by pressing on the chest

May be most useful with abnormal chest compliance - e.g. obesity. However, may be equivalent to just use the high PEEP table. 


### Stress Index

Idea - attempting to avoid over distention or under-distention. Ideally, a straight line (on ACVC with square waveform and paralyzed). If upward inflection - over distention. If downward deflection - under-distention.

### Driving pressure

Bundle of low-tidal volume, low plateau, and PEEP improves mortality. But can we be more targeted? 

The difference between plateau and peep is a surrogate for the amount of stress being applied to the lung. This may be directly what we are achieving with LTVV. 

## Ventilator Dyssynchrony

RT protocols?

Goals: allow safe ventilation with the lightest possible sedation. Deeper sedation is almost always a brute force way to fix this but has downsides - optimal ventilator settings have fewer downsides.

4 most common types: 

### Double triggering

- two breaths delivered despite one patient inspiration. 
- Happens when the inspiratory time set by the vent is shorter than the inspiratory time the patient wants (neural I time). This is particularly problematic when the patient's drive to breath is high (and we are giving LTVV.. much more common when using low Vt. Recall ARMA allowed 4-8 ml/kg IBW). 
- Problem: causes double 'stacking' = the second breath comes before the exhalation of the last one leading to tidal volume is twice what you wanted. (e.g. 12 cc/kg)
- solution: you can increase vent inspiratory time or increase volume a little bit. Or, sedate/paralyze (this might be better earlier in the hospital)
- (Note: if you are in a pressure controlled mode, increase PIP or decrease the expiratory flow trigger to prolong the time of the breath)

### Flow starvation

- patients wants more flow than the ventilator is giving
- identified in VC with a pressure dip without flow changes. Easiest to see this in a square waveform
- problem: over-use and injury of the muscles, high trans pulmonary pressure.
- solution: most people comfortable with 50-60 lpm flow rate -> can go up to 80s. Without high peaks (though will not necessarily be problematic 


Does the switch to a square waveform actually change the starvation?

### Ineffective trigger

- patient attempts to initiate a breath but the vent isn't giving it
- identifiable by a dip in the pressure waveform that doesn't correspond to a breath
- many reasons: trigger is not sensitive enough? (Rare), Is there Auto-PEEP (the patient has to overcome the intrinsic PEEP)? Is there obstruction in the tube (kink, water, gunk)? Is the patient incredibly weak e.g. due to sedation or weakening?  Practically, weakness and auto peep are most common.

### Reverse trigger

- patient inspiratory effort is delayed... pathophysiology is not all that well understood. Possibly related to diaphragm anaomolies. Often seems not to get better with deep sedation. Sometimes worse when waking up from deep sedation.
- in VC: dip in flow late in the cycle; in PC you see a rebound increase in flow
- you can use NMB to fix... or just leave it.

#### Heliox
O2 input with Helium replacing nitrogen as the inert gas. Helium is less dense, thus more able to maintain laminar flow = less airway resistance. Mixed 60% He / 40% O2, thus cannot be used in situations where FiO2 over 40% is required. 

##Weaning and Liberation from the Ventilator
- minimize sedatives and NM blockade (intermittent doses > continuous infusion) throughout duration
- early mobilization (lessen risk of ICU-acquired weakness)
- SBT (T-piece vs PSV equal, no vs 5 PEEP equal) / SAT daily
- cuff leak test with steroids if there is no cuff leak
- prophylactic NIV for patients who are at high risk for reintubation (vs HFNC?)


##Waveform Capnography

Remember, unlike in the OR where patient's lung mechanics are generally relatively normal - the EtCO2 will diverge from the PaCO2 if there is significant deadspace.

Changes in EtCO2 can represent: 
1. Changes in metabolism (e.g. malignant hyperthermia)
2. Changes in circulation (e.g. going toward 0 in obstructive shock) 
3. Changes in ventilation (e.g. decreasing with increasing deadspace) 

https://www.thoracic.org/professionals/clinical-resources/video-lecture-series/critical-care/waveform-capnography.php

## Inspiratory Efforts

Described here by Thind: https://criticalcarenow.com/assessing-inspiratory-efforts-in-intubated-patients/

Pvent = positive airway pressure provided by the vent. 

Pmus = inspiratory muscular effort of the patient. Pressure time productive of Pmus is respiratory effort.

Pmus + Pvent = Ventilatory load

Pes (esophageal pressure) often used as a surrogate for Ppl (pleural pressure)

Pmus = [(Chest wall elastance) * Vt] - change in Pes * t


Alternatively, Pocc (occlusion pressure) can be used instead of esophageal pressure monitoring

End-expiratory airway occlusion performed - creating a negative deflection in airway pressure - the size of which corresponds to the amount of effort.

Application? Diaphragm 'protection' = attempting to neither use to little nor too much patient effort. Pmus 5-10 and Pocc 8 to 20 cmh2o have been proposed as a sweet spot. Idea is to apply proper Pvent to avoid over or under Pmus.


## Obstructive Lung Disease

Roughly 15% of patients who require NIV ultimately fail and require intubation. Heliox has not been shown to reduce this portion.

Pathophys: Expiratory flow limitation leads to Dynamic hyperinflation (increased relaxation volume at end-tidal expiration) leading to Auto-PEEP aka Intrinscic PEEP (elevated pressure in airway at end-expiration). 

Paradigm: prioritize avoidance of ventilator induced injury (hyperinflation -> hypotension, barotrauma) over normalization of CO2.

![alt](https://photos.collectednotes.com/photos/5187/682d99e6-aa0a-435f-ab22-eaa15b495c9c)

CHEST 2015; 147 ( 6 ): 1671 - 1680

Auto-PEEP in severe asthma is often 10-15 cmH2O

![alt](https://photos.collectednotes.com/photos/5187/15548993-2136-4f54-841a-a58663a03b5a)

Clinical experience suggests maintaining Peak pressures below 50cmH2O is safe (has been integrated in several study protocols), but increases beyond this have not been associated with risk of barotrauma. 

RR 10-14, Vt 7 to 9 ml/kg a reasonable starting point (don't often need MV high - since VO2 is normal and there is little harm to elevated pCO2 per se). 100 L/min flow rate with square waveform can allow adequate exhalation time.  (6-8 ml/Kg, RR 12, 60-90 flow rate suggested elsewhere). 

Monitoring of Auto-PEEP with PPlat (targetting <30 cmH2O) recommended (In addition to exp hold - why not just one? - "at the end of expiration the smaller airways may close preventing the over-pressurised alveoli to which they connect from equilibrating with the rest of the respiratory circuit. Thus the expiratory hold manoeuvre will underestimate the actual PEEPi. 
Similarly, failure of the expiratory flow curve to reach baseline is an insensitive test
Plateau pressure (Pplat) will also tend to increase as PEEPi increases, but this could also occur due to decreased lung compliance so increased PEEPi cannot be assumed).)" 

In extremis, can disconnect the vent, allow a prolonged pause, then measure the Plat - if it has dropped signficantly from before, intrinsic PEEP was present

PEEP selection: Generally, increase extrinsic PEEP until Plat increases, then back off (this occurs due to expiratory flow limitation in heterogenous lungs ... ?)

Need to keep in mind if the patient is triggering the vent or not (want to apply some extrinsic PEEP to avoid wasted efforts that do not trigger the vent due to auto-PEEP).

What leads to elevated pCO2? NOT exclusively (or primarily) related to reduced MV - increased deadspace driven by alveolar overdistension (that won't be improved by MV) 

1. Bronchodilators
2. Corticosteroids (onset 6-12 hours)
3. Drugs to optimize patient-ventilator interaction (generally, deep sedation. NMBA, when performed, with intermittent dosing.)

Complications

- pneumothorax in 3-6%
- ineffective triggering of vent if breathing (due to auto-PEEP leading to larger requirement to generate lower than atmospheric pressures.



##References: 
1. Mayo Clin Proc. September 2017;92(9):1382-1400 n http://dx.doi.org/10.1016/j.mayocp.2017.05.004