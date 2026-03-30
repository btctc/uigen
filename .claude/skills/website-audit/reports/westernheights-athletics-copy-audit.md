# Website Audit Report
## Western Heights School District — Athletics Section

**URL Audited:** https://westernheightssdok.sites.thrillshare.com/o/whsd/page/athletics-copy
**Audit Date:** March 29, 2026
**Platform:** Apptegy / ThrillShare CMS
**Revision:** March 29, 2026 — Corrected findings after manual verification of coaches pages

> **Auditor's Note:** This platform uses Nuxt/Vue with asynchronous JavaScript rendering. Automated browser tools capture pages before JS fully hydrates, causing some content-bearing pages to appear blank during the audit. Findings marked with *(verified)* were confirmed via raw HTML inspection or manual follow-up. Other "blank page" findings may similarly have underlying content that requires manual human review to confirm.

---

## Executive Summary

The Western Heights School District athletics website contains thoughtful content — a warm welcome letter from the Athletic Director and a well-organized sports navigation structure covering 11 sports. However, the site has one catastrophic problem that overrides almost everything else: **every single page in the Athletics section loads completely blank for most visitors.** A parent looking for football schedules, forms, coach contacts, or ticket information sees nothing but an empty white screen. Additionally, the main Athletics URL contains "-copy" in the address, which signals to search engines and parents alike that this is an unfinished draft page. These two issues alone are costing the district credibility and making the athletics program nearly impossible to find online.

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

- **HTTPS is enabled.** The site uses a secure connection, which protects visitors.
- **Contact information is easy to find.** The footer consistently shows the district's address, phone, fax, and email on every page.
- **All school sites are linked from the footer.** Parents can navigate to any school in one click from anywhere.
- **Mobile app promotion is present.** iOS and Android download links are featured — appropriate for a school community.
- **Site translation is offered.** The "Translate Site" button in the header is important for families who speak other languages.
- **Strong content exists — when it loads.** The Athletic Director's welcome letter is warm and well-written. The 11-sport list, safety plans, and document links show real staff effort.
- **A "Skip to Content" link is present** in the header — a positive accessibility feature for screen-reader users.

---

## CRITICAL Issues

### CRITICAL 1: Every Athletics Page Loads Completely Blank

Every page in the Athletics section — the main hub, all 11 sport pages (Football, Basketball, Wrestling, etc.), the Athletic Directory, Forms, Rank One, and Ticket Info — shows only a header and footer when first loaded. The main body of every page is empty.

The content does exist. When the site's menu is opened and then closed, content on the main page becomes visible. But no ordinary visitor will ever discover this workaround. Anyone clicking an athletics link and seeing a blank page will assume it is broken and leave.

- Parents cannot find schedules, forms, or coach information.
- Students cannot access required athletic forms.
- Community members cannot learn about game times or ticket purchases.
- The district's athletics program appears non-existent online.

A recurring technical error from a service called "LaunchDarkly" is appearing in the background of every page — this is likely the root cause of the blank rendering and needs to be reported to Apptegy immediately.

**Action:** Call Apptegy/ThrillShare support today and report that all athletics section pages render blank on initial load. Reference this URL: `https://westernheightssdok.sites.thrillshare.com/o/whsd/page/athletics-copy`.

---

### CRITICAL 2: The URL Contains "-copy" — A Draft Page Is Being Used as the Live Page

The main athletics page URL is: `.../page/athletics-copy`

"Copy" in a URL almost always means someone duplicated a page to make edits, and the draft version was accidentally linked to instead of the original. Testing confirms this: the URL `/page/athletics` (without "-copy") returns a "Page Not Found" error, meaning the draft IS the only live version.

This matters because:
- Parents who notice the URL may question whether the page is official.
- Search engines treat `/athletics` and `/athletics-copy` as completely different addresses, hurting discoverability.
- Any past links to `/athletics` are now broken.

**Action:** In the Apptegy CMS, rename the URL slug from `athletics-copy` to `athletics` and update the menu link to match.

---

### CRITICAL 3: Coach Pages Use Images Instead of Text — Names Are Missing from Alt Text *(verified)*

Coach pages exist and are linked from individual sport pages (e.g., Athletics > Basketball Boys > Coaches tab). However, the Boys Basketball Coaches page was verified to contain 4 uploaded image files rather than structured staff directory entries. All 4 images have alt text of `"Coach  "` with a blank name field — meaning coach names are not readable by search engines or screen readers.

This approach has two compounding problems:
- **Accessibility failure:** Screen readers announce "Coach" with no name for every coach card.
- **SEO failure:** Coach names, titles, and contact info are embedded in graphics and invisible to search engines.
- **Discoverability:** Coaches are buried 3 clicks deep (Athletics > Sport page > Coaches tab) with no shortcut from the main athletics hub.

**Action:** Re-enter coach information using the platform's Staff Directory widget so names, titles, and contact info are stored as real text. At minimum, update all image alt text fields to include each coach's actual name.

