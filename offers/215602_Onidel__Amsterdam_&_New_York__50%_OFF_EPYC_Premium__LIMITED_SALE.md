---
id: 215602
title: "Onidel | Amsterdam & New York | 50% OFF EPYC Premium | LIMITED SALE"
date: "2026-03-25T02:29:56+00:00"
author: "Unknown"
link: "https://lowendtalk.com/discussion/215602/onidel-amsterdam-new-york-50-off-epyc-premium-limited-sale"
---
# Onidel | Amsterdam & New York | 50% OFF EPYC Premium | LIMITED SALE
**Link:** [Original Thread](https://lowendtalk.com/discussion/215602/onidel-amsterdam-new-york-50-off-epyc-premium-limited-sale)

Hello ![;)](https://lowendtalk.com/resources/emoji/wink.png ";)")

We are doing a **very limited 50% OFF** sale on [EPYC Premium](https://onidel.com/services/premium-vps) VPS servers in [Amsterdam](https://onidel.com/services/premium-vps/amsterdam) 🇳🇱 and [New York](https://onidel.com/services/premium-vps/new-york) 🇺🇸.

Here is what we offer:

* AMD EPYC Milan vCPUs
* Super-fast triple replicated [NVMe storage backed by CEPH](https://kb.onidel.com/hc/kb/articles/1756043909-self_healing-failover-virtual-machines#distributed-storage-with-triple-replication)
* [High-Availability](https://kb.onidel.com/hc/kb/articles/1756043909-self_healing-failover-virtual-machines) of Compute, Network and Storage
* 1 Gbps connectivity
* [Bandwidth Pooling](https://kb.onidel.com/hc/kb/articles/1756044057-data-transfer-bandwidth-pooling)
* [Private Networking](https://kb.onidel.com/hc/kb/articles/1771555524-private-networking-vpc)
* [Enterprise-Grade 2.5+ Tbps DDoS protection](https://kb.onidel.com/hc/kb/articles/1756044026-d_do_s-mitigation) (only in Amsterdam)
* Dedicated IPv4 address
* [Routed /64 IPv6](https://kb.onidel.com/hc/kb/articles/1756042502-i_pv6-configuration-on-linux) subnet
* [BGP/BYOIP](https://kb.onidel.com/hc/kb/articles/1772277030-bgp-and-byoip-bring-your-own-ip) (with $10 setup fee)
* [Custom Control Panel](https://cloud.onidel.com) built by us from scratch
* [Custom ISO](https://kb.onidel.com/hc/kb/articles/1770735119-custom-iso) support
* [SEV-SNP](https://kb.onidel.com/hc/kb/articles/1771943583-sev_snp-verified-boot-and-memory-encryption) Memory Encryption
* and many more...

---

Amsterdam 🇳🇱
------------

[Digital Realty AMS5](https://kb.onidel.com/hc/kb/articles/1756088660-datacenters#netherlands) Facility - [Looking Glass](https://lg-ams.onidel.com)

### ONI-2

2 vCPU (EPYC Milan)  
4 GB RAM  
40 GB NVMe SSD  
5 TB traffic @ 1 Gbps  
1 IPv4 + /64 IPv6

$118.80/year -> **$58.40/year**

[Order here](https://cloud.onidel.com)

### ONI-3

4 vCPU (EPYC Milan)  
8 GB RAM  
80 GB NVMe SSD  
10 TB traffic @ 1 Gbps  
1 IPv4 + /64 IPv6

$237.60/year -> **$118.80/year**

[Order here](https://cloud.onidel.com)

Promo code: `50OFF2026AMS` (limited to **25 uses**)

Minimum configuration: 2 vCPU, 4 GB RAM and 40 GB NVMe ([ONI-2 plan](https://onidel.com/services/premium-vps/amsterdam))  
Works also on custom configurations, as long as they're above the minimum required specs.

YABS (ONI-2 in Amsterdam):

```
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #
#              Yet-Another-Bench-Script              #
#                     v2025-04-20                    #
# https://github.com/masonr/yet-another-bench-script #
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #

Wed Mar 25 00:54:06 UTC 2026

Basic System Information:
---------------------------------
Uptime     : 0 days, 0 hours, 2 minutes
Processor  : AMD EPYC 7713 64-Core Processor
CPU cores  : 2 @ 1996.249 MHz
AES-NI     : ✔ Enabled
VM-x/AMD-V : ✔ Enabled
RAM        : 3.8 GiB
Swap       : 0.0 KiB
Disk       : 39.3 GiB
Distro     : Debian GNU/Linux 13 (trixie)
Kernel     : 6.12.74+deb13+1-amd64
VM Type    : KVM
IPv4/IPv6  : ✔ Online / ✔ Online

IPv6 Network Information:
---------------------------------
ISP        : Onidel Pty Ltd
ASN        : AS152900 Onidel Pty Ltd
Host       : Onidel Pty Ltd
Location   : Amsterdam, North Holland (NH)
Country    : Netherlands

fio Disk Speed Tests (Mixed R/W 50/50) (Partition /dev/vda1):
---------------------------------
Block Size | 4k            (IOPS) | 64k           (IOPS)
  ------   | ---            ----  | ----           ---- 
Read       | 336.44 MB/s  (84.1k) | 3.66 GB/s    (57.2k)
Write      | 337.33 MB/s  (84.3k) | 3.68 GB/s    (57.5k)
Total      | 673.78 MB/s (168.4k) | 7.34 GB/s   (114.7k)
           |                      |                     
Block Size | 512k          (IOPS) | 1m            (IOPS)
  ------   | ---            ----  | ----           ---- 
Read       | 15.24 GB/s   (29.7k) | 14.60 GB/s   (14.2k)
Write      | 16.05 GB/s   (31.3k) | 15.57 GB/s   (15.2k)
Total      | 31.30 GB/s   (61.1k) | 30.17 GB/s   (29.4k)

iperf3 Network Speed Tests (IPv4):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping           
-----           | -----                     | ----            | ----            | ----           
Clouvider       | London, UK (10G)          | 1.01 Gbits/sec  | 1.02 Gbits/sec  | 7.99 ms        
Eranium         | Amsterdam, NL (100G)      | 1.06 Gbits/sec  | 1.02 Gbits/sec  | 0.979 ms       
Uztelecom       | Tashkent, UZ (10G)        | 434 Mbits/sec   | 950 Mbits/sec   | 92.5 ms        
Leaseweb        | Singapore, SG (10G)       | 238 Mbits/sec   | 909 Mbits/sec   | --             
Clouvider       | Los Angeles, CA, US (10G) | 345 Mbits/sec   | busy            | 141 ms         
Leaseweb        | NYC, NY, US (10G)         | 405 Mbits/sec   | 928 Mbits/sec   | 76.3 ms        
Edgoo           | Sao Paulo, BR (1G)        | 300 Mbits/sec   | 777 Mbits/sec   | 237 ms         

iperf3 Network Speed Tests (IPv6):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping           
-----           | -----                     | ----            | ----            | ----           
Clouvider       | London, UK (10G)          | 1.06 Gbits/sec  | 998 Mbits/sec   | 7.90 ms        
Eranium         | Amsterdam, NL (100G)      | 1.06 Gbits/sec  | 1.01 Gbits/sec  | 0.912 ms       
Uztelecom       | Tashkent, UZ (10G)        | 410 Mbits/sec   | 940 Mbits/sec   | 92.5 ms        
Leaseweb        | Singapore, SG (10G)       | 275 Mbits/sec   | 889 Mbits/sec   | 162 ms         
Clouvider       | Los Angeles, CA, US (10G) | 371 Mbits/sec   | 852 Mbits/sec   | 141 ms         
Leaseweb        | NYC, NY, US (10G)         | 423 Mbits/sec   | 881 Mbits/sec   | 76.3 ms        
Edgoo           | Sao Paulo, BR (1G)        | 123 Mbits/sec   | 449 Mbits/sec   | 238 ms         

Geekbench 6 Benchmark Test:
---------------------------------
Test            | Value                         
                |                               
Single Core     | 1295                          
Multi Core      | 2372                          
Full Test       | https://browser.geekbench.com/v6/cpu/17258125

YABS completed in 14 min 43 sec
```

---

New York 🇺🇸
-----------

[Evocative DC (EWR1)](https://kb.onidel.com/hc/kb/articles/1756088660-datacenters#usa) Facility - [Looking Glass](https://lg-ny.onidel.com)

### ONI-1

1 vCPU (EPYC Milan)  
2 GB RAM  
20 GB NVMe SSD  
2 TB traffic @ 1 Gbps  
1 IPv4 + /64 IPv6

$59.40/year -> **$29.70/year**

[Order here](https://cloud.onidel.com)

### ONI-2

2 vCPU (EPYC Milan)  
4 GB RAM  
40 GB NVMe SSD  
4 TB traffic @ 1 Gbps  
1 IPv4 + /64 IPv6

$118.80/year -> **$58.40/year**

[Order here](https://cloud.onidel.com)

### ONI-3

4 vCPU (EPYC Milan)  
8 GB RAM  
80 GB NVMe SSD  
6 TB traffic @ 1 Gbps  
1 IPv4 + /64 IPv6

$237.60/year -> **$118.80/year**

[Order here](https://cloud.onidel.com)

Promo code: `50OFF2026NY` (limited to **75 uses**)  
Minimum configuration: 1 vCPU, 2 GB RAM and 20 GB NVMe ([ONI-1 plan](https://onidel.com/services/premium-vps/new-york))  
Works also on custom configurations, as long as they're above the minimum required specs.

YABS (ONI-2 in New York):

```
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #
#              Yet-Another-Bench-Script              #
#                     v2025-04-20                    #
# https://github.com/masonr/yet-another-bench-script #
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #

Wed Mar 25 00:54:09 UTC 2026

Basic System Information:
---------------------------------
Uptime     : 0 days, 0 hours, 2 minutes
Processor  : AMD EPYC 7713 64-Core Processor
CPU cores  : 2 @ 2000.004 MHz
AES-NI     : ✔ Enabled
VM-x/AMD-V : ✔ Enabled
RAM        : 3.8 GiB
Swap       : 0.0 KiB
Disk       : 39.3 GiB
Distro     : Debian GNU/Linux 13 (trixie)
Kernel     : 6.12.74+deb13+1-amd64
VM Type    : KVM
IPv4/IPv6  : ✔ Online / ✔ Online

IPv6 Network Information:
---------------------------------
ISP        : Onidel Pty Ltd
ASN        : AS152900 Onidel Pty Ltd
Host       : NoPKT LLC
Location   : New York, New York (NY)
Country    : United States

fio Disk Speed Tests (Mixed R/W 50/50) (Partition /dev/vda1):
---------------------------------
Block Size | 4k            (IOPS) | 64k           (IOPS)
  ------   | ---            ----  | ----           ---- 
Read       | 308.40 MB/s  (77.1k) | 4.72 GB/s    (73.7k)
Write      | 309.22 MB/s  (77.3k) | 4.74 GB/s    (74.1k)
Total      | 617.62 MB/s (154.4k) | 9.46 GB/s   (147.9k)
           |                      |                     
Block Size | 512k          (IOPS) | 1m            (IOPS)
  ------   | ---            ----  | ----           ---- 
Read       | 16.47 GB/s   (32.1k) | 18.61 GB/s   (18.1k)
Write      | 17.35 GB/s   (33.8k) | 19.86 GB/s   (19.3k)
Total      | 33.82 GB/s   (66.0k) | 38.47 GB/s   (37.5k)

iperf3 Network Speed Tests (IPv4):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping           
-----           | -----                     | ----            | ----            | ----           
Clouvider       | London, UK (10G)          | 239 Mbits/sec   | 955 Mbits/sec   | 89.9 ms        
Eranium         | Amsterdam, NL (100G)      | 329 Mbits/sec   | 865 Mbits/sec   | 84.7 ms        
Uztelecom       | Tashkent, UZ (10G)        | 243 Mbits/sec   | 776 Mbits/sec   | 178 ms         
Leaseweb        | Singapore, SG (10G)       | 137 Mbits/sec   | 772 Mbits/sec   | 227 ms         
Clouvider       | Los Angeles, CA, US (10G) | 168 Mbits/sec   | 982 Mbits/sec   | 55.5 ms        
Leaseweb        | NYC, NY, US (10G)         | 1.07 Gbits/sec  | 1.02 Gbits/sec  | 2.81 ms        
Edgoo           | Sao Paulo, BR (1G)        | 159 Mbits/sec   | 848 Mbits/sec   | 127 ms         

iperf3 Network Speed Tests (IPv6):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping           
-----           | -----                     | ----            | ----            | ----           
Clouvider       | London, UK (10G)          | 333 Mbits/sec   | 944 Mbits/sec   | 89.8 ms        
Eranium         | Amsterdam, NL (100G)      | 264 Mbits/sec   | 847 Mbits/sec   | 84.7 ms        
Uztelecom       | Tashkent, UZ (10G)        | 145 Mbits/sec   | 857 Mbits/sec   | 178 ms         
Leaseweb        | Singapore, SG (10G)       | 102 Mbits/sec   | 796 Mbits/sec   | 227 ms         
Clouvider       | Los Angeles, CA, US (10G) | 116 Mbits/sec   | 967 Mbits/sec   | 55.4 ms        
Leaseweb        | NYC, NY, US (10G)         | 1.07 Gbits/sec  | 1.01 Gbits/sec  | 2.83 ms        
Edgoo           | Sao Paulo, BR (1G)        | 201 Mbits/sec   | 910 Mbits/sec   | 127 ms         

Geekbench 6 Benchmark Test:
---------------------------------
Test            | Value                         
                |                               
Single Core     | 1488                          
Multi Core      | 2749                          
Full Test       | https://browser.geekbench.com/v6/cpu/17258096

YABS completed in 13 min 30 sec
```

---

Important notes
---------------

### Refunds

All sales are final. Refunds may be issued as [account credit](https://kb.onidel.com/hc/kb/articles/1756033443-terms-of-service#account-credit) on a case-by-case basis. We reserve the right to determine the eligibility of any refund request. Please ask if you have any questions before making an order.

### Questions

In case of any questions or doubts please check our [knowledgebase](https://kb.onidel.com/) or ask us here ( [@onidel](https://lowendtalk.com/profile/onidel) [@oloke](https://lowendtalk.com/profile/oloke) ) or via [ticket from the panel](https://cloud.onidel.com/account/tickets/new) ![:)](https://lowendtalk.com/resources/emoji/smile.png ":)")
