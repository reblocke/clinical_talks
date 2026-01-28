//Statistics simulation

clear
set obs 1000000
set seed 12345
generate id = _n

//Generate Pneumonia Cases 
generate mrsa_fate = runiform() //random number between 0-1
recode mrsa_fate (min/0.963=0) (0.963/max=1), gen(has_mrsa) // 3.7% w MRSA
label define mrsa_lab 0 "Pneumonia not from MRSA" 1 "MRSA Pneumonia"
label values has_mrsa mrsa_lab

//Generaxte Brian's guesses
generate brian_no = 0
generate coin_fate = runiform() // random number between 0-1
generate brian_coin = 0 if coin_fate < 0.5
replace brian_coin = 1 if coin_fate >= 0.5
generate dice_fate = runiformint(1, 6)
generate brian_dice = 0 if dice_fate <= 4
replace brian_dice = 1 if dice_fate >=5
label values brian_no mrsa_lab
label values brian_coin mrsa_lab
label values brian_dice mrsa_lab


//Adjudicate Guesses
//generate correct = 1 if has_mrsa == brian_dumb
//replace correct = 0 if has_mrsa != brian_dumb
//label define correct_lab 0 "Incorrect" 1 "Correct"
//label values correct correct_lab

//tab correct
//diagt has_mrsa brian_dumb

logistic has_mrsa brian_no brian_dice brian_coin
lroc
