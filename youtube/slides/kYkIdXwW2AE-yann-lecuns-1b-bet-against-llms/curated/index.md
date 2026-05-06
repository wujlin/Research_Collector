# Curated Slides: Yann LeCun's $1B Bet Against LLMs

This curated subset is for note writing. It removes low-information black frames, sponsor frames, and obvious transition frames from the raw scene-detect output, while adding manual samples from conceptually important gaps.

## Frames

1. `00-00-24_llm_not_language_or_generative.jpg` @ `00:00:24`
   - LLM is not enough as a label: LeCun route is neither language-rooted nor directly generative.
2. `00-01-43_two_paths_roadmap.jpg` @ `00:01:43`
   - Historical fork between discriminative/generative AI and joint embedding approaches.
3. `00-02-16_jepa_basic_mapping.jpg` @ `00:02:16`
   - JEPA predicts target embeddings from context embeddings, instead of directly predicting surface outputs.
4. `00-04-57_self_supervised_cake.jpg` @ `00:04:57`
   - Self-supervised learning is the main cake; supervised and reinforcement learning are smaller layers.
5. `00-05-25_transformer_language_path.jpg` @ `00:05:25`
   - The language path becomes successful through Transformer/GPT next-token self-supervision.
6. `00-12-31_language_vs_video_uncertainty.jpg` @ `00:12:31`
   - Language uncertainty can be represented as probabilities over discrete tokens.
7. `00-13-14_blurry_video_average.jpg` @ `00:13:14`
   - Pixel-level video prediction averages multiple possible futures and becomes blurry.
8. `00-15-25_siamese_joint_embedding.jpg` @ `00:15:25`
   - Siamese networks are an early joint-embedding architecture: compare representations, not reconstructions.
9. `00-17-14_view_embedding_alignment.jpg` @ `00:17:14`
   - Two views of the same object should map to aligned embeddings.
10. `00-18-28_representation_collapse.jpg` @ `00:18:28`
   - If every input maps to the same vector, the alignment loss is satisfied but representation collapses.
11. `00-22-25_barlow_batch_outputs.jpg` @ `00:22:25`
   - Barlow Twins starts from comparing neuron outputs across batches and augmented views.
12. `00-23-40_cross_correlation_matrix.jpg` @ `00:23:40`
   - Cross-correlation matrix makes redundancy between embedding dimensions explicit.
13. `00-24-23_identity_matrix_objective.jpg` @ `00:24:23`
   - Ideal cross-correlation is close to identity: diagonal aligned, off-diagonal decorrelated.
14. `00-28-49_patch_embedding_similarity.jpg` @ `00:28:49`
   - DINO-style patch embeddings show semantic structure without pixel reconstruction.
15. `00-32-03_jepa_architecture.jpg` @ `00:32:03`
   - JEPA predicts future-state embeddings rather than future pixels.
16. `00-33-03_goal_conditioned_planning.jpg` @ `00:33:03`
   - Action-conditioned JEPA can be used for planning toward a goal embedding.
17. `00-34-42_jepa_family_roadmap.jpg` @ `00:34:42`
   - The later roadmap connects JEPA, V-JEPA, V-JEPA2, V-JEPA3 and related systems.
18. `00-35-20_agentic_world_model_claim.jpg` @ `00:35:20`
   - LeCun frames agentic systems as requiring prediction of action consequences.
