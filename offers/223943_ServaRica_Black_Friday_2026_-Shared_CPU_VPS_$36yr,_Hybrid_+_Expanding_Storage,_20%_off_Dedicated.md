---
id: 223943
title: "ServaRica Black Friday 2026 -Shared CPU VPS $36/yr, Hybrid + Expanding Storage, 20% off Dedicated"
date: "2026-11-27T04:48:06+00:00"
author: "Unknown"
link: "https://lowendtalk.com/discussion/223943/servarica-black-friday-2026-shared-cpu-vps-36-yr-hybrid-expanding-storage-20-off-dedicated"
---
# ServaRica Black Friday 2026 -Shared CPU VPS $36/yr, Hybrid + Expanding Storage, 20% off Dedicated
**Link:** [Original Thread](https://lowendtalk.com/discussion/223943/servarica-black-friday-2026-shared-cpu-vps-36-yr-hybrid-expanding-storage-20-off-dedicated)

Hi everyone,

This year was very hard on all of us. Hardware prices went up significantly and we had to do a lot of optimizations just to keep going and we managed it.  
And despite the hardware prices we did one of the cheapest Black friday deals considering the hardware prices.  
This year we are launching three new product lines and taking 20% off every dedicated-core slice plans (v2 and V3 plans).

**Sale window:** November 26, 10 PM ET to December 26, 8 PM ET, or until a plan sells out.  
**Every Black Friday price is recurring:** you pay it on every renewal, monthly or yearly, not just on the first bill. Since we started in 2010, we have never raised the price on a single existing customer, and we don’t plan to start.

All plans with full details and benchmarks: **<https://servarica.com/black-friday/>**

What's new
----------

**1. Shared CPU VPS (V2 Shared Slim Slices)**  
We spent a lot of time making those as performant as possible and since the cpu is shared a lot of work done to make them fair while give the users the ability to use the servers as much as they can   
Based on AMD EPYC 7452 or 7532 with all-NVMe storage, from **$4/mo or $36/yr**. You get 25% of every vCPU guaranteed, all the time, and you can burst to 100% on CPU credits. Credits refill whenever you are below 25%. If your average CPU use over a day stays under 25%, you will essentially never be limited, and a server is never suspended for CPU use. Based on our analysis of how servers actually use their CPU, being limited should be very rare. Your cpu credit balance is shown in the client area.

**2. Pegasus Hybrid Storage**  
Terabytes of HDD plus a fast NVMe system disk in the same VPS(hybrid), from 1 TB to 16 TB. **Monthly transfer is doubled for Black Friday, and the doubled transfer is recurring too.**

**3. Shrimp Unlimited Expanding Storage**  
Storage that grows by itself every day. Pick how fast it grows, from 1 GB to 10 GB a day. NVMe system disk included, and transfer is doubled for Black Friday here too.

**4. 20% off every V2 and V3 dedicated-core slice with code `BF2026`**  
Recurring, on monthly and yearly billing. The order links below already add the code to your cart.

Pegasus and Shrimp replace our older storage lines: Chimera, Opossum, Polar Bear, Killer Whale, Penguin, Mammoth and Horse are no longer sold. Nothing changes for existing customers on those plans.

How the new storage plans work
------------------------------

Each Pegasus and Shrimp VPS has two disks: an **NVMe system disk** for the OS and databases, and an **HDD disk** for bulk data. Moving files to the HDD once they are quiet keeps heavy random I/O off the hard drives, so the HDD layer stays fast for everyone.

Both disks run on our **Ceph cluster with 4+2 erasure coding**: two disks or hosts can fail at the same time without losing data, the same protection level as RAIDZ2 but over full servers cluster.

Disk I/O on the shared CPU plans follows the same credit rules as CPU: 25% guaranteed, full speed on credits. Details: <https://servarica.com/fair-io-usage/>

**Plan names explanation**

* **S** = storage slice: 1 TB HDD + 20 GB NVMe (05S = half a slice: 500 GB HDD + 10 GB NVMe)
* **C** = compute slice: 2 shared vCPU + 2 GB RAM
* **G** = how many GB the storage grows every day (Shrimp only)

So **Pegasus 4S2C** is 4 TB HDD + 80 GB NVMe with 4 vCPU and 4 GB RAM, and **Shrimp 1S2C3G** starts at 1 TB HDD + 20 GB NVMe with 4 vCPU and 4 GB RAM, and grows by 3 GB a day. Need a different mix? Open a ticket and we will create a plan for your configuration.

Plans
-----

Prices are monthly or yearly, recurring. Code `BF2026` is already in the dedicated-core order links.

**Shared CPU VPS (V2 Shared Slim Slices)**  
AMD EPYC 7452 or 7532, all NVMe.

* **Shared Slim 2**: 2 vCPU · 2 GB RAM · 60 GB NVMe · 4 TB transfer · **$4/mo or $36/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=698)
* **Shared Slim 4**: 4 vCPU · 4 GB RAM · 120 GB NVMe · 8 TB transfer · **$6/mo or $66/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=699)
* **Shared Slim 8**: 8 vCPU · 8 GB RAM · 240 GB NVMe · 16 TB transfer · **$11.20/mo or $123.20/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=700)

