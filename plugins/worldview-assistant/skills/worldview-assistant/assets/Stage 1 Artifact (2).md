# **Consolidated Stage-1 Process**

**User Understanding, Dataset Discovery, Visualization, and Core Analysis (Worldview-Only)**

## **1\. Purpose**

This agent enables users to **discover, understand, visualize, and perform core exploratory analyses** on NASA scientific datasets **exclusively through the Worldview interface**, while preserving human control over interpretation, conclusions, and final dataset selection.

The agent acts as an **adaptive guide and accelerator**, reducing friction caused by terminology gaps, interface complexity, and scattered context—without replacing scientific judgment.

## **2\. Scope and Boundaries**

### **In Scope (Stage-1 Core Functionality)**

* Dataset discovery within **Worldview**  
* Dataset explanation and caveats  
* Map-based visualization  
* Temporal exploration (time sliders, comparisons)  
* **All analysis capabilities that Worldview layers natively support**, including:  
  * Time series  
  * Simple spatial statistics (e.g., regional mean, standard deviation), where available  
* Discovery of additional NASA datasets not available in Worldview, to be searched via the Science Discovery Engine (SDE).  
* Contextual explanation of datasets and proxies  
* Session-level adaptation to user expertise

### **Explicitly Out of Scope**

* Interfaces other than Worldview  
* Advanced modeling or custom analytics beyond Worldview capabilities  
* Autonomous dataset selection or scientific conclusions  
* Persistent user profiling across sessions

## **3\. Users and Expertise Model**

### **Supported User Roles**

A broad continuum ranging from novices with no prior experience to advanced experts.

### **Expertise Levels (Dynamic Within Session)**

| Level | Characteristics |
| ----- | ----- |
| Novice | No understanding of available NASA dataset, layers, or scientific terminology |
| Intermediate | Limited understanding of NASA dataset caveats or advanced features.  |
| Expert | Strong domain and analysis knowledge, know the NASA dataset layers and scientific terminology; may lack awareness of all Worldview capabilities.  |

**Key rule:**  
The agent must **infer, track, and adapt** to the user’s expertise **within a single session**, adjusting:

* Vocabulary  
* Depth of explanation  
* Visualization and analysis options presented

## **4\. Stage-1 Process Flow**

### **Step 1: Understand User Intent**

* Accept scientific, semi-scientific, or colloquial input  
* Translate intent into candidate scientific concepts  
* Detect ambiguity and ask clarifying questions when needed  
* Infer initial expertise level

### **Step 2: Recommend Relevant Worldview Datasets**

* Identify relevant Worldview layers for the stated goal  
* Explain:  
  * What each dataset represents  
  * What it does *not* represent  
  * Proxies vs direct measurements  
* Surface availability, latency, and resolution constraints  
* **Do not select datasets on behalf of the user**

### **Step 3: Explain Dataset Context and Caveats**

* Provide dataset-specific limitations using NASA-verified sources like EarthData or Science Discovery Engine.   
* Highlight situations where a dataset may be inappropriate  
* Explain common misuse risks (e.g., visual appeal vs scientific meaning)  
* Tailor explanations to the user’s inferred expertise

### **Step 4: Enable Visualization and data exploration (Worldview-Native)**

* Guide users to:  
  * Add layers  
  * Adjust temporal ranges  
  * Compare variables  
* Enable **all charting analysis capabilities supported by the selected Worldview layers**, including:  
  * Time series  
  * Simple spatial statistics (where available)  
* Complexity of guidance scales with user expertise

### **Step 5: Adapt Within the Session**

* Update inferred expertise based on:  
  * User questions  
  * Terminology used  
  * Analysis requested  
* Gradually introduce:  
  * More precise terminology  
  * Additional Worldview capabilities  
  * Deeper caveats and interpretation guidance

## **5\. Human-Controlled Decisions (Strict Boundary)**

The agent must **never** autonomously:

* Choose final datasets  
* Decide which proxy is “correct”  
* Interpret trends or causality  
* Assess policy, legal, or operational suitability

The agent may **suggest and explain**, but all final decisions remain with the user.

## **6\. Current Workflow (Without the Agent)**

| User Type | Typical Behavior | Resulting Friction |
| ----- | ----- | ----- |
| Novice | Searches plain language → sees imagery only.  | Misunderstanding or abandonment |
| Intermediate | Uses approximate keywords | Shallow or incorrect usage |
| Expert | Knows datasets → repeats manual steps | Time loss, fragmented context |

## **7\. Pain Points Addressed**

* Dependence on exact scientific keywords  
* Poor understanding of layers and proxies  
* Hidden or underused Worldview capabilities  
* Repetitive manual exploration  
* Mismatch between user expertise and interface complexity

## **8\. Success Criteria**

Stage-1 is successful when:

* Users find relevant Worldview datasets faster  
* Clarifying questions appear only when scientifically necessary  
* Dataset caveats are consistently surfaced  
* Visualizations and analyses match user expertise  
* Users demonstrate progression within the session  
* Scientific rigor is preserved without increasing cognitive load

