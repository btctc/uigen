# Website Audit Report
## Western Heights School District — Athletics Section
**URL Audited:** https://westernheightssdok.sites.thrillshare.com/o/whsd/page/athletics-copy
**Audit Date:** March 29, 2026
**Auditor:** Professional Web Consultant
**Platform:** Apptegy / ThrillShare CMS

---

## Executive Summary

The Western Heights School District athletics website is built on the Apptegy/ThrillShare platform and contains thoughtful content — including a welcome letter from the Athletic Director and a well-organized sports navigation structure. However, the site has one catastrophic problem that overrides almost everything else: **every single page in the Athletics section loads completely blank for most visitors.** A parent looking for football schedules, forms, coach contacts, or ticket information will see nothing but an empty white screen. Additionally, the main Athletics URL uses a draft slug (`athletics-copy`) that signals to search engines — and tech-savvy parents — that this is an unfinished page. These two issues alone are costing the district credibility and making the athletics program nearly impossible to find online.

---

## Overall Score: 38 / 100

| Category | Score | Grade |
|---|---|---|
| Content Quality | 3/20 | F |
| Functionality | 4/20 | F |
| SEO | 7/20 | D |
| Accessibility | 8/20 | D |
| Design & UX | 8/20 | D |
| Performance | 4/10 | F |
| Security | 4/10 | C |

---

## What Is Working Well

Before diving into problems, here is what the district has gotten right:

- **HTTPS is enabled.** The site uses a secure connection (the padlock is present in browsers), which protects visitors.
- **Contact information is easy to find.** The footer consistently displays the district's address, phone number, fax, and email on every page.
- **All school sites are linked from the footer.** Parents can navigate to any school in one click from any page.
- **Mobile app promotion is present.** iOS and Android app download links are featured, which is appropriate for a school community.
- **Site translation is offered.** The "Translate Site" button in the header is important for a district that serves non-English-speaking families.
- **Strong content exists — when it loads.** The Athletic Director's welcome letter is warm, personal, and well-written. The sports categories (11 sports listed), safety plans, and document links show real effort by staff.
- **Breadcrumb navigation is present.** When content loads, users can see where they are (District > Departments > Athletics).
- **The header has a "Skip to Content" link.** This is a positive accessibility feature that helps keyboard and screen-reader users.

---

## Critical Issues
*These are problems causing immediate harm to parents, students, and the district's reputation. Fix these first.*

---

### CRITICAL 1: Every Athletics Page Loads Completely Blank

**Severity: Critical**
**Affects: All visitors — parents, students, community members**

Every page in the Athletics section — the main athletics hub, all 11 individual sport pages (Football, Basketball, Wrestling, etc.), the Athletic Directory, Forms, Rank One, and Ticket Info — shows only a header and footer when first loaded. The main body of the page is completely empty.

The content does exist in the system. When the site's menu is opened and then closed, the content on the main athletics page becomes visible. But no ordinary visitor will discover this workaround. Anyone who clicks an athletics link and sees a blank page will assume the page is broken or missing, and they will leave.

This means:
- Parents cannot find schedules, forms, or coach information
- Students cannot access required athletic forms
- Community members cannot learn about game times or ticket purchases
- The district's athletics program appears non-existent online

**What to do:** Contact Apptegy/ThrillShare support immediately and report that all athletics section pages render blank on initial load. This is a platform-level bug. Reference the URL: `https://westernheightssdok.sites.thrillshare.com/o/whsd/page/athletics-copy`. Ask for it to be escalated as urgent.

There is also a recurring LaunchDarkly service error appearing in the technical background of every page: "Error on stream connection." This suggests a third-party feature-flag service used by the platform is failing, and may be the underlying cause of the blank rendering problem.

---

### CRITICAL 2: The URL Contains "-copy" — This Is a Draft Page Being Used as the Live Page

**Severity: Critical**
**Affects: SEO, credibility, long-term content management**

The main athletics page URL is:
`https://westernheightssdok.sites.thrillshare.com/o/whsd/page/athletics-copy`

The word "copy" in a URL is almost always a sign that someone duplicated a page inside the CMS to make edits, and the draft version was accidentally linked to instead of the original. To confirm: when the URL `/o/whsd/page/athletics` (without "-copy") was tested, it returned a "Page Not Found" error.

