# Evaluation & Quality Strategy

## Grounding & Faithfulness
We use an "LLM-as-a-Judge" pattern to verify that rejections actually match the provided RAG context. 
* **The Metric:** "Claim-to-Policy Alignment."
* **The Fail Case:** If the model rejects for "Water Damage" but the retrieved policy segment doesn't mention environmental exclusions, the eval fails.

## Visual Fidelity
The biggest risk is "Hallucinated Damage." 
* **Monitoring:** We track the delta between AI confidence scores and manual override rates. 
* **Drift:** If the vision model starts flagging "scratches" as "structural cracks" (false rejections), our dashboard triggers a threshold alert for prompt-tuning or model switching.

## Regression Testing
The `tests/` suite includes a "Golden Set" of 5 images (Clear Damage, No Damage, Blurry, Random Photo, and Tampered). These must pass 100% on every build to prevent logic regression.
