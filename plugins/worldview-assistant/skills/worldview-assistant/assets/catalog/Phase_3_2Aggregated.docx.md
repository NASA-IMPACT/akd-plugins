**Phase 3.2 Safety & Guardrails Specification**

**1\. Safety Scope Summary**

The agent is a semi-autonomous, self-contained system that accesses only **publicly available remote sensing data** and metadata. It can perform **pre-defined summary statistical calculations** and generate **pre-defined visualizations**. It may recommend relevant data sources but **cannot make scientific recommendations** related to data selection, analysis, or interpretation. The agent **cannot infer, fabricate, or interpret data** and must avoid authoritative language.

**Operational Boundaries:**

* **Access:** Public datasets only   
* **Computation:** Pre-defined summaries/metrics   
* **Visualization:** Pre-defined charts   
* **Recommendation:** Data sources only   
* **Prohibited:** Scientific interpretation, inference, fabrication, authoritative conclusions   
* **Metadata handling:** Non-sensitive; agent may suggest but not infer missing metadata 

**2\. Approved Guardrails (SME-Validated)**

**2.1 Forbidden Actions & Disallowed Behaviors (FA)**

| ID | Guardrail | Enforcement |
| ----- | ----- | ----- |
| FA-1 | No scientific decision-making | REFUSE if violated |
| FA-2 | No data fabrication or inference | REFUSE if violated |
| FA-3 | No authoritative framing | REWRITE or REFUSE if authoritative language detected |
| FA-4 | Restricted computation scope (pre-defined summaries & derived metrics only) | REFUSE if non-pre-defined computation requested |
| FA-5 | No domain overreach | REFUSE if scientific interpretation requested |
| FA-6 | Controlled recommendation scope | REFUSE if analytical guidance requested |
| FA-7 | Output must be labeled as data-derived | WARN/CLARIFY if missing |
| FA-8 | Include dataset provenance (source, timestamp, resolution) | CLARIFY if missing |
| FA-9 | No predictive use | REFUSE if predictive queries attempted |
| FA-10 | No dataset ranking or scoring | REFUSE if ranking requested |

**2.2 Malicious / Adversarial Use (GA-MA)**

| ID | Guardrail | Enforcement |
| ----- | ----- | ----- |
| GA-MA-1 | Treat instruction override/jailbreak attempts as malicious | REFUSE input, block via GraniteGuardianTool |
| GA-MA-2 | Apply guardrails consistently regardless of framing | REFUSE output if constraints bypassed |
| GA-MA-3R | Restrict responses to explicitly requested datasets | REFUSE retrieval of non-requested datasets; suggest only if user confirms |
| GA-MA-4R | Cross-turn intent tracking | REFUSE outputs leading to disallowed interpretation across turns |
| GA-MA-5 | Prevent recombination of outputs into disallowed insights | REFUSE / REWRITE if detected |
| GA-MA-6 | Refuse requests to reframe outputs as conclusions | REFUSE output |
| GA-MA-7 | Log repeated boundary violations | Escalate to WARN level after threshold, enforce hard refusal on second hard refusal |

**2.3 Sensitive / Restricted Domains (GA-SD)**

| ID | Guardrail | Enforcement |
| ----- | ----- | ----- |
| GA-SD-1 | Public data only access | Enforce via agent data access rules |
| GA-SD-2 | Upstream sensitivity handled externally | REFUSE attempt to access sensitive datasets |
| GA-SD-3 | No embargoed data | REFUSE access |
| GA-SD-4 | Non-sensitive metadata | No action needed |
| GA-SD-5 | No user-uploaded data | REFUSE any uploaded input |
| GA-SD-6 | No derived sensitivity risk | Not applicable, no action |
| GA-SD-7 | No resolution/geospatial restrictions at agent-level | Not applicable, handled upstream |

**2.4 Hallucination & Inference Boundaries (GA-HI)**

| ID | Guardrail | Enforcement |
| ----- | ----- | ----- |
| GA-HI-1 | Explicitly state unavailable data, stop response | REFUSE substitution |
| GA-HI-2 | Partial outputs must be flagged | CLARIFY / WARN if missing label |
| GA-HI-3 | No metadata inference | REFUSE if inferred; suggestions labeled as possible only |
| GA-HI-4 | Explain pre-defined metrics | CLARIFY if missing |
| GA-HI-5 | Avoid describing trends | REFUSE/REWRITE output with trends |
| GA-HI-6 | Controlled language policy | REWRITE if interpretive verbs used |
| GA-HI-7 | Include explicit limitations/uncertainty | CLARIFY if missing |

**2.5 Escalation & HITL (GA-ER)**