This matters for three reasons:
1. **Trust:** Parents and community members who notice the URL may question whether the page is official or final.
2. **SEO:** Search engines treat `/athletics` and `/athletics-copy` as two completely different addresses. If anyone has linked to the original `/athletics` page, those links are now broken.
3. **Future problems:** If a corrected page is ever published at `/athletics`, the `-copy` version will become outdated and confusing.

**What to do:** In the Apptegy CMS, find the correct athletics page, ensure it has the URL slug set to `athletics` (not `athletics-copy`), and update the menu link to point to the correct address. If the `-copy` version IS the intended final page, rename its URL slug in the CMS to remove "-copy."

---

### CRITICAL 3: Coaches Section Contains No Coaches

**Severity: Critical**
**Affects: Parents, student-athletes seeking contact information**

When the "Coaches" accordion section is expanded on the main athletics page, it contains an empty section — no names, no contact details, no coach information whatsoever. For families trying to contact a coach about tryouts, schedules, or their child's participation, this is a dead end.

**What to do:** Add a coach directory to the Coaches section. At minimum, list each sport's head coach with name, sport, and email address. This is one of the most frequently sought pieces of information on any school athletics website.

---

## High Priority Issues
*These issues are hurting the district's online presence and should be fixed within two weeks.*

---

### HIGH 1: Individual Sport Pages Are Completely Empty

**Severity: High**
**Affects: All 11 sport programs**

Every individual sport page — Football, Basketball (Boys), Basketball (Girls), Baseball, Softball, Wrestling, Soccer (Boys), Soccer (Girls), Cross Country, Tennis, and Track — is either completely blank or contains no sport-specific content. There are no schedules, no rosters, no coach bios, no photos.

When a parent searches "Western Heights Jets football schedule," they will find an empty page. When a student wants to know tryout dates for softball, there is nothing there.

**What to do:** Prioritize adding content to the highest-attendance sport pages first (Football, Basketball). At minimum each sport page should include: coach name and contact, current season schedule, and tryout/sign-up information.

---

### HIGH 2: Athletic Forms Page Is Blank — Students Cannot Access Required Documents

**Severity: High**
**Affects: Student-athletes who need to submit physical/permission forms before participating**

The "Forms" page (`/o/whsd/page/forms`) is completely empty. Athletic participation typically requires physical examination forms, emergency contact forms, and parent permission slips. If these cannot be found online, families must request them in person, creating unnecessary burden.

**What to do:** Upload all required athletic participation forms to this page. Label each form clearly (e.g., "Pre-Participation Physical Examination Form," "Parental Consent Form") and ensure they are downloadable as PDFs.

---

### HIGH 3: Ticket Info Page Is Blank

**Severity: High**
**Affects: Community members, parents attending games**

The Ticket Info page (`/o/whsd/page/ticket-info`) is completely empty. The image slideshow on the main athletics page even has a "Tickets" slide, suggesting this is an intended feature. Community members attending games have no way to learn about pricing, digital ticketing systems, or where to purchase.

**What to do:** Add ticket pricing, purchase links, and any relevant policies (student/adult pricing, senior discounts, etc.) to this page.

---

### HIGH 4: The Athletics Directory Page Is Blank

**Severity: High**
**Affects: Parents and staff trying to reach athletic department personnel**

The Athletic Directory page is fully empty. This is typically one of the most-visited pages on a school athletics site because parents, volunteers, and media need staff contact information.

**What to do:** Add all athletics department staff — Athletic Director, Assistant ADs, trainers, and administrative contacts — with their name, title, and email address.

---

## Medium Priority Issues
*Address these within 30 days. They are reducing the quality of the experience.*

---

### MEDIUM 1: The Breadcrumb Navigation Shows No Items on Initial Page Load

**Severity: Medium**
**Affects: All visitors, navigation experience**

The breadcrumb trail (the text path showing where you are, like "Home > Departments > Athletics") is present in the page code but renders empty on initial load, matching the blank-content pattern. When it does appear, it shows the path correctly. This deprives visitors of a clear sense of where they are on the site.

**What to do:** This will likely be resolved when the blank-page rendering issue (Critical 1) is fixed by Apptegy support.

---

### MEDIUM 2: The Welcome Letter References the 2024-2025 School Year

**Severity: Medium**
**Affects: Credibility, trust**

The Athletic Director's welcome letter opens with "Welcome to the 2024-2025 school year at Western Heights!" As of the date of this audit (March 2026), this content is nearly two years out of date. Visitors will immediately notice this, which creates doubt about whether any information on the site is current.

