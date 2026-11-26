---
id: 223921
title: "WebDeck - A hosting control panel built around isolation, now in free open beta for everyone!"
date: "2026-11-26T22:26:12+00:00"
author: "Unknown"
link: "https://lowendtalk.com/discussion/223921/webdeck-a-hosting-control-panel-built-around-isolation-now-in-free-open-beta-for-everyone"
---
# WebDeck - A hosting control panel built around isolation, now in free open beta for everyone!
**Link:** [Original Thread](https://lowendtalk.com/discussion/223921/webdeck-a-hosting-control-panel-built-around-isolation-now-in-free-open-beta-for-everyone)

Hi all,

For a little over a year I've been building **WebDeck**, a control panel for Linux servers. It already runs my own sites and a handful of customers' servers, and as of version 2.3.6 it's in **open beta: free for anyone, every feature unlocked, until 1 May 2027**.

I'd like people who run real servers to break it and tell me what's wrong.

**Site:** <https://www.webdeckpanel.co.uk>  
**Install guide:** <https://www.webdeckpanel.co.uk/downloads>  
**Documentation:** <https://www.webdeckpanel.co.uk/docs>  
**Release notes:** <https://www.webdeckpanel.co.uk/releases>  
**Features:** <https://www.webdeckpanel.co.uk/features>

---

What it is
----------

A full hosting panel for your own server: websites, PHP, email, DNS, databases, SSL, backups, resellers and a WHMCS module, with admin, reseller and customer logins. One licence per server, never per account.

It installs on a fresh **Debian, Ubuntu, AlmaLinux or Rocky Linux** server with **Apache or nginx**, and comes with a **cPanel importer** so you can move accounts straight across.

Why another panel?
------------------

Shared hosting panels tend to charge per account, then want a paid add-on before one customer is properly separated from the next. I wanted a panel where **isolation is the default and costs nothing extra**, and where the price doesn't climb every time you add a customer.

Isolation and security
----------------------

This is where most of the year went.

* **Every website runs as its own system user**, with its own PHP process, PHP version, extensions, `php.ini` and kernel-enforced CPU, memory and process limits.
* **Each site's PHP sits behind its own sealed socket.** One customer's `.htaccess`, symlinks or look-alike database names can't reach another customer's PHP, files or data.
* **The file manager, backups, restores and app installer** are built so a planted symlink can't trick the panel into writing outside the site.
* **Customer SQL imports run as a throwaway database user** scoped to that one database, not as an admin.
* **Signed updates**, with automatic rollback if an update doesn't come up healthy.
* **Self-healing:** the panel checks its own config, permissions and services and repairs drift in the files it manages.
* **Tested adversarially:** each release goes through an acceptance suite where isolated accounts try to read, change and delete each other's files, databases and sites.

I'm not claiming it's unbreakable. That's what the beta is for.

Features
--------

* **Websites:** one-step site creation, free Let's Encrypt SSL, redirects, directory privacy, hotlink protection, Git deploy
* **PHP:** per-site versions, extensions and limits
* **Email:** mailboxes with enforced quotas, DKIM/SPF/DMARC, a deliverability checker, webmail
* **DNS:** built-in authoritative DNS with a secondary nameserver cluster
* **Databases:** MariaDB, phpMyAdmin single sign-on, real per-database users, remote MySQL for named IPs
* **Backups:** scheduled full and incremental backups to SFTP/FTP/local, customers' own schedules, encrypted panel backups, restore to a chosen day
* **WordPress toolkit:** real staging with its own database, push to live, known-vulnerability checks
* **59 one-click apps**
* **cPanel importer**
* **Resellers and white-label:** packages, branding, bandwidth metering
* **WHMCS provisioning module**
* **WAF:** ModSecurity with the OWASP rule set
* **AI website builder and SEO tools:** optional, off by default, uses your own API key
* **Free panel hostname with a trusted certificate** from first boot

Installation
------------

On a **fresh** server, as root:

```
wget https://www.webdeckpanel.co.uk/downloads/webdeck-installer.tar.gz && tar xzf webdeck-installer.tar.gz && cd webdeck-installer-pkg && bash install.sh
```

**Minimum:** 1 vCPU, 1 GB RAM, 10 GB disk. **Recommended:** 2 vCPU, 4 GB RAM, 40 GB disk

Full guide: <https://www.webdeckpanel.co.uk/docs>

What you should know going in
-----------------------------

* **Ubuntu and Debian have had the most testing.** AlmaLinux and Rocky are supported but less proven, so reports from them are especially useful.
* **OpenLiteSpeed** is limited to a single hosting account for now, because per-site PHP separation isn't finished on it. Use Apache or nginx for multiple customers.
* Use a **fresh server** and **keep your own backups**. It's a beta.

The deal
--------

* **Free until 1 May 2027**, possibly longer. No card, no licence key to enter.
* When the beta ends, your server keeps full access for a further **60 days**.
* After that, beta servers get **30% off** Pro (normally £12 a month per server), or can drop to the free tier (2 hosting accounts, 4 websites).
* **Nothing ever gets switched off.** Whatever happens to the licence (or to me), your sites, mail and databases keep running.

About the AI
------------

WebDeck was built with the help of AI models. I'd rather say that up front than have someone assume the worst.

It isn't a weekend of prompts. It's over a year of work: I run it on production servers, read what gets written, and every release goes through the testing above plus outside review when it can. All I ask is that you install it and judge what's in front of you before writing it off as slop. If it is slop, please tell me where.

Bugs and flaws
--------------

If you find a bug, a security flaw or something that's just badly done, email **[[email protected]](/cdn-cgi/l/email-protection)**. For security issues, please email rather than post the details publicly. Blunt feedback is welcome in the thread too.

Thanks for giving it a look. Go break it!

Need somewhere to try it? VM6 does UK VPS from £1.75/mo: <https://www.vm6.co.uk>
