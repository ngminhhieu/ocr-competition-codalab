#!/bin/bash

rm competition.zip

zip -j scoring_program.zip ./scoring_program/*

zip -j public_ground_truth.zip ./public/ground_truth.csv

zip -j private_ground_truth.zip ./private/ground_truth.csv

zip -j warmup_ground_truth.zip ./warm_up/ground_truth.csv

zip competition.zip competition.yaml data.html evaluation.html logo.png overview.html terms.html scoring_program.zip public_ground_truth.zip private_ground_truth.zip warmup_ground_truth.zip

rm public_ground_truth.zip

rm private_ground_truth.zip

rm scoring_program.zip

rm warmup_ground_truth.zip