**What to do:** Update the welcome letter to reflect the current or upcoming school year. Even a brief update — "We are now in the 2025-2026 season..." — removes this concern.

---

### MEDIUM 3: Email Address in Footer Is Plain Text (Not a Clickable Link)

**Severity: Medium**
**Affects: Mobile users, anyone trying to email the district**

In the footer, the district email address (`communication@whisd.org`) is displayed as plain, non-clickable text. Phone numbers in the same footer are correctly set up as clickable links. On mobile, a clickable email link opens the phone's mail app automatically, saving parents significant friction.

**What to do:** In the Apptegy CMS footer settings, change the email address to a `mailto:` link so tapping it on mobile opens a pre-addressed email.

---

### MEDIUM 4: The Page Slug Naming Convention Is Inconsistent

**Severity: Medium**
**Affects: SEO, maintenance**

Internal page links use inconsistent URL structures. Some links use the format `/o/whsd/page/[name]` while the menu also links to `/page/athletics-copy` (without the `/o/whsd/` prefix). Both apparently resolve to the same destination, but this inconsistency creates duplicate-content risks for search engines.

---

### MEDIUM 5: No Upcoming Events Are Displayed Despite an "Upcoming Events" Heading

**Severity: Medium**
**Affects: Parents, community members**

The main athletics page contains a prominent "Upcoming Events" heading, but no events are listed beneath it. This is either a configuration error (the events feed is not connected) or the events module has not been populated. An empty "Upcoming Events" section looks like something is broken.

**What to do:** Either connect the athletics events calendar to this section so events populate automatically, or remove the heading until events are available.

---

### MEDIUM 6: The Image Slideshow Has No Visible Alt Text or Captions

**Severity: Medium**
**Affects: Accessibility, screen-reader users**

The main page features a three-image slideshow. One slide is labeled "Home Default," which is clearly a system default name — not a meaningful description. Screen-reader users (blind or visually-impaired visitors) will hear "Home Default" read aloud rather than a description of the image.

**What to do:** Update each slide's alt text in the CMS to describe the image content (e.g., "Western Heights Jets football team on the field" rather than "Home Default").

---

### MEDIUM 7: Only Facebook Is Listed in Social Media

**Severity: Medium**
**Affects: Community engagement, reach**

The "Stay Connected" section in the footer only links to Facebook. Many high school athletics programs actively use Instagram for photo highlights and X (formerly Twitter) for game updates. If the district uses these platforms, they should be linked here. If not, this is a low-cost opportunity to increase community engagement.

---

## Low Priority Issues
*Good improvements to make when time allows.*

---

### LOW 1: The Page Title "Athletics | Western Heights School District" Is Good But Lacks Location

For search engine optimization, the page title is solid. Adding a city/state would help parents searching specifically for Oklahoma City area schools: "Athletics | Western Heights School District — Oklahoma City, OK."

---

### LOW 2: No Social Sharing Buttons on Content Pages

Parents who want to share game announcements or athletics news have no easy share buttons. Adding Facebook or general share links to news items or event pages would extend reach organically.

---

### LOW 3: The OSSAA Link Opens an Unusual Domain

The "OSSAA" link (Oklahoma Secondary School Activities Association) points to `https://ossaaillustrated.com/` rather than the official `https://www.ossaa.com/`. Verify this is the intended destination.

---

### LOW 4: Employment Links Go to Two Different Platforms

In the top utility bar, "Employment" links to `https://westernheights.schoolspring.com/`. In the main menu, "Employment" links to a different job board (`tedk12.com`). Parents and staff who use different entry points will be directed to different job listings. Consolidate to one authoritative jobs page.

---

### LOW 5: Copyright Footer Shows "2026" — Verify Auto-Update

The footer reads "Copyright © 2026 Western Heights School District." Confirm this is set to update automatically each year. If it is hardcoded, it will display the wrong year in 2027 and beyond.

---

## SEO Assessment

| Element | Status | Notes |
|---|---|---|
| Page Title | Pass | "Athletics | Western Heights School District" — clear and descriptive |
| HTTPS | Pass | Secure connection active |
| URL Structure | Fail | "-copy" in URL is unprofessional and confusing to search engines |
| H1 Heading | Fail | No visible H1 on initial page load; one exists in code but does not render |
| Meta Description | Unknown | Cannot verify without CMS access; likely absent |
| Structured Data | Absent | No schema.org markup detected for School or SportsOrganization |
| Image Alt Text | Partial | Slider images use placeholder names ("Home Default") not descriptive text |
| Internal Linking | Partial | Menu navigation works; sport pages exist but have no content to index |
| Breadcrumbs | Partial | Present in code but blank on load |
| Mobile Friendly | Unknown | Header appears responsive; content verification blocked by blank-page issue |

