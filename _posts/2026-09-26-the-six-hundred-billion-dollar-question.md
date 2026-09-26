---
layout: post
title: "The Six-Hundred-Billion-Dollar Question: The Answer Is Not in the Price"
date: 2026-09-26
description: The price of a token is collapsing and the value of AI is waiting. Both are true at once, and the reason is that metis accumulates on institutional time, not technical time.
tags: ai-economics ai-strategy metis essay
categories: essays
giscus_comments: false
related_posts: false
---

> This blog post is machine-translated from the original Chinese version.
> Link: [https://mp.weixin.qq.com/s/YcHE_AX1vSjriCkwluatqw](https://mp.weixin.qq.com/s/YcHE_AX1vSjriCkwluatqw)

In early 2023, processing a million tokens through the GPT-4 API cost thirty dollars. By the end of 2025, a model of equivalent capability had fallen below ten cents per million — a 99.7% collapse in three years. It is hard to find a product in the history of commerce whose unit price has gone to zero at this speed.

In 2024, David Cahn of Sequoia Capital asked a question: at the current rate of infrastructure investment, AI companies would need to generate roughly six hundred billion dollars in annual revenue to justify what was being spent. When he first ran the arithmetic in 2023, the gap was two hundred billion. A year later it had tripled. Now, in 2026, the gap has not closed; it is still widening. Allianz Research puts the divergence between AI capital expenditure and revenue growth at 46%, above the 32% that preceded the telecom bust of 2001.

The larger problem is that AI has stopped being *cool*, and stopped being *mysterious*. Benedict Evans, formerly of a16z, offers a sharper judgment: large models are becoming a commodity. Models are extremely hard to build, he grants — but so were flat panel displays, and nobody ever got rich merely by manufacturing displays. On his account the frontier labs have no moat and no defensibility beyond their ability to raise capital, have found product-market fit nowhere outside coding and marketing, and have no real product at all: only a text box and an API.

Read only these figures and these opinions and the conclusion looks settled: AI is a bubble, and the underlying AI layer will be the least valuable product in it.

**My view is that this conclusion is reached too quickly.** Too quickly because it conflates *price* with *value*, and conflates *technology* with *application*.

In fiscal 2026, NVIDIA's data center business reached one hundred ninety-four billion dollars in revenue. Meta and Oracle plan to double capital expenditure in 2026. Combined annual capex across Microsoft, Alphabet, AWS and Meta rose from roughly two hundred twenty billion in 2024 to three hundred sixty billion in 2025, to seven hundred billion in 2026 guidance. Meanwhile the optical communications market inside AI data centers is growing at 60% a year, and silicon photonics shipments are projected to grow more than fivefold by 2030. This is not speculative capital chasing a narrative. These are the largest technology companies on earth betting hard currency on an economic transition they believe is irreversible. They may well be wrong about the *rate* of spending — history shows that such errors are fatal — but they are unlikely to be wrong about its *direction*. There is an old line on Wall Street: don't fight the tape. We can question the valuations, question the pace, question near-term returns. But we should first ask ourselves: who is closer to the answer — me, or the several hundred financial engineers inside those firms?

The bubble thesis reaches most often for the fiber optic analogy of the 1990s: telecom companies laid far more network than demand required, investors lost money, many firms went bankrupt, and so AI infrastructure will travel the same road. But the analogy has a structural flaw. **Fiber is a physical asset laid once.** Once laid, it is laid; it becomes a sunk cost, anyone can use it, and whoever installed it retains no ongoing pricing power. WorldCom did not fail because fiber had no value; it failed because once fiber exists, its supplier loses the right to price it. Railroads follow the same logic: after the track is down, the money is made by those who run trains on it, not by those who laid it.

Compute is not fiber. **Compute is a continuously consumed resource, not infrastructure laid once.** Training and inference burn through chips every day — literally — and each generation carries a significant performance gap over the last, so that yesterday's silicon cannot simply substitute for tomorrow's demand. This means the commercial logic of a compute supplier resembles an energy company (continuous supply, continuous billing, technical iteration manufacturing replacement demand) far more than a railroad company (build it, then wait for others to come). NVIDIA's one hundred ninety-four billion dollars in fiscal 2026 data center revenue is not the echo of a sunk investment. It is a consumption market in continuous operation.

**So my first judgment is this:** compute, power, and optical interconnect — the substrate layers — retain enormous value potential, and unlike the infrastructure bubbles of history, the continuously consumed nature of compute gives its suppliers far stronger value capture. But the price collapse is real: not at the hardware layer, at the model layer. The price of a token is going to zero, and what that tells us is that the center of value capture is shifting from *who owns the model* to *who can build something real with it*. Evans says as much himself: the money will flow to the application layer — to companies that embed AI in specific workflows, own distribution, and solve actual problems.

So who is making money at the application layer?

The answer is: almost nobody.

A RAND Corporation report from late 2025 found that 80.3% of enterprise AI projects failed to deliver their promised business value. A third were abandoned before reaching production; nearly three in ten shipped but fell short of expectations; nearly a fifth run to this day and will never recover their cost. MIT's Project NANDA found in July 2025 that 95% of organizations deploying generative AI saw no measurable return whatsoever. McKinsey's 2025 global AI survey reports that 88% of organizations use AI in at least one function, while only 39% see any EBIT impact — and McKinsey notes, pointedly, that the organizations seeing real financial return had redesigned their end-to-end workflows *before* selecting a model technology.

a16z's early-2026 analysis places its bet on what it calls the *thick app*: not a thin wrapper over a large model, but multi-model orchestration, autonomy control, context engineering. The traditional SaaS logic no longer applies; AI has to eat labor.

But why have so many projects failed? Why did McKinsey find that the decisive factor was not technology but workflow redesign? **Because what the overwhelming majority of domain AI projects are doing is not solving a technical problem. They are attempting to force a form of knowledge that cannot be formalized into formal shape.**

In an earlier piece — *What AI Cannot Do Is Precisely What Lives on the Computer* — I proposed a frame: the Greeks distinguished *techne*, knowledge that can be encoded and taught, from *metis*, the practical, situated, relational wisdom that resists codification. **AI is, in essence, a *techne* machine.** It performs astonishingly on tasks high in *techne*, and it fails systematically on tasks high in *metis*.

That piece listed five structural features for judging the *metis* content of a task: irreversibility of consequence, irreducibility of relationship, open-ended normative structure, adversarial co-evolution, and non-delegable responsibility. Look again at the enterprise AI failures and the pattern maps almost one to one.

This is why domain AI cannot simply be dismissed as a *wrapper*. The real question is not whether the technology is strong enough, but whether *metis* can be put inside it. And the accumulation of *metis* does not track the speed of technical iteration — now measured in months, sometimes weeks — but the speed of institutional iteration, measured in years and sometimes decades. For a medical AI to deliver genuine clinical decision support, it needs more than a better model: it needs clinical trials, the evolution of regulatory frameworks, the rebuilding of trust between physician and patient, the maturation of liability. None of this has a fast-forward button.

**So my second judgment is this:** the current time window is not long enough for a domain AI that fundamentally transforms productivity to have appeared. Not because AI cannot do it, but because *metis* accumulates slowly, and we have only just begun.

Exactly one domain has already produced genuine productivity: writing code.

Cursor reached two billion dollars in annual revenue faster than any SaaS product before it — from one million to two billion in twenty-eight months. Claude Code went from zero to two and a half billion in annualized revenue in nine. JetBrains' early-2026 survey found 90% of developers using at least one AI tool at work, with individual productivity gains between 21% and 55%.

This is not an accident. Return to the *metis* frame: **of all professional work, writing code has the lowest *metis* content.** Information is highly concentrated — it is all on the screen. The rules are explicit: syntax and the compiler. Results are verifiable: the tests pass or they do not. It satisfies the conditions for a *techne* machine almost perfectly. Consequences are reversible before deployment; adversarial co-evolution is very weak, since code does not change its behavior because you wrote it; and the structure of responsibility is relatively clear — you wrote it, so you wrote it. Even here, in the lowest-*metis* domain we have, *metis* still generates problems, as I argued in *When Code Begins to Write Itself*.

The common view now is that AI has delivered real productivity only in programming, and from this people doubt whether AI is genuinely useful anywhere else. **But this reverses the causation.** AI succeeded in programming first *precisely because* programming is the professional domain lowest in *metis*. Other domains are not places AI can never reach; they are places where the *metis* requires far longer to accumulate, embed, and iterate. Put differently: AI's success in programming is its floor, not its ceiling.

An engine that reaches the level of general human intelligence will necessarily produce value across every human domain. This is not faith; it is structural inference. In radiology we have a notion called *Aunt Minnie*: if someone walks into the room and her face, her voice, her bearing and her habits are all your Aunt Minnie's, then she is your Aunt Minnie. AI is the same. If a system can understand language, handle knowledge, carry out reasoning, form plans, solve problems, create content and call tools — and if across a widening range of real work settings its performance approaches or exceeds that of an ordinary human — then in economic terms it already possesses the functional properties of a person, and it will almost certainly produce value across every human domain, inevitably replacing, amplifying, or restructuring a great deal of work formerly done by people.

But we must remember that **time is not a variable one skips lightly**. Medical AI waits for systems of clinical validation to catch up. Legal AI waits for frameworks of responsibility to mature. Educational AI waits for pedagogy to shift from *transmitting knowledge* to *constructing capability*. Every domain has its own rhythm of *metis* accumulation, and that rhythm is set not by the throughput of a GPU but by the speed at which human society evolves.

So the six-hundred-billion-dollar question is not *can AI companies earn six hundred billion*. It is *are we willing to wait for the metis to grow*. The price is collapsing — that is true. The value is waiting — that is also true. **Both are true at once, and they do not contradict each other.** The domain AI that genuinely changes how people work will have to wait the way fiber waited for YouTube: ten years, until healthcare and law and education and finance — those fields most deeply embedded in *metis* — one by one, slowly, make AI a part of themselves.
