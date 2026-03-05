---
id: 215072
title: "Onidel | Ho Chi Minh, Vietnam | EPYC KVM | 50% OFF"
date: "2026-03-05T15:48:47+00:00"
author: "Unknown"
link: "https://lowendtalk.com/discussion/215072/onidel-ho-chi-minh-vietnam-epyc-kvm-50-off"
---
# Onidel | Ho Chi Minh, Vietnam | EPYC KVM | 50% OFF
**Link:** [Original Thread](https://lowendtalk.com/discussion/215072/onidel-ho-chi-minh-vietnam-epyc-kvm-50-off)

Hi LET,

We have just deployed a new cluster in Ho Chi Minh. This is our effort to keep infrastructures in Vietnam on par with what we have in other locations. What you'll get in Ho Chi Minh:

* AMD EPYC Rome
* NVMe Block Storage (Triple replication by Ceph)
* Dedicated IPv4
* Routed IPv6 (pending for BGP announcement, ETA next week)
* 1 Gbps network port
* BW Pooling
* Private network
* High-availability at compute, storage and network-level.
* and more.

The hardware market has been insane over the past few months, as we all know. However, we are offering 50% off recurring pricing on these plans for a limited time.

This promotion applies to annual payments and is valid from now until 00:00 UTC on 8 March 2026.

Minimum config: 1 vCPU, 2 GBs of RAM, 20 GBs of Disk.

---

Use promo code: **VIETNAMISBACK**

**All sales are final. Refunds may be issued as account credit on a case-by-case basis. We reserve the right to determine the eligibility of any refund request. Please ask if you have any questions before making an order.**

---

While you can configure custom config from our control panel, below are the few reference configs:

**ONI-1** $59.40/yr $29.70/yr

* 1 vCPU AMD EPYC Rome
* 2 GBs of RAM
* 20 GBs of NVMe Block Storage (Ceph)
* 1 TB of Data transfer @ 1Gbps
* 1 x IPv4  
  👉 [Login to Order](https://cloud.onidel.com/cloud/compute/vm/deploy)

**ONI-2** $118.80/yr $58.40/yr

* 2 vCPU AMD EPYC Rome
* 4 GBs of RAM
* 40 GBs of NVMe Block Storage (Ceph)
* 2 TB of Data transfer @ 1Gbps
* 1 x IPv4  
  👉 [Login to Order](https://cloud.onidel.com/cloud/compute/vm/deploy)

**ONI-3** $237.60/yr $118.80/yr/yr

* 4 vCPU AMD EPYC Rome
* 8 GBs of RAM
* 80 GBs of NVMe Block Storage (Ceph)
* 4 TB of Data transfer @ 1Gbps
* 1 x IPv4  
  👉 [Login to Order](https://cloud.onidel.com/cloud/compute/vm/deploy)

---

You can find more details about our services, features, and network on our website: <https://onidel.com>

Looking Glass: <https://lg.onidel.com> (by [@oloke](https://lowendtalk.com/profile/oloke) with ❤️‍🔥)

As many people may ask, BGP is currently not available.

Questions? Ask here and me or [@oloke](https://lowendtalk.com/profile/oloke) will assist you.

---

### YABS

```
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #
#              Yet-Another-Bench-Script              #
#                     v2025-04-20                    #
# https://github.com/masonr/yet-another-bench-script #
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #

Thu Mar  5 14:30:28 UTC 2026

Basic System Information:
---------------------------------
Uptime     : 0 days, 0 hours, 44 minutes
Processor  : AMD EPYC 7302 16-Core Processor
CPU cores  : 2 @ 2994.372 MHz
AES-NI     : ✔ Enabled
VM-x/AMD-V : ✔ Enabled
RAM        : 3.8 GiB
Swap       : 0.0 KiB
Disk       : 39.3 GiB
Distro     : Debian GNU/Linux 13 (trixie)
Kernel     : 6.12.48+deb13-amd64
VM Type    : KVM
IPv4/IPv6  : ✔ Online / ❌ Offline

IPv4 Network Information:
---------------------------------
ISP        : CGD
ASN        : Unknown
Host       : CGD Technology Company Limited
Location   : Thành Phố Tam Kỳ, Da Nang City ()
Country    : Vietnam

fio Disk Speed Tests (Mixed R/W 50/50) (Partition /dev/vda1):
---------------------------------
Block Size | 4k            (IOPS) | 64k           (IOPS)
  ------   | ---            ----  | ----           ---- 
Read       | 296.44 MB/s  (74.1k) | 3.74 GB/s    (58.5k)
Write      | 297.22 MB/s  (74.3k) | 3.76 GB/s    (58.8k)
Total      | 593.67 MB/s (148.4k) | 7.51 GB/s   (117.4k)
           |                      |                     
Block Size | 512k          (IOPS) | 1m            (IOPS)
  ------   | ---            ----  | ----           ---- 
Read       | 6.69 GB/s    (13.0k) | 4.66 GB/s     (4.5k)
Write      | 7.05 GB/s    (13.7k) | 4.97 GB/s     (4.8k)
Total      | 13.75 GB/s   (26.8k) | 9.64 GB/s     (9.4k)

iperf3 Network Speed Tests (IPv4):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping           
-----           | -----                     | ----            | ----            | ----           
Clouvider       | London, UK (10G)          | 334 Mbits/sec   | 100 Mbits/sec   | 231 ms         
Eranium         | Amsterdam, NL (100G)      | 597 Mbits/sec   | 411 Mbits/sec   | 229 ms         
Uztelecom       | Tashkent, UZ (10G)        | 409 Mbits/sec   | 325 Mbits/sec  | 304 ms         
Leaseweb        | Singapore, SG (10G)       | 1.03 Gbits/sec  | 420 Mbits/sec   | 53.5 ms        
Clouvider       | Los Angeles, CA, US (10G) | 145 Mbits/sec   | 475 Mbits/sec   | 196 ms         
Leaseweb        | NYC, NY, US (10G)         | 387 Mbits/sec   | 136 Mbits/sec   | 260 ms         
Edgoo           | Sao Paulo, BR (1G)        | busy            | 246 Mbits/sec   | 370 ms

Geekbench 6 Benchmark Test:
---------------------------------
Test            | Value                         
                |                               
Single Core     | 1381                          
Multi Core      | 2528                          
Full Test       | https://browser.geekbench.com/v6/cpu/16878328

YABS completed in 11 min 59 sec
```
