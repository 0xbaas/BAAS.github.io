---
title: "OSEP vs HTB CAPE: My honest take after passing both"
date: 2026-05-08 00:00:00 +0200
categories: [Certifications]
tags: [osep, htb-cape, active-directory, red-teaming, kerberos, offsec]
description: "My honest comparison of OSEP and HTB CAPE after passing both, covering the pros and cons of each certification and which one you should choose depending on your goals."
image:
  path: /assets/img/posts/osep-vs-htb-cape/cape_vs_osep.png
  alt: OSEP and HTB CAPE comparison blog
---

<div class="post-lead" markdown="1">

Over the past year I earned two certifications that get compared a lot: OffSec's **OSEP** and Hack The Box's **HTB CAPE**. I understand why people put them in the same conversation. They are both offensive certifications, both sit above OSCP-level material, and both involve internal networks.

</div>

<figure class="post-figure wide-figure transparent-figure">
  <img src="/assets/img/posts/osep-vs-htb-cape/osep-cape-certificates-transparent.png" alt="OSEP and HTB CAPE certificates side by side">
</figure>

## My background before both exams

Before OSEP and CAPE, I had already completed **OSCP, CRTO, CRTP and CARTE**. I also had a background in programming.

That meant I was not starting from zero. There was already a decent base in Active Directory, Kerberos, red team methodology, internal network assessments and writing my own Python tooling. I also work as an ethical hacker, so I had done real penetration testing before taking both exams.

<figure class="post-figure medium-figure">
  <img src="/assets/img/posts/osep-vs-htb-cape/osep-vs-cape.png" alt="OSEP vs HTB CAPE personal comparison visual">
</figure>

## What OSEP is good for

OSEP is at its best when you treat it as an introduction to offensive tooling, AV evasion and Windows internals, not as a advanced Active Directory course.

The course gives you hands-on practice with **AV evasion concepts, process injection, reflective loading, Windows internals and custom C# tooling**. The malware-development style content in OSEP is mostly written in C#. That is not the most common language for serious malware development, but it does make the concepts approachable for people coming from OSCP or general penetration testing. As an introduction, it works pretty well.

That is where OSEP still has value. You get exposure to the basics of the PE structure, reflective DLL injection and how payloads are loaded into memory. Reflective DLL injection is an old technique, but the concept is still relevant because Metasploit and other offensive frameworks still rely on similar ideas.

AMSI is another good example. A lot of testers just throw an AMSI bypass into their payload and move on. OSEP pushes you to ask better questions: what is AMSI actually doing, where does it sit in the execution flow, and what are you actually patching?

The strongest part of OSEP is that it forces you to stop being a copy-paste RTO. Payload gets caught? You fix it. Tool breaks? You modify it. You learn to troubleshoot your own attacks instead of relying on pre-built binaries / BOFs that magically work in a lab.

<div class="cert-card-list" markdown="1">

- **AV evasion concepts** — understanding why detection triggers and how to work around it.
- **PE structure and reflective loading** — core basics behind how payloads are loaded into memory.
- **AMSI internals** — understanding what is being inspected and what a bypass is actually changing.
- **Windows internals** — practical knowledge that becomes useful once you start modifying tools.
- **Custom C# tooling** — building and adapting your own code instead of only running public tools.
- **Linux domain-joined hosts** — keytabs, ticket caches and Kerberos from a Linux perspective.

</div>

I also liked the Linux domain-joined host content from OSEP. Working with Kerberos from Linux, dealing with credential caches and interacting with a domain from a non-Windows perspective is also useful. CAPE does not cover that angle in the same way.

## Where OSEP falls short

As an Active Directory course, OSEP feels outdated and should be updated.

The AD content gives you some domain attacks, Kerberos, lateral movement and forest material, but it does not feel like a current advanced AD exploitation course. Compared to CAPE, the attack paths felt more predictable, the AD difficulty felt much lower, and the material did not push me into the same level of enumeration, chaining and reasoning.

OSEP still teaches useful offensive tradecraft, but as an Active Directory course, it leaves too many modern and commonly abused techniques out of scope.

Here are a couple of examples that should be covered in any serious modern AD course which isn't the case for OSEP:

<div class="missing-list" markdown="1">

- No serious **AD CS** coverage beyond the most familiar paths.
- No real focus on **Shadow Credentials** or modern certificate-backed abuse, even though these are good options when OPSEC matters.
- No real coverage of **PKINIT**-related techniques such as Pass-the-Certificate and UnPAC-style abuse.
- No meaningful **ACL/DACL** chaining beyond the basic ones.
- No **NTLM relay** coverage as a core attack path.
- No coverage of enterprise technologies such as **SCCM** and **WSUS**.

</div>

## What makes CAPE a great course

<figure class="post-figure wide-figure shadow-figure">
  <img src="/assets/img/posts/osep-vs-htb-cape/CAPE_description.jpg" alt="Contents of HTB CAPE">
</figure>

CAPE feels like it was built by people who actually wanted to teach hackers advanced Active Directory.

It covers a lot of the areas I expect from a modern AD-focused certification: deep manual enumeration with LDAP, Kerberos abuse, NTLM relaying, AD CS attack paths, delegation, different types of trusts, a lot of ACL abuse, the power of machine accounts, certificate templates, SQL, Exchange, SCCM, WSUS and much more.

It teaches you how different parts of Active Directory connect to each other, and how small misconfigurations can become a real attack path when you understand the environment properly.

It is not just basic Kerberoasting, password spraying across multiple machines, or blindly following a BloodHound graph. CAPE expects you to understand why the path exists and how the pieces fit together.

That said, some parts of the course could use an update. A full module is still dedicated to CrackMapExec, while NetExec has been around for a while now and is much more relevant for current AD work. With all the automated modules NetExec has today, that is exactly the kind of tooling an AD pentester should be learning in the course.

