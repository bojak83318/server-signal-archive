---
id: 217217
title: "Affordable S3 Object Storage – Pay As You Go – EU/US/Asia Locations"
date: "2026-05-13T09:50:25+00:00"
author: "Unknown"
link: "https://lowendtalk.com/discussion/217217/affordable-s3-object-storage-pay-as-you-go-eu-us-asia-locations"
---
# Affordable S3 Object Storage – Pay As You Go – EU/US/Asia Locations
**Link:** [Original Thread](https://lowendtalk.com/discussion/217217/affordable-s3-object-storage-pay-as-you-go-eu-us-asia-locations)

For anyone dealing with backups, CDN origins, media delivery, AI datasets, logs, or large-scale file storage — object storage is usually the cheapest and most scalable option compared to classic VPS disks.

I came across HostingB2B Object Storage  
and the setup is actually pretty interesting for LET users.

Main points:

S3-compatible object storage  
Pay As You Go billing  
**Additional storage only costs €0.12 per GB/month**  
**Additional Outgoing traffic (GB) €0.04/month**  
Multiple locations:

🇱🇺 Luxembourg  
🇩🇪 Darmstadt, Germany  
🇺🇸 Chicago, USA  
🇸🇬 Singapore

Typical use cases:

* Offsite backups (rclone/restic/borg)
* Media hosting
* CDN origin storage
* AI/ML datasets
* Storing logs, archives, snapshots
* Static assets for apps/websites
* Video libraries

The nice part is that you don’t need to overpay for huge fixed plans. You scale storage only when needed, which is exactly how object storage should work. S3 compatibility also means it works with most existing tools immediately.

For Europe-based users, having Luxembourg + Germany locations is useful for latency and data locality. Chicago + Singapore also makes it decent for global deployments.

Looks more aimed at infra people, SaaS projects, hosting providers, developers, and anyone tired of attaching giant storage volumes to VPSes just for backups.

Curious if anyone here already tested it against B2 / Wasabi / R2-style workloads.

Order Now - <https://my.hostingb2b.com/order/s3-object-storage/s3-object-storage>
