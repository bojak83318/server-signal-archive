---
id: 204849
title: "SCALEBLADE | 50% off NEW 9950X Ryzen VPS | London, United Kingdom"
date: "2026-01-26T15:55:11+00:00"
author: "Unknown"
link: "https://lowendtalk.com/discussion/204849/scaleblade-50-off-new-9950x-ryzen-vps-london-united-kingdom"
---
# SCALEBLADE | 50% off NEW 9950X Ryzen VPS | London, United Kingdom
**Link:** [Original Thread](https://lowendtalk.com/discussion/204849/scaleblade-50-off-new-9950x-ryzen-vps-london-united-kingdom)

Hi LET!

Last week we soft-launched our new Liquid Cooled 9950X VPS lineup. I'm here on LET with 50% off monthly orders and 40% off hourly with some added LET exclusive upgrades!

See all plans here: <https://scaleblade.com/products/vps>

Use discount code `LOWENDAPRIL25` for 50% off monthly vps and 40% off hourly vps.

**Featured 9950X Plans:**
-------------------------

**[NEW] KVM-R9-1GB** - £6 £3/month  
1 9950X core, 1GB RAM, 20GB NVMe, 2TB bandwidth on 10Gbps port.

**[NEW] KVM-R9-2GB** - £12 £6/month  
1 9950X core, 2GB RAM, 40GB NVMe, 4TB bandwidth on 10Gbps port.

**KVM-R5-2GB** - £8 £4/month  
1 5950X core, 2GB RAM, 30GB NVMe, 4TB bandwidth on 10Gbps port.

**KVM-R5-4GB** - £16 £8/month  
2 5950X core, 4GB RAM, 60GB NVMe, 8TB bandwidth on 10Gbps port.

DEPLOY: <https://my.scaleblade.com>  
REMEMBER TO USE THE CODE `LOWENDAPRIL25` FOR DISCOUNT AND UPGRADES.  
Looking glass: <https://scaleblade.com/locations/london>

More LowEndUpgrades? Of course..
--------------------------------

With any VM purchase using the discount code you can claim one of the two upgrades on your vm:

* 1 additional v-core (give your vm that extra kick it needs at no added cost)
* double bandwidth (2x bandwidth multiplier, permanently no questions asked)

How do you redeem this? Simply make your vm purchase and reply to this thread with your upgrade request and [your service id](https://i.imgur.com/xyYNvgx.png "your service id").

Features and Roadmap
--------------------

All vms come with the following:

* Free BGP IPv4/6 Sessions through our panel, no setup fee just confirm your ASN and go!
* Free BYOIP (without an ASN), we can announce ips for you and route them without you needing an ASN.
* Routed IPv6 /64 (b00b subnet cuz lol) with each VM
* 10GbE Uplink port (new accounts may need to open a support ticket to have the new-account limit removed if regular LET).
* Even cheaper monthly pricing for IPv6 only VMs.
* Service data residency, keep your data in one place to comply with local data protection laws for your business.
* High capacity T1 access + direct LINX peering.

In the next few weeks we are working on off-site backup and restore functionality for data-redundancy sensitive projects.

YABS (KVM-R9-3G, no upgrades)
-----------------------------

```
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #
#              Yet-Another-Bench-Script              #
#                     v2025-04-20                    #
# https://github.com/masonr/yet-another-bench-script #
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #

Tue Apr 22 08:51:34 UTC 2025

Basic System Information:
---------------------------------
Uptime     : 0 days, 0 hours, 2 minutes
Processor  : AMD Ryzen 9 9950X 16-Core Processor
CPU cores  : 1 @ 4291.916 MHz
AES-NI     : ✔ Enabled
VM-x/AMD-V : ✔ Enabled
RAM        : 2.9 GiB
Swap       : 0.0 KiB
Disk       : 59.0 GiB
Distro     : Debian GNU/Linux 12 (bookworm)
Kernel     : 6.1.0-13-amd64
VM Type    : KVM
IPv4/IPv6  : ✔ Online / ✔ Online

IPv6 Network Information:
---------------------------------
ISP        : Scaleblade, Ltd.
ASN        : AS52041 Scaleblade, Ltd.
Host       : Scaleblade Vmnet
Location   : Saint Andrews Quay, England (ENG)
Country    : United Kingdom

fio Disk Speed Tests (Mixed R/W 50/50) (Partition /dev/sda1):
---------------------------------
Block Size | 4k            (IOPS) | 64k           (IOPS)
  ------   | ---            ----  | ----           ----
Read       | 570.52 MB/s (142.6k) | 2.93 GB/s    (45.9k)
Write      | 572.02 MB/s (143.0k) | 2.95 GB/s    (46.1k)
Total      | 1.14 GB/s   (285.6k) | 5.89 GB/s    (92.0k)
           |                      |
Block Size | 512k          (IOPS) | 1m            (IOPS)
  ------   | ---            ----  | ----           ----
Read       | 3.33 GB/s     (6.5k) | 3.42 GB/s     (3.3k)
Write      | 3.51 GB/s     (6.8k) | 3.65 GB/s     (3.5k)
Total      | 6.85 GB/s    (13.3k) | 7.08 GB/s     (6.9k)

iperf3 Network Speed Tests (IPv4):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping
-----           | -----                     | ----            | ----            | ----
Clouvider       | London, UK (10G)          | 8.71 Gbits/sec  | 7.25 Gbits/sec  | 1.10 ms
Eranium         | Amsterdam, NL (100G)      | 9.20 Gbits/sec  | 8.55 Gbits/sec  | 7.06 ms
Uztelecom       | Tashkent, UZ (10G)        | busy            | 1.97 Gbits/sec  | 83.5 ms
Leaseweb        | Singapore, SG (10G)       | 578 Mbits/sec   | 1.03 Gbits/sec  | --
Clouvider       | Los Angeles, CA, US (10G) | 469 Mbits/sec   | 1.46 Gbits/sec  | 129 ms
Leaseweb        | NYC, NY, US (10G)         | 522 Mbits/sec   | 2.79 Gbits/sec  | 74.4 ms
Edgoo           | Sao Paulo, BR (1G)        | 549 Mbits/sec   | 689 Mbits/sec   | 197 ms

iperf3 Network Speed Tests (IPv6):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping
-----           | -----                     | ----            | ----            | ----
Clouvider       | London, UK (10G)          | 8.75 Gbits/sec  | 6.37 Gbits/sec  | 1.12 ms
Eranium         | Amsterdam, NL (100G)      | 6.99 Gbits/sec  | busy            | 6.98 ms
Uztelecom       | Tashkent, UZ (10G)        | 1.37 Gbits/sec  | 2.22 Gbits/sec  | 83.5 ms
Leaseweb        | Singapore, SG (10G)       | 443 Mbits/sec   | 1.09 Gbits/sec  | 162 ms
Clouvider       | Los Angeles, CA, US (10G) | 815 Mbits/sec   | 1.39 Gbits/sec  | 129 ms
Leaseweb        | NYC, NY, US (10G)         | 799 Mbits/sec   | 2.47 Gbits/sec  | 74.5 ms
Edgoo           | Sao Paulo, BR (1G)        | 429 Mbits/sec   | 711 Mbits/sec   | 197 ms

Geekbench 6 Benchmark Test:
---------------------------------
Test            | Value
                |
Single Core     | 3397
Multi Core      | 3426
Full Test       | https://browser.geekbench.com/v6/cpu/11632302

YABS completed in 11 min 36 sec
```

T&C's
-----

* New accounts are subject to a 100Mbps port limit for the first 14 days by default. LowEndTalk users can open a ticket and verify using a non-spam LowEndTalk account to circumvent this.
* Bandwidth limits are set as soft-cap, we will not turn your VM off if you exceed or give you a huge bill, excessive bandwidth usage (outside your purchased cap) may result in port speed limitation. We always try to work directly with clients to resolve any issues regarding resource over usage.
* Full terms and conditions for services can be found [within our AUP](https://scaleblade.com/legal/acceptable-use "within our AUP").
