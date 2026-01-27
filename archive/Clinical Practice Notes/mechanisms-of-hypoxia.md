# mechanisms of hypoxia

##History
Research started to explain why WW2 pilots crashed at high altitude. Initially thought it was CO poisoning.
e.g. Rley and Cournand J Appl Physiol 1949

How this physiology was discovered: 
MIGET (Multiple Inert Gas Elimination Technique): 6 different gasses varying in solubility. Don't react with body = inert. Obey Henry's law

- Highly Soluble (Acetone) = differentiates high V/Q from deadspace. 
- Poorly Soluble (sulfur hexafluoride) = differentiates low V/Q from shunt

Measure mixed venous concentration and exhaled gas composition to determine many different V/Q ratios in normal lung. 

Can also do for a disease lung (e.g. emphysema) to differentiate different distributions of V/Q units.

[ ] image from lecture - MIGET 


##Terminology: 

- SpO2: peripheral estimate of SaO2
- PaO2 = chemical activity of O2
- CaO2 = ml O2 per dL of blood (depends on Hgb)
- SaO2 = CaO2 / O2 carrying capacity (does not depend on Hgb)

Note: O2 poorly soluble in water = why do we have hemoglobin

West Zone 1: ventilation > perfusion
West Zone 2: equal
West Zone 3: ventilation. < perfusion

##Alveolar Gas Equation

What is alveolar air? Consider, air composition varies throughout the lung (space) and throughout the respiratory cycle (time). 

Alveolar air: hypothetical mean such that RQ = Gas RQ = Blood RQ 

In english, that the amount of O2 that leaves the alveoli is equal to the amount of O2 that enters the blood. Additionally, the amount of CO2 that leaves the blood is equal to the amount added to the O2. Lastly, that the ratio of O2 transferred over CO2 transferred is equal to RQ.

Arterial_pCO2 =ish to ideal pCO2. Thus Simplified (which is when CO2 = 0): PAO2 = (PB-47) * FiO2 - (PaCO2 / RER). 

####Full Alveolar Gas Equation

Reference: DOI 10.1093/bjaceaccp/mkh008

The full equation is: 

PAO2 = (PB-47)*FiO2 - (PaCO2/RER) + [FiO2 * PaCo2 * (1-RER)/RER]

This extra terms accounts for the fact that when RER =/= 1, then the mass action of molecules in won't equal out (e.g. at RQ 0.8, VCO2 = .2 L/min, VO2 = .25 L/min - then 50cc of gas needs to passively infuse to remain at FRC). 