**Pegasus Hybrid Storage**  
Transfer shown is already doubled for Black Friday.

* **Pegasus 1S1C**: 2 vCPU · 2 GB RAM · 20 GB NVMe + 1 TB HDD · 6 TB transfer · **$5/mo or $49/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=701)
* **Pegasus 2S1C**: 2 vCPU · 2 GB RAM · 40 GB NVMe + 2 TB HDD · 12 TB transfer · **$8.50/mo or $84/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=710)
* **Pegasus 3S2C**: 4 vCPU · 4 GB RAM · 60 GB NVMe + 3 TB HDD · 18 TB transfer · **$13/mo or $129/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=711)
* **Pegasus 4S2C**: 4 vCPU · 4 GB RAM · 80 GB NVMe + 4 TB HDD · 24 TB transfer · **$16/mo or $159/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=712)
* **Pegasus 6S3C**: 6 vCPU · 6 GB RAM · 120 GB NVMe + 6 TB HDD · 36 TB transfer · **$24/mo or $239/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=717)
* **Pegasus 8S3C**: 6 vCPU · 6 GB RAM · 160 GB NVMe + 8 TB HDD · 48 TB transfer · **$30/mo or $299/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=715)
* **Pegasus 16S4C**: 8 vCPU · 8 GB RAM · 320 GB NVMe + 16 TB HDD · 96 TB transfer · **$56/mo or $559/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=716)

**Shrimp Unlimited Expanding Storage**  
HDD shown is the starting size. Transfer shown is already doubled for Black Friday.

* **Shrimp 05S1C1G**: 2 vCPU · 2 GB RAM · 10 GB NVMe + 500 GB HDD, +1 GB/day · 6 TB transfer · **$6/mo or $59/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=702)
* **Shrimp 05S1C2G**: 2 vCPU · 2 GB RAM · 10 GB NVMe + 500 GB HDD, +2 GB/day · 12 TB transfer · **$9.50/mo or $94/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=703)
* **Shrimp 1S2C3G**: 4 vCPU · 4 GB RAM · 20 GB NVMe + 1 TB HDD, +3 GB/day · 18 TB transfer · **$15.50/mo or $154/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=707)
* **Shrimp 2S3C5G**: 6 vCPU · 6 GB RAM · 40 GB NVMe + 2 TB HDD, +5 GB/day · 24 TB transfer · **$26.50/mo or $264/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=708)
* **Shrimp 2S3C10G**: 6 vCPU · 6 GB RAM · 40 GB NVMe + 2 TB HDD, +10 GB/day · 36 TB transfer · **$42/mo or $419/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=709)

**V3 KVM Slim Slices (dedicated cores, code BF2026)**  
AMD EPYC 7663, NVMe. 1 dedicated core, 1 GB RAM and 30 GB NVMe per slice.

* **Slim 2**: 2 cores · 2 GB RAM · 60 GB NVMe · 6 TB transfer · **$5.60/mo or $61.60/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=647&promocode=BF2026)
* **Slim 4**: 4 cores · 4 GB RAM · 120 GB NVMe · 12 TB transfer · **$9.60/mo or $105.60/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=648&promocode=BF2026)
* **Slim 6**: 6 cores · 6 GB RAM · 180 GB NVMe · 18 TB transfer · **$13.60/mo or $149.60/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=649&promocode=BF2026)
* **Slim 8**: 8 cores · 8 GB RAM · 240 GB NVMe · 24 TB transfer · **$17.60/mo or $193.60/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=650&promocode=BF2026)
* **Slim 12**: 12 cores · 12 GB RAM · 360 GB NVMe · 36 TB transfer · **$25.60/mo or $281.60/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=651&promocode=BF2026)
* **Slim 16**: 16 cores · 16 GB RAM · 480 GB NVMe · 48 TB transfer · **$33.60/mo or $369.60/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=652&promocode=BF2026)
* **Slim 24**: 24 cores · 24 GB RAM · 720 GB NVMe · 72 TB transfer · **$49.60/mo or $545.60/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=653&promocode=BF2026)
* **Slim 32**: 32 cores · 32 GB RAM · 960 GB NVMe · 96 TB transfer · **$65.60/mo or $721.60/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=654&promocode=BF2026)