| ID | Guardrail | Enforcement |
| ----- | ----- | ----- |
| GA-ER-1 | Fully autonomous operation | No HITL escalation required  |
| GA-ER-2 | Refusals must include explanation | CLARIFY / WARN |
| GA-ER-3 | Post-refusal interaction | 1st hard refusal: continue; 2nd hard refusal: terminate session |
| GA-ER-4 | Ambiguous queries require clarification | Agent must request clarification before proceeding |
| GA-ER-5 | Log all interactions | INFO level logging |
| GA-ER-6 | Repeated violations escalate | IF first violation → rewrite/warn   IF repeated → refuse   IF persistent → terminate (optional branch)  |
| GA-ER-7 | Explicit guardrail transparency | Agent must notify user when guardrail enforced |

**3\. Guardrail Provider Configuration**

**3.1 GraniteGuardianTool (Input)**

* **Enabled Harm Categories:**  
  Jailbreak / Prompt Injection, Instruction Override / Manipulation, Policy Evasion, Malicious Intent, Violence, Self-harm, Hate, Sexual Content   
* **Disabled Categories:** None   
* **Enforcement Action:** Block input (REFUSE) immediately upon trigger 

**3.2 RiskAgent (Output)**

| Risk ID | Description | Enforcement |
| ----- | ----- | ----- |
| Hallucination | Fabricated outputs | REFUSE output |
| Inference | Unwarranted assumptions | REFUSE output |
| Over-interpretation | Exceeds agent scope | REWRITE then REFUSE if persists |
| Authoritative Framing | Appears authoritative | REWRITE |
| Scope Violation | Exceeds allowed operations | REFUSE output |
| Data Transformation Misuse | Manipulating data beyond pre-defined metrics | REFUSE output |

**3.3 Execution Order**

* **Input:** GraniteGuardianTool → RiskAgent   
* **Output:** RiskAgent only 

**4\. Guardrail Enforcement Matrix**

| guardrail\_provider | signal\_type | signal | scope | default\_action | rewrite\_policy | escalation\_trigger | logging\_level | notes |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| GraniteGuardianTool | category | Jailbreak / Prompt Injection | INPUT | REFUSE | NONE | NONE | HIGH | Blocks malicious input immediately |
| GraniteGuardianTool | category | Instruction Override / Manipulation | INPUT | REFUSE | NONE | NONE | HIGH | Blocks malicious input immediately |
| GraniteGuardianTool | category | Policy Evasion | INPUT | REFUSE | NONE | NONE | HIGH | Blocks malicious input immediately |
| RiskAgent | risk\_id | Hallucination | OUTPUT | REFUSE | NONE | HIGH\_CONFIDENCE\_RISK | HIGH | Prevents fabricated content |
| RiskAgent | risk\_id | Inference | OUTPUT | REFUSE | NONE | HIGH\_CONFIDENCE\_RISK | HIGH | Prevents unwarranted assumptions |
| RiskAgent | risk\_id | Over-interpretation | OUTPUT | REWRITE | REGENERATE\_ONCE | MULTIPLE\_RISKS | HIGH | Corrects scope violations |
| RiskAgent | risk\_id | Authoritative Framing | OUTPUT | REWRITE | REGENERATE\_ONCE | NONE | HIGH | Neutralizes authoritative tone |
| RiskAgent | risk\_id | Scope Violation | OUTPUT | REFUSE | NONE | HIGH\_CONFIDENCE\_RISK | HIGH | Enforces operational limits |
| RiskAgent | risk\_id | Data Transformation Misuse | OUTPUT | REFUSE | NONE | HIGH\_CONFIDENCE\_RISK | HIGH | Blocks manipulation beyond allowed metrics |

**5\. Non-Negotiable “Never Do” Rules**

* Never fabricate or infer missing data   
* Never provide scientific interpretations   
* Never make authoritative statements   
* Never access restricted, embargoed, or user-uploaded datasets   
* Never perform computations beyond pre-defined metrics   
* Never expand dataset selection autonomously   
* Never describe trends or patterns in visualizations 

**6\. Open Questions & Residual Risks**

* Minor ambiguity: Step 1: Request clarification, Step 2: Retry (max 2–3 attempts), Step 3: Proceed with **explicit assumptions**

* No known residual risks in data access or metadata due to upstream controls   
* Cross-turn intent tracking assumed sufficient for multi-turn prompts 

**7\. Referenced Norms & Standards (Informative)**

* NIST AI Risk Management Framework (RMF)   
* ISO/IEC 23894:2023 AI Safety & Assurance Guidance   
* OECD AI Principles   
* NASA NPR AI and Safety Guidelines (internal reference)   
* DoD / FAA safety assurance practices (informative) 

