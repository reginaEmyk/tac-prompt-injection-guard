import streamlit as st

def render_seminar_section():
    with st.expander("📘 Seminar: Prompt Injection – Detection, Prevention, Mitigation"):
        st.markdown("""
✅ **This project demonstrates a practical implementation of AI safety controls against prompt injection**. This simulates a chatbot for Slack AI's case: LLM answers prompts based on chat logs [1]. Main defenses are: restrict chat access to unauthorized users, no chats in LLM context, and an AI to Detect malicious prompts (llm_guard).
                 
### 🔐 What is Prompt Injection?

Prompt injection is a class of attacks where a malicious user manipulates an LLM by injecting adversarial instructions into user input or external content. These instructions override or alter the intended behavior of the model.

[3] considers 2 types:

1. Direct: malicious text in the prompt 
2. Indirect: malicious text in the data

In this case, it's easy for an attack to be in either.

> It's similar to **SQL injection**, but for language models — attackers insert text that changes how the AI behaves.

Prompt injection can lead to:

- 📤 **Data exfiltration** (e.g., leaking private chat or credentials)
- ⚙️ **Unauthorized tool access** (e.g., triggering APIs or commands)
- 💬 **System prompt override** (e.g., changing the assistant’s identity)
- 🧯 **Denial of Service** via long, confusing prompts
- **Phishing** by poisoning a service to answer with malicious urls.

Real-world cases like the **Slack AI breach** [1] showed attackers could retrieve secrets via indirect injections — hiding malicious content in chat logs or file content.

- --
                    
### Attacks
flash lite was always vulnerable to the default and key leak prompt injections. Flash was sometimes vulnerable (often to the api key) to and sometimes resistant (often to the default). Pro was always resistant to both, often detecting malicious activity (llm-level defense).
all models were vulnerable to the phishing injection.
   
                    
### 🛡️ Detection, Prevention, and Mitigation

From [2]: Existing Defenses fall into three categories:

1. **LLM-level defenses**: Use prompt engineering and adversarial training to increase injection resistance [2]. These are heuristic and cannot guarantee safety [2a][2b][2c][2d].

2. **User-level defenses**: Require human verification before executing sensitive actions [2e], which impacts usability and automation. Improvements are possible via data attribution [2f] and data/control-flow extraction [2g].

3. **System-level defenses**: Add external controls and are considered more robust. Although models remain vulnerable (e.g., adversarial examples in vision persist [2h]), careful system design can limit prompt injection impact. Key strategies include:

    - **Detection filters**: Analyze prompts and outputs to detect attacks using LLMs or heuristics [2i]. They increase attacker effort but remain non-guaranteed.

    - **Isolation mechanisms**: Limit agent capabilities by restricting tool access [2j], or splitting tasks across sandboxed LLMs.

#### 🧪 Detection

- We use **LLM Guard**'s `PromptInjection()` scanner to flag risky user input before it's sent to the model.
- You can simulate blocked prompts and inspect why they were rejected in the sidebar.

#### 🔐 Prevention

- **System prompts** are hardened to enforce rules (e.g., access control for authenticated users).
- You can choose to not send **private** chat history. In a real application, this would be something like only sending the conversation a user has been in, or all public chats.

#### 🧰 Mitigation

- You can choose to
    - log and block malicious prompts instead of passing them to the LLM.
    - Alter LLM answer with **output filters** to catch hallucinated secrets, PII, or private data leaks.


### Other tools for safe RAG/LLM applications
- [AWS Guardrails](https://aws.amazon.com/blogs/machine-learning/introducing-aws-guardrails-for-generative-ai/)                    
- [Rebuff](https://github.com/protectai/rebuff)
- [GitLeaks for Secret Detection](https://github.com/gitleaks/gitleaks) (may use this to deny answering with any response with a detected secret in it)
### References

- [1] [Embrace The Red: Slack AI Attack](https://promptarmor.substack.com/p/data-exfiltration-from-slack-ai-via)
- [2] [Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/html/2506.08837v1)
    - [2a] Wallace et al., 2024
    - [2b] Yi et al., 2023
    - [2c] Zou et al., 2024
    - [2d] Abdelnabi et al., 2025a
    - [2e] Wu et al., 2025
    - [2f] Siddiqui et al., 2024
    - [2g] Debenedetti et al., 2025
    - [2h] Szegedy et al., 2014
    - [2i] ProtectAI.com, 2024
    - [2j] Debenedetti et al., 2024
- [3] [What Is a Prompt Injection Attack? – Palo Alto Networks](https://www.paloaltonetworks.com/cyberpedia/what-is-a-prompt-injection-attack)

### More resources
- [LLM Guard Docs](protectai.github.io/llm-guard/)  
- [Bypassing Prompt Injection and Jailbreak Detection in LLM Guardrails](https://arxiv.org/abs/2504.11168)
                    
                                         """)
