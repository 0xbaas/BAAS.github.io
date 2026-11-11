---
layout: post
title: "Live walkthrough: Advanced Active Directory"
date: 2025-09-28
categories: [HTB Walkthroughs]
tags: [hackthebox, active-directory, windows, kerberos, gmsa, dpapi, rbcd]
description: "A live walkthrough of Vintage, a hard Windows Active Directory machine with NTLM fully disabled. I cover Kerberos authentication, legacy computer accounts, gMSAs, targeted Kerberoasting, DPAPI and delegation."
toc: true
permalink: /posts/htb-vintage/
image:
  path: /assets/img/posts/htb-vintage/banner.png
  alt: "Vintage: Advanced Active Directory live walkthrough"
---

Vintage is a hard Windows Active Directory machine on Hack The Box. It follows an assumed breach scenario, meaning you start with credentials for a regular domain user. From there, I look for misconfigured AD permissions and exposed credentials that I can use to move between accounts and escalate privileges.

**NTLM is fully disabled**, so you have to use Kerberos to authenticate to the domain.

## What the walkthrough covers

- **Kerberos authentication:** getting your tools working with Kerberos tickets.
- **BloodHound:** mapping out users, computers and groups to find permissions you can use to gain more access.
- **Pre-Windows 2000 computer accounts:** how old compatibility settings can leave computer accounts with predictable passwords.
- **Group Managed Service Accounts (gMSAs):** why an automatically managed password can still be exposed if the wrong accounts are allowed to retrieve it.
- **Targeted Kerberoasting:** using write access to an account to obtain a service ticket for offline password cracking.
- **DPAPI:** finding saved Windows credentials and understanding what you need to decrypt them.
- **Resource-Based Constrained Delegation (RBCD):** how services can act on behalf of other users, and how incorrect delegation permissions can be abused.

## Watch the live walkthrough

You can follow the full walkthrough in the video below.

{% include embed/youtube.html id='PeP24PorZ2Q' %}
