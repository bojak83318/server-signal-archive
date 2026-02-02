---
id: 214140
title: "Onidel | Sydney & Singapore | Storage VM | Object Storage | 50% OFF | 24HRS ONLY"
date: "2026-02-02T06:00:18+00:00"
author: "Unknown"
link: "https://lowendtalk.com/discussion/214140/onidel-sydney-singapore-storage-vm-object-storage-50-off-24hrs-only"
---
# Onidel | Sydney & Singapore | Storage VM | Object Storage | 50% OFF | 24HRS ONLY
**Link:** [Original Thread](https://lowendtalk.com/discussion/214140/onidel-sydney-singapore-storage-vm-object-storage-50-off-24hrs-only)

G'day!

We are running a **24-hour promo** for **Storage VM and Object Storage** in **Singapore** and **Sydney**!

This was originally planned for Sydney only, but we expect plenty of questions about transferring between the two locations - so to keep things simple, we are opening it up to both.

Before we get into the details, let me introduce Kip, our beloved mascot, unboxing your promo 🎁 Thanks [@fluffernutter](https://lowendtalk.com/profile/fluffernutter) for the awesome artwork!

![](https://vault.moe/803SCABifQY8.png)

🌎 Home page: <https://onidel.com>  
🎛️ Control panel: <https://cloud.onidel.com>  
🔍 Looking glass: <https://lg.onidel.com>

Storage VM - 50% off annually
=============================

---

Our Storage VMs are backed by NVMe block storage for the root disk and HDD block storage for the data disk, all powered by Ceph with triple replication to ensure high availability, strong data durability, and data integrity.

BOX-1 - $33/yr
--------------

1 vCPU | 1 GB RAM | 20 GB NVMe | 1000 GB HDD | 1 TB @ 1Gbps  
[Login to order](https://cloud.onidel.com/cloud/compute/vm/deploy)

BOX-2 - $57/yr
--------------

1 vCPU | 1 GB RAM | 20 GB NVMe | 2000 GB HDD | 2 TB @ 1Gbps  
[Login to order](https://cloud.onidel.com/cloud/compute/vm/deploy)

BOX-3 - $84/yr
--------------

1 vCPU | 2 GB RAM | 20 GB NVMe | 3000 GB HDD | 3 TB @ 1Gbps  
[Login to order](https://cloud.onidel.com/cloud/compute/vm/deploy)

BOX-4 - $114/yr
---------------

2 vCPU | 2 GB RAM | 20 GB NVMe | 4000 GB HDD | 4 TB @ 1Gbps  
[Login to order](https://cloud.onidel.com/cloud/compute/vm/deploy)

---

Object Storage - 50% off annually ($2.50/TB/mo)
===============================================

---

Our object storage is S3-compatible, with unlimited ingress and 3x egress included. To simplify management and integration, we provide bucket-scoped credentials, so there's no need to manage policies manually if you want to segregate access control between buckets.

Features such as CORS, lifecycle rules, and static website hosting can be configured directly from the control panel, and custom domains are fully supported as well.

![](https://i.imgur.com/ggXKEbo.png)

Singapore test file: <https://hello.s3.ap-southeast-1.onidel.cloud/memtest86-iso.iso>  
Sydney test file: <https://hello.s3.ap-southeast-2.onidel.cloud/memtest86-iso.iso>

[Login to order](https://cloud.onidel.com/cloud/storage/object-storage/order)

---

FAQ
===

Q: Can I transfer the service between locations?  
A: Unless explicitly stated at the time of order, services cannot be transferred between locations.

Q: Can I upgrade my object storage?  
A: Yes, you can upgrade at any time. Any additional capacity will be charged on a pro-rated basis at the rate in effect at the time of the upgrade.

Q: How can I use my custom domain?  
A: Please refer to this knowledge base article: [KB](https://kb.onidel.com/hc/kb/articles/1766052912-how-to-use-your-own-domain-with-onidel-object-storage)

Q: Does bandwidth usage include inbound or outbound traffic?  
A: Both inbound and outbound traffic count toward your bandwidth usage. We also offer bandwidth pooling, so if you have multiple VMs within the same region, their bandwidth allocations can be combined into a single pool and shared across all VMs.

Q: What happens if my bandwidth usage exceeds the allocation?  
A: For VMs, network speeds will be throttled to 5 Mbps upload and 5 Mbps download. For object storage, excess bandwidth will be charged at $0.01 per GB.

Q: What are the object storage service limits?  
A: The service supports up to 100 buckets, 1000 concurrent connections and 3 million objects per bucket by default. The object limit can be increased by opening a support ticket.

---

Storage VM YABS
===============

```
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #
#              Yet-Another-Bench-Script              #
#                     v2025-04-20                    #
# https://github.com/masonr/yet-another-bench-script #
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #

Mon Feb  2 02:50:23 UTC 2026     

Basic System Information:                                                                                       
---------------------------------                                                                               
Uptime     : 0 days, 0 hours, 7 minutes                                                                         
Processor  : Intel(R) Xeon(R) Gold 6136 CPU @ 3.00GHz                                                           
CPU cores  : 2 @ 2993.008 MHz                                                                                   
AES-NI     : ✔ Enabled                                                                                          
VM-x/AMD-V : ✔ Enabled                                                                                          
RAM        : 1.9 GiB                                                                                            
Swap       : 0.0 KiB                                                                                            
Disk       : 3.9 TiB                                                                                            
Distro     : Ubuntu 24.04.3 LTS
Kernel     : 6.8.0-85-generic     
VM Type    : KVM                 
IPv4/IPv6  : ✔ Online / ✔ Online                                                                                

IPv6 Network Information:                                                                                       
---------------------------------                                                                               
ISP        : Onidel Pty Ltd                                                                                     
ASN        : AS152900 Onidel Pty Ltd                                                                            
Host       : Hypercore Cloud Hosting                                                                            
Location   : Sydney, New South Wales (NSW)                                                                      
Country    : Australia                                                                                          

fio Disk Speed Tests (Mixed R/W 50/50) (Partition /dev/vdb):
---------------------------------
Block Size | 4k            (IOPS) | 64k           (IOPS)                                         
  ------   | ---            ----  | ----           ----                                          
Read       | 40.03 MB/s   (10.0k) | 656.92 MB/s  (10.2k)                                         
Write      | 40.13 MB/s   (10.0k) | 660.38 MB/s  (10.3k)                                         
Total      | 80.16 MB/s   (20.0k) | 1.31 GB/s    (20.5k)                                         
           |                      |                                                              
Block Size | 512k          (IOPS) | 1m            (IOPS)                                         
  ------   | ---            ----  | ----           ----                                          
Read       | 914.85 MB/s   (1.7k) | 904.44 MB/s    (883)                                         
Write      | 963.46 MB/s   (1.8k) | 964.67 MB/s    (942) 
Total      | 1.87 GB/s     (3.6k) | 1.86 GB/s     (1.8k)

iperf3 Network Speed Tests (IPv4):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping                          
-----           | -----                     | ----            | ----            | ----                          
Clouvider       | London, UK (10G)          | 478 Mbits/sec   | 363 Mbits/sec   | 272 ms                        
Eranium         | Amsterdam, NL (100G)      | 416 Mbits/sec   | 705 Mbits/sec   | 275 ms                        
Uztelecom       | Tashkent, UZ (10G)        | 435 Mbits/sec   | 389 Mbits/sec   | 362 ms                        
Leaseweb        | Singapore, SG (10G)       | 766 Mbits/sec   | 776 Mbits/sec   | --                            
Clouvider       | Los Angeles, CA, US (10G) | 597 Mbits/sec   | 860 Mbits/sec   | 143 ms                        
Leaseweb        | NYC, NY, US (10G)         | 596 Mbits/sec   | 797 Mbits/sec   | 246 ms                        
Edgoo           | Sao Paulo, BR (1G)        | 371 Mbits/sec   | 285 Mbits/sec   | 313 ms                        

iperf3 Network Speed Tests (IPv6):                                                                              
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping           
-----           | -----                     | ----            | ----            | ----           
Clouvider       | London, UK (10G)          | 478 Mbits/sec   | 161 Mbits/sec   | 272 ms         
Eranium         | Amsterdam, NL (100G)      | 486 Mbits/sec   | 437 Mbits/sec   | 275 ms         
Uztelecom       | Tashkent, UZ (10G)        | busy            | 165 Mbits/sec   | 362 ms         
Leaseweb        | Singapore, SG (10G)       | 753 Mbits/sec   | 706 Mbits/sec   | 119 ms         
Clouvider       | Los Angeles, CA, US (10G) | 594 Mbits/sec   | 846 Mbits/sec   | 143 ms         
Leaseweb        | NYC, NY, US (10G)         | 588 Mbits/sec   | 803 Mbits/sec   | 246 ms         
Edgoo           | Sao Paulo, BR (1G)        | 397 Mbits/sec   | 198 Mbits/sec   | 313 ms         

Geekbench 6 Benchmark Test:                                                                                     
---------------------------------                       
Test            | Value                         
                |                               
Single Core     | 980                                                                                           
Multi Core      | 1759                                                                                          
Full Test       | https://browser.geekbench.com/v6/cpu/16379365                                  

YABS completed in 18 min 35 sec
```
