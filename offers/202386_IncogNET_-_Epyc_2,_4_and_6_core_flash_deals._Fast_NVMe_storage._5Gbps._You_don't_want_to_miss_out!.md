---
id: 202386
title: "IncogNET - Epyc 2, 4 and 6 core flash deals. Fast NVMe storage. 5Gbps. You don't want to miss out!"
date: "2025-11-09T12:57:40+00:00"
author: "Unknown"
link: "https://lowendtalk.com/discussion/202386/incognet-epyc-2-4-and-6-core-flash-deals-fast-nvme-storage-5gbps-you-dont-want-to-miss-out"
---
# IncogNET - Epyc 2, 4 and 6 core flash deals. Fast NVMe storage. 5Gbps. You don't want to miss out!
**Link:** [Original Thread](https://lowendtalk.com/discussion/202386/incognet-epyc-2-4-and-6-core-flash-deals-fast-nvme-storage-5gbps-you-dont-want-to-miss-out)

[![image](https://assets.incognet.io/assets/images/promo/let-banner.png)](https://incognet.io)

Oh snap, it's another **[IncogNET](https://incognet.io)** offer thread. This time I'm bringing something completely different to the table, and for the time being, exclusively for LowEndTalk!

IncogNET was founded in 2020 and over the years, our VPS plans have remained more or less the same, with the only modifications to our plans being additional value added features that we added over time. This included things such as increasing the port speed from 1Gbps to 5Gbps in all locations and adding features such as offsite snapshots (one at first, now five) and an external VPS firewall. Despite this, our plan specs (CPU, RAM, DISK) have remained rather traditional over the years, and have not really changed.

As our small business continues to grow, we're presented with new opportunities for continuing our growth and taking things to a new level. We're committed to moving towards fully owned and operated hardware in 2025 and have begun to replace some of our older, rented Epyc based servers with newer Epyc gear. The exclusive promotional plans below take advantage of our new server specs that will soon to be deployed in all 3 of our USA locations, allowing us to modernize some plan offerings by giving you more cores and more RAM than our traditional VPS plans.

For now, we have only deployed this in our Liberty Lake, Washington location but will have the same server specs built and shipped to Missouri and Pennsylvania in the coming months.

**But you probably don't care about all of that**, you're just here for some good deals, right?

[![image](https://assets.incognet.io/assets/images/promo/let-flash-deals_1.png)](https://incognet.io)

| **Deal #1** | **Deal #2** | **Deal #3** |
| --- | --- | --- |
| - 2 vCPU - 4GB RAM - 40GB NVMe   ---   - 10TB/mo @ 5Gbps BW - 1 IPv4 Address - 1 IPv6 /64 Subnet   ---   - 5 Free Snapshots (offsite) - VPS Firewall - Many templates or BYO-iso | - 4 vCPU - 6GB RAM - 60GB NVMe   ---   - 10TB/mo @ 5Gbps BW - 1 IPv4 Address - 1 IPv6 /64 Subnet   ---   - 5 Free Snapshots (offsite) - VPS Firewall - Many templates or BYO-iso | - 6 vCPU - 8GB RAM - 80GB NVMe   ---   - 10TB/mo @ 5Gbps BW - 1 IPv4 Address - 1 IPv6 /64 Subnet   ---   - 5 Free Snapshots (offsite) - VPS Firewall - Many templates or BYO-iso |
| [Buy Now](https://portal.incognet.io/store/west-coast-vps/lbrtylk-2-vcpu-4gb-ram-40gb-nvme-5gbps)   ---  - $80 for 1 Year (Best Deal) - $45 for 6/mo - $25 for 3/mo | [Buy Now](https://portal.incognet.io/store/limited-time-promotional-plans-kvm-vps/lbrtylk-4-vcpu-6gb-ram-60gb-nvme-5gbps)   ---  - $100 for 1 Year (Best Deal) - $60 for 6/mo | [Buy Now](https://portal.incognet.io/store/limited-time-promotional-plans-kvm-vps/lbrtylk-6-vcpu-8gb-ram-80gb-nvme-5gbps)   ---  - $120 for 1 Year (Best Deal) |

**No coupon code needed.** These plans can be ordered direct from our portal. Other, shorter, payment terms are available at checkout, but not advertised as they exceed the $10/mo rule on LET.

---

YABS and Speedtests
-------------------

2 vCPU, 4GB RAM, 40GB NVMe YABS:

```
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #
#              Yet-Another-Bench-Script              #
#                     v2025-01-01                    #
# https://github.com/masonr/yet-another-bench-script #
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #

Sat Feb  1 06:23:06 PM UTC 2025

Basic System Information:
---------------------------------
Uptime     : 0 days, 3 hours, 1 minutes
Processor  : AMD EPYC 7B12 64-Core Processor
CPU cores  : 2 @ 2245.778 MHz
AES-NI     : ✔ Enabled
VM-x/AMD-V : ✔ Enabled
RAM        : 3.8 GiB
Swap       : 0.0 KiB
Disk       : 39.3 GiB
Distro     : Debian GNU/Linux 12 (bookworm)
Kernel     : 6.1.0-9-amd64
VM Type    : KVM
IPv4/IPv6  : ✔ Online / ✔ Online

IPv6 Network Information:
---------------------------------
ISP        : IncogNET LLC
ASN        : AS210630 IncogNET LLC
Host       : Incognet LLC
Location   : Liberty Lake, Washington (WA)
Country    : United States

fio Disk Speed Tests (Mixed R/W 50/50) (Partition /dev/vda1):
---------------------------------
Block Size | 4k            (IOPS) | 64k           (IOPS)
  ------   | ---            ----  | ----           ---- 
Read       | 210.95 MB/s  (52.7k) | 2.42 GB/s    (37.8k)
Write      | 211.51 MB/s  (52.8k) | 2.43 GB/s    (38.0k)
Total      | 422.47 MB/s (105.6k) | 4.85 GB/s    (75.8k)
           |                      |                     
Block Size | 512k          (IOPS) | 1m            (IOPS)
  ------   | ---            ----  | ----           ---- 
Read       | 3.90 GB/s     (7.6k) | 4.36 GB/s     (4.2k)
Write      | 4.11 GB/s     (8.0k) | 4.65 GB/s     (4.5k)
Total      | 8.01 GB/s    (15.6k) | 9.02 GB/s     (8.8k)

iperf3 Network Speed Tests (IPv4):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping           
-----           | -----                     | ----            | ----            | ----           
Clouvider       | London, UK (10G)          | 1.25 Gbits/sec  | 853 Mbits/sec   | 137 ms         
Eranium         | Amsterdam, NL (100G)      | 2.75 Gbits/sec  | 3.09 Gbits/sec  | 162 ms         
Uztelecom       | Tashkent, UZ (10G)        | 1.74 Gbits/sec  | 955 Mbits/sec   | 363 ms         
Leaseweb        | Singapore, SG (10G)       | 2.15 Gbits/sec  | 1.97 Gbits/sec  | 185 ms         
Clouvider       | Los Angeles, CA, US (10G) | 3.22 Gbits/sec  | 2.80 Gbits/sec  | 33.5 ms        
Leaseweb        | NYC, NY, US (10G)         | 4.06 Gbits/sec  | 3.26 Gbits/sec  | 82.9 ms        
Edgoo           | Sao Paulo, BR (1G)        | 2.85 Gbits/sec  | 648 Mbits/sec   | 181 ms         

iperf3 Network Speed Tests (IPv6):
---------------------------------
Provider        | Location (Link)           | Send Speed      | Recv Speed      | Ping           
-----           | -----                     | ----            | ----            | ----           
Clouvider       | London, UK (10G)          | 1.26 Gbits/sec  | 526 Mbits/sec   | 137 ms         
Eranium         | Amsterdam, NL (100G)      | 2.70 Gbits/sec  | 2.70 Gbits/sec  | 162 ms         
Uztelecom       | Tashkent, UZ (10G)        | 111 Mbits/sec   | 1.06 Gbits/sec  | 270 ms         
Leaseweb        | Singapore, SG (10G)       | 2.66 Gbits/sec  | 2.43 Gbits/sec  | 184 ms         
Clouvider       | Los Angeles, CA, US (10G) | 3.22 Gbits/sec  | 2.95 Gbits/sec  | 33.5 ms        
Leaseweb        | NYC, NY, US (10G)         | 4.09 Gbits/sec  | 3.32 Gbits/sec  | 69.9 ms        
Edgoo           | Sao Paulo, BR (1G)        | 2.74 Gbits/sec  | 1.07 Gbits/sec  | 181 ms         

Running GB6 benchmark test... *cue elevator music*
```

(My local / home connection dropped during GB6, too lazy to re-initiate the test and wait)

2 vCPU, 4GB RAM, 40GB NVMe NWS.SH speedtest:

```
---------------------------------- nws.sh ---------------------------------
      A simple script to bench network performance using speedtest-cli     
---------------------------------------------------------------------------
 Version            : v2025.01.28
 Global Speedtest   : wget -qO- nws.sh | bash
 Region Speedtest   : wget -qO- nws.sh | bash -s -- -r <region>
---------------------------------------------------------------------------
 Basic System Info
---------------------------------------------------------------------------
 CPU Model          : AMD EPYC 7B12 64-Core Processor
 CPU Cores          : 2 @ 2245.778 MHz
 CPU Cache          : 512 KB
 AES-NI             : ✔ Enabled
 VM-x/AMD-V         : ✔ Enabled
 Total Disk         : 39.3 GB (1.3 GB Used)
 Total RAM          : 3.8 GB (279.8 MB Used)
 System uptime      : 0 days, 0 hour 0 min
 Load average       : 0.13, 0.03, 0.01
 OS                 : Debian GNU/Linux 12
 Arch               : x86_64 (64 Bit)
 Kernel             : 6.1.0-9-amd64
 Virtualization     : KVM
 TCP Control        : bbr
---------------------------------------------------------------------------
 Basic Network Info
---------------------------------------------------------------------------
 Primary Network    : IPv6
 IPv6 Access        : ✔ Online
 IPv4 Access        : ✔ Online
 ISP                : IncogNET LLC
 ASN                : AS210630 IncogNET LLC
 Host               : Incognet LLC
 Location           : Liberty Lake, Washington-WA, United States
---------------------------------------------------------------------------
 Speedtest.net (Region: GLOBAL)
---------------------------------------------------------------------------
 Location         Latency     Loss    DL Speed       UP Speed       Server      

 ISP: IncogNET 

 Nearest          0.52 ms     0.0%    3965.52 Mbps   4866.46 Mbps   Crunchbits - Spokane, WA 

 Kochi, IN        249.51 ms   0.0%    1749.29 Mbps   357.29 Mbps    Asianet Broadband - Cochin 
 Bangalore, IN    253.87 ms   0.0%    2233.42 Mbps   337.41 Mbps    Bharti Airtel Ltd - Bangalore 
 Chennai, IN      274.14 ms   0.0%    1860.33 Mbps   312.07 Mbps    Jio - Chennai 
 Mumbai, IN       269.26 ms   0.0%    1644.53 Mbps   374.36 Mbps    Tata Teleservices Ltd - Mumbai 
 Delhi, IN        265.13 ms   0.0%    2631.18 Mbps   297.98 Mbps    Tata Play Fiber - New Delhi 

 Seattle, US      8.45 ms     N/A     3649.81 Mbps   4424.58 Mbps   Comcast - Seattle, WA 
 Los Angeles, US  32.70 ms    0.0%    3583.09 Mbps   2695.53 Mbps   ReliableSite Hosting - Los Angeles, CA 
 Dallas, US       FAILED                                                        
 Miami, US        89.55 ms    N/A     3084.21 Mbps   964.35 Mbps    Boost Mobile - Miami, FL 
 New York, US     66.41 ms    0.0%    3695.90 Mbps   3016.72 Mbps   GSL Networks - New York, NY 
 Toronto, CA      72.08 ms    0.0%    3167.93 Mbps   1312.67 Mbps   Rogers - Toronto, ON 
 Mexico City, MX  71.32 ms    N/A     3549.45 Mbps   1259.19 Mbps   INFINITUM - Ciudad de México 

 London, UK       144.27 ms   0.0%    3659.56 Mbps   1818.35 Mbps   VeloxServ Communications - London 
 Amsterdam, NL    151.65 ms   0.0%    3653.42 Mbps   1359.45 Mbps   31173 Services AB - Amsterdam 
 Paris, FR        138.35 ms   N/A     3549.02 Mbps   1409.23 Mbps   Axione - Paris 
 Frankfurt, DE    150.55 ms   0.0%    6.23 Mbps      412.44 Mbps    Clouvider Ltd - Frankfurt am Main 
 Warsaw, PL       173.45 ms   0.0%    3550.03 Mbps   1420.55 Mbps   Play - Warszawa 
 Bucharest, RO    189.11 ms   0.0%    3437.73 Mbps   1109.31 Mbps   Vodafone Romania Mobile - Bucharest - Bucharest 
 Moscow, RU       190.39 ms   0.0%    3576.98 Mbps   1306.94 Mbps   RETN - Moscow 

 Jeddah, SA       211.11 ms   0.0%    3491.28 Mbps   1264.25 Mbps   Saudi Telecom Company 
 Dubai, AE        267.90 ms   0.0%    3277.69 Mbps   1070.09 Mbps   e& UAE - Dubai 
 Istanbul, TR     207.00 ms   0.0%    2488.07 Mbps   808.74 Mbps    Turkcell - Istanbul 
 Tehran, IR       228.98 ms   0.3%    2463.42 Mbps   304.43 Mbps    MCI         
 Cairo, EG        195.67 ms   N/A     562.04 Mbps    330.85 Mbps    Orange Egypt - Cairo 

 Tokyo, JP        109.72 ms   16.7%   3631.12 Mbps   611.24 Mbps    GSL Networks - Tokyo 
 Shanghai, CU-CN  FAILED                                                        
 Suzhou, CT-CN    191.94 ms   N/A     3346.43 Mbps   1083.57 Mbps   China Telecom JiangSu 5G - Suzhou 
 Hong Kong, CN    144.36 ms   N/A     3330.09 Mbps   1312.48 Mbps   Misaka Network, Inc. - Hong Kong 
 Singapore, SG    FAILED - IP has been rate limited. Try again after 1 hour.                                                  
 Jakarta, ID      FAILED - IP has been rate limited. Try again after 1 hour.                                                  
---------------------------------------------------------------------------
 Avg DL Speed       : 2919.91 Mbps
 Avg UL Speed       : 1327.42 Mbps

 Total DL Data      : 110.05 GB
 Total UL Data      : 44.23 GB
 Total Data         : 154.28 GB
---------------------------------------------------------------------------
 Duration           : 14 min 1 sec
 System Time        : 01/02/2025 - 19:26:12 UTC
 Total Script Runs  : 97746
---------------------------------------------------------------------------
 Result             : https://result.nws.sh/r/1738437944_UZN08V_GLOBAL.txt
---------------------------------------------------------------------------
```

*Note: The speedtest results above are achieved on the same plan available for purchase but with an updated sysctl.conf file (shown below). I'll continue to test and tweak the sysctl.conf file and likely find a happy medium that is suitable for all plans that may replace the default one or offer a custom Debian template that includes the Xanmod kernel + some sysctl.conf tweaks and some other minor modifications that may increase performance.*

```
########################################################################
# /etc/sysctl.conf - Optimized for Network Performance and Throughput  #
# Debian 12 VPS (2 CPU, 4 GB RAM, stock kernel)                        #
########################################################################

# Increase the maximum number of open file descriptors (for network apps)
fs.file-max = 1000000

# Increase the maximum number of incoming connections
net.core.somaxconn = 1024

# Increase the maximum number of packets allowed to queue on the input side
net.core.netdev_max_backlog = 250000

# Increase the maximum socket receive and send buffer sizes (in bytes)
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216

# Increase TCP read and write buffer space [min, default, max] (in bytes)
net.ipv4.tcp_rmem = 4096 87380 16777216
net.ipv4.tcp_wmem = 4096 16384 16777216

# Increase the size of the listen queue for new TCP connections
net.ipv4.tcp_max_syn_backlog = 4096

# Expand the local (ephemeral) port range
net.ipv4.ip_local_port_range = 1024 65535

# Enable TCP window scaling (should be enabled by default, but enforced here)
net.ipv4.tcp_window_scaling = 1

# Reduce the time TCP sockets remain in FIN-WAIT-2 state
net.ipv4.tcp_fin_timeout = 15

# Enable TCP Fast Open (improves performance for some connections)
net.ipv4.tcp_fastopen = 3

# Disable slow start after idle to speed up connection recovery
net.ipv4.tcp_slow_start_after_idle = 0

# Enable SYN cookies to help protect against SYN flood attacks
net.ipv4.tcp_syncookies = 1

# Set the default queuing discipline and enable BBR congestion control.
# (BBR is supported on modern kernels and can improve throughput/latency.)
net.core.default_qdisc = fq
net.ipv4.tcp_congestion_control = bbr

# Enable keepalive for idle TCP connections; adjust as needed
net.ipv4.tcp_keepalive_time = 600
net.ipv4.tcp_keepalive_intvl = 60
net.ipv4.tcp_keepalive_probes = 5
```

Looking Glass
-------------

* Liberty Lake, WA: <https://lblk-us.lg.as210630.net> (The advertised promo is for this location only)
* Kansas City, MO: <https://kcmo-us.lg.as210630.net>
* Allentown, PA: <https://altw-us.lg.as210630.net>
* Naaldwijk, Netherlands: <https://ndwk-nl.lg.as210630.net>

More Info
---------

**Payments Accepted:** Crypto, processed in-house (XMR, LTC, BTC, Doge, Dash) and practically every other useful coin processed via Trocador. PayPal (Subscription or No Subscription) and GoCardless.

**Updated Bandwidth Policy:** These plans use an updated bandwidth policy not yet available on our standard plans, where "technically" the bandwidth is "unlimited", but only the first 10TB/mo is at 5Gbps. Afterwards, you're automatically throttled to 50Mbps which is better than the old method of having your network automatically suspended. This resets monthly so if you ever get throttled, you should automatically go back to 5Gbps at the new month. We may adjust the throttle speed at some point to find a happy medium between "people abusing this because they think it's unlimited" and "the throttle speed is too slow to be useful for actual busy sites and projects".

**This is an unmanaged service:** Don't expect fast support. We do not advertise it nor offer it. Our helpdesk is very full right now and we're working through priority tickets as able. We do plan on hiring additional help this year so that we can have more competitive support, but we are a small business and hiring competent, native English speaking staff and offering a proper, livable wage is simply out of reach at this time.

**FAQ:**

Q: Can I host \_\_\_?  
A: If its legal in the United States, sure.

Q: DMCA?  
A: Read above. DMCA is a US Law and this is in the United States. Host that stuff outside the US.

Q: Refund policy?  
A: 72 hours (Not crypto)

Q: Is this available in other locations?  
A: Not at this time. We're deploying the same hardware to other locations in the coming month, but may not offer this plan specifically. We do have plans to offer some "CPU Optimized" variants of our existing stock plans, however.