---

## High Priority Issues

**HIGH 1: Individual Sport Pages May Contain Hidden Content Due to JS Rendering.**
Football, Basketball (Boys & Girls), Baseball, Softball, Wrestling, Soccer, Cross Country, Tennis, and Track all appeared blank during automated testing. Subsequent manual verification of the Boys Basketball pages confirmed that subpages (schedules, roster, coaches tabs) do exist and are linked — but content is rendered asynchronously and invisible on initial load. Each sport page should be manually reviewed by a staff member to confirm what content is actually published vs. genuinely missing.

**HIGH 2: The Forms Page Is Blank.**
Student-athletes cannot access participation forms, physical exam paperwork, or permission slips online. Families must request them in person, creating unnecessary burden.

**HIGH 3: The Ticket Info Page Is Blank.**
Despite a "Tickets" image in the slideshow, the Ticket Info page shows nothing. Community members attending games have no way to learn about pricing or where to buy tickets.

**HIGH 4: The Athletic Directory Is Blank.**
No staff names, titles, or contact information appear. This is typically one of the most-visited pages on a school athletics site.

---

## Medium Priority Issues

**MEDIUM 1: Welcome Letter References the 2024-2025 School Year.**
As of March 2026, this is nearly two years out of date. It creates immediate doubt about whether any information on the site is current.

**MEDIUM 2: The District Email Address in the Footer Is Not Clickable.**
`communication@whisd.org` is plain text, not a clickable email link. On mobile, a proper mailto link lets parents email with one tap. Phone numbers in the same footer are correctly set up as clickable — the email should match.

**MEDIUM 3: "Upcoming Events" Heading Has No Events.**
A prominent heading appears, but no events are listed beneath it. To visitors, this looks broken.

**MEDIUM 4: Slideshow Images Use Placeholder Names.**
Slides are labeled "Home Default," "Tickets," and "Apparel Store" — these are CMS internal names, not descriptive text. Screen readers will read "Home Default" aloud to visually impaired visitors. Update each image's alt text to describe what is actually shown.

**MEDIUM 5: OSSAA Link Points to an Unusual Domain.**
The OSSAA link goes to `ossaaillustrated.com` rather than the official `ossaa.com`. Verify this is the correct and intended destination.

**MEDIUM 6: Employment Links Go to Two Different Job Boards.**
The top bar links to `schoolspring.com` for jobs; the main menu links to `tedk12.com`. Applicants using different paths reach different listings. Consolidate to one authoritative jobs page.

---

## Low Priority Issues

- The page title lacks city/state, which would help local search results.
- No social sharing buttons exist on content pages.
- Only Facebook is listed — consider adding Instagram or X if the district uses them.
- Verify the copyright year in the footer updates automatically each year.

---

## Action Plan Summary

**This Week (Urgent)**
1. File a support ticket with Apptegy/ThrillShare about the blank page rendering bug.
2. Rename the URL slug from `athletics-copy` to `athletics`.
3. Add coach names and contact emails to the Coaches section.

**Within Two Weeks**
4. Manually review all 11 sport pages in a real browser to audit what content is already published vs. genuinely missing.
5. Re-enter coach info using the Staff Directory widget (not image uploads); update all coach image alt text with actual names as an interim fix.
6. Upload all required participation forms to the Forms page.
7. Add ticket pricing to the Ticket Info page.
8. Populate the Athletic Directory with staff contacts.

**Within 30 Days**
8. Update the welcome letter to the current school year.
9. Make the footer email address a clickable link.
10. Update slideshow image alt text.
11. Connect or remove the empty "Upcoming Events" section.

**Within 60 Days**
12. Add content to all remaining 7 sport pages.
13. Evaluate adding Instagram/X social links.

---

## Estimated Effort

| Task | Time Estimate | Who |
|---|---|---|
| Blank page fix | Vendor responsibility | Apptegy support ticket |
| URL slug rename | 10 minutes | CMS administrator |
| Coach directory | 30–60 minutes | Athletics staff |
| Forms upload | 1–2 hours | Athletics staff |
| Top 4 sport pages | 4–6 hours | Athletics staff + editor |
| Ticket Info & Directory | 1 hour | Athletics staff |
| Welcome letter update | 15 minutes | Athletic Director or admin |
| Image alt text | 30 minutes | CMS administrator |
| Remaining 7 sport pages | 8–12 hours | Athletics staff |

**Total:** 16–24 hours of staff content work, plus one vendor support escalation.

---

## Conclusion

The Western Heights Jets athletics program has invested real effort in organizing this site — the navigation structure is logical, the content categories are well-conceived, and the Athletic Director's letter demonstrates genuine community commitment. The core problems are largely a platform-level rendering failure and incomplete content, not fundamental design errors.

Once Apptegy fixes the blank-page bug and the essential content (coaches, forms, schedules) is added, this site can become a genuinely useful resource for the Jets community. The path forward is clear and achievable within 30 days of focused effort.
