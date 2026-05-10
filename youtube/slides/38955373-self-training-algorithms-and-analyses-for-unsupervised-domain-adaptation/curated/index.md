# Curated Slides: Self-training Algorithms and Analyses for Unsupervised Domain Adaptation

- Source: SlidesLive `38955373`
- Full slide deck: [`../all/index.md`](../all/index.md)
- Curated frame count: `31`
- Strategy: semantic selection aligned with the talk logic, replacing the earlier evenly spaced sample.

## Frames

- ![Title and workshop context](01-title.png) `slide 001` - Title and workshop context
- ![Remote sensing example: labels are expensive and target regions shift](02-remote-sensing-motivation.png) `slide 006` - Remote sensing example: labels are expensive and target regions shift
- ![UDA framing and this talk focuses on self-training](03-uda-this-talk-self-training.png) `slide 011` - UDA framing and this talk focuses on self-training
- ![Setting 1: auxiliary information](04-setting1-auxiliary-information.png) `slide 012` - Setting 1: auxiliary information
- ![Setting 2: gradual shifts](05-setting2-gradual-shifts.png) `slide 013` - Setting 2: gradual shifts
- ![Outline connecting auxiliary information and gradual shifts](06-outline-two-settings.png) `slide 014` - Outline connecting auxiliary information and gradual shifts
- ![Setup question: how to use unlabeled data with auxiliary information](07-setup-question.png) `slide 022` - Setup question: how to use unlabeled data with auxiliary information
- ![Baseline 1: aux-inputs architecture](08-aux-inputs-baseline.png) `slide 023` - Baseline 1: aux-inputs architecture
- ![Aux-inputs improves ID but hurts OOD accuracy](09-aux-inputs-hurt-ood.png) `slide 026` - Aux-inputs improves ID but hurts OOD accuracy
- ![Aux-outputs pretraining then finetuning pipeline](10-aux-outputs-pretraining-pipeline.png) `slide 031` - Aux-outputs pretraining then finetuning pipeline
- ![Aux-outputs improves OOD while ID is not as good as aux-inputs](11-aux-outputs-improves-ood.png) `slide 034` - Aux-outputs improves OOD while ID is not as good as aux-inputs
- ![In-N-Out combines aux-inputs pseudo-labels with aux-output initialization](12-in-n-out-algorithm.png) `slide 039` - In-N-Out combines aux-inputs pseudo-labels with aux-output initialization
- ![In-N-Out improves accuracy over baselines on ID and OOD](13-in-n-out-results.png) `slide 040` - In-N-Out improves accuracy over baselines on ID and OOD
- ![Theory setup: multi-task linear regression graph](14-theory-multitask-linear-regression.png) `slide 041` - Theory setup: multi-task linear regression graph
- ![Why aux-inputs helps ID but can hurt OOD](15-aux-inputs-theory-id-vs-ood.png) `slide 046` - Why aux-inputs helps ID but can hurt OOD
- ![Why aux-outputs improves OOD robustness](16-aux-outputs-theory-robustness.png) `slide 051` - Why aux-outputs improves OOD robustness
- ![Pretraining plus self-training for further gains](17-pretraining-self-training-gains.png) `slide 056` - Pretraining plus self-training for further gains
- ![Summary of aux-inputs, aux-outputs, and In-N-Out](18-auxiliary-summary.png) `slide 057` - Summary of aux-inputs, aux-outputs, and In-N-Out
- ![Understanding self-training for gradual domain adaptation](19-gradual-domain-adaptation-title.png) `slide 059` - Understanding self-training for gradual domain adaptation
- ![Gradual domain adaptation setup and goal](20-gradual-domain-setup.png) `slide 064` - Gradual domain adaptation setup and goal
- ![Gradual domain adaptation example: train plus test on target](21-gradual-domain-example.png) `slide 067` - Gradual domain adaptation example: train plus test on target
- ![Gradual self-training traces the decision boundary across domains](22-gradual-self-training.png) `slide 072` - Gradual self-training traces the decision boundary across domains
- ![Assumption: shift smaller than margin under Lipschitz model](23-shift-margin-assumption.png) `slide 074` - Assumption: shift smaller than margin under Lipschitz model
- ![Source classifier becomes stale as the domain path moves](24-source-classifier-stale.png) `slide 079` - Source classifier becomes stale as the domain path moves
- ![Theory results for gradual self-training](25-theory-results.png) `slide 081` - Theory results for gradual self-training
- ![Self-training and stability summary](26-self-training-stability.png) `slide 084` - Self-training and stability summary
- ![Gradual self-training empirical results](27-gradual-results.png) `slide 085` - Gradual self-training empirical results
- ![Essential ingredients: regularization, hard pseudolabels, experiments](28-essential-ingredients-experiments.png) `slide 088` - Essential ingredients: regularization, hard pseudolabels, experiments
- ![When GST works: Wasserstein-infinity shifts](29-wasserstein-infinity-shifts.png) `slide 089` - When GST works: Wasserstein-infinity shifts
- ![When GST does not work: KL shifts](30-kl-shifts-failure-mode.png) `slide 090` - When GST does not work: KL shifts
- ![Final remarks: domain adaptation needs structure](31-final-remarks.png) `slide 093` - Final remarks: domain adaptation needs structure