## Why CAPE feels harder

The hardest thing of CAPE is doing proper enumeration.

Mapping the environment properly matters. You have to understand what users can do, which machines are interesting, which services matter, where trust relationships exist, which permissions are dangerous and which small findings can be chained together.

<div class="clean-takeaway" markdown="1">

CAPE punishes lazy methodology.

</div>

If your whole strategy is "run BloodHound and wait for a path", you will definitely struggle. Following BloodHound blindly actually made me waste time during my exam. There will be a lot of moments where you know what you need to do, but still have to figure out how to exploit it properly.

Kerberos is the perfect example. CAPE pushes you to understand Kerberos at the protocol level. What does a ticket actually represent? Which service is it meant for? What does the SPN tell you, and what happens when that SPN is missing or pointing somewhere unexpected? Are you dealing with a ghost SPN, an SPN-jacking opportunity or an SPN-less situation? Are you looking at the normal AS/TGS flow, U2U, S4U2Self or S4U2Proxy? And why does all of this matter for delegation, ticket abuse and the attack path in front of you?

The same goes for NTLM. CAPE makes it painfully clear why NTLM keeps causing problems in enterprise networks. Poisoning, relaying, coercion, weak signing configurations, Pass-the-Hash and exposed services start connecting into one bigger picture.

So again, it is mostly about understanding the environment well enough to find the right attack path, validate it manually and chain it properly.

<div class="image-grid two" markdown="1">

<figure class="post-figure">
  <img src="/assets/img/posts/osep-vs-htb-cape/cape-path-start.jpg" alt="Starting the HTB Active Directory Penetration Tester path">
  <figcaption>25% through the course in January 2025</figcaption>
</figure>

<figure class="post-figure">
  <img src="/assets/img/posts/osep-vs-htb-cape/cape-social-announcement.jpg" alt="Social post about starting the HTB CAPE path">
  <figcaption>I finished all 253 sections in October 2025 before taking the CAPE exam.</figcaption>
</figure>

</div>

## Exam comparison

<figure class="post-figure">
  <img src="/assets/img/posts/osep-vs-htb-cape/exam-comparisons.png" alt="OSEP vs CAPE exam">
</figure>

OSEP was honestly not as hard as I expected. The exam was really fun, but the big environment felt manageable and somewhat straightforward.

OSEP is a 48-hour hands-on exam. You compromise machines, pivot, deal with AV and write a report. You will need at least 10 points or get the `secret.txt`. Without relying on a C2, I completed it in around nine hours.

<figure class="post-figure">
  <img src="/assets/img/posts/osep-vs-htb-cape/osep_result.jpg" alt="OSEP exam results">
</figure>

CAPE felt larger, more modern and more demanding. The exam forced you to enumerate properly, take solid notes and chain multiple attacks across the environment. I probably would not have passed without doing a lot of preparation on VulnLab first, especially because one of the forests was well configured and therefore much harder to attack. VulnLab’s AD Chains helped me a lot during my prep. You will need more than the course to pass in my opinion.

<figure class="post-figure wide-figure">
  <img src="/assets/img/posts/osep-vs-htb-cape/htb_profile.png" alt="HTB profile showing CAPE exam passed">
</figure>

CAPE is a 10-day hands-on exam across multiple networks. You need to collect enough points and submit a proper commercial-style report. You will also need 90/100 points which is very strict in my opinion.

<figure class="post-figure">
  <img src="/assets/img/posts/osep-vs-htb-cape/cape-exam-lab.jpg" alt="HTB CAPE exam lab points progress">
    <figcaption>I had two and a half days left to write my report, which ended up being 130 pages long.</figcaption>
</figure>

<figure class="post-figure">
  <img src="/assets/img/posts/osep-vs-htb-cape/cape-exam-feedback.jpg" alt="HTB CAPE examiner feedback">
  <figcaption>Feedback from mrb3n himself.</figcaption>
</figure>

<figure class="post-figure">
  <img src="/assets/img/posts/osep-vs-htb-cape/cape-badge-completed.jpg" alt="HTB CAPE badge completed">
  <figcaption>86th in the world :)</figcaption>
</figure>

## Which one should you choose first?

If you care about OffSec recognition and want a logical follow-up after OSCP, OSEP is still a solid choice. It is well known, looks good on a CV and teaches useful evasion skills, as mentioned earlier. It can also open doors if your goal is to move toward red teaming.

The reality is that most HR people, and even many technical interviewers, will recognize OSEP long before they understand what 'HTB CAPE' even is.

HTB CAPE, on the other hand, will make you a much better hacker and much stronger on the AD side. There is a lot to research, and the course throws many new concepts at you. If you take the time to properly understand them, CAPE will seriously level up the way you approach Active Directory environments.

But for now, most people have no idea what HTB CAPE is, let alone how difficult or valuable it actually is.

## Prep resources that helped me

<div class="decision-box" markdown="1">

- **For CAPE:** VulnLab AD Chains and Mini Pro Labs on HTB.
- **For OSEP:** The Pro Lab Zephyr, completing it both with and without a C2.
- **For OSEP specifically:** get very comfortable with PowerShell ;)

</div>

## Final note

OSEP is a good certification, but not for the reason a lot of people think. It is not a modern Active Directory certification. It is more about evasion, Windows internals, offensive tooling and the basics behind payload development, with some Active Directory in it.

And that is fine, as long as you know what you are getting into.

That is why comparing OSEP and CAPE too directly does not really make sense. OSEP gives you a useful foundation in offensive tooling and evasion. CAPE is the one that forces you to become stronger at modern Active Directory.

If you are working on one of these certifications soon: good luck, take proper notes and enjoy the journey!
