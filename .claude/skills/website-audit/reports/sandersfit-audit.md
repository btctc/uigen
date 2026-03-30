# Website Audit Report — sandersfit.com

**Prepared by:** Professional Web Consultant
**Date:** March 28, 2026
**Website:** https://sandersfit.com
**Business:** SandersFit Performance Center, Dallas, TX

---

## Executive Summary

SandersFit Performance Center has a visually bold website that communicates a premium fitness brand and clearly showcases its offerings — personal training, rehab and recovery, and nutrition. However, several navigation links are broken (clicking "Programs," "Recovery," and "Trainers" in the menu goes nowhere), the site has font-loading errors on every single page, and conflicting business hours across two pages could be sending potential customers away before they ever walk through the door. Fixing these three issues alone could measurably increase the number of people who contact the gym.

---

## What's Working Well

**1. Strong first impression and brand identity.**
Within five seconds a visitor understands this is a high-performance sports fitness center in Dallas. The headline "Become a Member" paired with a "Sign Up" button is clear and direct. The brand hashtag "#ItsJustWork" gives the gym a distinct personality.

**2. Celebrity and professional athlete credibility.**
Derrick Henry is referenced and shown training at the facility. The contact page highlights 3 NFL Rushing Champions training there. This is powerful social proof that very few gyms can claim and it should be featured more prominently.

**3. Transparent pricing on the membership page.**
Four membership tiers ($30, $99, $149, $199 per month) are clearly laid out with what's included at each level. Three of the four tiers have direct "Sign Up" buttons that link to an online booking system (Mindbody). This removes friction for potential members who are ready to buy.

**4. Contact information is prominent and consistent (almost).**
Phone number (214-843-7498) and email (letswork@sandersfit.com) appear in the top bar on every page. The address is also in the top bar and footer. This is excellent practice.

**5. Working contact form with service checkboxes.**
The contact page has a functional form where visitors can select which service they are interested in (personal training, rehab, nutrition, etc.), making it easy to route inquiries.

**6. The Rehab & Therapy subdomain (sfrt.sandersfit.com) is impressive.**
This is a completely separate, well-built website with doctor bios, multiple locations (Dallas, Amarillo, Fort Worth, Frisco, Colleyville, Midlothian), real patient testimonials with names, and clear service descriptions. This is a major business asset.

**7. Detailed service pages.**
The Personal Training, Nutrition, and Rehab & Recovery pages have substantial, well-written content explaining the process and methodology. This helps with Google rankings and builds trust with potential customers.

**8. Trainer credentials are visible.**
Melvin Sanders' credentials (CPT, CSCS, IOM, Biomechanics) are listed, and his background as a former San Antonio Spurs player adds significant credibility.

---

## Critical Issues

These issues are actively costing the business customers right now.

### Issue 1 — Three Navigation Links Are Completely Broken

**Impact: High — visitors clicking these links go nowhere.**

In the main menu, three links do nothing when clicked:
- "Programs" — links to `#` (dead end)
- "Recovery" — links to `#` (dead end)
- "Trainers" — links to `#` (dead end)

When a potential customer clicks "Trainers" or "Programs" and nothing happens, they assume the site is broken or unprofessional. Many will leave without contacting you. These pages either need to be built and linked, or the menu items need to be removed until the pages are ready.

### Issue 2 — Business Hours Are Listed Differently in Two Places

**Impact: High — confusing customers before they even visit.**

The Contact page lists hours as **Monday–Friday 5:00 AM – 9:00 PM**.
The footer on every page lists hours as **Monday–Friday 6:00 AM – 8:00 PM**.
Saturday hours also differ: the footer says **6:00 AM – 12:00 PM**, while the membership page implies **8:00 AM – 2:00 PM**.

A customer who shows up at 5:30 AM based on the contact page will find the gym closed. One who shows up at 8:15 PM based on the contact page may also find it closed. This erodes trust immediately.

### Issue 3 — Five Font-Loading Errors on Every Single Page

**Impact: Medium-High — the site may display incorrect fonts or fall back to default system fonts.**

Every page on the site produces 5 errors when loading:
- Montserrat font failed to load
- Anton font failed to load
- Roboto font failed to load
- Roboto Slab font failed to load
- Racing Sans One font failed to load

These fonts are being requested from a local server path rather than from Google's servers. The design may look noticeably different from what was intended. Visitors may see generic fonts instead of the branded typography.

### Issue 4 — Google Maps API Is Running Without a Valid Key

**Impact: Medium — any maps or location features on the site may not work properly.**

The site is loading Google Maps with an empty API key (`key=`). Google deprecated this practice, and any map embeds on the site likely show an error overlay or "development only" watermark to visitors. Location-based features may fail completely.

### Issue 5 — No Customer Testimonials on the Main Website

**Impact: Medium — missing the single most powerful tool for converting visitors.**

The rehab subdomain (sfrt.sandersfit.com) has excellent, detailed testimonials from real clients. The main sandersfit.com website has zero testimonials for its core services — personal training and nutrition. Testimonials are the number one factor that convinces someone to make a purchase decision for a fitness service. This is a significant missed opportunity.

---

## Recommended Improvements
*(Fix within 30 days)*

**1. Fix or remove the three broken navigation links.**
Either build the "Programs," "Recovery," and "Trainers" pages and link them properly, or temporarily remove those items from the menu. A broken menu link is worse than no menu link.

**2. Standardize business hours across the entire website.**
Pick the correct hours, update them in one place, and make sure they match what appears on your Google Business Profile listing. Incorrect hours cause bad reviews.

