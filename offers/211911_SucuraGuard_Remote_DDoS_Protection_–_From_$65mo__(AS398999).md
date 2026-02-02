---
id: 211911
title: "SucuraGuard Remote DDoS Protection – From $65/mo  (AS398999)"
date: "2025-11-29T23:02:29+00:00"
author: "Unknown"
link: "https://lowendtalk.com/discussion/211911/sucuraguard-remote-ddos-protection-from-65-mo-as398999"
---
# SucuraGuard Remote DDoS Protection – From $65/mo  (AS398999)
**Link:** [Original Thread](https://lowendtalk.com/discussion/211911/sucuraguard-remote-ddos-protection-from-65-mo-as398999)

![](https://sucuranetworks.ca/sucuraguard-let.svg)

SucuraGuard Remote DDoS Protection – AS398999
=============================================

Straightforward remote DDoS protection for networks that need reliable L3/L4 filtering without enterprise-level pricing. Traffic is scrubbed through our network and returned to you over GRE tunnels.

**What we're good for:** Common flood attacks (SYN, UDP, ICMP, reflection/amplification). Small to medium volumetric attacks.  
**What we're not (yet):** A solution for 500Gbps+ sustained attacks or complex application-layer threats. We're the middle ground for networks that need consistent protection without breaking the bank. Our capacity and capabilities are growing over time.

---

🎉 LowEndTalk Exclusive Launch Offer
-----------------------------------

**First 10 customers** who order any plan **WITH the BGP add-on** receive:

**20% OFF FOR LIFE** on their recurring invoice

This means if you're bringing your own AS/prefixes:

* SG-100: **$115/mo** → **$92/mo** (normally $65 + $50 BGP)
* SG-1G: **$135/mo** → **$108/mo** (normally $85 + $50 BGP)
* SG-10G: **$325/mo** → **$260/mo** (normally $275 + $50 BGP)

**Requirements:**  
- Must have your own AS number and announce your own prefixes  
- Minimum /24 IPv4  
- Use promo code `LETBGP20` at checkout  
- Offer valid for first 10 signups only

**⚠️ IMPORTANT:** This discount is **ONLY** valid for orders that include the BGP add-on ($50/mo). Orders placed with the `LETBGP20` coupon code that do not include BGP services will be automatically cancelled and refunded. No exceptions.

---

Network Information
-------------------

* **ASN:** AS398999
* **Scrubbing Capacity:** 780Gbps across multiple active centers
* **Method:** GRE tunnel-based with optional BGP
* **BGP Tools:** <https://bgp.tools/as/398999>
* **PeeringDB:** <https://www.peeringdb.com/net/25055>

**Test IPs:**  
- `142.238.30.10` – Chicago, IL  
- `142.238.30.20` – Toronto, ON  
- `142.238.30.30` – Seattle, WA  
- `142.238.30.40` – New York, NY  
- `142.238.30.50` – Ashburn, VA (deployment in progress)  
- `142.238.30.60` – Frankfurt, DE

*Note: Some scrubbing locations are being finalized. All capacity is actively coming online.*

---

Plans
-----

**Order Page:** <https://services.sucura.ca/store/remote-ddos-protection>

### SG-100 – 100 Mbps Clean – $65/month USD

* 1× GRE tunnel
* 1× /29 IPv4 subnet provided (or bring your own prefix with BGP add-on)
* Good for: Small VPS operations, game servers, personal projects

### SG-1G – 1 Gbps Clean – $85/month USD

* 1× GRE tunnel
* 1× /29 IPv4 subnet provided (or bring your own prefix with BGP add-on)
* Good for: Moderate hosting workloads, frequent but not massive attacks

### SG-10G – 10 Gbps Clean – $275/month USD

* 1× GRE tunnel
* 1× /28 IPv4 subnet provided (or bring your own prefix with BGP add-on)
* Good for: Larger networks, higher sustained clean traffic requirements

**Optional Add-On:**  
- **BGP Session** – $50/month – Announce your own prefixes to AS398999 (requires minimum /24 IPv4)

**Billing:** Month-to-month, no contracts. Cancel anytime.

**Need something different?** We offer custom packages and solutions tailored to your specific needs. Just ask in our Discord or submit a ticket – we're flexible and happy to work with you.

---

How It Works
------------

**Without BGP (GRE only):**  
1. We provide you a /29 or /28 subnet from our IP space  
2. You configure GRE tunnel to our scrubbing endpoints  
3. All traffic to those IPs is automatically filtered 24/7  
4. Clean traffic delivered back to your origin via GRE

**With BGP add-on:**  
1. You announce your prefix(es) to AS398999  
2. Either always-on (we accept all announcements) or on-demand (announce during attack)  
3. GRE tunnel configured for return traffic  
4. You control traffic flow via BGP communities (prepend, blackhole, etc.)

---

What's Included
---------------

✓ L3/L4 DDoS mitigation (SYN/ACK, UDP, ICMP, fragmentation, protocol attacks)  
✓ Reflection/amplification filtering (DNS, NTP, SSDP, Memcached, etc.)  
✓ Consistent rule-set across all plans  
✓ IPv4 support  
✓ **Nexus Portal** – Real-time traffic monitoring and attack visibility for your services  
✓ Attack reporting with traffic graphs and filtered packet statistics

**Current Limitations:**  
- L7/application-layer filtering is limited (we focus on volumetric/protocol attacks)  
- IPv6 support coming soon

---

Who This Is For
---------------

✓ Small to mid-size hosting providers  
✓ Game server operators (Minecraft, FiveM, Rust, etc.)  
✓ VPS/VDS providers needing edge protection  
✓ Startups and budget-conscious operations  
✓ Anyone who needs reliable protection without enterprise pricing

**What to expect:**  
- Solid L3/L4 protection for common attack vectors  
- Transparent pricing, no hidden costs or surprise bills  
- No contracts - cancel anytime if we're not a good fit  
- We're honest about our capabilities and actively improving

---

Company Info
------------

* **Company:** Sucura Networks Inc.
* **Website:** <https://sucuranetworks.ca>
* **Service Page:** <https://sucuranetworks.ca/ddos-protection.html>
* **Network Status:** <https://sucuranetworks.ca/status.html>
* **Support:** Open ticket at <https://services.sucura.ca> or reply here

Setup typically completed within 24 hours of order.

**Need urgent help or currently under attack?** Visit our website and click "Join Our Discord" for immediate assistance, or submit a ticket at <https://services.sucura.ca>

**To claim the LET BGP discount:** Use code `LETBGP20` and ensure you add the BGP Session add-on to your cart. Orders without BGP will be cancelled. Limited to first 10 customers with BGP sessions only.

---

**Coming Soon:** We're actively working on launching our Dedicated Server and VPS/VM lineup. All services will include SucuraGuard DDoS protection by default at no extra cost. Stay tuned or join our Discord for updates!