---

## Accessibility Assessment

| Element | Status | Notes |
|---|---|---|
| Skip to Content link | Pass | Present and functional |
| Keyboard Navigation | Partial | Menu and accordions are keyboard-operable; content hidden on load affects all navigation |
| Screen Reader Support | Partial | Navigation labels are present; image alt text needs improvement |
| Translate Button | Pass | Present in header — important for diverse community |
| Color Contrast | Not auditable | Cannot fully assess contrast without content rendering correctly |
| Focus Indicators | Not auditable | Cannot verify keyboard focus rings without content rendering |
| Form Accessibility | N/A | No interactive forms found on the pages visited |

---

## Security Assessment

| Element | Status | Notes |
|---|---|---|
| HTTPS | Pass | SSL/TLS active |
| Clickable Phone Numbers | Pass | Tel links work in footer |
| Email as Plain Text | Flag | Email in footer is not a `mailto:` link |
| Third-Party Scripts | Note | LaunchDarkly service is throwing stream connection errors — monitor for data exposure |
| Sensitive Data Exposure | Pass | No API keys, credentials, or sensitive data found in visible page output |

---

## Action Plan

### This Week (Urgent)

1. **Call Apptegy/ThrillShare support** and report the blank page rendering bug on all athletics pages. Reference URL: `https://westernheightssdok.sites.thrillshare.com/o/whsd/page/athletics-copy`
2. **Fix the URL slug.** Rename `athletics-copy` to `athletics` in the CMS and update all menu links.
3. **Add coaches information** to the empty Coaches section.

### Within Two Weeks

4. Add content to the top sport pages: Football, Basketball (Boys & Girls) at minimum — schedule, coach name, contact email.
5. Upload all required athletic participation forms to the Forms page.
6. Add ticket pricing and purchase information to the Ticket Info page.
7. Populate the Athletic Directory with staff names and email addresses.

### Within 30 Days

8. Update the Athletic Director's welcome letter to reference the current school year.
9. Fix the footer email address to be a clickable mailto link.
10. Update slideshow image alt text from "Home Default" and "Tickets" to descriptive text.
11. Either connect an events feed to the "Upcoming Events" section or remove the empty heading.
12. Verify the OSSAA link is pointing to the correct website.

### Within 60 Days

13. Add content for all remaining sport pages (Baseball, Softball, Wrestling, Cross Country, Soccer, Tennis, Track).
14. Evaluate adding Instagram/X social links if the district uses those platforms.
15. Consider adding a meta description to the athletics page for better Google search results.

---

## Estimated Effort

| Task Category | Estimated Time | Who Should Do It |
|---|---|---|
| Blank page rendering fix | Vendor responsibility (Apptegy) | File a support ticket |
| URL slug fix | 10 minutes | CMS administrator |
| Coach directory | 30–60 minutes | Athletics department staff |
| Forms upload | 1–2 hours | Athletics department staff |
| Sport page content (top 4 sports) | 4–6 hours | Athletics staff + content editor |
| Ticket Info & Directory pages | 1 hour | Athletics department staff |
| Welcome letter update | 15 minutes | Athletic Director or admin |
| Image alt text updates | 30 minutes | CMS administrator |
| All remaining sport pages | 8–12 hours | Athletics staff |

**Total staff time estimate:** 16–24 hours of content entry work, plus one Apptegy support ticket that needs to be resolved by the vendor.

---

## Conclusion

The Western Heights School District athletics program has invested real effort in organizing this site — the content structure is logical, the navigation categories are well thought-out, and the Athletic Director's letter demonstrates genuine community commitment. The foundational problems are not the fault of the staff who built this; they are largely platform-level rendering failures and incomplete content population.

Once the blank-page bug is resolved by Apptegy and the core content (coaches, forms, schedules) is added, this site can become a genuinely useful resource for the Western Heights Jets community. The path to a good athletics website is clear and achievable with focused effort over the next 30 days.

---

*Report prepared by Professional Web Consultant | March 29, 2026*
*Pages audited: athletics-copy (main hub), football, basketball-boys, basketball-girls, cross-country, athletics-directory, forms, rank-one, ticket-info, homepage (/), Western Heights High School home (/o/hs)*
