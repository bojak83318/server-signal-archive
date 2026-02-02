---
id: 206727
title: "servaRICA – New KVM VPS Launch: Chimera Hybrid, Slim & FAT Slices – Blazing Disk Speed"
date: "2025-11-26T14:09:22+00:00"
author: "Unknown"
link: "https://lowendtalk.com/discussion/206727/servarica-new-kvm-vps-launch-chimera-hybrid-slim-fat-slices-blazing-disk-speed"
---
# servaRICA – New KVM VPS Launch: Chimera Hybrid, Slim & FAT Slices – Blazing Disk Speed
**Link:** [Original Thread](https://lowendtalk.com/discussion/206727/servarica-new-kvm-vps-launch-chimera-hybrid-slim-fat-slices-blazing-disk-speed)

New KVM Plans – Chimera, Slim, and FAT Slice Lines
==================================================

Hi LET,

This is one of the most exciting offer threads we've shared since we started on LET!

We’ve just introduced **new plans** hosted on our new **KVM platform**. Whether you’re after high-density compute, budget-friendly performance, or storage-heavy options — we have something for everyone.

We’ve listened to your suggestions and feedback. These new plans are a direct response to that.

While we liked Xen (and have a huge automation stack built around it), many clients have asked for alternatives — and we’re delivering.

We also brought over our popular "slice" plan concept to KVM and introduced a new **hybrid storage** line named **Chimera**.  
Chimera pricing is intentionally low — we want users to try it and give us feedback on performance and stability. (later for new orders those plans will have 20% increase but who have them before will keep same old price)

---

all the plans are here   
<https://clients.servarica.com/store/kvm-vps-plans>

Chimera Hybrid Plans (OS on NVMe, extra storage on HDD)
-------------------------------------------------------

| Name | CPU | RAM | NVMe Disk | HDD Storage | Price | Link |
| --- | --- | --- | --- | --- | --- | --- |
| Chimera Hybrid Plan 1 | 2 Cores Shared | 4GB | 90GB NVMe | 2TB | $5/m | [Order Now](https://clients.servarica.com/store/kvm-vps-plans/chimera-hybrid-plan-1) |
| Chimera Hybrid Plan 2 | 4 Cores Shared | 8GB | 180GB NVMe | 4TB | $10/m | [Order Now](https://clients.servarica.com/store/kvm-vps-plans/chimera-hybrid-plan-2) |

**Bandwidth – Chimera Hybrid**

| Plan | Bandwidth Cap / Speed Profile |
| --- | --- |
| Chimera Hybrid Plan 1 | 250Mbps unlimited / 1Gbps up to 12TB, then 10Mbps |
| Chimera Hybrid Plan 2 | 250Mbps unlimited / 1Gbps up to 18TB, then 10Mbps |

> Note: We do have higher Chimera specs available — but they go beyond LET offer limits.

---

KVM Slim Slice Plans (High Density, Performance)
------------------------------------------------

| Name | CPU | RAM | NVMe Disk | Price | Link |
| --- | --- | --- | --- | --- | --- |
| KVM Slim Slice 2 | 2 Dedicated Cores | 8GB | 250GB | $5/m | [Order Now](https://clients.servarica.com/store/proxmox-vps-plans/kvm-slim-slice-2-plan) |
| KVM Slim Slice 4 | 4 Dedicated Cores | 16GB | 500GB | $8/m | [Order Now](https://clients.servarica.com/store/proxmox-vps-plans/kvm-slim-slice-4-plan) |

**Bandwidth – KVM Slim Slice**

| Plan | Bandwidth Cap / Speed Profile |
| --- | --- |
| Slim Slice 2 | 250Mbps unlimited / 10Gbps up to 2TB, then 10Mbps |
| Slim Slice 4 | 250Mbps unlimited / 10Gbps up to 4TB, then 10Mbps |

---

KVM FAT Slice Plans (Performance + Storage)
-------------------------------------------

| Name | CPU | RAM | NVMe Disk | Price | Link |
| --- | --- | --- | --- | --- | --- |
| FAT Slice 2 | 2 Dedicated Cores | 8GB | 500GB | $6/m | [Order Now](https://clients.servarica.com/store/proxmox-vps-plans/kvm-fat-slice-2-plan) |
| FAT Slice 4 | 4 Dedicated Cores | 16GB | 1TB | $10/m | [Order Now](https://clients.servarica.com/store/proxmox-vps-plans/kvm-fat-slice-4-plan) |

**Bandwidth – KVM FAT Slice**

| Plan | Bandwidth Cap / Speed Profile |
| --- | --- |
| FAT Slice 2 | 250Mbps unlimited / 10Gbps up to 8TB, then 10Mbps |
| FAT Slice 4 | 250Mbps unlimited / 10Gbps up to 16TB, then 10Mbps |

> Cores in KVM slices plans are dedicated but **not pinned** like in Xen (yet). That said, we always under-provision VPS total cores in each host (number of vps vcores is always less than the host total cores) , so you can safely use 100% of your allocated cores all the time with no congestion.

---

We Grow Thanks to You
---------------------

We don’t advertise — we grow through your referrals.  
If you like what we offer, share it with friends, forums, and communities.  
Your support helps us keep building great value products.

---

About servaRICA
---------------

**servaRICA** is a Canadian-based VPS provider operating from Montreal since 2010.  
We fully own and operate our infrastructure and network for consistent, quality service.

* **Location:** Montreal, Quebec, Canada
* **Looking Glass:** [ping.servarica.com](https://ping.servarica.com)
* **Speed Test:** [speedtest.servarica.net](https://speedtest.servarica.net)

### FAQ & Details

* **Terms of Service:** [servarica.com/terms-of-service](https://servarica.com/terms-of-service/)
* **Payment Methods:** PayPal, Alipay, Credit Card, BTC, ETH, and other cryptos
* "Crypto payment refund will be on credit only"
* **Storage Redundancy:** All storage uses RAIDZ2 for data protection

### Node Specs

* **CPU:** AMD EPYC 7532 for Unified KVM Plans and Intel Gold for Chimera plans
* **RAM:** 128GB or more
* **Storage:** NVMe or SAN (RAIDZ2)
* **Uplink:** 10Gbps

We’d love to hear your feedback or questions — just reply below!

Thanks,  
**Hani**
