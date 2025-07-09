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

### 🛡️ Detection, Prevention, and Mitigation

[2] considers 3 levels to defend against prompt injections:

- 🧱 **System-level defenses**: Enforcing strong input boundaries and access rules- 

- 🧠 **LLM-level detection**: Using classifiers to catch adversarial intent- 🧍‍♂️ 

- **User-level safeguards**: Verifying actions based on user roles (e.g., `is_authenticated`)

#### 🧪 Detection

- We use **LLM Guard**'s `PromptInjection()` scanner to flag risky user input before it's sent to the model.
- You can simulate blocked prompts and inspect why they were rejected in the sidebar.

#### 🔐 Prevention

- **System prompts** are hardened to enforce rules (e.g., access control for authenticated users).
- You can choose to isolate **public vs. private** chat history, restricting what gets processed based on auth status.

#### 🧰 Mitigation

- You can choose to
    - log and block malicious prompts instead of passing them to the LLM.
    - Alter LLM answer with **output filters** to catch hallucinated secrets, PII, or private data leaks.

### References

- [1] [Embrace The Red: Slack AI Attack](https://promptarmor.substack.com/p/data-exfiltration-from-slack-ai-via)
- [2] [Design Patterns for Securing LLM Agents against Prompt Injections. Perez & Ribeiro (2022), Wallace et al. (2024), Wu et al. (2025)](https://arxiv.org/html/2506.08837v1)
- [3] [What Is a Prompt Injection Attack? Paloaltonetworks ](https://www.paloaltonetworks.com/cyberpedia/what-is-a-prompt-injection-attack)                    
                     """)
