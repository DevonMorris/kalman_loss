# Kalman Loss

You've heard of [Kalman Gain](https://en.wikipedia.org/wiki/Kalman_filter#Kalman_gain_derivation)
, but have you heard of **Kalman Loss**? Kalman Loss is a revolutionary new
technology that takes what you already know about weight loss and adds *Space-Age Technology*
from the Apollo missions to more accurately track your weight-loss journey. Buy now
:gem: :raised_hands:.

More seriously, I've been more health-focused in the last 12 months. During fall
of 2021, I lost ~25lbs using alternate day fasting and rowing. I went from ~200lbs
to a low of 173lbs. Over the holidays, I ate well and barely exercised and need
to get back on the grind. This repo will help me track my progress and predict
if I'll meet my goal of 165lbs by mid April.

## Problem

Although this is really an estimation and controls problem, I'm treating it as
simply an estimation problem. I have already chosen my policy (control law) to
be the following

* Fast once every 2 days
* Row 10k on fasting days
* Lift weights on non-fasting days

As such, I can "measure" a couple of factors here.
* Weight as reported by my home scale
* Daily active calories as reported by my apple watch
* Daily ingested calories as reported by a calorie checking app and my honesty

(For mathematical modeling purposes, I'll use these two calorie measures as
control inputs)

I want to infer the following state variables.
* "True Weight" (weight with daily fluctuations smoothed)
* Caloric Conversion (number of 1000s of calories equating to 1lb lost)
* Non-active daily calories ([BMR](https://en.wikipedia.org/wiki/Basal_metabolic_rate) + [TEF](https://en.wikipedia.org/wiki/Specific_dynamic_action) + [NEAT](https://en.wikipedia.org/wiki/Thermogenesis))

## Mathematical Formulation
