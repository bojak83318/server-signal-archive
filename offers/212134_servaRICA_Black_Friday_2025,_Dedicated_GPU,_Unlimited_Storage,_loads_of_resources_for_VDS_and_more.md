---
id: 212134
title: "servaRICA Black Friday 2025, Dedicated GPU, Unlimited Storage, loads of resources for VDS and more"
date: "2025-12-30T18:47:35+00:00"
author: "Unknown"
link: "https://lowendtalk.com/discussion/212134/servarica-black-friday-2025-dedicated-gpu-unlimited-storage-loads-of-resources-for-vds-and-more"
---
# servaRICA Black Friday 2025, Dedicated GPU, Unlimited Storage, loads of resources for VDS and more
**Link:** [Original Thread](https://lowendtalk.com/discussion/212134/servarica-black-friday-2025-dedicated-gpu-unlimited-storage-loads-of-resources-for-vds-and-more)

Hi Everyone
===========

This year we struggled hard to secure these offers. The market for almost every component has gone significantly up, but we managed to maintain pricing because we purchased most hardware early and avoided the spikes.

We have now restocked:

* **Slim and Fat slices** (very popular)
* **Greyhound dedicated servers** (EPYC-based)
* **All storage and unlimited storage plans**

---

What's New
==========

### 1. VPS With Fully Dedicated NVIDIA P40 (24GB VRAM)

We are introducing a new concept: VPS instances with a **fully dedicated NVIDIA P40 GPU**.

* Each server has 8 GPUs
* We run only 8 VMs per server
* Each VM gets **one full GPU via API passthrough**
* The GPU appears exclusively in your VPS

We created this model to control GPU-related costs, as GPU servers are expensive due to high power draw and rapid depreciation. If this concept gains traction, we will offer newer and more powerful GPUs in the future. The P40 setup is to test demand.

---

### 2. New Dedicated Server Line: "Wolfhound"

A new line based on **Intel Gold 6248** (or Platinum).  
These servers support adding **2 x 18TB HDDs**.

---

Highlights
==========

* All cores are dedicated in FAT and SLIM slices plans
* Expandable options: daily storage increases for unlimited plans
* Generous NVMe storage
* Large RAM allocations
* EPYC compute across many offerings

---

Future Offers and Market Conditions
===================================

Hardware pricing over the last 3 months:

* RAM up 3x
* NVMe up 2x
* HDDs up ~1.5x
* Servers and CPUs relatively stable, but lower-end models are out of stock

Vendors indicate that this may not be temporary and could last through **2026**.

Most of the hardware for current offers was purchased before the spike. We decided to absorb the increases and keep pricing unchanged, but this is not sustainable long term if costs remain high.

We are planning future offers and would like your feedback. These apply to new orders only.

Options being considered:

1. **Keep prices the same** but reduce RAM and NVMe/HDD by up to 50%
2. **Keep specs the same** but increase prices by 25–50%
3. Offer **newer hardware** (4th or 5th gen EPYC) but with reduced dedicated CPU, RAM, and storage

Please let us know what you prefer.

---

KVM Slim Slice Plans (VDS Dedicated CPU Cores and ultra fast NVMe Disks)
------------------------------------------------------------------------

**Order Link:** [KVM SLIM SLICES](https://clients.servarica.com/store/bf-2025-kvm-slim-slice)

| Name | CPU | RAM | NVMe Disk | Price | Link |
| --- | --- | --- | --- | --- | --- |
| KVM Slim Slice 2 | 2 Dedicated Cores | 8GB | 250GB | $5/m | [Order Now](https://clients.servarica.com/store/bf-2025-kvm-slim-slice/kvm-slim-slice-2) |
| KVM Slim Slice 4 | 4 Dedicated Cores | 16GB | 500GB | $8/m | [Order Now](https://clients.servarica.com/store/bf-2025-kvm-slim-slice/kvm-slim-slice-4) |
| KVM Slim Slice 6 | 6 Dedicated Cores | 24GB | 750GB | $11/m | [Order Now](https://clients.servarica.com/store/bf-2025-kvm-slim-slice/kvm-slim-slice-6) |
| KVM Slim Slice 8 | 8 Dedicated Cores | 32GB | 1000GB | $14/m | [Order Now](https://clients.servarica.com/store/bf-2025-kvm-slim-slice/kvm-slim-slice-8) |
| KVM Slim Slice 16 | 16 Dedicated Cores | 64GB | 2000GB | $26/m | [Order Now](https://clients.servarica.com/store/bf-2025-kvm-slim-slice/kvm-slim-slice-16) |

**Bandwidth – KVM Slim Slice**

| Plan | Bandwidth Cap / Speed Profile |
| --- | --- |
| Slim Slice 2 | 250Mbps unlimited / 10Gbps up to 8TB, then 10Mbps |
| Slim Slice 4 | 250Mbps unlimited / 10Gbps up to 16TB, then 10Mbps |
| Slim Slice 6 | 250Mbps unlimited / 10Gbps up to 24TB, then 10Mbps |
| Slim Slice 8 | 250Mbps unlimited / 10Gbps up to 32TB, then 10Mbps |

Cores in KVM slices plans are dedicated but **not pinned** like in Xen (yet). That said, we always under-provision VPS total cores in each host (number of vps vcores is always less than the host total cores) , so you can safely use 100% of your allocated cores all the time with no congestion.

---

KVM FAT Slice Plans ((VDS Dedicated Cores and double ultra fast NVMe Disks))
----------------------------------------------------------------------------

**Order Link:** [KVM FAT SLICES](https://clients.servarica.com/store/bf-2025-kvm-fat-slice)

| Name | CPU | RAM | NVMe Disk | Price | Link |
| --- | --- | --- | --- | --- | --- |
| FAT Slice 2 | 2 Dedicated Cores | 8GB | 500GB | $6/m | [Order Now](https://clients.servarica.com/store/bf-2025-kvm-fat-slice/kvm-fat-slice-2) |
| FAT Slice 4 | 4 Dedicated Cores | 16GB | 1TB | $10/m | [Order Now](https://clients.servarica.com/store/bf-2025-kvm-fat-slice/kvm-fat-slice-4) |
| FAT Slice 6 | 6 Dedicated Cores | 24GB | 1.5TB | $14/m | [Order Now](https://clients.servarica.com/store/bf-2025-kvm-fat-slice/kvm-fat-slice-6) |
| FAT Slice 8 | 8 Dedicated Cores | 32GB | 2TB | $18/m | [Order Now](https://clients.servarica.com/store/bf-2025-kvm-fat-slice/kvm-fat-slice-8) |
| FAT Slice 16 | 16 Dedicated Cores | 64GB | 4000GB | $34/m | [Order Now](https://clients.servarica.com/store/bf-2025-kvm-fat-slice/kvm-fat-slice-16) |

**Bandwidth – KVM FAT Slice**

| Plan | Bandwidth Cap / Speed Profile |
| --- | --- |
| FAT Slice 2 | 250Mbps unlimited / 10Gbps up to 8TB, then 10Mbps |
| FAT Slice 4 | 250Mbps unlimited / 10Gbps up to 16TB, then 10Mbps |
| FAT Slice 6 | 250Mbps unlimited / 10Gbps up to 24TB, then 10Mbps |
| FAT Slice 8 | 250Mbps unlimited / 10Gbps up to 32TB, then 10Mbps |

Cores in KVM slices plans are dedicated but **not pinned** like in Xen (yet). That said, we always under-provision VPS total cores in each host (number of vps vcores is always less than the host total cores) , so you can safely use 100% of your allocated cores all the time with no congestion.

---

Chimera Hybrid Plans (OS on NVMe, extra storage on HDD)
-------------------------------------------------------

**Order Link:** [Chimera Hybrid Plans](https://clients.servarica.com/store/bf-2025-kvm-hybrid)

| Name | CPU | RAM | NVMe Disk | HDD Storage | Price | Link |
| --- | --- | --- | --- | --- | --- | --- |
| Chimera Hybrid Plan 1 | 2 Cores Shared | 4GB | 65GB NVMe | 2TB | $5/m | [Order Now](https://clients.servarica.com/store/bf-2025-kvm-hybrid/chimera-hybrid-1) |
| Chimera Hybrid Plan 2 | 4 Cores Shared | 8GB | 130GB NVMe | 4TB | $10/m | [Order Now](https://clients.servarica.com/store/bf-2025-kvm-hybrid/chimera-hybrid-2) |
| Chimera Hybrid Plan 3 | 6 Cores Shared | 16GB | 260GB NVMe | 8TB | $20/m | [Order Now](https://clients.servarica.com/store/bf-2025-kvm-hybrid/chimera-hybrid-3) |
| Chimera Hybrid Plan 4 | 8 Cores Shared | 32GB | 520GB NVMe | 16TB | $40/m | [Order Now](https://clients.servarica.com/store/bf-2025-kvm-hybrid/chimera-hybrid-4) |

**Bandwidth – Chimera Hybrid**

| Plan | Bandwidth Cap / Speed Profile |
| --- | --- |
| Chimera Hybrid Plan 1 | 250Mbps unlimited / 1Gbps up to 12TB, then 10Mbps |
| Chimera Hybrid Plan 2 | 250Mbps unlimited / 1Gbps up to 18TB, then 10Mbps |
| Chimera Hybrid Plan 3 | 250Mbps unlimited / 1Gbps up to 24TB, then 10Mbps |
| Chimera Hybrid Plan 4 | 250Mbps unlimited / 1Gbps up to 48TB, then 10Mbps |

---

HDD Storage VPS Plans
---------------------

**Order Link:** [HDD Storage VPS Plans](https://clients.servarica.com/store/bf-2025-big-storage)   
\*\*All plans except Opossum 1 have unlimited 250mbps option with daily increase of 1mbps/day

| Plan | RAM | CPU | Storage | Bandwidth | Price | link |
| --- | --- | --- | --- | --- | --- | --- |
| --------------- | ---- | --------- | ---------- | ------------- |  |  |
| Opossum 1 | 1GB | 1 Shared | 1TB HDD | 4TB @ 1Gbps | $29/year | [order](https://clients.servarica.com/store/bf-2025-big-storage/opossum-1-storage) |
| Opossum 2 | 2GB | 2 Shared | 1TB HDD | 12TB @ 1Gbps | $36/year | [order](https://clients.servarica.com/store/bf-2025-big-storage/opossum-2-storage) |
| Polar Bear Storage | 2GB | 2 Shared | 2TB HDD | 12TB @ 1Gbps | $5/month or $48/year | [order](https://clients.servarica.com/store/bf-2025-big-storage/polar-bear-storage) |
| Killer Whale Storage | 2GB | 2 Shared | 3.5TB HDD | 18TB @ 1Gbps | $84/year | [order](https://clients.servarica.com/store/bf-2025-big-storage/killer-whale-storage) |
| Penguin Storage | 6GB | 4 Shared | 4TB HDD | 18TB @ 1Gbps | $11.11/month | [order](https://clients.servarica.com/store/bf-2025-big-storage/penguin-storage) |
| Mammoth Storage | 8GB | 4 Shared | 8TB HDD | 24TB @ 1Gbps | $20/month | [order](https://clients.servarica.com/store/bf-2025-big-storage/mammoth-storage) |

---

Dedicated Servers
-----------------

**Order Link:** [Dedicated Servers Plans](https://clients.servarica.com/store/bf-2025-dedicated-servers)

| Plan Name | CPU Spec | Core | Thread | RAM | SSD | HDD | Bandwidth | Monthly | link |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EPYC Greyhound Dedicated | AMD EPYC 7551P | 32 | 64 | 128GB DDR4 ECC | 3.2TB NVMe | can add 1xHDD | 100TB/M on 10Gbps | $75 | [order](https://clients.servarica.com/store/bf-2025-dedicated-servers/epyc-greyhound-dedicated) |
| EPYC Greyhound 7532 | AMD EPYC 7532 | 32 | 64 | 128GB DDR4 ECC | 3.2TB NVMe | can add 1xHDD | 100TB/M on 10Gbps | $95 | [order](https://clients.servarica.com/store/bf-2025-dedicated-servers/epyc-7532-greyhound-dedicated-server) |
| Wolfhound Dedicated 6248 | GOLD 6248 or Plantinuim 8260 | 20 | 40 | 128GB DDR4 ECC | 3.2TB NVMe | can add 2xHDD | 100TB/M on 10Gbps | $75 | [order](https://clients.servarica.com/store/bf-2025-dedicated-servers/wolfhound-dedicated-server) |
| Bee dedicated GPU VPS | Intel E5-2580v4 | 6 | - | 30GB | 400GB NVMe | - | 100TB/M on 10Gbps | $79 | [order](https://clients.servarica.com/store/bf-2025-dedicated-servers/bee-dedicated-gpu-vps) |

Due to delay in hardware arrival we will deliver Bee GPU servers after 10 days or before

---

About servaRICA
===============

servaRICA is a VPS provider based in Montreal, Canada. We own and operate our network and infrastructure, active since 2010.

* Location: Montreal, Quebec, Canada
* Looking Glass: <https://ping.servarica.com>
* Speed Test: <https://speedtest.servarica.net>

### FAQ

* TOS and AUP: <https://servarica.com/terms-of-service/>
* Payment Methods: PayPal, Alipay, credit cards, cryptocurrencies (BTC, ETH, etc.)
* Storage RAID: All storage servers use RAIDZ2

### Node Specs for Unified Plans

* CPU: AMD EPYC 7532 or 7452
* RAM: 128GB+
* Storage: NVMe
* Uplink: 10Gbps

### Node Specs for Hybrid Plans :

* CPU: E5-2696v4 or E5-2699v4
* RAM: 128GB+
* Storage: NVMe or SAN (RAIDZ2)
* Uplink: 10Gbps

### Node Specs for Storage Plans :

* CPU: Gold 5118
* RAM: 128GB+
* Storage: SAN (RAIDZ2)
* Uplink: 10Gbps

### Node Specs for dedicated GPU plans :

* CPU: E5-2680v4
* RAM: 128GB+
* Storage: NVMe

\* Uplink: 10Gbps
-----------------

Let us know what you think.
