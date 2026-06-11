# **OUTPUT SECTION** 

# (NASA Worldview Chatbot – Phase 2.3)

## **1\. Consumer Model**

## **1.1 User Knowledge Levels (Dataset Understanding)**

The system must support three knowledge levels:

* **Beginner**  
* **Intermediate**  
* **Advanced**

### **1.2 User Identification Workflow**

* At the start of the interaction, the agent should ask the user to self-identify as:  
  * Beginner  
  * Intermediate  
  * Advanced  
* During clarifying questions, the agent may refine its understanding of user dataset literacy and adjust presentation accordingly.

## **1.3 Schema Strategy**

* Role-specific output schemas are required.  
* Core output structure remains consistent across all levels.  
* Intermediate and Advanced levels may expose additional technical options and metadata.  
* Structural model approach (fully distinct vs shared-base vs conditional variants):  
   → Implement a shared **base schema with conditional extensions**.

## 

## 

## 

## **1.4 Exposure Differences by Level**

| Feature | Beginner | Intermediate | Advanced |
| ----- | ----- | ----- | ----- |
| Narrative explanation | Simplified | Moderate detail | Technical detail |
| Citation visibility | Hidden by default | Optional | Optional |
| Provenance metadata | Hidden by default | Optional | Optional |
| Missing data indicators | Simplified | Explicit | Explicit |
| Processing level visibility | Optional | Visible | Visible |
| DOI display | Optional | Visible | Visible |

## **2\. Core Output Structure (Engineering Layer – Not Necessarily Fully Visible to User)**

* All outputs must satisfy:  
* Deterministic structure (identical input → identical structural output)  
* Required fields always present  
* Missing fields explicitly marked  
* Structural determinism mandatory  
* Narrative wording may vary if meaning remains uniquely interpretable  
* Missing data explanation required where possible  
* Missing data handling may vary by knowledge level

## **3\. Citation & Provenance (Optional Exposure Model)**

## **3.1 Default Behavior**

* Citation and provenance are not shown by default.  
* At the end of the response, the agent should offer options such as:  
  * “Would you like to see dataset details and citation information?”  
  * “Show technical metadata”  
  * “Download dataset link”

If user selects “Yes”, then full citation must be provided.

## **3.2 Required Citation Fields (When Enabled)**

Each data value must include:

* Source dataset name  
* Immutable identifier (DOI or persistent ID)  
* Satellite / instrument  
* Processing level  
* Data timestamp  
* Link to data catalog  
* Dataset version

## **4\. Provenance Format (Optional)**

* Human-readable provenance required only if the user requests it.  
* Machine-readable provenance is not exposed to users unless Advanced mode is active.  
* Internally, provenance must remain structurally available.

# **5\. Uncertainty Handling**

## **5.1 General Requirement**

Uncertainty disclosure must appear whenever applicable.

## **5.2 Dataset-Specific Uncertainty**

If citable uncertainty information exists:

* Include dataset-specific uncertainty with citation.

## **5.3 Generic Fallback (Mandatory if no dataset-specific info)**

Include: “All Earth observation data comes with uncertainty but I cannot find specific information about the uncertainty in this dataset.”

## **6\. Restrictions on Agent Claims**

### **Prohibited**

* Policy recommendations (strictly prohibited)

### **Permitted Only If Cited Per Statement**

* Causal claims  
* Predictive statements  
* Interpretations  
* Conclusive statements  
* Severity statements

No uncited interpretive or causal statements allowed.

## **7\. Missing Data Rules**

* Explicit values must be included for missing mandatory fields.  
* Missing fields must be explained where possible.  
* Scientists & internal users require explicit missing indicators.  
* Public/K–12 handling may be simplified (role-dependent).

Example missing indicator:  
`NOT_AVAILABLE_FROM_SOURCE`

# **8\. Disclaimer Requirement**

Every response must include a non-authoritative disclaimer.

The agent:

* Must not present itself as final scientific authority.

* Must not imply policy guidance.

## **9. Visualization Handling**

* Worldview visualizations must be provided as URLs.

Encoded image data is not required.

# **10\. Output Style**

**Hybrid format (Structured \+ Narrative)**

Each response must contain:

1. Structured backend schema (deterministic, complete)  
2. User-facing narrative explanation (adapted to knowledge level)  
3. Optional metadata expansion (user-triggered)

