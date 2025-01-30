import random
# This is an synthetic email generator. This file used for generate varies of parameters for the email generation.


### **Key Parameters for Variation:**

# 1. **Email Thread Length** – Vary the number of exchanges (short, medium, long).
#    - **Short** (1-2 emails)
#    - **Medium** (3-5 emails)
#    - **Long** (6+ emails)
# 2. **Client Persona** – Define different types of clients, such as:
#    - **Risk-Averse Investor** (prefers stable stocks, bonds)
#    - **Aggressive Trader** (interested in high-risk, high-reward stocks)
#    - **Retiree Planning for Income** (focus on dividends, stability)
#    - **Tech Enthusiast** (invests in tech startups and crypto)
#    - **Corporate Executive** (interested in stock options and insider trading regulations)
# 3. **Broker's Style** – Vary how the broker communicates:
#    - **Formal and Professional**
#    - **Casual and Personable**
#    - **Sales-Oriented and Persuasive**
#    - **Highly Analytical and Data-Driven**
# 4. **Market Conditions** – Simulate different economic environments:
#    - **Bull Market** (high growth, optimism)
#    - **Bear Market** (decline, caution)
#    - **Volatile Market** (uncertainty, rapid price swings)
#    - **Stable Market** (low volatility, slow growth)
# 5. **Investment Topics** – Cover various investment concerns:
#    - **Stock Recommendations** (blue-chip vs. speculative stocks)
#    - **Portfolio Diversification**
#    - **Tax and Regulatory Concerns**
#    - **Market Timing vs. Long-Term Investing**
#    - **ESG Investing (Ethical & Sustainable Investing)**
# 6. **Client's Level of Experience** – Different levels of market knowledge:
#    - **Beginner (needs explanations)**
#    - **Intermediate (some knowledge, asks specific questions)**
#    - **Expert (wants deep analysis and trends)**
# 7. **Urgency** – Simulate different urgency levels in communication:
#    - **Routine Check-in**
#    - **Time-Sensitive Trade Advice**
#    - **Crisis Handling (market crash, bad investment, SEC issues)**
# 8. **Medium** – How the emails are structured:
#    - **Long, Detailed Responses**
#    - **Concise, Action-Oriented Replies**
#    - **Mixed (some long, some short)**

investmentExperience = ["**Beginner (needs explanations)**", "**Intermediate (some knowledge, asks specific questions)**", "**Expert (wants deep analysis and trends)**"]
emailLength = ["**Short** (1-2 emails)", "**Medium** (3-5 emails)", "**Long** (6+ emails)"]
clientPersona = ["**Risk-Averse Investor** (prefers stable stocks, bonds)", "**Aggressive Trader** (interested in high-risk, high-reward stocks)", "**Retiree Planning for Income** (focus on dividends, stability)", "**Tech Enthusiast** (invests in tech startups and crypto)", "**Corporate Executive** (interested in stock options and insider trading regulations)"]
brokerStyle = ["**Formal and Professional**", "**Casual and Personable**", "**Sales-Oriented and Persuasive**", "**Highly Analytical and Data-Driven**"]
marketConditions = ["**Bull Market** (high growth, optimism)", "**Bear Market** (decline, caution)", "**Volatile Market** (uncertainty, rapid price swings)", "**Stable Market** (low volatility, slow growth)"]
investmentTopics = ["**Stock Recommendations** (blue-chip vs. speculative stocks)", "**Portfolio Diversification**", "**Tax and Regulatory Concerns**", "**Market Timing vs. Long-Term Investing**", "**ESG Investing (Ethical & Sustainable Investing)"]
clientExperience = ["**Beginner (needs explanations)**", "**Intermediate (some knowledge, asks specific questions)**", "**Expert (wants deep analysis and trends)**"]
urgency = ["**Routine Check-in**", "**Time-Sensitive Trade Advice**", "**Crisis Handling (market crash, bad investment, SEC issues)**"]
structureOfConversation = ["**Long, Detailed Responses**", "**Concise, Action-Oriented Replies**", "**Mixed (some long, some short)**"]