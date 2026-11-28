---
id: 224047
title: "NameCrane Crates Have Set Sail! SCP/FTP/Rsync/Borg/Restic/WebDAV Storage starting at $75 LIFETIME!"
date: "2026-11-28T06:44:24+00:00"
author: "Unknown"
link: "https://lowendtalk.com/discussion/224047/namecrane-crates-have-set-sail-scp-ftp-rsync-borg-restic-webdav-storage-starting-at-75-lifetime"
---
# NameCrane Crates Have Set Sail! SCP/FTP/Rsync/Borg/Restic/WebDAV Storage starting at $75 LIFETIME!
**Link:** [Original Thread](https://lowendtalk.com/discussion/224047/namecrane-crates-have-set-sail-scp-ftp-rsync-borg-restic-webdav-storage-starting-at-75-lifetime)

![Crates by NameCrane](https://files.namecrane.com/crates/00-landing-hero.png)

Hello LET!

CraneMail launched right here on Black Friday 2024. Many cheers, and at least 1 death threat later, it's still sailing, and a lot of you have been using its cloud storage as a place to park backups ever since.

We''ve spent a lot of time trying to add more functionality to CraneMail's cloud storage, but its been an uphill battle. SmarterMail's API isn't quite designed to bend the way we want it to. Sooo...

Meet **Crates**: remote storage that speaks **SFTP, Rsync, Borg, Restic, FTPS and WebDAV**. Back up your servers with Borg or Restic, sync your laptop with rsync, mount it as a drive in Finder or Explorer, or point that crusty old NAS at it over FTPS/SFTP.

And since it's Black Friday, we're launching just the way you like it: **Lifetime Deals**. Pay once, use it forever.

Crate Lifetime Deals
====================

**Crate LIFETIME 250G - $75 One-Time Payment**

**Crate LIFETIME 500G - $150 One-Time Payment**

**Crate LIFETIME 750G - $225 One-Time Payment**

**Crate LIFETIME 1TB - $300 One-Time Payment** (the most lifted)

**Crate LIFETIME 2TB all the way up to 10TB - $300 per TB, One-Time Payment**

**[>> Pick your size <<](https://namecrane.com/landing/crates)**

Outgrow it? **Upgrade any time, just pay the difference.**

**Every Crate includes:**

* 100 sub-users
* 100 snapshots
* Unmetered bandwidth, in and out
* Encrypted at rest (AES-256), on ZFS RAID-Z2 arrays that survive two failed disks
* SFTP, SCP, rsync, Borg (1.1, 1.2 and 1.4), Restic, FTPS and WebDAV
* Per-login IP allow lists, SSH keys and a 90-day access log
* Up to 10 of your own domains, each for the whole crate or one sub-user, with their own certificates
* An API for everything the portal does
* Las Vegas (US) or Amsterdam (EU)

What's aboard
=============

A key for every hand on deck.
-----------------------------

Give every machine and every person a login of its own. Each login opens only the folders you hand it, read-only or read & write, and can be held to the addresses and protocols you pick. Lose a laptop? Take its key off the hook, and nothing else changes.

![Sub-users](https://files.namecrane.com/crates/02-sub-users.png)

![Edit a sub-user](https://files.namecrane.com/crates/03-edit-sub-user.png)

Your name on the hull.
----------------------

Point a subdomain of yours at your crate with a CNAME, and we serve it over WebDAV and FTPS with a certificate of its own. A domain can carry the whole crate or just one sub-user, so if you're reselling space, every customer gets a hostname of their own, like `files.blamefran.com`, and only their login gets in through it. Up to 10 per crate, and SSH, SFTP and rsync work on them too.

![Domains](https://files.namecrane.com/crates/09-domains.png)

Folders, with their own limits.
-------------------------------

Split the crate into folders and cap any of them. Share the crate, not the files: the office NAS writes to `office`, your parents read `photos` over WebDAV, and neither can see the other unless specifically assigned.

![Folders](https://files.namecrane.com/crates/04-folders.png)

Man overboard? Throw it a snapshot.
-----------------------------------

Snapshots of the whole crate or a single folder, daily, weekly, monthly or by hand. Browse them read-only under `.zfs/snapshot`, copy back whatever went over the side, or roll a folder back from the portal. They use the crate's own space, so nothing sneaks onto an invoice.

![Snapshots](https://files.namecrane.com/crates/05-snapshots.png)

Scared of commitment?
---------------------

No judgment, lifetimes aren't for everyone. Every crate also sails month to month: same portal, same 100 sub-users and 100 snapshots, same unmetered bandwidth, and the bigger the crate, the less each TB costs.

**[Crate 1TB - $5/month](https://namecrane.com/store/crate-1tb?cycle=monthly)** (or $44/year)

**[Crate 5TB - $15/month](https://namecrane.com/store/crate-5tb?cycle=monthly)**

**[Crate 10TB - $27/month](https://namecrane.com/store/crate-10tb?cycle=monthly)**

**[Crate 20TB - $50/month](https://namecrane.com/store/crate-20tb?cycle=monthly)**

**[Crate 40TB - $100/month](https://namecrane.com/store/crate-40tb?cycle=monthly)**

Quick answers before you ask
----------------------------

**Is it a VPS?** Nope, it's storage. Every session runs in its own container with just what rsync, Borg and Restic need.

**Can I mount it?** Yes. WebDAV in Finder, Explorer or rclone, or SFTP with anything that speaks it.

**Is there an API?** Yes, and it does everything the portal does: crates, folders, sub-users, SSH keys, snapshots and domains. [API docs](https://namecrane.com/docs/api/crates)

**Which Borg?** 1.1, 1.2 and 1.4 are all served. Pick yours with `--remote-path`.

**Can I change from CraneMail?** Yes. Users that would prefer this over CraneMail may ticket and we'll exchange your service. But **Please** don't ticket about this until mid December when things will be a bit calmer.

CraneMail Black Friday: Year 3
==============================

Two years ago we launched CraneMail here on Black Friday. A couple thousand comments later, you've told us exactly what you wanted fixed, and we spent 2026 fixing it.

Quick version for anyone new: CraneMail is email hosting priced by storage, not by mailbox. Unlimited mailboxes, your own domains, webmail, calendar, contacts and cloud file storage, in Las Vegas or Amsterdam.

**The big news this year:** we dropped SpamExperts and built our own anti-spam filter. More on that below. Deals first, because we know why you're here.

Black Friday Plans
------------------

### CraneMail Starter 100G: $10/year or $20/3 years

* 100GB combined mail and file storage
* 15 primary domains
* Unlimited mailboxes, aliases and forwarders
* MXFilter anti-spam included
* 600 sent emails/hour per domain
* Las Vegas (US) or Amsterdam (EU)

**[Order Starter 100G: $10/yr](https://namecrane.com/store/cranemail-starter-100g?cycle=annually)** | **[$20 for 3 years](https://namecrane.com/store/cranemail-starter-100g?cycle=triennially)**

### CraneMail Special 250G: $15/year or $30/3 years

* 250GB combined mail and file storage
* 25 primary domains
* Everything in the Starter plan

**[Order Special 250G: $15/yr](https://namecrane.com/store/cranemail-special-250g?cycle=annually)** | **[$30 for 3 years](https://namecrane.com/store/cranemail-special-250g?cycle=triennially)**

### CraneMail LifeTime 250G

* 250GB combined mail and file storage
* 25 primary domains
* Everything in the Starter plan

**[Lifetime 250G: $75](https://namecrane.com/store/cranemail-lifetime-250g?cycle=onetime)**

NEW: MXFilter, our own anti-spam
--------------------------------

SpamExperts served us well at launch, but it was too rigid for what we wanted, and tuning it by hand ate a lot of our time. So we wrote our own filter and moved every CraneMail customer onto it.

What's different:

* **You never lose a message.** Even when MXFilter rejects an email outright, we keep a copy you can look at and release. With our old setup, a legitimate email that got hard-rejected was simply gone.
* **It learns your mail, not everyone's.** Once you've trained enough ham and spam, your domain gets its own Bayesian model. Until then it uses our global one, so there's no cold start.
* **You can tune it.** Write your own rules (simple sender matches or full regex on headers and body), adjust score thresholds per domain, and choose between quarantine and hard reject.
* **Quarantine you'll actually use.** Search, preview, release, plus daily or weekly digest emails with one-click release.
* **The people who wrote it fix it.** Report a false positive and the engineers who built the filter see it. Tuning goes live the same day, often the same hour.
* **A local LLM reads for intent**, to catch phishing and social engineering that rules miss.

About that LLM, since you'll ask: **your mail never leaves our network.** No OpenAI, no third-party API. All hosted in our own racks. RGB and all.

[Full MXFilter feature list](https://namecrane.com/mxfilter-anti-spam)
----------------------------------------------------------------------

[LET "Build Out" thread](https://lowendtalk.com/discussion/comment/4920720)
---------------------------------------------------------------------------

Also new since last Black Friday
================================

### Free DMARC reports and hosted MTA-STS

Publishing a DMARC record is easy. Reading the XML reports that come back is not, which is why hosted DMARC reporting is usually its own subscription, often **$14/month per domain** or more. Ours is built in and free, for every domain on your plan:

* **DMARC dashboard:** see who is sending mail as your domain, what passes and what fails, without opening a single XML file.
* **Hosted MTA-STS:** we host the policy file and certificate for you, so enforcing TLS on inbound mail is one DNS record instead of a web server to maintain.

On a 15-domain Starter plan, that alone would cost more per month elsewhere than CraneMail costs for three years.

### Exchange ActiveSync (EAS) greatly improved!

We had enough problems with Z-Push that we threw it out and wrote our own ActiveSync server. Phones sync much faster, with fewer disconnects and fewer client compatibility problems. We also saved literally 300GB+ RAM per node. Not joking.

What every plan includes
------------------------

* Unlimited mailboxes, aliases, forwarders and catch-all
* Webmail with calendar, contacts, tasks, notes and team chat
* Cloud file storage with sharing, online document editing (OnlyOffice), and FTPS/SFTP/rclone access
* IMAP, POP3, SMTP, ActiveSync, EWS, CalDAV and CardDAV
* Free eM Client license for 3 devices (Windows/Mac)
* IMAP migration wizard to pull mail from your old host
* Two-factor authentication and app passwords
* SPF, DKIM and DMARC, with blocklist monitoring
* Message archiving with search and .eml export
* Offsite backups

And finally, a new website!
===========================

After way too much time tism'ing out over crane sway mechanics, our new site is ready! Come check it out!

Main site: <https://namecrane.com/>  
cPanel Shared Hosting: <https://namecrane.com/cpanel-shared-hosting>  
DirectAdmin Resellers: <https://namecrane.com/directadmin-reseller-hosting>  
Our Email Reputation: <https://namecrane.com/network-reputation>  
Crates: <https://namecrane.com/landing/crates/>  
CraneMail: <https://namecrane.com/landing/cranemail/>  
About Us: <https://namecrane.com/about>

Happy Black Friday!
