---
id: 210689
title: "DigitalFyre's Holla Holla Five Dolla Deal!"
date: "2025-10-22T08:19:40+00:00"
author: "Unknown"
link: "https://lowendtalk.com/discussion/210689/digitalfyres-holla-holla-five-dolla-deal"
---
# DigitalFyre's Holla Holla Five Dolla Deal!
**Link:** [Original Thread](https://lowendtalk.com/discussion/210689/digitalfyres-holla-holla-five-dolla-deal)

Hi LET!

Again, thank you for your support for our first promo! This one is a little different. We have a limited stock left, **only 24**, of the following configuration in New York City, in the Telehouse facility (our old NYC Location before moving to the current one)

### The configuration is simple:

* 4 vCPU Xeon Silver 4215R (Fair Use/Share)
* 4 GB RAM
* 100 GB NVMe Storaage (Gen3)
* 1x IPv4 + 1x /64 IPv6
* 1 Gbit Uplink
* 5 TB Bandwidth outbound + Free inbound
* VirtFusion Control Panel
* 2 Manual Backup slots included
* 14 Day Refund Policy on the custom offer
* $5.00/mo
* [ORDER LINK](https://console.digitalfyre.com/store/forgeflex) (Custom Link. No coupons.)

### What is this for?

* Hosting websites that need a bit of extra storage
* Running a DB
* Whatever you need, really

### FAQ

Q: Is this provisioned automatically?  
A: Nope. Manual activation (Due to the Stacking Option)

Q: Can I upgrade the resources?  
A: No. These are sold as is. But... 👇

Q: Can I stack more than one?  
A: You can stack RAM, CPU, Storage, and Bandwidth. However, **CPU Stacking is limited to 16 vCPU cores**. Also, IP Addresses do **not** stack.

Q: How do I stack?  
A: When ordering, select the number of instances at the checkout page. Your order will be provisioned according to the number of cases you ordered

Q: Can I run BGP?  
A: Sorry, not at this particular facility 😕.

Q: Is this for production use or idling?  
A: For both.

Q: What can I NOT do, then?  
A: Anything our [TOS](https://www.digitalfyre.com/terms-of-service/) & [AUP](https://www.digitalfyre.com/aup/) says you can't do.

Q: Email ports blocked?  
A: Yes, always. But hey! If you have a valid use case, please open a ticket and we'll review!

Q: Annual Payments?  
A: Nope. Monthly only

Q: You said this is the old facility. Does this mean that the plan service has an expiration date?  
A: Absolutely not. If we relocate out of Telehouse, your services will be migrated, and your IP addresses will **not** change.

Q: Can I attach an HDD Block?  
A: Nope. NVMe only :-)

Q: Do you plan to offer HDD Storage VMs?  
A: Yes, soon. Working out some stuff, and those WILL come. I promise! 🤞🏼

Q: YABS?  
A: YABS!

```
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #
#              Yet-Another-Bench-Script              #
#                     v2025-04-20                    #
# https://github.com/masonr/yet-another-bench-script #
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #

Mon Oct 20 07:10:49 PM EDT 2025

Basic System Information:
---------------------------------
Uptime     : 0 days, 0 hours, 1 minutes
Processor  : Intel(R) Xeon(R) Silver 4215R CPU @ 3.20GHz
CPU cores  : 8 @ 3199.998 MHz
AES-NI     : ✔ Enabled
VM-x/AMD-V : ✔ Enabled
RAM        : 7.7 GiB
Swap       : 4.0 GiB
Disk       : 196.9 GiB
Distro     : Debian GNU/Linux 13 (trixie)
Kernel     : 6.12.38+deb13-amd64
VM Type    : KVM
IPv4/IPv6  : ✔ Online / ✔ Online

IPv6 Network Information:
---------------------------------
ISP        : DigitalFyre Internet Solutions, LLC.
ASN        : AS64245 DigitalFyre Internet Solutions, LLC.
Host       : DigitalFyre Internet Solutions, LLC.
Location   : New York, New York (NY)
Country    : United States

fio Disk Speed Tests (Mixed R/W 50/50) (Partition /dev/sda3):
---------------------------------
Block Size | 4k            (IOPS) | 64k           (IOPS)
  ------   | ---            ----  | ----           ---- 
Read       | 265.78 MB/s  (66.4k) | 1.81 GB/s    (28.3k)
Write      | 266.48 MB/s  (66.6k) | 1.82 GB/s    (28.4k)
Total      | 532.27 MB/s (133.0k) | 3.63 GB/s    (56.7k)
           |                      |                     
Block Size | 512k          (IOPS) | 1m            (IOPS)
  ------   | ---            ----  | ----           ---- 
Read       | 1.17 GB/s     (2.2k) | 1.29 GB/s     (1.2k)
Write      | 1.23 GB/s     (2.4k) | 1.37 GB/s     (1.3k)
Total      | 2.40 GB/s     (4.6k) | 2.66 GB/s     (2.6k)

iperf3 Network Speed Tests (IPv4):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping           
-----           | -----                     | ----            | ----            | ----           
Clouvider       | London, UK (10G)          | 876 Mbits/sec   | 902 Mbits/sec   | 70.8 ms        
Eranium         | Amsterdam, NL (100G)      | 845 Mbits/sec   | 868 Mbits/sec   | 75.5 ms        
Uztelecom       | Tashkent, UZ (10G)        | 264 Mbits/sec   | 730 Mbits/sec   | 157 ms         
Leaseweb        | Singapore, SG (10G)       | 453 Mbits/sec   | 781 Mbits/sec   | --             
Clouvider       | Los Angeles, CA, US (10G) | 874 Mbits/sec   | 911 Mbits/sec   | 61.7 ms        
Leaseweb        | NYC, NY, US (10G)         | 932 Mbits/sec   | 941 Mbits/sec   | 2.63 ms        
Edgoo           | Sao Paulo, BR (1G)        | 795 Mbits/sec   | 879 Mbits/sec   | 111 ms         

iperf3 Network Speed Tests (IPv6):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping           
-----           | -----                     | ----            | ----            | ----           
Clouvider       | London, UK (10G)          | 870 Mbits/sec   | 890 Mbits/sec   | 70.7 ms        
Eranium         | Amsterdam, NL (100G)      | 736 Mbits/sec   | 843 Mbits/sec   | 75.4 ms        
Uztelecom       | Tashkent, UZ (10G)        | 777 Mbits/sec   | 797 Mbits/sec   | 157 ms         
Leaseweb        | Singapore, SG (10G)       | 358 Mbits/sec   | 764 Mbits/sec   | 223 ms         
Clouvider       | Los Angeles, CA, US (10G) | 857 Mbits/sec   | 898 Mbits/sec   | 61.6 ms        
Leaseweb        | NYC, NY, US (10G)         | 912 Mbits/sec   | 926 Mbits/sec   | 2.53 ms        
Edgoo           | Sao Paulo, BR (1G)        | 753 Mbits/sec   | 856 Mbits/sec   | 111 ms         

Geekbench 6 Benchmark Test:
---------------------------------
Test            | Value                         
                |                               
Single Core     | 1178                          
Multi Core      | 5190                          
Full Test       | https://browser.geekbench.com/v6/cpu/14570384

YABS completed in 13 min 22 sec
```

I hope you like this offer!

### Cat Tax

![](https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3NjIxNDB5bGZuNG54OG1ydDhneWZ5ZTRxczY4Z3NzeDdqazdqeXM0cyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/7NoNw4pMNTvgc/giphy.gif)

Note: Edited to add the part about the IPs since I forgot to add it. 🤦‍♂️
