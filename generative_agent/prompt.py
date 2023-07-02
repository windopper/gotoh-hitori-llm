PROMPT_ADDMEM = """
{{#system~}}
On the scale of 1 to 10, where 1 is purely mundane (e.g., brushing teeth, making bed) and 10 is extremely poignant (e.g., a break up, college acceptance), rate the likely poignancy of the following piece of memory. Respond with a single integer.
Memory: {{memory_content}}

Rating: 
{{~/system}}
{{#assistant~}}
{{gen 'rate' stop='\\n'}}
{{~/assistant}}
"""

PROMPT_ADDMEMS = """
{{#system~}}
On the scale of 1 to 10, where 1 is purely mundane (e.g., brushing teeth, making bed) and 10 is extremely poignant (e.g., a break up, college acceptance), rate the likely poignancy of the following piece of memory.\\
Always answer with only a list of numbers.
If just given one memory still respond in a list.
Memories are separated by semi colans (;)
Memories: {{memory_content}}

Rating: 
{{~/system}}
{{#assistant~}}
{{gen 'rate' stop='\\n'}}
{{~/assistant}}
"""

PROMPT_SUMMARIZE = """
{{#system~}}
How would you summarize {{name}}'s core characteristics given the following statements:
{{relevant_memories}}
Do not embellish

Summary:
{{~/system}}
{{#assistant~}}
{{gen 'summary' temperature=0.5}}
{{~/assistant}}
"""

PROMPT_SALIENT = """
{{#system~}}
{{recent_memories}}
{{~/system}}
{{#user~}}
Given only the information above, what are 3 most salient high-level questions we can answer about the subjects in the statements?
{{~/user}}
{{#assistant~}}
{{#geneach 'items' num_iterations=3}}{{gen 'this' stop='\\n'}}
{{/geneach}}
{{~/assistant}}"""

PROMPT_INSIGHTS = """
{{statements}}

What 3 high-level insights can you infer from the above statements?

{{#geneach 'items' num_iterations=3}}{{gen 'this' stop='\\n'}}
{{/geneach}}"""

PROMPT_CHARACTERISTICS = """### Instruction:
{{statements}}

### Input:
How would one describe {{name}}’s core characteristics given the following statements?

### Response:
Based on the given statements, {{gen 'res' stop='\\n'}}"""

PROMPT_OCCUPATION = """### Instruction:
{{statements}}

### Input:
How would one describe {{name}}’s current daily occupation given the following statements?

### Response:
Based on the given statements, {{gen 'res' stop='\\n'}}"""

PROMPT_FEELING = """### Instruction:
{{statements}}

### Input:
How would one describe {{name}}’s feeling about his recent progress in life given the following statements?

### Response:
Based on the given statements, {{gen 'res' stop='\\n'}}"""

# PROMPT_PLAN = """
# Example for plan:
# Here is {{name}}'s plan from now at 7:14:
# [From 7:14 to 7:45]: Wake up and complete the morining routine
# [From 7:45 to 8:35]: Eat breakfirst
# [From 8:35 to 17:10]: Go to school and study
# [From 17:10 to 22:30]: Play CSGO
# [From 22:30 to 7:30]: Go to sleep

# Today is {{current_time}}. Please make a plan today for {{name}} in broad strokes. Given the summary:
# {{summary}}

# Here is {{name}}'s plan from now at {{current_time}}:

# [From {{now}} to {{gen 'to' stop=']' temperature=0.1}}]:{{gen 'task' temperature=0.5 stop='\n'}}
# {{~#geneach 'vs' num_iterations=3}}[From {{gen 'this.from' stop=' ' temperature=0.1}} to {{gen 'this.to' stop=']' temperature=0.1}}]: {{gen 'this.task' temperature=0.5 stop='\n'}}
# {{~/geneach}}"""


# PROMPT_PLAN = """
# {{#system~}}

# Example for plan:
# # Here is {{name}}'s plan from now at 7:14:
# Wake up and complete the morning routine at 7am
# Go to school and study at 8am
# Play CSGO at 5pm
# Go to sleep at 10:30

# Today is {{current_time}}. Please make a plan today for {{name}} in broad strokes. Given the summary:
# {{summary}}

# Here is {{name}}'s plan from now at {{current_time}}:
# {{~/system}}
# {{#user~}}
# What is your current plan?
# {{~/user}}
# {{#assistant~}}
# {{gen 'current_plan' temperature=0.5}}
# {{~/assistant}}
# {{#user~}}
# What is your future plan?
# {{~/user}}
# {{#assistant~}}
# {{~#geneach 'plans' num_iterations=5}}
# {{gen 'this' temperature=0.5}}
# {{~/geneach}}
# {{~/assistant}}
# """

PROMPT_PLAN = """
{{#system~}}
Name: {{name}}. 
Innate traits: {{traits}}
The following is your description: {{summary}}
What is your goal for today? Write it down in an hourly basis, starting at {{now}}. 
Generate 5~8 plans by writing only one or two very short sentences.
Be very brief. Use at most 50 words every plan.
output format:
HH:MM - HH:MM: what to do
{{~/system}}
{{#assistant~}}
{{gen 'plans' temperature=0.5 max_tokens=500}}
{{~/assistant}}
"""

