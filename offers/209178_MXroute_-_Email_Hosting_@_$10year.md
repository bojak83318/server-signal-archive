---
id: 209178
title: "MXroute - Email Hosting @ $10/year"
date: "2025-11-04T13:48:47+00:00"
author: "Unknown"
link: "https://lowendtalk.com/discussion/209178/mxroute-email-hosting-10-year"
---
# MXroute - Email Hosting @ $10/year
**Link:** [Original Thread](https://lowendtalk.com/discussion/209178/mxroute-email-hosting-10-year)

Hey friends,

It has been a while since I posted an offer here, so I wanted to lay down a fairly traditional offer that hasn't seen light in a while. The old 10GB for $10/year promo. If you don't care what else I have to say, here is the link to that offer:

<https://accounts.mxroute.com/?cmd=cart&action=add&id=304> (No limit on domains or email accounts, 10GB total storage counted by usage not allocations)

That said, I'd like to tell you a bit about where we've been and where we're going, with a short introduction for anyone new.

MXroute is a "bring your own domain" email service with wild and crazy ideas about maximizing potential for inbox delivery of customer's outbound email, and rethinking most things from the ground up. While we were founded on a licensed software stack (WHMCS + cPanel, now HostBill + DirectAdmin), that was always just about getting the front-end done and not having to worry with it. As our customer base changed, users collectively wanted more than just quality outbound and passable inbound. However, all of the premade solutions that fit the bill for them don't fit the way we bill our customers. Trust me, when anyone hears that we bill users for disk space instead of $ per email account, they stop talking to us. We are a horrible fit for just up and licensing something like Stalwart that just gives most people what they want up front. Never gonna happen. To meet our customers needs, we have to do everything we can in-house. That means creative solutions to everything. It also means we get to reinvent the wheel in new and exciting ways.

What we offer:

* SMTP, IMAP, POP3
* Roundcube, Crossbox
* Custom (as in made by us) in-house spam filtering
* Front row tickets to crusades against spammers

Where we've been:

This year we released what we called "MXroute 3.2" and it's a dramatic change for how we deploy these creative solutions. Now we bundle them together, announce them, and deploy them. While the job demands tweaking in production, we're limiting that in favor of big releases. With that release we put out Domain Verification, solving a gaping security issue with most shared hosting systems since the beginning of time (and still present on what I would say is most shared hosting servers). We also released a conditional opt out for our new Expert Spam Filtering system, formerly referred to as "susranges." Here's how that went:

1. Domain verification was a slam dunk. Users were able to jump right into it and almost never had to talk to us about it.
2. Expert Spam Filtering has been a massive success, less than 100 users have disabled it. The goal here was to map out the parts of the internet we want to receive mail from, the parts that we don't, and then fill in the exceptions to both. Our whitelist request form was so busy for the exception requests that it did upset some users, with a wait time that pushed near to 1 month. While upsetting users is never the goal, the fact remains that this process upset less users than were upset about the spam that this system prevented, so we still call it a net positive (if someone is going to be upset, let's make it the smaller group). That whitelist is empty, new entries are being processed more rapidly (AI with human supervision), and that flood of whitelist requests is now down to a trickle. This means we did it, we pulled it off, susranges/Expert Spam Filtering is a massive success.

Where we're going:

To finally seal the deal on making sure that every customer has an inbound spam filtering solution that works for them, the MXroute 3.3 release will include a new spam filtering option that allows customers to completely bypass all of our filtering logic and replace it with something new: AI. Users will be able to bring their own API key for ChatGPT, Claude, or Gemini and have it filter their inbound mail. Users who prefer not to send their mail to a public facing LLM will be able to purchase a subscription to our own in-house LLM for filtering instead. This will be optional, and once complete our focus will continue to be on our own filtering systems.

The MXroute 3.3 release will also include a redesign of the spam filtering configuration page in DirectAdmin, bringing it in line with how we feel our customers will benefit best from the settings, and providing access to the new optional AI system.

There's so much more to come this year (Return of native iOS push? Maybe.), that's just the easy part. That's the part we've almost got in the bag (AI spam filtering is already tested and working, not yet available).

So if you just want email, we've got that. But if you also want a movement, a passionate direction, we've got that too. If you're not on board already, we'd love to have you.