![alt](https://photos.collectednotes.com/photos/5187/70f0a422-964e-4f5d-ab80-500f75a3e38b)

However, when FiO2 * (1-RQ) is << 1, the term becomes less consequential and can be safely ignored. This functionally assuming that inspired and expired ventilation are identical. 

##Shunt
Can be cardiac or pulmonary (definition: never contacts alveolar air). Chronic lung diseases (COPD, asthma) result in little shunt, while acute lung diseases (e.g. PNa) can have large shunts. 

How do you calculate the shunt fraction?

Qs/Qt = 100 * (CiO2 - CaO2) / (CiO2 - CvO2) 

Qs / Qt = 100 x (CiO2- CaO2) / [(CiO2 - CaO2) + 0.1 x VO2/Qt)

In shunt, what is the V/Q? (answer: 0)

Hypercapnia can also (in additional to hypoxemia) occur if shunting is massive (40% shunt fraction -> 10 mmHg increase of CO2, prior to compensation)



##Dead space

How do you calculate the dead space fraction?

In deadspace, what is the V/Q? (answer: infinity)

Similar to shunt fraction, deadspace fraction can be calculated as: 

Vd/Vt = 100 * (PaCO2 - PECO2)/PaCO2

Normal Vd is near 150 mL (anatomic deadspace, very little physiologic deadspace)

##V/Q mismatch 

Note: the fact that V = / = Q does not lead to hypoxemia. It's the unequal distribution throughout the lung that does. Mismatch is bit of a misnomer. 

[ ] Consider: what would happen if you put someone on milrinone => increase Q through, but homogeneously. Would A-a gradient change? 
Not - and in practice, because blood flow distribution throughout the lung becomes more homogeneous, A-a gradient decreases

Normal overall V = 4L, Q= 5L/min (corresponding to RER 0.8)

Will cause both hypercapnia and hypoxemia (see below) 

Does it correct with oxygen? It depends

- if ventilation limited (= V/Q under 1, aka West zone 1): yes
- if perfusion limited (= V/Q over 1, aka West zone 3): no

With PEEP?

PEEP improves oxygen by recruiting collapsed lungs and reducing intrapulmonary shunt (more helpful if V/Q under 1 aka West Zone 1 = more recruitable lung exists). 

Rearranging based on the assumption of RQ = Gas RQ = Blood RQ, one can graph the different possible solutions to partial pressures of O2 and CO2, which functionally corresponds to different partial pressures of blood exiting parts of the lungs with this type of physiology: 

![alt](https://photos.collectednotes.com/photos/5187/ddd646d2-9d32-4261-9176-10b11d0f97e3)

 DOI: 10.1183/09031936.00039214

What happens as the lung gets more dispersion in V/Q for different parts of the lungs?  (below done by simulation, same ref as above)

![alt](https://photos.collectednotes.com/photos/5187/3656c981-7442-482b-8a5d-cf6aa76e8b56)

- regional airway obstruction: O2 will be effected more than CO2
- regional vascular obstruction: CO2 will be effected more than O2

However, the body will be restored, but at the price of increased A-a gradient or ventilation.

What are the 3 ways that the body can compensate for V/Q mismatching? 

1. Tissues extract more blood from the Hb (price: more SpO2 drop than expected)
2. Hyperventilate (price: work of breathing if altered mechanics, limited ability to correct for blood on the low O2 dissoc curve e.g. shunt) 
3. Increase CO 

## Hypoventilation
Causes hypoxemia and hypercapnia

![alt](https://photos.collectednotes.com/photos/5187/16866771-4e1c-4bde-83b8-38f4e3e1b1d4)

## Reduced Mixed Venous O2 
Occurs when Q' (or DO2) is low in relation to VO2 (e.g. heart failure or very high VO2). This will be more problematic if V/Q mismatch is present. 

## Other, less common clinically
### Diffusion limitation across the blood:gas barrier at alveoli
Reduced DLCO 

Healthy, at sea level: 0.25s equilibrium time required for O2 in capillary. At rest, expected 0.75s transit time for blood through lungs (3:1 reserve)

- Can impact in exercise: longer dwell time of blood in the pulmonary capillaries to oxygenate... symptoms predominantly occur when cardiac output increases (fast blood movement). Athletes with very high cardiac output do sometimes reach this threshold. 
- Also more impactful at elevation (mechanism: lower inspired 02 = less gradient for O2 transit = slower rate)
- to what extent does this occur in ILD? common when DLCo 50% or less, particularly with exercise

Note: diffusion limitation of CO2 does NOT occur, because it is 20x more soluble in the blood:gas barrier 

### Reduced PiO2
- note, not necessarily decreased FiO2 (rare, occurs during asphyxiation) - %O2 stays the same as elevation changes.  This will not cause hypercapnia unless PCO2 increased (e.g. asphyxiation)

![alt](https://photos.collectednotes.com/photos/5187/86decceb-85cd-4114-bfd3-0c45c16cd1df)

## Ways to quantify oxygenation efficiency

- PaO2 / FiO2 (traditionally used in ARDS)
- SaO2 or SpO2 / FiO2
- P (A-a) O2 (conceptually important, but always elevated if on supplemental O2. Additionally, deviations of R from 0.8 will introduce error) 
- Qs / Qt (traditionally used in peds cards / cong heart)

![alt](https://photos.collectednotes.com/photos/5187/6b15cdbe-65a4-427e-984f-61f6682b2755)