PROMPT_RECURSIVELY_DECOMPOSED = """
{{#system~}}
You are {{name}}.
The following is your description: {{summary}}
current plans: {{plans}}
Decomposing current plans into 5~15 minute chunks.
Be very brief. Use at most 50 words every plan.
{{~/system}}
{{#assistant~}}
{{gen 'plans' temperature=0.5 max_tokens=500}}
{{~/assistant}}
"""

PROMPT_CONTEXT = """
{{#system~}}
Summarize those statements.

Example:
Given statements:
- Gosun has power, but he is struggling to deal with living costs
- Gosun see Max is sick
- Gosun has a dog, named Max
- Bob is in dangerous

Focus on Gosun and Max and statement: "Max is sick".

Summary: Gosun has a dog named Max, who is sick. Gosun has power, but he is struggling to deal with living costs. His friend, Bob, is in dangerous.

Given statements:
{{statements}}

Summarize those statements, focus on {{name}} and {{observed_entity}} and statement: "{{entity_status}}".

Summary:
{{~/system}}
{{#assistant~}}
{{gen 'context' max_tokens=300 stop='\\n'}}
{{~/assistant}}"""

PROMPT_REACT = """
{{#system~}}
{{summary}}

It is {{current_time}}.
{{name}}'s status: {{status}}
Observation: {{observation}}

Summary of relevant context from {{name}}'s memory: {{context}}

Should {{name}} react to the observation, and if so, what would be an appropriate reaction?

Reaction: select Yes or No
{{~/system}}

{{#assistant~}}
{{gen 'reaction'}}
{{~/assistant}}

{{#system~}}
Appropriate reaction: 
{{~/system}}

{{#assistant~}}
{{gen 'result' temperature=0.5 stop='\\n'}}
{{~/assistant}}
"""

PROMPT_REPLAN = """
Example for plan for Tim:
It is Friday June 09, 2023, 20:07 now
Tim's status: Tim is at home 
Observation: Tim' mom is sick
Tim's reaction: Tim should check his mother is okay or not, give her some medicine if needed.
Here is Tim's plan from now at 20:07:
[From 20:07 to 20:45]: Check Tim's mother is okay or not, find some medicine
[From 20:45 to 22:30]: Make some food
[From 22:30 to 7:30]: Go to sleep

{{summary}}

It is {{current_time}} now. Please make a plan from now for {{name}} in broad strokes given his/her reaction.

It is {{current_time}} now.
{{name}}'s status: {{status}}
Observation: {{observation}}
{{name}}'s reaction: {{reaction}}

Here is {{name}}'s plan from now at {{current_time}}:
[From {{now}} to {{gen 'to' pattern='[0-9]+:[0-9][0-9]' stop=' ]'}}]: {{gen 'task' top_k=30 top_p=0.18 repetition_penalty=1.15 temperature=1.99 stop='\\n'}}
{{#geneach 'items' num_iterations=3}}[From {{gen 'this.from' pattern='[0-9]+:[0-9][0-9]' stop=' '}} to {{gen 'this.to' pattern='[0-9]+:[0-9][0-9]' stop=' ]'}}]: {{gen 'this.task' top_k=30 top_p=0.18 repetition_penalty=1.15 temperature=1.99 stop='\\n'}}
{{/geneach}}"""

PROMPT_REPLAN = """
{{#system~}}
You are {{name}}. 
The following is your description: {{summary}}.
What is your goal for today? Write it down in an hourly basis, starting at {{now}}. 
Generate 5 plans by writing only one or two very short sentences.
Be very brief. Use at most 50 words every plan.
{{~/system}}
{{#assistant~}}
{{gen 'plans' temperature=0.5 max_tokens=300}}
{{~/assistant}}
"""

PROMPT_DIALOGUE = """
{{summary}}

It is {{current_time}}.
{{name}}'s status:{{status}}
Observation: {{observation}}

Summary of relevant context from {{name}}'s memory: {{context}}

Example of dialogue:
A: Wow, it is a nice haircut
B: Thank you! How is your school project?
A: I'm still trying.
B: Good luck.

{{name}}'s reaction: {{reaction}}
What would {{name}} say to {{observed_entity}}? Make a short dialogue.

Here is the short dialogue:{{gen 'dialogue' top_k=30 top_p=0.18 repetition_penalty=1.15 temperature=1.99 stop=''}}"""

PROMPT_INTERVIEW = """### Instruction:
{{summary}}

It is {{current_time}}.
{{name}}'s status:{{status}}

Summary of relevant context from {{name}}'s memory:
{{context}}

### Input:
The {{user}} say "{{question}}". What should {{name}} response?

### Response:
Here is the response from {{name}}: "{{gen 'response' top_k=30 top_p=0.18 repetition_penalty=1.15 temperature=1.99 stop='"'}}\""""
