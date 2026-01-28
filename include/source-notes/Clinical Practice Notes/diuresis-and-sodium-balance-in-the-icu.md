# Diuresis and Sodium Balance in the ICU

## Goals

Fluid restrictions do not work and do not matter. In fact, they don't even make sense

"Sodium retention drives volume overload, with fluid retention largely a passive, secondary phenomenon. However, parameters (urine output, body weight) used to monitor therapy in ADHF measure fluid rather than sodium balance. Thus, the accuracy of fluid-based metrics hinges on the contested assumption that urinary sodium content is consistent."

https://www.sciencedirect.com/science/article/abs/pii/S2213177919300289

Salt restrictions do not work: https://www.coreimpodcast.com/2020/05/20/salt-restriction-in-heart-failure-mind-the-gap-segment/


## Practical

- do not wait 6h to redose lassie if attempting to find a threshold dose. If they haven't made urine in 2h when a foley is in place (or if you've done a bladder scan), they are not going to. Increase the dose
-starting dose: 2.5x outpatient dose, in IV form (per DOSE trial - https://pubmed.ncbi.nlm.nih.gov/21366472/)
-do not discontinue ACEi for CHF exacerbation if BP can tolerate and you think their AKI is cardiorenal. Same for BB - https://pubmed.ncbi.nlm.nih.gov/29423950/

Should we even be monitoring I/O? 
- Using the FeNa (simple conceptually) or NRPE [Na in mol = eGFR * BSA/1.73 * (SerumCr/UrineCr) * 60 minute * 3.25h * (Urine Na / 1000 ml)]. Cohorts: Rao, V.S. et al. J Am Coll Cardiol. 2021;77(6):695–708. , RCT pending: https://clinicaltrials.gov/ct2/show/NCT04481919
- *Note: in that study - 84% arrived on 1500mg equiv of lasix within 2d = 70mg/lasix an hour => "There were no clinically diagnosed episodes of ototoxicity."

https://twitter.com/ebtapper/status/1363237763143860233?s=20

- should we be following I/O at all? Daily weights at all? If we can measure Natriuresis, which is what we care about - might that save significant resources? 
- "In the DOSE(Diuretic Optimization Strategies Evaluation) trial, an National Institutes of Health–funded trial of diuretic strategies conducted at heart failure centers of excellence, the correlation between fluid and weight loss was r ¼ 0.55 (r2 ¼ 0.3). This correlation indicates
there is approximately 70% discrepancy between the information provided by these 2 metrics.

-How much lasix does it take to cause ototoxicity?



[ ] update this with PGR information. 



## Sodium overload and 'fluid overload'

Why is sodium overload so common?

https://annalsofintensivecare.springeropen.com/track/pdf/10.1186/s13613-021-00851-3.pdf

 Outside the hospital: a normal diet is 2.3g (100 mmol) and 2-2.5L of water is usual => 40-50 mmol/l 

- Maintenance fluids are a huge source of this in people who use it. 
- 2L LR = more sodium than the highest recommended intake. 
- Na load from dissolved medication (8.6%, in add'n to many meds paired with Na) and TKO (32.6%) also 

With Na load - body needs to defend tonicity. 

With increased Na load, takes ~3-5 days to reach a new steady state (meaning, for the kidneys to increase secretion to match the sodium load). 

Why? The nephron doesn't have a dedicated method to excrete sodium.  Instead, the kidneys concentrate urine (which is energy intensive and requires corticoids) by increasing urea in the medulla.  

The practical maximum concentration of urine Na is 250-300 mmol/l - beyond that, restoring osmolality requires free water. Application: when someone becomes hypernatremic, we have the energy expenditure in the kidneys in overdrive - they are maxing out but unable to cope with the demand we've put on them.

Note: this balance is disturbed by ATN (less concentration ability), catabolism (need to excrete solutes), hyperglycemia (osmotic diuresis)

### Clinical impact? 
 
TOPMAST trial: Na 154 (NaCl) was compared to NaCl 54 (hypotonic) - with identical drain outputs. In 48h, the difference in fluid retention was ~887 mL despite identical volume influenced. Meaning, nearly 1L of the positive balance (roughly 1/4) is attributable to the sodium load. 

-- more patients in the hypertonic group developed pulmonary edema (17% vs 3%, suggesting that this retention may be primarily intravascular)

-- other studies suggest that positive sodium balance (but not positive fluid balance) is related to a next-day reduction in P/F ratio.

### Interventions

Don't use maintenance fluids often. If you do, use 1mmol Na / kg per day and 25 mL / kg per day.

One possible way to help: urea to help the kidneys increase their concentration gradient to allow more sodium excretion.  Needs to be studied

Use D5w as your backer solution: studied in [40, Bihari. https://pubmed.ncbi.nlm.nih.gov/30482136/] - decreased daily Na administered by half leading to less daily fluid balance and electrolyte disturbances. 

![alt](https://photos.collectednotes.com/photos/5187/93303c08-20eb-4acb-a340-d487e8a2b032)

(Note, the dextrose.. 

1L D5w = ~50g of dextrose, (3.4 calories per gram of dextrose), ~175 calories.

Risk of hyponatremia? Only if ADH is present - if a patient is developing hyponatremia from fluid administration, either they are getting very large amounts of free water (can be calculated based on GFR and dilute urine ~50 mOsm/l). No difference in rates of hyponatremia in [40, Bihari https://pubmed.ncbi.nlm.nih.gov/30482136/] 

Why? Unlike 3-5d to up regulate the concentration of urine, dilution of urine can happen immediately. Isosthenuric urine is energy neutral (right?), but up-down regulation are not equally fast.

Is it better to reconstitute D5w or use the usual and add lasix? Not sure - but adding lasix ( = causes diuresis in excess of natriuresis, added risk of hyperntramia)
-indapamide might be used here to avoid the intense kaliuresis of thiazides (it is thiazide-like, https://pubmed.ncbi.nlm.nih.gov/26948252/)
 
Na overload as a cause of BUN elevation?

23. Rakova N, Kitada K, Lerchl K, Dahlmann A, Birukov A, Daub S, et al.
Increased salt consumption induces body water conservation and
decreases fuid intake. J Clin Invest. 2017;127(5):1932–43.
24. Kitada K, Daub S, Zhang Y, Klein JD, Nakano D, Pedchenko T, et al. High
salt intake reprioritizes osmolyte and energy metabolism for body fuid
conservation. J Clin Invest. 2017;127(5):1944–59.
25. Kerstens MN, van der Kleij FG, Boonstra AH, Sluiter WJ, Koerts J, Navis
G, et al. Salt loading afects cortisol metabolism in normotensive
subjects: relationships with salt sensitivity. J Clin Endocrinol Metab.
2003;88(9):4180–5

We often associated the elevated BUN with the lasix, but it may actually be the increased sodium that we are using the lasix to treat that causes the BUN.

## Harms of Fluid overload

Observational data that positive fluid balance after day 3 is correlate with worse outcomes


Isotonic crystalloid distributes from the plasma into the interstitial fluid in 20-30 minutes.

## Diuresis strategy

After shock resolved, begin diuresis

Key question: what to do if hypotension recurs? https://twitter.com/hassanyth/status/1359197676592631815?s=20

Transcapillary Plasma Refilling Rate:  when removing fluid, how fast does the fluid pull back in to the circulating blood volume.

Traditionally, described by starling forces. However, some thought that the glycocalyx creates an intermediate compartment.  Refill rate is known to be effected by the adrenergic nervous system (increased by beta 2, some alpha 1)

Takes 20-30 minutes for the oncotic pressure of albumin (20%) to increase plasma fluid volume. 

In non-edematous states, muscles are the biggest contributor (they have ~5L of interstitial fluid, 14L of intracellular fluid).  Restoration of blood volume after moderate hemorrhage: 87% by 6h, 95% by 12h, 100% by 18h. Similarly, change from upright to spin position will induce a 10% hemodilution that occurs in roughly 15-30 minutes. Anesthesia/vasodilation causes a similar effect.

In HD/UF, most machines come with a monitor that estimates blood volume (to ensure it doesn't drop too much by removing too quick) that works based on the plasma density.

Dialysis flow rate induced decreases in blood volume: https://www.karger.com/Article/Abstract/501407 . Plasma refill rate after fast UF => 10 ml/kg/hr = few hours to re-equilibrate after rapid 1.5L diuresis. 2-6 mL/kg/hr after iHD

Review of mechanisms in hemorrhage, position, vasodilation, dialysis: https://pubmed.ncbi.nlm.nih.gov/31288231/ 
 
