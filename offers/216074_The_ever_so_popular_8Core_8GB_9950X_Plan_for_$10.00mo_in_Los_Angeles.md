---
id: 216074
title: "The ever so popular 8Core 8GB 9950X Plan for $10.00/mo in Los Angeles"
date: "2026-04-09T06:57:49+00:00"
author: "Unknown"
link: "https://lowendtalk.com/discussion/216074/the-ever-so-popular-8core-8gb-9950x-plan-for-10-00-mo-in-los-angeles"
---
# The ever so popular 8Core 8GB 9950X Plan for $10.00/mo in Los Angeles
**Link:** [Original Thread](https://lowendtalk.com/discussion/216074/the-ever-so-popular-8core-8gb-9950x-plan-for-10-00-mo-in-los-angeles)

Hi LET,

I'll keep it simple ![:smiley:](https://lowendtalk.com/resources/emoji/smiley.png ":smiley:")

Some of you remember us from our first offer back in 2025. At the time, the S2 Plan for $6.5 became popular, and many users asked to upgrade to 8GB of RAM, which rounded up to $10.00/mo

We added some new stock in Los Angeles, and there are **20 VMs** of that configuration available:

* 8 AMD Ryzen 9950X vCores
* 8 GB DDR5
* 65 GB NVMe Gen4
* 8 TB Bandwidth
* 10 Gbit Uplink
* 1x IPv4 + /64 IPv6 Subnet
* 2 Free backup slots
* KVM / VirtFusion
* Linux, ISO, and Windows (BYOL)
* $10.00/mo
* Los Angeles, CA [Equinix LA3]

[Looking Glass](https://glass.digitalfyre.com)

**YABS:**

```
root@precious-kick:~# curl -sL https://yabs.sh | bash
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #
#              Yet-Another-Bench-Script              #
#                     v2025-04-20                    #
# https://github.com/masonr/yet-another-bench-script #
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #

Wed Apr  8 11:05:10 PM PDT 2026

Basic System Information:
---------------------------------
Uptime     : 0 days, 0 hours, 1 minutes
Processor  : AMD Ryzen 9 9950X 16-Core Processor
CPU cores  : 8 @ 4291.916 MHz
AES-NI     : ✔ Enabled
VM-x/AMD-V : ✔ Enabled
RAM        : 7.7 GiB
Swap       : 4.0 GiB
Disk       : 64.0 GiB
Distro     : Debian GNU/Linux 13 (trixie)
Kernel     : 6.12.38+deb13-amd64
VM Type    : KVM
IPv4/IPv6  : ✔ Online / ✔ Online

IPv6 Network Information:
---------------------------------
ISP        : DigitalFyre Internet Solutions, LLC.
ASN        : AS64245 DigitalFyre Internet Solutions, LLC.
Host       : DigitalFyre Internet Solutions, LLC.
Location   : Los Angeles, California (CA)
Country    : United States

fio Disk Speed Tests (Mixed R/W 50/50) (Partition /dev/sda3):
---------------------------------
Block Size | 4k            (IOPS) | 64k           (IOPS)
  ------   | ---            ----  | ----           ---- 
Read       | 745.59 MB/s (186.3k) | 4.81 GB/s    (75.3k)
Write      | 747.56 MB/s (186.8k) | 4.84 GB/s    (75.7k)
Total      | 1.49 GB/s   (373.2k) | 9.66 GB/s   (151.0k)
           |                      |                     
Block Size | 512k          (IOPS) | 1m            (IOPS)
  ------   | ---            ----  | ----           ---- 
Read       | 4.50 GB/s     (8.8k) | 4.84 GB/s     (4.7k)
Write      | 4.74 GB/s     (9.2k) | 5.16 GB/s     (5.0k)
Total      | 9.25 GB/s    (18.0k) | 10.01 GB/s    (9.7k)

iperf3 Network Speed Tests (IPv4):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping           
-----           | -----                     | ----            | ----            | ----           
Clouvider       | London, UK (10G)          | 1.41 Gbits/sec  | 916 Mbits/sec   | 126 ms         
Eranium         | Amsterdam, NL (100G)      | 1.59 Gbits/sec  | 1.78 Gbits/sec  | 130 ms         
Uztelecom       | Tashkent, UZ (10G)        | busy            | 861 Mbits/sec   | 231 ms         
Leaseweb        | Singapore, SG (10G)       | 805 Mbits/sec   | 985 Mbits/sec   | 199 ms         
Clouvider       | Los Angeles, CA, US (10G) | 8.67 Gbits/sec  | 7.94 Gbits/sec  | 1.25 ms        
Leaseweb        | NYC, NY, US (10G)         | 3.68 Gbits/sec  | 3.03 Gbits/sec  | 62.3 ms        
Edgoo           | Sao Paulo, BR (1G)        | 785 Mbits/sec   | 1.24 Gbits/sec  | 210 ms         

iperf3 Network Speed Tests (IPv6):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping           
-----           | -----                     | ----            | ----            | ----           
Clouvider       | London, UK (10G)          | 1.40 Gbits/sec  | 883 Mbits/sec   | 125 ms         
Eranium         | Amsterdam, NL (100G)      | 1.64 Gbits/sec  | 1.73 Gbits/sec  | 130 ms         
Uztelecom       | Tashkent, UZ (10G)        | 810 Mbits/sec   | 828 Mbits/sec   | 231 ms         
Leaseweb        | Singapore, SG (10G)       | 567 Mbits/sec   | 885 Mbits/sec   | 198 ms         
Clouvider       | Los Angeles, CA, US (10G) | 8.78 Gbits/sec  | 8.03 Gbits/sec  | 1.30 ms        
Leaseweb        | NYC, NY, US (10G)         | 3.28 Gbits/sec  | 2.82 Gbits/sec  | 62.3 ms        
Edgoo           | Sao Paulo, BR (1G)        | busy            | 932 Mbits/sec   | 216 ms         

Geekbench 6 Benchmark Test:
---------------------------------
Test            | Value                         
                |                               
Single Core     | 3428                          
Multi Core      | 14203                         
Full Test       | https://browser.geekbench.com/v6/cpu/17539952

YABS completed in 10 min 33 sec
```

How to get it: [Order the S2 Plan from our site](https://console.digitalfyre.com/order/vps/small-s2 "Order the S2 Plan from our site"), select Los Angeles, and the first **20 orders** will get that promotional upgrade upon provisioning.

**Things to note:**

* Valid for new & existing clients.
* For production use
* Cannot be used to upgrade an existing service.
* Sold as is. Resources are not upgradeable.

  + But you can stack up to 4 of these, just open a support ticket (IPs do not stack)
* Monthly billing only.
* Cannot swap CPU cores for RAM.
* Email ports are blocked.
* Please use accurate account information (name, address, etc.) when ordering. If MaxMind flags your order due to GFW & proxy use, we'll reinstate it.
* As the node fills up, YABS results ***will*** fluctuate.
* 14 Day Refund Policy for the promotional offer
* We allow service transfers for free (first time only, second time will incur a $5.00 one-time fee) ![;)](https://lowendtalk.com/resources/emoji/wink.png ";)") If you bought a couple and your friend wants one, just let us know, and we'll guide you through the transfer process.
* Orders are provisioned during business hours, and sometimes manual review takes a little bit of time to complete!

Thank you so much! If you order one, we hope you enjoy it!

**Obligatory Cat Tax:**

![](https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ZzZkZnBmZG13bzExMXJ5NWlyeXUzMTBoaGJscjVodzFndDB0MzJ1MiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/x3Y2FMbk7BLW5n0dtE/giphy.gif)
