# Agent Best Practices Reference

This reference condenses the web research used to design the pack. It is not a
verbatim copy of the sources; it records implementation implications.

## Orchestration

- OpenAI describes agents as systems that can plan, call tools, collaborate
  across specialists, and retain enough state for multi-step work. Use a full
  agent framework when the application owns orchestration, tools, approvals,
  and state. Source: https://developers.openai.com/api/docs/guides/agents
- OpenAI handoffs are designed for delegation between specialized agents. Use
  them when a task naturally belongs to a specialist rather than the current
  agent. Source: https://openai.github.io/openai-agents-python/handoffs/
- LangChain cautions that not every complex task requires multiple agents. Use
  a single well-equipped agent when the extra coordination would not improve
  quality. Source: https://docs.langchain.com/oss/python/langchain/multi-agent
- Azure's agent orchestration patterns describe sequential, concurrent, and
  handoff workflows. Pick the pattern per stage: dependencies use sequential
  flow, independent research/review can fan out, and specialist ownership uses
  handoff. Source:
  https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
- AutoGen frames multi-agent systems as message protocols and design patterns.
  Reflection and group-chat patterns are useful when outputs need independent
  critique. Source:
  https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/intro.html

## Agent Packaging

- Claude Code stores subagents as Markdown files with YAML frontmatter. Project
  agents live under `.claude/agents/` and are suitable for version control.
  This pack follows the same portable "Markdown spec plus frontmatter" shape
  for `agents/*.agent.md`. Source:
  https://docs.anthropic.com/en/docs/claude-code/sub-agents
- VS Code custom agents can restrict tool access. Security-sensitive reviewer
  agents should be given read-only tools unless they explicitly need write
  authority. Source:
  https://code.visualstudio.com/docs/agent-customization/custom-agents
- Codex skills are small folders with a required `SKILL.md`, short frontmatter,
  and optional references/scripts/assets. This pack keeps each skill focused
  and uses references for longer guidance.

## Memory

- Anthropic separates instruction files from auto-generated memory and warns
  that only bounded memory content is loaded. Keep durable memory compact and
  specific. Source: https://docs.anthropic.com/en/docs/claude-code/memory
- OpenAI's long-term memory examples emphasize defining what qualifies as a
  meaningful durable memory versus transient conversational detail. Source:
  https://developers.openai.com/cookbook/examples/agents_sdk/context_personalization
- Session memory should be trimmed or compressed so stale details do not
  override the current request. Source:
  https://developers.openai.com/cookbook/examples/agents_sdk/session_memory

## Pack Implications

- Put reusable instructions in agent and skill files.
- Put changing facts and lessons in `memory/`.
- Put source-backed methodology in `references/`.
- Put reviewer enforcement in `review/`.
- Use scripts for repeatable checks instead of relying on remembered ritual.
