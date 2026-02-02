---
id: 212263
title: "MXroute - Email Hosting, Black Friday reseller offer for LET"
date: "2026-01-23T16:16:39+00:00"
author: "Unknown"
link: "https://lowendtalk.com/discussion/212263/mxroute-email-hosting-black-friday-reseller-offer-for-let"
---
# MXroute - Email Hosting, Black Friday reseller offer for LET
**Link:** [Original Thread](https://lowendtalk.com/discussion/212263/mxroute-email-hosting-black-friday-reseller-offer-for-let)

Hey friends,

As usual most of our Black Friday promotions are available at <https://mxroute.blackfriday>. For LET, I'm focusing on one promotion for our reseller services. I want to warn you in advance, reseller services are not for newbies. You are going to have to personally build your user's template using DirectAdmin's visual editor to create for them a nice interface. By default it'll be littered with all of the DirectAdmin functions that you don't want them to have access to for an email only service, most of which will not properly function because we've stripped out key components for them. We have documentation for resellers which may routinely need adjustment based on what you see, because DA is always updating things: <https://docs.mxroute.com/docs/reseller/create-packages.html>

Here is the offer:

Reseller75  
Storage: 75GB  
Users: Unlimited  
Domains: Unlimited  
Email Accounts: Unlimited

Pricing:  
$50/year  
$90/2years  
$130/3years

Order link: <https://accounts.mxroute.com/?cmd=cart&action=add&id=311>

Notes:  
To add our new "DNS Records" page you'll add a custom menu item that links to "/plugin?src=/CMD\_PLUGINS/dns\_records"

To add our new "Expert Spam Filters" page you'll add a custom menu item that links to "/plugin?src=/CMD\_PLUGINS/mxfilter"

Some more technical words:

This promo will be deployed on our new Fusion server. This server will now house regular, large storage, and reseller packages. Rather than beating the box to hell, the number of resellers per server will be limited as we transition into this. The idea is that eventually every server will contain resellers, but they will be limited in number. The goal is to eventually not have any gigantic reseller-only servers.

Less technical words:

First, the elephant in the room. No we do not terminate resellers because their customer was a spammer. We expect you to try to prevent it, and if you repeatedly bring spammers to our platform while making it clear that you have zero intentions on even attempting prevention, you may be asked to leave. Let's put that to bed. Spammers are liars, stop listening to them.

Every year MXroute has grown dramatically, and 2025 has been no exception. I wanted 2025 to be something of a "golden age" for MXroute and in my view we've achieved that. Let's talk about what 2025 brought us:

* New "DNS Records" page in control panel that simplifies SPF/DKIM.
* New "Expert Spam Filtering" page that allows users to opt out of what we formerly called "susranges." The exception being that if you don't want our strongest spam filter, you cannot forward email to Google, Microsoft, Yahoo, AOL, or T-Online. The inbound filter plays a key role in maintaining our outbound reputation, and if you want to circumvent our efforts there then we need to protect our reputation in the places where it matters most.
* In reaction to the most common customer request, we rejected over 80 million spam emails to date in 2025. A handful of people were upset about this new filtering effort, but I've seen quite plainly that it is impossible to not upset someone routinely. Do something, upset someone. Do nothing, upset someone else. The only reasonable goal is to create change that positively impacts the most number of users while upsetting the least number. While we rejected over 80 million spam emails, we only processed 834 whitelist requests. The number of daily whitelist requests continually shrinks, exactly as we intended. So we're not just upsetting few, we're continually shrinking the number of people we're upsetting as we go. If that's not a solid definition of success, I don't know what is.
* We finalized our plans for transitioning away from server "types" with the launch of our new "Fusion" server. New customers (only on Fusion server today), and hopefully all customers eventually, will be able to move between regular, large storage, and reseller services without server migration.
* Blocked senders now receive a support ticket with logs and notes detailing why it was blocked, giving you an opportunity to fix the problem and then we can remove the block.

Let's talk about what the rest of 2025, and 2026, will hopefully bring us (no promises, just goals):

* Server upgrades. We'll be upgrading servers and standardizing our methods for doing this with little to no disruption to users. We've had success there, we're looking to streamline it.
* AI spam filtering. I don't mean "yet another algorithm" here. I mean full human reasoning by LLM to determine spam in ways that spammers cannot simply "trick" it by spelling HomeDepot as H0m3D3p0t. Imagine three text boxes that ask: "Tell me about yourself," "What type of email do you like to receive," "What type of email do you not like to receive." Imagine instead of SpamAssassin headers saying things like "This email had a link, that adds 0.1 to the spam score" we have a summary that says "I know that Bob is a small town baker. Bob likes to receive email from his customers and vendors. Bob doesn't like to receive email about SEO. This email is the type of email that Bob does not like to receive, so I've marked it as spam." You'll provide your own API key for ChatGPT, Gemini, or Claude. We're looking into providing in-house AI as a subscription for those with privacy concerns. This whole feature will be optional, standard filtering will not be replaced. It has already been tested, the biggest hurdles are not about "how" to implement the technical parts.
* Further UX improvements at order time and in the control panel.
* We hope to have Push restored for iOS Mail through a proper method, we are in discussions with Apple at this time. Z-Push is dead, it is not a net positive.
* Improved access to SMTP logs for everyone.
* SMTP relay product. We don't just want to push one out, we want to stick to one of the original MXroute missions of making it easy to budget without making you feel like you need to be staring at a usage graph.

We're not really in this to do things the way they've always been done. Email is an increasingly stressful product for a lot of people, and we won't solve that by copying what has been done a thousand times. All of our solutions come from our own experiences and conversations with users, not from copying what others have always done. I'm very thankful to those of you who have been with us on this journey, and to those who are just joining it.

Happy Black Friday my friends.
