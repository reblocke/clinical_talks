# MRSA Nasal Swab


## VA dataset
CID 2019 DOI: 2020;71(5):1142–8

All patients 18+ screened with MRSA nasal swab at admission - 245,000 patients. 
Positive MRSA Nares in 22%. 

They looked at the subsequent likelihood of cultures being positive for various pathogens at various sites.  Note: this does not establish true infection vs colonization: reference standard is just subsequent culture. 

### Pneumonia

Model: 
100ish people with pneumonia. 12 have MRSA PNa. 88 do not

- People with MRSA pneumonia: 9 test positive, 3 test negative
- People without MRSA pneumonia: 17 test positive, 71 test negative

![alt](https://photos.collectednotes.com/photos/5187/2fe27f09-108b-488c-b74a-2ed0b20638d7)

Actual data:

- Sensitivity: 76.2% = chance in somebody who does NOT have the disease (no MRSA PNa) that you get it right (says no MRSA)
- Specificity: 80.3% = chance in somebody who has the disease that the test gets it right

However, when practicing medicine - we don't know who has the disease vs not (that's the point of the workup). We just know the test result. 

If we combine knowledge of the prevalence of the condition we are looking forward, we can calculate the positive and negative predictive value of a test:

- Positive predictive value: 35% = chance in somebody who has a positive test that it gets it right
- Negative predictive value: 96.1% = chance that the test gets it right in someone with a negative test

However, this tells you information in ALL comers (in a hypothetical person) - but does not allow you to tailor the information to a clinical situation. 

E.g. we know that cavitary pneumonias are MRSA in ____, and that empyemas are MRSA in 15% - how can we utilize this information? 

#### Likelihood Ratios 

- Pretest ODDS (P / 1-P)

- Pretest odds * LR = post-test odds

What is the positive likelihood ratio? 

- P(test + in diseased person) / P (test + in non diseased person) 
- sensitivity / 1-specificity

What is the negative likelihood ratio? 

- P(test - in disease person/ P(test - in nondisease person) ok
- 1-sensitivity / specificity

In case of MRSA nasal swab for pneumonia: 

Positive LR: 3.9
Negative LR: 0.3

Pre-test odds in PNA:  0.12 / 0.88 = .136 

0.136 * .3 (negative test) => 4% chance of MRSA PNa after negative chance (=NPV of 96%)

0.136 * 3.9 (positive test -> 0.53 odds = ~35% chance of PNa (=PPV 35%)

#### Application

Where this gets powerful is when we change the pre-test odds

Pretest odds of MRSA in empyema? 20%

Necrotizing pneunonia after viral infection? 50%

https://calculator.testingwisely.com/playground/5/76.2/80.3/positive


### Other infections

- ENT: -LR 0.28
- PNa: -LR 0.31
- Blood: -LR 0.37
- Urine: -LR 0.37
- Wound: -LR 0.49
- Heart: -LR 0.51

Utility is based in pre-test odds!
