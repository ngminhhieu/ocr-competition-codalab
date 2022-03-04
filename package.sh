#!/bin/bash

rm competition.zip

zip -j scoring_program.zip ./scoring_program/*

zip -j public_ground_truth.zip ./data/public/ground_truth.csv

zip -j private_ground_truth.zip ./data/private/ground_truth.csv

zip -j warmup_ground_truth.zip ./data/warm_up/ground_truth.csv

zip -j competition.zip html/award.html html/dataset.html html/evaluation.html html/overview.html html/submission.html html/tasks.html html/terms.html

zip -j competition.zip competition.yaml scoring_program.zip public_ground_truth.zip private_ground_truth.zip warmup_ground_truth.zip

zip -j competition.zip log/logo.svg

rm public_ground_truth.zip

rm private_ground_truth.zip

rm scoring_program.zip

rm warmup_ground_truth.zip