**3. Resolve the font-loading errors.**
Your web developer needs to update the font URLs to load from Google Fonts directly (fonts.googleapis.com) instead of the local server path that is currently returning errors. This is likely a 15-minute fix for a developer.

**4. Add 3–5 client testimonials to the main homepage.**
Pull the best reviews from Google, ask clients for permission, and add them to the homepage. Alternatively, embed your Google reviews widget. Seeing reviews from real clients on the homepage will directly increase sign-ups.

**5. Replace the Google Maps API with a properly configured key.**
Your developer needs to obtain a free Google Maps API key and add it to the site. Without this, any maps embedded on the site are not functioning correctly for visitors.

**6. Add a social media link section to the main site footer.**
The rehab subdomain has Instagram and TikTok links. The main site has social icons in the top bar but they are not labeled, which makes them easy to miss. Add labeled, working social media links to the footer.

**7. Fix the typos found on service pages.**
- Membership page: "canellation" (should be "cancellation") — appears three times
- Contact page: "Square Feeet" (should be "Square Feet")
- Rehab page: "IV Theraphy" and "Cryotheraphy" (both should not have the extra 'h')
- Personal training page: "SanderFit" (missing the 's') appears in body copy
- Melvin Sanders page: "Stregnth" (should be "Strength") in the skills section

Typos signal a lack of attention to detail, which is a concern for a business selling elite performance training.

---

## Quick Wins
*(Can each be fixed in under one hour)*

1. **Hours conflict** — Update contact page hours to match footer hours (or vice versa). Takes 5 minutes in WordPress.

2. **Fix "canellation" typo** — It appears three times on the membership page. Fix in WordPress editor in 5 minutes.

3. **Fix "Square Feeet" typo** — One word, one minute to fix on the contact page.

4. **Fix "IV Theraphy" and "Cryotheraphy"** — Two typos on the Rehab & Recovery page.

5. **Fix "Stregnth" on Melvin Sanders page** — One typo that undercuts the professional credibility of the owner's profile page.

6. **Remove or hide the broken nav links** — If "Programs," "Recovery," and "Trainers" pages don't exist yet, remove the links from the menu. This takes 5 minutes in WordPress menu settings.

7. **Add a "Book Online" button linking to Mindbody** — On the homepage hero section, add a secondary button pointing to the Mindbody booking page. You already have this on the membership page; adding it to the homepage will capture visitors who are ready to act immediately.

---

## Estimated Investment

| Task | Estimated Cost |
|------|---------------|
| Fix broken nav links (build or remove) | $200 – $800 (build pages) or free (remove links) |
| Fix hours discrepancy | Free (self-fix in WordPress) |
| Fix font-loading errors | $50 – $150 (1 hour developer time) |
| Fix Google Maps API key | $50 – $150 (1 hour developer time) |
| Fix all typos (7 identified) | Free (self-fix in WordPress) |
| Add testimonials to homepage | $100 – $300 (design and copy) |
| Add social media links to footer | Free (self-fix in WordPress) |
| **Total estimated range** | **$400 – $1,400** |

Note: Most of these fixes can be made by a WordPress-familiar person or a junior developer. None require rebuilding the site.

---

## Pages Reviewed

| Page | URL | Status | Title Found | Notes |
|------|-----|--------|-------------|-------|
| Homepage | sandersfit.com | Working | SandersFit Performance Center – DFW's Premier Sports and Nutrition Performance Center | 5 font errors on load |
| Membership | sandersfit.com/membership/ | Working | Membership – SandersFit Performance Center | "canellation" typo x3 |
| Contact | sandersfit.com/contact/ | Working | Contact – SandersFit Performance Center | Hours conflict with footer; "Square Feeet" typo |
| Personal Training | sandersfit.com/one-on-one-training/ | Working | One-on-one-training – SandersFit Performance Center | "SanderFit" typo in body |
| Nutrition | sandersfit.com/nutrition/ | Working | Nutrition – SandersFit Performance Center | Content is thorough |
| Rehab & Recovery | sandersfit.com/rehab-recovery/ | Working | Rehab & Recovery – SandersFit Performance Center | "IV Theraphy", "Cryotheraphy" typos |
| Melvin Sanders | sandersfit.com/melvin-sanders/ | Working | Melvin Sanders – SandersFit Performance Center | "Stregnth" typo; Rate ($220/hr) listed on page |
| Rehab & Therapy (subdomain) | sfrt.sandersfit.com | Working | Sandersfit Rehab & Therapy | Separate well-built site; 6 locations; real testimonials |
| Programs | sandersfit.com (nav link) | BROKEN | N/A | Links to `#` — does nothing |
| Recovery | sandersfit.com (nav link) | BROKEN | N/A | Links to `#` — does nothing |
| Trainers | sandersfit.com (nav link) | BROKEN | N/A | Links to `#` — does nothing |

---

## Technical Issues Log

| Issue | Severity | Location |
|-------|----------|----------|
| 5 font files failing to load (Montserrat, Anton, Roboto, Roboto Slab, Racing Sans One) | High | All pages |
| Google Maps API key missing/empty | Medium | All pages |
| jQuery Migrate script loaded (outdated compatibility shim) | Low | All pages |
| 3 navigation links pointing to `#` | High | All pages |
| Hours listed differently on Contact page vs. footer | High | Contact page + footer |
| No SSL issues detected | Good | All pages |
| Page titles present and descriptive | Good | All pages |

---

*Report generated March 28, 2026. Screenshots and page snapshots are saved alongside this report.*
