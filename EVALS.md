# Evaluation & Quality Strategy

## Grounding & Faithfulness (Strategic Roadmap)
For production, the proposed approach is an **LLM-as-a-Judge** pattern to verify that deterministic rejections stay aligned with retrieved RAG context.
* **Metric:** Policy Alignment Score.
* **Strategy:** An independent model (GPT-4o) audits decisions to confirm that if a claim was rejected for "Water Damage," the retrieved policy segment actually contained that specific exclusion. This acts as a guardrail against retrieval noise or logic-grounding failures.

## Visual Fidelity & Drift
The primary operational risk is "Visual Hallucination" or over-detection of damage in low-quality photos. 
* **Monitoring:** I've designed the system to track the delta between AI confidence and manual override rates in the HITL (Human-in-the-Loop) queue. 
* **Drift Detection:** If the vision model begins flagging cosmetic wear as structural damage, it indicates drift. In a production environment, this would trigger an alert to re-evaluate prompt constraints or model versioning.

## Validation Set
I am using a reference set of **5 core test images** (located in `data/test_images/`) representing the primary high-risk policy boundaries:
1. **Water Damage (damage1):** Environmental exclusion path.
2. **Water Damage (damage2):** Environmental exclusion path (validation of visual consistency).
3. **Thermal/Burn Damage (damage3):** Safety/Liability escalation path.
4. **Thermal/Burn Damage (damage4):** Safety/Liability escalation path (validation of risk-aware gating).
5. **Display Pixel Failure (damage5):** Standard approval path (validates functional hardware defect coverage per Segment 2).

Validation involves ensuring these "Golden Cases" maintain 100% accuracy through any logic updates in the `RulesEngine`.
