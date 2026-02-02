---
id: 207939
title: "SYSADMIN DAY? AMD EPYC / RYZEN | Basically Dedicated in US & CA & EU | COLO | ANYCAST & MORE"
date: "2025-08-16T17:09:01+00:00"
author: "Unknown"
link: "https://lowendtalk.com/discussion/207939/sysadmin-day-amd-epyc-ryzen-basically-dedicated-in-us-ca-eu-colo-anycast-more"
---
# SYSADMIN DAY? AMD EPYC / RYZEN | Basically Dedicated in US & CA & EU | COLO | ANYCAST & MORE
**Link:** [Original Thread](https://lowendtalk.com/discussion/207939/sysadmin-day-amd-epyc-ryzen-basically-dedicated-in-us-ca-eu-colo-anycast-more)

![](https://terabit.io/logo.png)

We're back and we've got some exciting news to share with you all. In the background we've been working on improving our network significantly, and doing this required a **significant** amount of underlying changes including our engineers rewriting our entire software suite to provide what we've been after. (Our offer's below this update segment)

### Network Improvements

**Global Latency:** We've worked hard with our partners and upstreams to reduce our global latency while adding over 1Tbit/second of capacity worldwide.

**Anycast:** Before, we had a few prefixes stuck in a single region due to legacy network decisions -- no more. Everything is fully anycasted, globally.

**Mitigation:** After over 100 hours of engineering work, our mitigation engine has been re-written from the ground up. It's 30% lighter, and a performance gain of 400% from the original engine.

**Routing:** Our underlying routing mechanism has been redone. You'll now experience the best paths possible including when available riding the local IXs or our longhauls.

**New Longhauls:** We're adding a 100G wave from Kansas to Dallas. We're adding a 100G wave from Montreal to NY.

**Upstream Carriers (US/CA/EU):**

```
Arelion
Tata
Cogent
GTT
NTT
Sparkle
```

**US-specific PNI/upstreaming:**

```
Comcast
Verizion
```

**EU-specific PNI/upstreaming:**

```
Core Backbone
Liberty Global
```

### New Service Offering: Anycast VPS

Do you have a VPS or Basically Dedicated in all 3 of our core regions (Montreal, Kansas, Amsterdam)?

Starting today, you can request an **Anycast VPS IP** address (+$3/mo) and bind that to your VPS or Basically Dedicated server in each region. Anycast IPs are assigned from our Premium Network.

### Anycast BGP Sessions

Do you have your own IPs? You can bring them to us, with an Anycast BGP Session from your services *or* with our Remote Mitigation service (open a ticket for more details!).

### Network Insight Analytics

It's here. If you're on our Premium Network you can now see your analytics right in our portal. [You can check it out here](https://my.terabit.io/attacks.php). These graphs are updated every 30 seconds on our portal.

Not on Premium? [Check out the preview here.](https://imgur.com/a/QA6A2kn "Check out the preview here.")

### The Offers

**Direct IPs for testing:**

Kansas: 165.140.202.5  
Montreal: 207.174.40.97  
Amsterdam: 165.140.203.3  
Anycast: 23.137.56.3

Standard VPS Lineup
-------------------

**Our Basic VPS**  
\* 1 vCore  
\* 2 GB Memory  
\* 25 GB NVMe  
\* [Order Here](https://my.terabit.io/index.php?rp=/store/vps/basic "Order Here") @ $4.99/month

Basically Dedicated
-------------------

Looking for the best of a Cloud Server with higher resource limitations, tuned for performance and ready to handle larger challenges? Maybe you're just after some large memory packages? We've got you covered. Our Basically Dedicated Servers have you covered! By popular demand, we have added Xeon options to our Basically Dedicated lineup.

**Basically Dedicated 16GB**  
\* 8 vCores  
\* 16 GB Memory  
\* 200 GB SSD NVMe  
\* [Order Here](https://my.terabit.io/index.php?rp=/store/basically-dedicated/16-gb-memory-8-vcores-200-gb-nvme "Order Here") for $10/month  
\* Coupon Code: `M8R1CK2`

**Looking for Xeon?**

**Basically Dedicated XEON 32GB**  
\* 8 vCores  
\* 32 GB Memory  
\* 100 GB SSD NVMe  
\* [Order Here](https://my.terabit.io/index.php?rp=/store/basically-dedicated/32-gb-memory-8-vcores-100-gb-ssd-xeon-only "Order Here") for $10/month **NO COUPON REQUIRED**

**Orders may not be provisioned immediately and may need to be provisioned manually. If your order does not provision automatically after payment, please open a ticket. If your order is marked as fraud, please open a ticket.**

Looking for more than 16GB of memory and 200GB of SSD NVMe storage? [Check out some of our lineup here](https://terabit.io/basically-dedicated "Check out some of our lineup here"), we now support up to 96 cores and 786GB of DDR5 memory.

Colocation, anybody?
--------------------

We're doing a limited time colocation special in Kansas!

**Limited Colo - 1U**  
\* 1 Rack Unit  
\* 100TB on 10Gbps  
\* 50w Power  
\* $14/month  
\* [Order Here](https://my.terabit.io/index.php?rp=/store/colocation/kansas-city-1u-50w-mini) (**ONLY 5 AVAILABLE**)  
\* Coupon Code: `MINIMINIMINI`

How about game server hosting?
------------------------------

We've got you covered there too. We support numerous game servers, starting from as low as $3/month. Powered by our own version of Pterodactyl, integrated deeply with our in-house DDoS Mitigation engine.

[Check it out here](https://terabit.io/gameservers "Check it out here")

FAQ
---

> Why didn't my order deploy?

If your order didn't automatically deploy, it means it was flagged by the system for manual review. We'll review it and get back to you, often times we will push it through unless it's hitting multiple indicators (eg, fraud).

> What's this fraud thing?

If your order was blocked by our fraud checker, just open a ticket and inquire, our staff will look into it. We do not automatically review fraud-flagged orders, only when a ticket is created we will look into it.

> I paid, why does it say it's not paid?

If you paid via Credit Card/Debit Card, and your order is not marked as paid but you see a transaction, that is simply a hold done by the payment processor -- we did not collect your money. Your bank will automatically release that hold, we can't expedite it -- this usually takes anywhere between 3 to 31 business days depending on who you bank with, the average seems to be 3 business days however. You can contact your bank for specifics on when a hold will get released. You should try your payment again, or another payment method (eg, PayPal or Crypto).

> You have a new Support Portal?

Yes, we do! We made the decision to branch out of the default support engine provided by our billing software (WHMCS), which was fundamentally lacking key features we needed and migrated to using a third-party self-hosted solution. Tickets are being migrated over, and you'll see the new ticket creation interface next time you need our help! ![:smile:](https://lowendtalk.com/resources/emoji/smile.png ":smile:")

What's in the pipeline for Terabit?
-----------------------------------

* We're working on finalizing all network upgrades globally with a bit more helper software being rewritten.
* Our new portal is in **BETA**, we'll be sending out invites soon! ![:smirk:](https://lowendtalk.com/resources/emoji/smirk.png ":smirk:")
* We're still working on Dubai.
* We've got Miami in sights for some core services we're planning on launching.
* We upgraded our IX ports, and added more transit to our network.
* We're working on a lot of different projects right now, so be sure to keep an eye out for updates!

![](https://i.imgur.com/9mMw8jI.jpeg)  
![](https://i.imgur.com/KlCWtoN.jpeg)  
Long Live The Rats.
