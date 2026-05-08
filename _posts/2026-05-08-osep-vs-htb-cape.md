---
title: OSEP vs HTB CAPE
date: 2026-05-08 00:00:00 +0000
categories: [Blog]
---

Hi all,

In the last 6 months I completed both OSEP and HTB CAPE exams. Since then I keep getting the same question:

what's the difference between these two?

Since HTB CAPE is still relatively new, there aren't many people who currently hold both certifications, so I figured this was a good time to make a post about it.

This comparison is obviously based on my own experience and the order in which I took the certs.

---

# OSEP & HTB CAPE

Both courses have the same core idea: teaching you how to operate in more realistic enterprise Active Directory environments where AV and other security controls are actually enabled. Both certs force you to think critically about every step you take and understand why something works, or why it suddenly stops working.

OSEP mainly focuses on evasion and execution, whereas HTB CAPE goes much deeper into modern Active Directory tradecraft with only a bit of evasion toward the end.

---

# OSEP

OSEP does a very good job at introducing people to the mindset behind malware development and evasion instead of just throwing payloads at Defender and hoping something works. The course teaches you how Windows processes, memory, and execution actually work under the hood, which becomes extremely valuable once you start writing or modifying your own tooling.

Things like reflective loading, process injection, AV evasion, and application whitelisting bypasses give you a strong foundation for understanding how modern offensive tooling operates in real environments. Even though many of the techniques are considered older tradecraft nowadays, the real value is in learning the concepts and mindset behind them.

Once you understand _why_ those techniques work, that knowledge transfers very well into building more advanced custom tooling and understanding modern tradecraft later on.

What OSEP also does really well as well is teaching how Kerberos works from a Linux domain-joined machine perspective. Concepts like keytabs, credential caches, `KRB5CCNAME`, and Linux-based Kerberos authentication were barely covered in HTB CAPE, which honestly was nice to see because they are extremely relevant in modern enterprise environments.

The course also teaches a lot of fun and practical things like kiosk escaping, abusing OLE and CLR within MSSQL, and other techniques that become really handy when operating through a C2 during internal engagements.

About the exam itself, the experience was also very different. OSEP is a 48-hour exam, but honestly the exam felt pretty straightforward without weird rabbit holes. I completed it in roughly 12 hours.

That said, OSEP is still lacking quite a bit on the Active Directory side, especially if you've already done HTB CAPE beforehand. It barely goes much deeper than what you learned during OSCP when it comes to AD.

ADCS has become a very important attack surface during internal engagements, yet OSEP only really covers the more well-known paths like ESC1 and ESC8. Shadow Credentials are not covered at all, while I personally think PKINIT deserved much more attention since there's a lot of interesting abuse possible there as well, such as Pass-the-Certificate (PtC) or UnPAC-the-Hash.

Another thing worth mentioning is that relaying is not allowed during the OSEP exam. That honestly removes a lot of realistic attack paths and techniques that are heavily used during modern internal engagements, especially around ADCS and Kerberos abuse.

---

# HTB CAPE

CAPE feels very different from OSEP.

The real challenge in CAPE is understanding a large Active Directory environment and figuring out what actually matters.

You're constantly put into situations where nothing looks obviously vulnerable, but smaller weaknesses slowly start connecting once you properly understand how Active Directory behaves. A large part of the course revolves around recognizing relationships, permissions, delegation issues, certificate abuse paths, and Kerberos behavior instead of simply finding "the exploit".

That's honestly where most people struggle.

CAPE forces you to slow down and really think about attack paths. You constantly end up chaining multiple smaller issues together into something impactful instead of relying on a single obvious misconfiguration.

The course also goes very deep into areas that are extremely relevant in modern enterprise environments today, especially ADCS and Kerberos abuse. Things like Shadow Credentials, ESC paths (ESC1-11), relaying scenarios, S4U abuse, PKINIT, SPN-related attacks, delegation issues, and certificate-based authentication are everywhere throughout the course.

Compared to OSEP, the Active Directory side honestly feels much closer to what you encounter during mature internal engagements today.

Another thing that stands out is how much CAPE improves your enumeration mindset. You stop looking for quick wins and start learning how to properly map environments, understand trust relationships, and identify subtle privilege escalation paths that are easy to miss if your AD fundamentals are weak.

CAPE also punishes tool dependency much harder. If your methodology mostly revolves around running BloodHound and waiting for an obvious path to appear, you'll probably struggle. The course constantly forces you to understand _why_ something matters instead of blindly trusting tooling output.

The exam itself reflects that difference as well. HTB CAPE is a 10-day exam, and I genuinely needed almost all of those days. The environments are much larger and more complex, especially once you reach the later forests.

I was honestly lucky I had spent a lot of time on [VulnLab](https://vulnlab.com) beforehand, because that experience saved me a huge amount of time during the final part of the exam.

Another thing people underestimate is how important organization becomes during CAPE. Because the exam lasts so long, note-taking, documentation, and keeping track of attack paths becomes part of the challenge itself.

---

# What to pursue, HTB CAPE or OSEP

The answer mostly depends on where you currently are in your journey.

If you really want to understand the ins and outs of Kerberos and Active Directory, I'd suggest HTB CAPE. The course is massive and there's a lot to digest, so expect it to be a slow grind at times.

OSEP is more lightweight on the Active Directory side, but it expects you to already have some understanding of evasion, Windows internals, and C#.

I would still recommend going for OSEP first since it has more market value overall and fits much better as a next step after OSCP.

If you struggle with execution and evasion, go for OSEP.

If you struggle with understanding AD and finding attack paths, go for CAPE.

---

# Final thoughts

At the end of the day, both certifications are very strong and complement each other surprisingly well.

OSEP teaches you how to get execution in hardened environments.

CAPE teaches you how to actually think inside modern Active Directory environments.

And honestly, that's the biggest difference between them.

In OSEP, you usually get stuck because something doesn't execute.

In CAPE, you get stuck because you don't fully understand the environment yet.

If your goal is becoming better at real-world internal operations and red teaming, you'll probably end up needing both skillsets anyway.
