---
id: 215785
title: "ComputeBox Turns 1 | AMD EPYC Turin + Milan + 4000ADA GPU | Hamburg & Bremen, Germany"
date: "2026-03-31T16:57:55+00:00"
author: "Unknown"
link: "https://lowendtalk.com/discussion/215785/computebox-turns-1-amd-epyc-turin-milan-4000ada-gpu-hamburg-bremen-germany"
---
# ComputeBox Turns 1 | AMD EPYC Turin + Milan + 4000ADA GPU | Hamburg & Bremen, Germany
**Link:** [Original Thread](https://lowendtalk.com/discussion/215785/computebox-turns-1-amd-epyc-turin-milan-4000ada-gpu-hamburg-bremen-germany)

Hey LET 👋

One year ago we introduced ourselves here as a brand-new provider out of Germany, and we're still here, still improving.

Three people run ComputeBox. We operate our own hardware in Mölln (near Hamburg) powered by 100% self-generated renewable energy, and in Bremen.

To mark year one, we're bringing back a fan-favourite deal and adding three more.

---

🎂 1-Year Anniversary Deals
--------------------------

All plans are **monthly prepaid, cancel anytime**, except Deal 4 which is billed 6 months upfront.

---

Deal 1, EPYC Milan (7763) | Hamburg
-----------------------------------

* **CPU:** AMD EPYC 7763 (Milan)
* **RAM:** 16 GB
* **vCores:** 6
* **Storage:** 100 GB NVMe
* **Traffic:** 2 TB
* **Network:** 2 Gbit/s
* **Backup Slots:** 5
* **Backup Storage:** 200 GB *(off-site, dedicated backup DC ~3 km from main DC)*
* **Price: €7.99/mo incl. VAT · €6.71/mo net**

👉 [Order incl. VAT](https://computebox.de/offer/birthday-milan?source=let&campaign=birthday) · [Order excl. VAT](https://computebox.de/offer/birthday-milan?vat=no&source=let&campaign=birthday)

YABS:

```
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #
#              Yet-Another-Bench-Script              #
#                     v2025-04-20                    #
# https://github.com/masonr/yet-another-bench-script #
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #

Sun Mar 29 08:59:04 UTC 2026

Basic System Information:
---------------------------------
Uptime     : 0 days, 17 hours, 0 minutes
Processor  : AMD EPYC 7763 64-Core Processor
CPU cores  : 6 @ 2445.404 MHz
AES-NI     : ✔ Enabled
VM-x/AMD-V : ✔ Enabled
RAM        : 15.6 GiB
Swap       : 0.0 KiB
Disk       : 96.8 GiB
Distro     : Ubuntu 24.04.4 LTS
Kernel     : 6.8.0-58-generic
VM Type    : KVM
IPv4/IPv6  : ✔ Online / ✔ Online

IPv6 Network Information:
---------------------------------
ISP        : CSN-CoLocation
ASN        : AS212341 Stephan Rakowski, trading as CSN-Solutions GmbH
Host       : CSN Solutions
Location   : Margetshöchheim, Bavaria (BY)
Country    : Germany

fio Disk Speed Tests (Mixed R/W 50/50) (Partition /dev/vda1):
---------------------------------
Block Size | 4k            (IOPS) | 64k           (IOPS)
  ------   | ---            ----  | ----           ----
Read       | 327.70 MB/s  (81.9k) | 2.94 GB/s    (46.0k)
Write      | 328.57 MB/s  (82.1k) | 2.96 GB/s    (46.2k)
Total      | 656.28 MB/s (164.0k) | 5.90 GB/s    (92.3k)
           |                      |
Block Size | 512k          (IOPS) | 1m            (IOPS)
  ------   | ---            ----  | ----           ----
Read       | 4.85 GB/s     (9.4k) | 5.88 GB/s     (5.7k)
Write      | 5.11 GB/s     (9.9k) | 6.27 GB/s     (6.1k)
Total      | 9.96 GB/s    (19.4k) | 12.15 GB/s   (11.8k)

iperf3 Network Speed Tests (IPv4):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping
-----           | -----                     | ----            | ----            | ----
Clouvider       | London, UK (10G)          | 1.90 Gbits/sec  | 1.87 Gbits/sec  | 73.7 ms
Eranium         | Amsterdam, NL (100G)      | 1.61 Gbits/sec  | 1.79 Gbits/sec  | 66.9 ms
Uztelecom       | Tashkent, UZ (10G)        | busy            | 1.49 Gbits/sec  | 97.1 ms
Leaseweb        | Singapore, SG (10G)       | 348 Mbits/sec   | 1.36 Gbits/sec  | 197 ms
Clouvider       | Los Angeles, CA, US (10G) | 403 Mbits/sec   | 1.24 Gbits/sec  | 157 ms
Leaseweb        | NYC, NY, US (10G)         | 522 Mbits/sec   | 1.85 Gbits/sec  | 86.0 ms
Edgoo           | Sao Paulo, BR (1G)        | 211 Mbits/sec   | 1.26 Gbits/sec  | 197 ms

iperf3 Network Speed Tests (IPv6):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping
-----           | -----                     | ----            | ----            | ----
Clouvider       | London, UK (10G)          | 1.41 Gbits/sec  | 1.90 Gbits/sec  | 63.8 ms
Eranium         | Amsterdam, NL (100G)      | 1.60 Gbits/sec  | 1.94 Gbits/sec  | 65.4 ms
Uztelecom       | Tashkent, UZ (10G)        | 712 Mbits/sec   | 1.79 Gbits/sec  | 96.2 ms
Leaseweb        | Singapore, SG (10G)       | 374 Mbits/sec   | 982 Mbits/sec   | 198 ms
Clouvider       | Los Angeles, CA, US (10G) | 426 Mbits/sec   | 1.30 Gbits/sec  | 157 ms
Leaseweb        | NYC, NY, US (10G)         | busy            | 1.58 Gbits/sec  | 85.9 ms
Edgoo           | Sao Paulo, BR (1G)        | busy            | 828 Mbits/sec   | 192 ms

Geekbench 6 Benchmark Test:
---------------------------------
Test            | Value
                |
Single Core     | 1445
Multi Core      | 6083
Full Test       | https://browser.geekbench.com/v6/cpu/17347656

YABS completed in 13 min 24 sec
```

---

Deal 2, EPYC Turin | Hamburg 💾 Backup-Focused
---------------------------------------------

* **CPU:** AMD EPYC 9655 (Turin)
* **RAM:** 12 GB
* **vCores:** 3
* **Storage:** 100 GB NVMe
* **Traffic:** 2 TB
* **Network:** 5 Gbit/s
* **Backup Slots:** 5
* **Backup Storage:** 200 GB *(off-site, dedicated backup DC ~3 km from main DC)*
* **Price: €8.99/mo incl. VAT · €7.55/mo net**

👉 [Order incl. VAT](https://computebox.de/offer/birthday-turin-hh?source=let&campaign=birthday) · [Order excl. VAT](https://computebox.de/offer/birthday-turin-hh?vat=no&source=let&campaign=birthday)

YABS:

```
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #
#              Yet-Another-Bench-Script              #
#                     v2025-04-20                    #
# https://github.com/masonr/yet-another-bench-script #
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #

Sun Mar 29 09:19:05 UTC 2026

Basic System Information:
---------------------------------
Uptime     : 0 days, 17 hours, 18 minutes
Processor  : AMD EPYC 9655 96-Core Processor
CPU cores  : 3 @ 2599.998 MHz
AES-NI     : ✔ Enabled
VM-x/AMD-V : ✔ Enabled
RAM        : 11.7 GiB
Swap       : 0.0 KiB
Disk       : 96.9 GiB
Distro     : Ubuntu 25.04
Kernel     : 6.14.0-15-generic
VM Type    : KVM
IPv4/IPv6  : ✔ Online / ✔ Online

IPv6 Network Information:
---------------------------------
ISP        : CSN-CoLocation
ASN        : AS212341 Stephan Rakowski, trading as CSN-Solutions GmbH
Host       : CSN Solutions
Location   : Margetshöchheim, Bavaria (BY)
Country    : Germany

fio Disk Speed Tests (Mixed R/W 50/50) (Partition /dev/vda1):
---------------------------------
Block Size | 4k            (IOPS) | 64k           (IOPS)
  ------   | ---            ----  | ----           ----
Read       | 507.85 MB/s (126.9k) | 4.36 GB/s    (68.2k)
Write      | 509.19 MB/s (127.2k) | 4.38 GB/s    (68.5k)
Total      | 1.01 GB/s   (254.2k) | 8.75 GB/s   (136.8k)
           |                      |
Block Size | 512k          (IOPS) | 1m            (IOPS)
  ------   | ---            ----  | ----           ----
Read       | 7.27 GB/s    (14.1k) | 6.92 GB/s     (6.7k)
Write      | 7.65 GB/s    (14.9k) | 7.38 GB/s     (7.2k)
Total      | 14.92 GB/s   (29.1k) | 14.31 GB/s   (13.9k)

iperf3 Network Speed Tests (IPv4):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping
-----           | -----                     | ----            | ----            | ----
Clouvider       | London, UK (10G)          | 3.06 Gbits/sec  | 3.20 Gbits/sec  | 14.1 ms
Eranium         | Amsterdam, NL (100G)      | 1.86 Gbits/sec  | 3.93 Gbits/sec  | 66.9 ms
Uztelecom       | Tashkent, UZ (10G)        | 728 Mbits/sec   | 2.45 Gbits/sec  | 91.8 ms
Leaseweb        | Singapore, SG (10G)       | 455 Mbits/sec   | 1.48 Gbits/sec  | 197 ms
Clouvider       | Los Angeles, CA, US (10G) | 530 Mbits/sec   | 1.01 Gbits/sec  | 154 ms
Leaseweb        | NYC, NY, US (10G)         | 855 Mbits/sec   | 3.01 Gbits/sec  | 85.3 ms
Edgoo           | Sao Paulo, BR (1G)        | 397 Mbits/sec   | 9.44 Mbits/sec  | 197 ms

iperf3 Network Speed Tests (IPv6):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping
-----           | -----                     | ----            | ----            | ----
Clouvider       | London, UK (10G)          | 2.20 Gbits/sec  | 3.80 Gbits/sec  | 13.8 ms
Eranium         | Amsterdam, NL (100G)      | 2.55 Gbits/sec  | 3.86 Gbits/sec  | 66.1 ms
Uztelecom       | Tashkent, UZ (10G)        | 1.08 Gbits/sec  | 1.92 Gbits/sec  | 91.8 ms
Leaseweb        | Singapore, SG (10G)       | 473 Mbits/sec   | 1.18 Gbits/sec  | 197 ms
Clouvider       | Los Angeles, CA, US (10G) | 547 Mbits/sec   | 946 Mbits/sec   | 154 ms
Leaseweb        | NYC, NY, US (10G)         | 856 Mbits/sec   | 2.84 Gbits/sec  | 85.4 ms
Edgoo           | Sao Paulo, BR (1G)        | 209 Mbits/sec   | 776 Mbits/sec   | 193 ms

Geekbench 6 Benchmark Test:
---------------------------------
Test            | Value
                |
Single Core     | 2531
Multi Core      | 6403
Full Test       | https://browser.geekbench.com/v6/cpu/17347898

YABS completed in 11 min 21 sec
```

---

Deal 3, EPYC Turin | Bremen 🌐 Traffic Beast
-------------------------------------------

Same specs as Deal 2, but optimised for bandwidth instead of backup space.

* **CPU:** AMD EPYC 9655 (Turin)
* **RAM:** 12 GB
* **vCores:** 3
* **Storage:** 100 GB NVMe
* **Traffic:** 15 TB
* **Network:** 5 Gbit/s
* **Price: €8.99/mo incl. VAT · €7.55/mo net**

🎟️ Use coupon code **EEUQ65L4** for 10% off, every billing cycle, limited to 50 VMs.

👉 [Order incl. VAT](https://computebox.de/offer/birthday-turin-hb?source=let&campaign=birthday) · [Order excl. VAT](https://computebox.de/offer/birthday-turin-hb?vat=no&source=let&campaign=birthday)

YABS:

```
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #
#              Yet-Another-Bench-Script              #
#                     v2025-04-20                    #
# https://github.com/masonr/yet-another-bench-script #
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #

Sun Mar 29 09:02:00 UTC 2026

Basic System Information:
---------------------------------
Uptime     : 0 days, 16 hours, 58 minutes
Processor  : AMD EPYC 9655 96-Core Processor
CPU cores  : 3 @ 2599.996 MHz
AES-NI     : ✔ Enabled
VM-x/AMD-V : ✔ Enabled
RAM        : 11.7 GiB
Swap       : 0.0 KiB
Disk       : 96.9 GiB
Distro     : Ubuntu 25.04
Kernel     : 6.14.0-15-generic
VM Type    : KVM
IPv4/IPv6  : ✔ Online / ✔ Online

IPv6 Network Information:
---------------------------------
ISP        : LWLcom GmbH
ASN        : AS47277 LWLcom GmbH
Host       : ComputeBox HB1
Location   : Flintbek, Schleswig-Holstein (SH)
Country    : Germany

fio Disk Speed Tests (Mixed R/W 50/50) (Partition /dev/vda1):
---------------------------------
Block Size | 4k            (IOPS) | 64k           (IOPS)
  ------   | ---            ----  | ----           ----
Read       | 707.32 MB/s (176.8k) | 5.11 GB/s    (79.9k)
Write      | 709.19 MB/s (177.2k) | 5.14 GB/s    (80.3k)
Total      | 1.41 GB/s   (354.1k) | 10.25 GB/s  (160.2k)
           |                      |
Block Size | 512k          (IOPS) | 1m            (IOPS)
  ------   | ---            ----  | ----           ----
Read       | 6.13 GB/s    (11.9k) | 6.56 GB/s     (6.4k)
Write      | 6.46 GB/s    (12.6k) | 7.00 GB/s     (6.8k)
Total      | 12.59 GB/s   (24.5k) | 13.57 GB/s   (13.2k)

iperf3 Network Speed Tests (IPv4):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping
-----           | -----                     | ----            | ----            | ----
Clouvider       | London, UK (10G)          | 2.61 Gbits/sec  | 3.89 Gbits/sec  | 26.5 ms
Eranium         | Amsterdam, NL (100G)      | 3.80 Gbits/sec  | 3.99 Gbits/sec  | 6.95 ms
Uztelecom       | Tashkent, UZ (10G)        | 891 Mbits/sec   | 2.32 Gbits/sec  | 84.9 ms
Leaseweb        | Singapore, SG (10G)       | 374 Mbits/sec   | 896 Mbits/sec   | 159 ms
Clouvider       | Los Angeles, CA, US (10G) | 445 Mbits/sec   | 1.30 Gbits/sec  | 153 ms
Leaseweb        | NYC, NY, US (10G)         | 446 Mbits/sec   | 2.68 Gbits/sec  | 93.0 ms
Edgoo           | Sao Paulo, BR (1G)        | 296 Mbits/sec   | 1.20 Gbits/sec  | 198 ms

iperf3 Network Speed Tests (IPv6):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping
-----           | -----                     | ----            | ----            | ----
Clouvider       | London, UK (10G)          | 2.06 Gbits/sec  | 3.88 Gbits/sec  | 26.5 ms
Eranium         | Amsterdam, NL (100G)      | 3.85 Gbits/sec  | 3.94 Gbits/sec  | 6.92 ms
Uztelecom       | Tashkent, UZ (10G)        | 1.07 Gbits/sec  | 6.40 Mbits/sec  | 84.9 ms
Leaseweb        | Singapore, SG (10G)       | 550 Mbits/sec   | 1.40 Gbits/sec  | 159 ms
Clouvider       | Los Angeles, CA, US (10G) | 188 Mbits/sec   | 1.41 Gbits/sec  | 153 ms
Leaseweb        | NYC, NY, US (10G)         | 503 Mbits/sec   | 2.77 Gbits/sec  | 92.9 ms
Edgoo           | Sao Paulo, BR (1G)        | 279 Mbits/sec   | 635 Mbits/sec   | 198 ms

Geekbench 6 Benchmark Test:
---------------------------------
Test            | Value
                |
Single Core     | 2589
Multi Core      | 6678
Full Test       | https://browser.geekbench.com/v6/cpu/17347681

YABS completed in 12 min 3 sec
```

---

Deal 4, EPYC Turin | Bremen 📦 6-Month Prepaid
---------------------------------------------

> ⚠️ This deal is billed **6 months upfront** (€32.94 incl. VAT · €27.66 net).

* **CPU:** AMD EPYC 9655 (Turin)
* **RAM:** 6 GB
* **vCores:** 2
* **Storage:** 60 GB NVMe
* **Traffic:** 10 TB
* **Network:** 5 Gbit/s
* **Price: €5.49/mo incl. VAT · €4.61/mo net** *(6 months prepaid)*

👉 [Order incl. VAT](https://computebox.de/offer/birthday-turin-hb-6m?source=let&campaign=birthday) · [Order excl. VAT](https://computebox.de/offer/birthday-turin-hb-6m?vat=no&source=let&campaign=birthday)

YABS:

```
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #
#              Yet-Another-Bench-Script              #
#                     v2025-04-20                    #
# https://github.com/masonr/yet-another-bench-script #
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #

Sun Mar 29 09:19:07 UTC 2026

Basic System Information:
---------------------------------
Uptime     : 0 days, 17 hours, 14 minutes
Processor  : AMD EPYC 9655 96-Core Processor
CPU cores  : 2 @ 2599.996 MHz
AES-NI     : ✔ Enabled
VM-x/AMD-V : ✔ Enabled
RAM        : 5.8 GiB
Swap       : 0.0 KiB
Disk       : 58.0 GiB
Distro     : Ubuntu 24.04.4 LTS
Kernel     : 6.8.0-58-generic
VM Type    : KVM
IPv4/IPv6  : ✔ Online / ✔ Online

IPv6 Network Information:
---------------------------------
ISP        : LWLcom GmbH
ASN        : AS47277 LWLcom GmbH
Host       : ComputeBox HB1
Location   : Flintbek, Schleswig-Holstein (SH)
Country    : Germany

fio Disk Speed Tests (Mixed R/W 50/50) (Partition /dev/vda1):
---------------------------------
Block Size | 4k            (IOPS) | 64k           (IOPS)
  ------   | ---            ----  | ----           ----
Read       | 610.07 MB/s (152.5k) | 6.57 GB/s   (102.7k)
Write      | 611.68 MB/s (152.9k) | 6.61 GB/s   (103.3k)
Total      | 1.22 GB/s   (305.4k) | 13.18 GB/s  (206.0k)
           |                      |
Block Size | 512k          (IOPS) | 1m            (IOPS)
  ------   | ---            ----  | ----           ----
Read       | 9.20 GB/s    (17.9k) | 9.75 GB/s     (9.5k)
Write      | 9.69 GB/s    (18.9k) | 10.40 GB/s   (10.1k)
Total      | 18.89 GB/s   (36.8k) | 20.16 GB/s   (19.6k)

iperf3 Network Speed Tests (IPv4):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping
-----           | -----                     | ----            | ----            | ----
Clouvider       | London, UK (10G)          | 2.03 Gbits/sec  | 3.84 Gbits/sec  | 21.7 ms
Eranium         | Amsterdam, NL (100G)      | 3.84 Gbits/sec  | 3.99 Gbits/sec  | 6.93 ms
Uztelecom       | Tashkent, UZ (10G)        | 812 Mbits/sec   | 2.09 Gbits/sec  | 86.2 ms
Leaseweb        | Singapore, SG (10G)       | 364 Mbits/sec   | 802 Mbits/sec   | 157 ms
Clouvider       | Los Angeles, CA, US (10G) | 476 Mbits/sec   | 1.04 Gbits/sec  | 153 ms
Leaseweb        | NYC, NY, US (10G)         | 369 Mbits/sec   | 2.52 Gbits/sec  | 92.7 ms
Edgoo           | Sao Paulo, BR (1G)        | 352 Mbits/sec   | 896 Mbits/sec   | 198 ms

iperf3 Network Speed Tests (IPv6):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping
-----           | -----                     | ----            | ----            | ----
Clouvider       | London, UK (10G)          | 2.26 Gbits/sec  | 3.89 Gbits/sec  | 21.6 ms
Eranium         | Amsterdam, NL (100G)      | 3.77 Gbits/sec  | 3.94 Gbits/sec  | 6.92 ms
Uztelecom       | Tashkent, UZ (10G)        | 625 Mbits/sec   | 1.90 Gbits/sec  | 86.2 ms
Leaseweb        | Singapore, SG (10G)       | 436 Mbits/sec   | 1.32 Gbits/sec  | 157 ms
Clouvider       | Los Angeles, CA, US (10G) | 561 Mbits/sec   | 952 Mbits/sec   | 153 ms
Leaseweb        | NYC, NY, US (10G)         | 471 Mbits/sec   | 2.38 Gbits/sec  | 92.7 ms
Edgoo           | Sao Paulo, BR (1G)        | 225 Mbits/sec   | 1.14 Gbits/sec  | 199 ms

Geekbench 6 Benchmark Test:
---------------------------------
Test            | Value
                |
Single Core     | 2621
Multi Core      | 4712
Full Test       | https://browser.geekbench.com/v6/cpu/17347906

YABS completed in 12 min 21 sec
```

---

🖥️ GPU VMs, RTX 4000 ADA | Hamburg
----------------------------------

Looking for GPU compute? We also offer VMs backed by NVIDIA RTX 4000 ADA GPUs, hosted in Hamburg. Available directly via our panel, no ticket needed.

🎟️ Use coupon code **1FB1Z0BG** for 15% off every billing cycle on all RTX 4000 ADA VM orders.

👉 [Order here](https://computebox.de/offer/rtx-4000-ada-birthday?source=let&campaign=birthday)

---

🔍 Looking Glass
---------------

* Hamburg: [lg.computebox.de](https://lg.computebox.de)
* Bremen: [lg-hb.computebox.de](https://lg-hb.computebox.de)

---

❓ FAQ
-----

**What payment methods do you accept?**  
PayPal and credit card via Stripe. No crypto.

**How does backup storage work?**  
Backup storage is billed based on actual data stored, not your full disk size. If your VM uses 10 GB, only 10 GB of backup space is consumed, not the full 100 GB disk allocation.

**Can I add more traffic, storage or backup space?**  
Yes. Additional traffic, disk storage, backup space and backup slots (subject to availability) can be added self-service through the panel. Package upgrades (more CPU cores or RAM) are not available, these are fixed deals.

**Do you support rDNS?**  
Yes. IPv4 rDNS is available in both Hamburg and Bremen. IPv6 rDNS is currently available in Bremen only, we are working on bringing it to Hamburg.

**Are these deals recurring?**  
Yes, the price is fixed monthly. No contract, cancel anytime. Deal 4 is prepaid 6 months upfront.

---

About ComputeBox
----------------

* 🇩🇪 Own hardware in Germany, Mölln/Hamburg and Bremen
* ♻️ 100% renewable energy at our Hamburg site
* 💾 Off-site backups at a dedicated backup DC ~3 km from the main datacenter (Hamburg)
* 🔧 KVM virtualisation, NVMe storage, IPv4 + IPv6 included
* 📊 Self-service add-ons for traffic, storage and backup space via the panel

🌐 [computebox.de](https://computebox.de?source=let&campaign=birthday)

---

-The ComputeBox Team
