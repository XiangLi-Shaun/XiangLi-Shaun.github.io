---
layout: post
title: Gentle Problems
date: 2026-05-11
description: The observation almost every retelling of Gowers' post missed — that the lower bound of mathematical contribution has moved, and that a capability boundary runs through even the purest techne.
tags: ai-mathematics metis techne essay
categories: essays
giscus_comments: false
related_posts: false
---

> This blog post is machine-translated from the original Chinese version.
> Link: [https://mp.weixin.qq.com/s/srq9dWWd43k3Eoz_gZCDtQ](https://mp.weixin.qq.com/s/srq9dWWd43k3Eoz_gZCDtQ)

I have a few things to say about the Gowers post that has been filling everyone's screen lately — [A recent experience with ChatGPT 5.5 Pro](https://gowers.wordpress.com/2026/05/08/a-recent-experience-with-chatgpt-5-5-pro/).

If you assume I am about to talk about Metis AI, I am not: what AI can do at present is still some distance from that boundary.

What I want to discuss is a core observation in Gowers' original that almost every retelling has passed over. He points out that the problems ChatGPT 5.5 Pro solved come from a paper of Nathanson's, written for students just entering research — in his words, *relatively gentle open problems*. The traditional way to start a new PhD student is to hand them an open problem that looks as though it might not be too hard but in fact takes real work; we used to do the same thing, though lately in CS it has turned into writing surveys and building benchmarks. But if an LLM can solve problems of this kind, then at least in mathematics that traditional path no longer works.

Then he writes the sentence actually worth attending to: the **lower bound** of a mathematical contribution now becomes *proving something an LLM cannot prove*, rather than merely *proving something nobody has proved*. What is precise about this observation is that he is describing the lower bound moving up, not the ceiling being reached. What the AI achieved was to compress into an hour a piece of work that would previously have taken a new PhD student several weeks. Work of that kind is, in essence, a non-trivial improvement made inside an existing research framework. That is remarkable — but the distance between it and *AI possessing the capability of a real mathematician* may be larger than many people imagine. **What AI can do at present is recombine existing parts in non-obvious ways. It cannot yet invent new parts.**

Gowers runs a thought experiment in the post: suppose a mathematician solves an important problem through a long conversation with an LLM, where the mathematician provides the guidance but the LLM does all of the technical work and supplies the central idea. Would we regard this as a major achievement of the mathematician? His answer: he does not think we would. But he adds immediately that mathematicians who have genuinely solved hard problems themselves turn out to have the advantage when collaborating with an LLM — *just as very good coders are better at vibe coding than not such good coders.*

Put those two judgments side by side and they become very interesting. **Inside the boundary of AI capability, the value of a human doing the work independently is falling** — it is gradually becoming unnecessary. **Above that boundary, the deep intuition a human accumulates through long training becomes more important**, because it determines whether you can effectively steer the AI toward what it cannot do on its own. I expect that very soon AI will re-scan, re-verify and then optimise, at an unprecedented scale, every problem that can be precisely described — mathematics among them. We have students doing exactly this in neuroimaging right now.

Two more words for our [Metis AI](https://arxiv.org/abs/2605.14407) framework. In that frame, mathematical proof is almost pure *techne*: the rules are explicit, the results are verifiable, and nothing depends on interpersonal relationships or institutional context. If AI is going to demonstrate capability in any field at all, a highly formalised branch like combinatorics is the most natural place to begin. So the performance of ChatGPT 5.5 Pro here is not surprising. What it did was take one more step on precisely the class of task AI was always best at.

But Gowers' observation reveals a subtler structure: **even inside a purely *techne* domain, there is a clear capability boundary.** On one side of it are the *gentle problems* — technical improvements made within an existing framework, which is the ideal battleground for an LLM's pattern recognition and recombination. On the other side is the work that requires years of accumulated intuition, that requires building deep connections between apparently unrelated fields, that requires judging which problems are worth spending time and energy on at all. These capacities are closer in nature to **knowing what is important** than to *being able to prove what is correct*. Even in the most purely formal of domains, once the difficulty of a problem crosses a certain line, what you need is no longer only *techne* but something like a mathematician's *metis*. It is not quite practical, relational, situated knowledge in the ordinary sense — but it refuses formalisation just as firmly, and it can only come from long personal practice.

Finally, a simple fact check. In the articles going around, Gowers is cast as someone who *once publicly mocked AI* and has now *admitted defeat for the first time*. None of that is in the original. Where the retellings have him saying the result was fully at the level of a doctoral thesis, even fit to serve as its most brilliant chapter, what he actually wrote was that it would make a perfectly reasonable chapter in a PhD thesis — a competent chapter, not a brilliant one. Gowers' tone is measured from beginning to end. He states explicitly that the result builds heavily on Rajagopal's ideas, rather than being an original breakthrough arriving out of nowhere. This systematic stripping-away of qualifiers is by now a standard operation in AI coverage, and I will say no more about it.