**V3 KVM FAT Slices (dedicated cores, code BF2026)**  
AMD EPYC 7663, NVMe. 1 dedicated core, 2 GB RAM and 30 GB NVMe per slice.

* **FAT 2**: 2 cores · 4 GB RAM · 60 GB NVMe · 6 TB transfer · **$7.20/mo or $79.20/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=665&promocode=BF2026)
* **FAT 4**: 4 cores · 8 GB RAM · 120 GB NVMe · 12 TB transfer · **$12.80/mo or $140.80/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=666&promocode=BF2026)
* **FAT 6**: 6 cores · 12 GB RAM · 180 GB NVMe · 18 TB transfer · **$18.40/mo or $202.40/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=667&promocode=BF2026)
* **FAT 8**: 8 cores · 16 GB RAM · 240 GB NVMe · 24 TB transfer · **$24/mo or $264/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=669&promocode=BF2026)
* **FAT 12**: 12 cores · 24 GB RAM · 360 GB NVMe · 36 TB transfer · **$35.20/mo or $387.20/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=668&promocode=BF2026)
* **FAT 16**: 16 cores · 32 GB RAM · 480 GB NVMe · 48 TB transfer · **$46.40/mo or $510.40/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=670&promocode=BF2026)
* **FAT 24**: 24 cores · 48 GB RAM · 720 GB NVMe · 72 TB transfer · **$68.80/mo or $756.80/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=671&promocode=BF2026)
* **FAT 32**: 32 cores · 64 GB RAM · 960 GB NVMe · 96 TB transfer · **$91.20/mo or $1,003.20/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=672&promocode=BF2026)

**V2 KVM Slim Slices (dedicated cores, code BF2026)**  
AMD EPYC 7532, NVMe. 1 dedicated core, 4 GB RAM and 125 GB NVMe per slice.

* **Slim 2**: 2 cores · 8 GB RAM · 250 GB NVMe · 8 TB transfer · **$12/mo or $132/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=611&promocode=BF2026)
* **Slim 4**: 4 cores · 16 GB RAM · 500 GB NVMe · 16 TB transfer · **$22.40/mo or $246.40/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=612&promocode=BF2026)
* **Slim 6**: 6 cores · 24 GB RAM · 750 GB NVMe · 24 TB transfer · **$32.80/mo or $360.80/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=613&promocode=BF2026)
* **Slim 8**: 8 cores · 32 GB RAM · 1 TB NVMe · 32 TB transfer · **$43.20/mo or $475.20/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=614&promocode=BF2026)
* **Slim 16**: 16 cores · 64 GB RAM · 2 TB NVMe · 64 TB transfer · **$84.80/mo or $932.80/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=615&promocode=BF2026)

**V2 KVM FAT Slices (dedicated cores, code BF2026)**  
AMD EPYC 7532, NVMe. 1 dedicated core, 4 GB RAM and 250 GB NVMe per slice.

* **FAT 2**: 2 cores · 8 GB RAM · 500 GB NVMe · 8 TB transfer · **$14.40/mo or $158.40/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=621&promocode=BF2026)
* **FAT 4**: 4 cores · 16 GB RAM · 1 TB NVMe · 16 TB transfer · **$27.20/mo or $299.20/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=622&promocode=BF2026)
* **FAT 6**: 6 cores · 24 GB RAM · 1.5 TB NVMe · 24 TB transfer · **$40/mo or $440/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=623&promocode=BF2026)
* **FAT 8**: 8 cores · 32 GB RAM · 2 TB NVMe · 32 TB transfer · **$52.80/mo or $580.80/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=624&promocode=BF2026)
* **FAT 16**: 16 cores · 64 GB RAM · 4 TB NVMe · 64 TB transfer · **$104/mo or $1,144/yr** · [Order](https://clients.servarica.com/cart.php?a=add&pid=625&promocode=BF2026)

**On every plan**

* Windows or Linux
* Two bandwidth options, picked at checkout: unlimited transfer on a 250 Mbps port that grows 1 Mbps a day up to 1 Gbps, or a 10 Gbps port with the monthly transfer listed (then about 10 Mbps)
* 7-day no-questions refund on your first order with us
* YABS results on every plan page, all linked from <https://servarica.com/black-friday/>

**About ServaRica**  
Montreal, Canada, since 2010. Our own hardware and our own network (AS26832), no overselling.  
Looking Glass: <https://ping.servarica.com> · Speed test: <https://speedtest.servarica.net>  
Payment: PayPal, Alipay, credit cards, crypto · TOS: <https://servarica.com/terms-of-service/>

Questions about any plan? Ask here and we will answer.
