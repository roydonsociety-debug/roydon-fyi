#!/usr/bin/env python3
"""
roydon.fyi site builder.
Generates all static HTML pages from a single source of truth.
Run once: python3 build.py
"""
import os
from pathlib import Path
from datetime import date

SITE_DIR = Path(__file__).parent

# ============================================================
# Shared header / footer
# ============================================================

NAV_ITEMS = [
    ('home', '/', 'Home'),
    ('temple-farm', '/temple-farm/', 'Temple Farm'),
    ('act', '/act/', 'Take Action'),
    ('about', '/about/', 'About'),
    ('contact', '/contact/', 'Contact'),
]

ISSUE_DATE = "15 May 2026"

def head(title, description=""):
    desc = description or "Information for residents of Roydon, Essex. Planning, conservation, and community matters."
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · roydon.fyi</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<link rel="stylesheet" href="/css/styles.css">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22 font-family=%22Georgia%22 fill=%22%232D4A2B%22>r</text></svg>">
</head>
<body>
"""

def masthead(active):
    nav_html = '\n      '.join(
        f'<a href="{href}" class="{"active" if key == active else ""}">{label}</a>'
        for key, href, label in NAV_ITEMS
    )
    return f"""<header class="masthead">
  <div class="masthead-inner">
    <div>
      <a href="/" class="wordmark">roydon<span class="dot">.</span><span class="tld">fyi</span></a>
      <span class="subtitle">Information for residents of Roydon, Essex</span>
    </div>
    <nav class="primary">
      {nav_html}
    </nav>
  </div>
</header>
"""

def footer():
    return f"""<footer class="site-footer">
  <div class="inner">
    <div>
      <h4>About this site</h4>
      <p>roydon.fyi is an information portal for residents of Roydon, Essex. It publishes briefings, evidence, and ways to engage with the planning process on local matters.</p>
      <p>Published by <strong>Friends of Roydon</strong>, an unincorporated residents' association.</p>
    </div>
    <div>
      <h4>Pages</h4>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/temple-farm/">Temple Farm</a></li>
        <li><a href="/act/">Take Action</a></li>
        <li><a href="/downloads/">Downloads</a></li>
        <li><a href="/about/">About</a></li>
        <li><a href="/contact/">Contact</a></li>
        <li><a href="/privacy/">Privacy</a></li>
      </ul>
    </div>
    <div>
      <h4>Contact</h4>
      <p><a href="mailto:roydonsociety@gmail.com">roydonsociety@gmail.com</a></p>
      <p class="small">Replies usually within a few days. Run by volunteers.</p>
    </div>
  </div>
  <div class="colophon">
    Set in Fraunces and Manrope. Hosted on Cloudflare Pages. No tracking, no ads, no cookies.
  </div>
</footer>
</body>
</html>"""

def page(title, active, content, description=""):
    return head(title, description) + masthead(active) + content + footer()

def issue_line(left, right=None):
    right = right or f"Updated {ISSUE_DATE}"
    return f'<div class="issue-line"><span>{left}</span><span class="right">{right}</span></div>'

# ============================================================
# Page contents
# ============================================================

PAGES = {}

# -----------------------------------------------
# HOMEPAGE
# -----------------------------------------------
PAGES['index.html'] = page("Home", "home", f"""
<main>
  {issue_line("Volume I · No. 1", f"Published {ISSUE_DATE}")}

  <div class="reading">
    <h1>An information hub for the village of <em>Roydon</em>.</h1>
    <p class="dek">Planning, conservation, and community matters, set out plainly. Currently focused on the proposed development at Temple Farm.</p>
  </div>

  <div class="counter-row">
    <div class="counter">
      <span class="num">3</span>
      <span class="label">Briefings published</span>
    </div>
    <div class="counter">
      <span class="num">5</span>
      <span class="label">Statutory bodies engaged</span>
    </div>
    <div class="counter">
      <span class="num">2026</span>
      <span class="label">Promotion agreement expiry</span>
    </div>
  </div>

  <h2 class="no-rule">Currently in focus</h2>

  <div class="grid-2">
    <a class="tile" href="/temple-farm/">
      <span class="meta">The campaign</span>
      <h3>Temple Farm</h3>
      <p>Dandara Homes has stated an intention to apply for outline planning permission for 200&ndash;250 homes on 70 acres of pasture inside the Lee Valley Regional Park. Archaeological evaluation was observed on site in April and May 2026.</p>
      <span class="arrow">Read the briefing →</span>
    </a>
    <a class="tile" href="/act/">
      <span class="meta">How you can engage</span>
      <h3>Take action</h3>
      <p>Pre-drafted emails to the Lee Valley Regional Park Authority, Natural England, the constituency MP, and Roydon Parish Council. One click opens your mail client with the message ready to send. Personalise the first line and send.</p>
      <span class="arrow">See the templates →</span>
    </a>
  </div>

  <h2>The case in three lines</h2>

  <div class="reading">
    <p>The Temple Farm pasture sits inside the statutory boundary of the Lee Valley Regional Park (protected by Act of Parliament, 1966), within the Impact Risk Zone for the Lee Valley SSSI, and adjacent to the Grade I listed St Peter&rsquo;s Church and the Grade II listed Temple Farmhouse within the Roydon Conservation Area.</p>
    <p>A Planning Inspector dismissed a much smaller scheme on this exact land in July 2022 (appeal reference APP/J1535/W/21/3275842), applying the &ldquo;footnote 7&rdquo; carve-out under the NPPF. A second Inspector applied the same mechanism to a different site in the Roydon Conservation Area fourteen months later.</p>
    <p>The site was not allocated for housing in the Local Plan adopted in March 2023. Today the Frederick family remain the registered freeholders. Dandara holds a Promotion Agreement dated 17 May 2016 over the pasture only, recorded as extended to 2026 in the April 2023 Savills sales brochure.</p>
  </div>

  <div class="btn-row">
    <a href="/temple-farm/briefing/" class="btn primary">Read the full briefing</a>
    <a href="/temple-farm/the-case/" class="btn">The case in plain English</a>
  </div>

  <h2>Latest entries</h2>

  <div class="timeline-entry">
    <div class="date-col">15 May 2026</div>
    <div>
      <h3>Five emails sent to statutory bodies and the MP</h3>
      <p>Correspondence opened with Roydon Parish Council, Essex County Council Place Services Archaeology, the Lee Valley Regional Park Authority, Natural England, and Chris Vince MP. Replies expected over the coming two to three weeks.</p>
    </div>
  </div>

  <div class="timeline-entry">
    <div class="date-col">13 May 2026</div>
    <div>
      <h3>HMLR title register obtained for EX311401</h3>
      <p>The current state of the principal Temple Farm title is now on file. All material facts in the published briefings are confirmed by the register.</p>
    </div>
  </div>

  <div class="timeline-entry">
    <div class="date-col">May 2026</div>
    <div>
      <h3>Archaeological evaluation observed on site</h3>
      <p>Colchester Archaeological Trust on site, evaluation trenches across the pasture. Consistent with pre-application work paid for by a developer six to twelve months before a planning application is lodged.</p>
    </div>
  </div>

  <p class="text-center mt-6"><a href="/temple-farm/timeline/" class="btn">Full timeline</a></p>

</main>
""", "Information for residents of Roydon, Essex. The Temple Farm planning briefing, evidence, and ways to engage.")


# -----------------------------------------------
# TEMPLE FARM HUB
# -----------------------------------------------
PAGES['temple-farm/index.html'] = page("Temple Farm", "temple-farm", f"""
<main>
  {issue_line("File · Temple Farm")}

  <div class="reading">
    <span class="kicker">Pre-application stage</span>
    <h1>Temple Farm, <em>Roydon</em></h1>
    <p class="dek">A 70-acre pasture on the western edge of Roydon, currently the subject of a Promotion Agreement between the Frederick family and Dandara. Pre-application work observed on site in April and May 2026.</p>
  </div>

  <div class="grid-2">
    <a class="tile" href="/temple-farm/briefing/">
      <span class="meta">The briefing</span>
      <h3>Residents&rsquo; briefing</h3>
      <p>The plain-English version of the case. About 1,500 words. Read on the page or download as PDF.</p>
      <span class="arrow">Read it →</span>
    </a>
    <a class="tile" href="/temple-farm/the-case/">
      <span class="meta">For sharing</span>
      <h3>The case in plain English</h3>
      <p>The argument distilled to 800 words. No jargon. The version to send to a neighbour on WhatsApp.</p>
      <span class="arrow">Read it →</span>
    </a>
    <a class="tile" href="/temple-farm/timeline/">
      <span class="meta">Public record</span>
      <h3>Timeline</h3>
      <p>Dated entries from the 2016 Promotion Agreement through the 2022 appeal dismissal to the present. What has happened, when, and what it means.</p>
      <span class="arrow">View →</span>
    </a>
    <a class="tile" href="/temple-farm/evidence/">
      <span class="meta">Source documents</span>
      <h3>Evidence file</h3>
      <p>HMLR title numbers, the 2022 appeal decision, the adopted Local Plan, the Lee Valley Regional Park Act 1966, the Roydon Conservation Area appraisal. All linked.</p>
      <span class="arrow">View →</span>
    </a>
  </div>

  <h2>Status</h2>
  <div class="panel note reading">
    <h3>As at {ISSUE_DATE}</h3>
    <p>The Frederick family remain registered freeholders. The 2023 Savills informal tender did not produce a completed sale on the main land holding. The Dandara Promotion Agreement (17 May 2016, with a 2021 extension to 2026 recorded in the April 2023 Savills brochure) remains in place and is registered against the land.</p>
    <p>In May 2026 Roydon Parish Council published a notice confirming that Dandara Homes has formally approached the Council stating an intention to apply for outline planning permission for 200 to 250 homes. Archaeological evaluation was observed on site over April and May 2026.</p>
    <p>No planning application has been lodged at the time of writing. The pre-application phase is typically six to twelve months long.</p>
  </div>

  <h2>Take action now</h2>
  <div class="reading">
    <p>Five organisations are worth writing to at the pre-application stage, before any application is formally lodged. Pre-drafted emails are on the action pages, each with several variants so messages aren&rsquo;t identical.</p>
  </div>
  <div class="btn-row">
    <a href="/act/" class="btn primary">See the action templates</a>
    <a href="/act/register/" class="btn">Register your concern</a>
  </div>

</main>
""")


# -----------------------------------------------
# BRIEFING PAGE (web version of residents' briefing)
# -----------------------------------------------
PAGES['temple-farm/briefing/index.html'] = page("Residents&rsquo; briefing", "temple-farm", f"""
<main>
  {issue_line("File · Temple Farm · Residents&rsquo; briefing")}

  <div class="reading">
    <span class="kicker">Briefing</span>
    <h1>Temple Farm, <em>Roydon</em></h1>
    <p class="dek">A short briefing for Roydon residents on the proposed development at Temple Farm. Updated {ISSUE_DATE}.</p>

    <div class="btn-row">
      <a href="/downloads/temple-farm-residents-briefing-v2.docx" class="btn">Download as Word document</a>
      <a href="/temple-farm/the-case/" class="btn">Shorter version (800 words)</a>
    </div>

    <h2 class="no-rule">1. What is happening</h2>
    <p class="dropcap">Temple Farm is approximately 70 acres of pasture on the western edge of Roydon village, owned by the Frederick family. Dandara, a national housebuilder, has held a Promotion Agreement over the pasture since May 2016. That agreement is recorded on the public title register and was extended in 2021 for a further five years, taking it to 2026.</p>
    <p>Pre-application activity stepped up sharply in early 2026. On 20 January 2026 Roydon Parish Council confirmed that Dandara Homes (Dandara&rsquo;s housebuilder arm) was planning a public consultation at St Peter&rsquo;s Church Hall in February and would brief Members privately before the 5 February Parish Council meeting. Dandara then postponed that private briefing on 29 January 2026 without giving reasons. The Council&rsquo;s own written summary on 7 February 2026 (&ldquo;Housing development in the Parish of Roydon&rdquo;) confirmed the scheme is for &ldquo;between 200 and 250 new homes on a 70-acre site&rdquo; and that Dandara had advised of &ldquo;delays in creating their Masterplan.&rdquo; By May 2026 the Council&rsquo;s Latest News page &ldquo;Temple Farm Housing Development Plans&rdquo; confirmed Dandara&rsquo;s formal approach and stated intention to apply for outline planning permission. Pre-application archaeological work by Colchester Archaeological Trust was also observed on the pasture in May 2026. This kind of work is paid for by developers six to twelve months before they submit a planning application.</p>

    <h2>2. What we know about the land and the agreement</h2>
    <p>The Promotion Agreement with the Frederick family is dated 17 May 2016 (confirmed on the public title register). The Savills marketing brochure from 2023 confirms it was extended in 2021 for a further five years, taking it to 2026. The agreement covers the pasture only, not the farm buildings or the family&rsquo;s homes. Dandara needs to submit a planning application or otherwise act soon before it loses its position over the pasture. That is why we are seeing pre-application work happening now.</p>
    <p>The land was offered for sale by Savills by informal tender in June 2023. It did not sell. The reasons it did not sell are useful context: the marketing required any buyer to lease the land back to the family for ten years, and to give the family 40 percent of any future planning uplift for 25 years. Those terms made the land unattractive to anyone other than a buyer already lined up with Dandara.</p>

    <h2>3. Why the site is protected</h2>
    <p>Temple Farm sits inside several overlapping protections, not just the standard Green Belt designation. Each is worth knowing about because each operates independently.</p>

    <h3>Inside the Lee Valley Regional Park</h3>
    <p>The Park was created by an Act of Parliament in 1966. The Act gives the Park a statutory purpose: a regional park for recreation, sport, entertainment, and as a nature reserve. The Lee Valley Regional Park Authority has a statutory duty to manage the Park for those purposes. The Temple Farm pasture sits firmly inside the Park boundary on the District Council&rsquo;s own constraints map. Residential development at the scale proposed is plainly inconsistent with the Park&rsquo;s statutory purpose.</p>

    <h3>Wildlife protections</h3>
    <p>The site falls inside the Impact Risk Zone for the Lee Valley Site of Special Scientific Interest. That triggers a mandatory consultation with Natural England on any planning application of this kind. Separately, traffic from a 250-home development engages the Epping Forest Special Area of Conservation through vehicle emissions. This was confirmed by a Planning Inspector in an earlier appeal on this exact land (Wyatt 2022, dismissing five dwellings).</p>

    <h3>Heritage and Conservation Area</h3>
    <p>The site is adjacent to St Peter&rsquo;s Church, which is Grade I listed (the highest grade in the English system, reserved for buildings of exceptional national interest). It is in the immediate setting of Temple Farmhouse, Grade II listed. It is also inside the Roydon Conservation Area, which has been formally designated for its historic and architectural character.</p>

    <h3>Flood Risk</h3>
    <p>Much of the site sits within Environment Agency Flood Zones 2 and 3. The adopted Local Plan (Policy P9(E)) explicitly excludes Roydon allocations on flood-risk grounds.</p>

    <h2>4. Planning history</h2>
    <p>This site has already been to a Planning Inspector once. In July 2022 Inspector S J Wyatt dismissed an appeal by the landowner herself against the refusal of just five dwellings on this same land (appeal reference APP/J1535/W/21/3275842). The Inspector applied the &ldquo;footnote 7&rdquo; carve-out in the National Planning Policy Framework: the protections at the site are strong enough to dis-apply the usual presumption in favour of sustainable development.</p>
    <p>Fourteen months later, in September 2023, a different Inspector applied the same mechanism to a different site within the same Roydon Conservation Area (Hughes 2023, Old Coal Yard). Two Inspectors, two sites, the same mechanism, the same outcome. The reliability of this protection in Roydon does not rest on a single decision.</p>
    <p>The site was not allocated for housing in the Local Plan adopted by the District Council in March 2023. The Council&rsquo;s own published evidence base assessed and rejected it.</p>

    <h2>5. The grey belt question</h2>
    <p>The Government changed the National Planning Policy Framework in December 2024 to introduce a new category called &ldquo;grey belt&rdquo; — Green Belt land that may be released for development where certain conditions are met. Some commentary on Roydon has assumed that this changes everything.</p>
    <p>It does not. The grey belt provisions explicitly preserve the &ldquo;footnote 7&rdquo; protections that defeated the 2022 appeal. Heritage harm, ecological designations, and flood risk all continue to operate as carve-outs that take a site out of grey belt and dis-apply the presumption in favour of release. Temple Farm engages all three of those carve-outs. The 2022 Inspector and the 2023 Inspector both applied exactly the mechanism that grey belt preserves.</p>

    <h2>6. What this means in practice</h2>
    <p>An application for 200 to 250 homes at Temple Farm faces a high evidential bar that Dandara have to clear. The body of evidence that already exists — two appeal decisions, the adopted Local Plan, the constraints map, the statutory protections — sits against them. The pre-application work being done now is essentially Dandara&rsquo;s attempt to design around those constraints.</p>
    <p>None of this is guaranteed. The planning system is not infallible. But the protections are real and they are robust to recent policy changes. The risk to the village is highest if an application is lodged and residents are unprepared for the 21-day consultation window. The risk is lowest if the statutory consultees are alert, the Parish Council&rsquo;s formal response is ready, and individual residents have a clear path to lodge their own representations.</p>

    <h2>7. What residents can do now</h2>
    <p>Six things help, in roughly descending order of usefulness:</p>
    <ol>
      <li>Email the Lee Valley Regional Park Authority. They have a statutory interest in this site and their position carries weight with the District Council. <a href="/act/lvrpa/">Pre-drafted email</a>.</li>
      <li>Email Natural England. The SSSI Impact Risk Zone and the Epping Forest SAC both trigger their interest. <a href="/act/natural-england/">Pre-drafted email</a>.</li>
      <li>Email Chris Vince MP. The constituency MP can write to the District Council and the Secretary of State. <a href="/act/mp/">Pre-drafted email</a>.</li>
      <li>Support the Parish Council&rsquo;s position. Let the Clerk know you back a strong Parish response. <a href="/act/parish/">Pre-drafted email</a>.</li>
      <li>Register your concern. The list of named residents is what makes formal representations weighty at the planning stage. <a href="/act/register/">Register</a>.</li>
      <li>Watch for the planning application. Sign up for an email alert through this site so you know within 24 hours of an application being lodged.</li>
    </ol>

    <h2>8. Sources</h2>
    <p class="smaller">Roydon Parish Council Latest News page, &ldquo;Temple Farm Housing Development Plans&rdquo; (May 2026). HMLR title register for EX311401, accessed 13 May 2026. Savills informal tender brochure, April 2023. Adopted Epping Forest Local Plan, March 2023. Planning Inspectorate appeal decision APP/J1535/W/21/3275842 (Wyatt, 2022). Planning Inspectorate appeal decision APP/J1535/W/22/3303841 (Hughes, 2023). Lee Valley Regional Park Act 1966, Section 12. National Planning Policy Framework, December 2024 revision. EFDC constraints map.</p>

  </div>
</main>
""")


# -----------------------------------------------
# THE CASE (plain English short version)
# -----------------------------------------------
PAGES['temple-farm/the-case/index.html'] = page("The case", "temple-farm", f"""
<main>
  {issue_line("File · Temple Farm · The case")}

  <div class="reading">
    <span class="kicker">800 words · plain English</span>
    <h1>Why Temple Farm should not be built on</h1>
    <p class="dek">The argument in 800 words, with no jargon and no planning references. If you only read one thing on this site, read this.</p>

    <h2 class="no-rule">It&rsquo;s protected by law</h2>
    <p>Temple Farm sits inside the Lee Valley Regional Park, which was created by an Act of Parliament in 1966 specifically to protect this corridor for recreation, sport, and nature. The Park has a statutory authority responsible for keeping it that way. A 250-home estate built inside it is plainly at odds with the purpose Parliament gave it.</p>

    <h2>It floods</h2>
    <p>Large parts of the pasture sit inside the Environment Agency&rsquo;s flood zones. The District Council&rsquo;s own adopted plan from March 2023 explicitly rules out allocating land in Roydon for housing on flood-risk grounds. Building on it does not change the water.</p>

    <h2>The listed buildings would be damaged</h2>
    <p>The site is next to St Peter&rsquo;s Church, which is Grade I listed — the very highest grade in the English heritage system, the same grade as Windsor Castle. It is in the setting of Temple Farmhouse, also listed. It is inside the Roydon Conservation Area. None of those things can be moved out of the way of a housing estate.</p>

    <h2>The wildlife protections engage</h2>
    <p>The pasture is inside a designated Impact Risk Zone for the Lee Valley Site of Special Scientific Interest, which means any housing application of this scale automatically triggers a consultation with Natural England. Separately, the additional traffic that 250 homes would generate engages the Epping Forest Special Area of Conservation through vehicle emissions, as a Planning Inspector confirmed in 2022.</p>

    <h2>A Planning Inspector has already said no</h2>
    <p>In July 2022 the landowner herself applied for permission to build just five houses on this exact land. The District Council refused. She appealed. The independent Planning Inspector dismissed her appeal. The Inspector&rsquo;s reasons are public and they apply with even greater force to a scheme fifty times larger.</p>
    <p>Fourteen months later, in September 2023, a different Inspector dismissed an appeal for seven houses on a different site inside the Roydon Conservation Area, using exactly the same legal mechanism. Two Inspectors, two refusals, the same reasoning. This is not a one-off.</p>

    <h2>It is not in the plan</h2>
    <p>The District Council adopted its current Local Plan in March 2023. The plan is the document that says where housing should go in the district over the next 15 years. The plan does not allocate Temple Farm for housing. The Council looked at it, weighed it against the other available sites, and decided no.</p>

    <h2>The infrastructure can&rsquo;t cope</h2>
    <p>Most of us know what happens to the level crossing at peak hours, what the school capacity already looks like, and how quickly the medical practice fills up. None of that gets better with 600 additional residents arriving over two or three years. The strategic infrastructure case has not been made.</p>

    <h2>The agreement is on a clock</h2>
    <p>Dandara is moving now because their Promotion Agreement with the Frederick family expires this year. They have until the end of 2026 to lodge an application and progress it, or they lose their position. That timing pressure is theirs, not the village&rsquo;s. There is no reason for the village to react to their deadline.</p>

    <h2>What &ldquo;grey belt&rdquo; means and doesn&rsquo;t mean</h2>
    <p>The Government changed national planning rules in December 2024 to introduce something called &ldquo;grey belt&rdquo; — Green Belt land that may be released for housing. Some have assumed that Temple Farm is now fair game. It is not. The grey belt rules preserve all the heritage, ecological, and flood-risk protections that defeated the 2022 appeal. Temple Farm engages all three. The mechanism that protected it before still works.</p>

    <h2>What you can do</h2>
    <p>The single most useful thing residents can do at this stage is make their concern visible to the statutory bodies before any application is lodged. <a href="/act/">Pre-drafted emails</a> to the Lee Valley Park Authority, Natural England, the constituency MP, and the Parish Council are available on this site. Each takes about 60 seconds to send. The more inboxes the application has to reckon with, the better the village&rsquo;s chances.</p>

    <p class="smaller"><a href="/temple-farm/briefing/">The longer version of this case is also available</a>, with full references and the detail of the planning law that underpins it.</p>

  </div>
</main>
""")


# -----------------------------------------------
# TIMELINE
# -----------------------------------------------
PAGES['temple-farm/timeline/index.html'] = page("Timeline", "temple-farm", f"""
<main>
  {issue_line("File · Temple Farm · Timeline")}

  <div class="reading">
    <span class="kicker">Public record</span>
    <h1>Temple Farm <em>timeline</em></h1>
    <p class="dek">Dated entries in reverse chronological order. Anything since the start of 2026 is current. Anything earlier is context.</p>
  </div>

  <div class="wide">

  <div class="timeline-entry">
    <div class="date-col">15 May 2026</div>
    <div>
      <h3>Five emails sent to statutory bodies and the MP</h3>
      <p>Correspondence opened with Roydon Parish Council, Essex County Council Place Services Archaeology, the Lee Valley Regional Park Authority, Natural England, and Chris Vince MP. Replies expected over the coming two to three weeks. The Parish Council was sent the full briefing pack; the others received targeted enquiries.</p>
    </div>
  </div>

  <div class="timeline-entry">
    <div class="date-col">13 May 2026</div>
    <div>
      <h3>HMLR title register obtained for EX311401</h3>
      <p>The current state of the principal Temple Farm title is now on file. All material facts in the published briefings are confirmed by the register: ownership by Bozena and Charles Frederick, the 17 May 2016 Promotion Agreement with Dandara, the registered charge in favour of Roydon Estates Limited dated 24 February 2023, and the restriction requiring a Roydon Estates certificate for any disposition.</p>
    </div>
  </div>

  <div class="timeline-entry">
    <div class="date-col">May 2026</div>
    <div>
      <h3>Archaeological evaluation observed on site</h3>
      <p>Colchester Archaeological Trust on site, evaluation trenches across the pasture, spoil heaps. Consistent with pre-application work commissioned by a developer six to twelve months before a planning application is lodged. Photographed for the evidence file.</p>
    </div>
  </div>

  <div class="timeline-entry">
    <div class="date-col">May 2026</div>
    <div>
      <h3>Roydon Parish Council publishes &ldquo;Temple Farm Housing Development Plans&rdquo;</h3>
      <p>The Council&rsquo;s Latest News page confirms that Dandara Homes has formally approached the Council stating an intention to apply for outline planning permission for 200 to 250 homes on the 70-acre site. The Council describes the arrangement as Dandara having &ldquo;an option to purchase.&rdquo;</p>
    </div>
  </div>

  <div class="timeline-entry">
    <div class="date-col">7 February 2026</div>
    <div>
      <h3>Parish Council summary published</h3>
      <p>Parish Council issues a written summary &ldquo;Housing development in the Parish of Roydon&rdquo; confirming the scheme is for &ldquo;between 200 and 250 new homes on a 70-acre site&rdquo; and noting that Dandara had advised of &ldquo;delays in creating their Masterplan.&rdquo;</p>
    </div>
  </div>

  <div class="timeline-entry">
    <div class="date-col">29 January 2026</div>
    <div>
      <h3>Dandara postpones the private Member briefing</h3>
      <p>Dandara cancels its planned private briefing to Parish Council Members ahead of the 5 February meeting. No reasons given. A public consultation at St Peter&rsquo;s Church Hall had been previously scheduled for February.</p>
    </div>
  </div>

  <div class="timeline-entry">
    <div class="date-col">20 January 2026</div>
    <div>
      <h3>Parish Council confirms Dandara approach</h3>
      <p>Roydon Parish Council confirms publicly that Dandara Homes is planning a public consultation at St Peter&rsquo;s Church Hall in February 2026, and would brief Members privately before the 5 February Parish Council meeting.</p>
    </div>
  </div>

  <div class="timeline-entry">
    <div class="date-col">December 2024</div>
    <div>
      <h3>NPPF revised to introduce grey belt</h3>
      <p>The Government&rsquo;s December 2024 revisions to the National Planning Policy Framework introduce the &ldquo;grey belt&rdquo; designation. Importantly, the footnote 7 carve-outs that protect heritage, ecological designations, and flood risk are preserved in the new framework.</p>
    </div>
  </div>

  <div class="timeline-entry">
    <div class="date-col">June 2023</div>
    <div>
      <h3>Savills informal tender, no completed sale</h3>
      <p>Temple Farm offered for sale by Savills by informal tender, deadline 14 June 2023. The terms required a 10-year farm business tenancy back to the Frederick family and 25 years of vendor overage at 40 percent of any planning uplift beyond agricultural value. No completed sale on the main land holding.</p>
    </div>
  </div>

  <div class="timeline-entry">
    <div class="date-col">March 2023</div>
    <div>
      <h3>Local Plan adopted, Temple Farm not allocated</h3>
      <p>Epping Forest District Council adopts its Local Plan. The plan does not allocate Temple Farm for housing. The Council&rsquo;s own evidence base assessed and rejected the site.</p>
    </div>
  </div>

  <div class="timeline-entry">
    <div class="date-col">7 March 2023</div>
    <div>
      <h3>Title consolidation and Dandara restriction registered</h3>
      <p>Ownership consolidated to Bozena Miranda Frederick and Charles Nicholas John Frederick. Restriction registered at the HMLR requiring a Roydon Estates Limited certificate of compliance with paragraph 5 of the Promotion Agreement Schedule for any disposition. Registered charge in favour of Roydon Estates Limited dated 24 February 2023.</p>
    </div>
  </div>

  <div class="timeline-entry">
    <div class="date-col">September 2023</div>
    <div>
      <h3>Hughes 2023, Old Coal Yard appeal dismissed</h3>
      <p>Inspector L Hughes dismisses an appeal for 7 dwellings on land at the Old Coal Yard, also within the Roydon Conservation Area (appeal reference APP/J1535/W/22/3303841). Applies the same footnote 7 mechanism that dismissed the Temple Farm appeal in 2022.</p>
    </div>
  </div>

  <div class="timeline-entry">
    <div class="date-col">July 2022</div>
    <div>
      <h3>Wyatt 2022, Temple Farm appeal dismissed</h3>
      <p>Inspector S J Wyatt dismisses an appeal by the landowner herself for 5 dwellings on this exact land (appeal reference APP/J1535/W/21/3275842). The decision applies the footnote 7 carve-out, finding that the heritage and ecological protections defeat the tilted balance in favour of sustainable development.</p>
    </div>
  </div>

  <div class="timeline-entry">
    <div class="date-col">2021</div>
    <div>
      <h3>Promotion Agreement extended</h3>
      <p>The Dandara Promotion Agreement is extended for a further five years, taking it to 2026. The extension is recorded in the April 2023 Savills sales brochure but is not entered on the HMLR title register.</p>
    </div>
  </div>

  <div class="timeline-entry">
    <div class="date-col">17 May 2016</div>
    <div>
      <h3>Promotion Agreement signed</h3>
      <p>Promotion Agreement signed between the three Frederick brothers (Stanley John, Nicholas Stanley, Christopher John), Roydon Estates Limited (Isle of Man), and Dandara IOM Holdings Limited. Five-year initial term, covering the pasture only, not the buildings or residences.</p>
    </div>
  </div>

  <div class="timeline-entry">
    <div class="date-col">1985</div>
    <div>
      <h3>Freehold acquired by the Frederick family</h3>
      <p>The registered freehold is acquired by the Frederick family from The Charlton Sand and Ballast Company Limited, by Conveyance dated 4 March 1985. Holland Hannen &amp; Cubitts (Investments) Limited appears as the second party to the Conveyance. The family had been farming Temple Farm since 1937, specialising in free-range Christmas turkeys.</p>
    </div>
  </div>

  </div>

</main>
""")


# -----------------------------------------------
# EVIDENCE
# -----------------------------------------------
PAGES['temple-farm/evidence/index.html'] = page("Evidence", "temple-farm", f"""
<main>
  {issue_line("File · Temple Farm · Evidence")}

  <div class="reading">
    <span class="kicker">Source documents</span>
    <h1>Evidence <em>file</em></h1>
    <p class="dek">Linked references to the documents this site relies on. Where a document is publicly hosted, the link goes there. Where it has been obtained from HMLR or another source, it is on the Downloads page.</p>
  </div>

  <h2 class="no-rule">Title registers</h2>
  <div class="reading">
    <p>The three Frederick titles. The first is the principal title containing the pasture in scope of the Dandara Promotion Agreement.</p>
    <ul>
      <li><strong>EX311401</strong> &mdash; Land on the north west side of Epping Road and on the south west side of High Street, Roydon, Harlow (Freehold). <a href="/downloads/">Title register on file, accessed 13 May 2026</a>.</li>
      <li><strong>EX316455</strong> &mdash; Adjacent Frederick title.</li>
      <li><strong>EX420012</strong> &mdash; Adjacent Frederick title.</li>
    </ul>
    <p>Any reader can verify these for &pound;3 each at <a href="https://www.gov.uk/search-property-information-land-registry">gov.uk/search-property-information-land-registry</a>.</p>
  </div>

  <h2>Planning Inspectorate appeal decisions</h2>
  <div class="reading">
    <p>Both decisions are publicly hosted on the Planning Inspectorate&rsquo;s decision portal. Both apply the &ldquo;footnote 7&rdquo; carve-out under the NPPF.</p>
    <ul>
      <li><strong>Wyatt 2022.</strong> Appeal reference <strong>APP/J1535/W/21/3275842</strong>. Five dwellings on Temple Farm. Dismissed July 2022 by Inspector S J Wyatt BSc(Hons) MA MRTPI.</li>
      <li><strong>Hughes 2023.</strong> Appeal reference <strong>APP/J1535/W/22/3303841</strong>. Seven dwellings at the Old Coal Yard, rear of 32 High Street, Roydon. Dismissed 4 September 2023 by Inspector L Hughes BA(Hons) MSc MRTPI.</li>
    </ul>
  </div>

  <h2>Planning policy</h2>
  <div class="reading">
    <ul>
      <li><strong>Adopted Local Plan, March 2023.</strong> Epping Forest District Council. <a href="https://www.eppingforestdc.gov.uk/planning-and-building/planning-policy/local-plan-2011-2033/">eppingforestdc.gov.uk/planning-and-building/planning-policy/local-plan-2011-2033/</a></li>
      <li><strong>National Planning Policy Framework (December 2024 revision).</strong> <a href="https://www.gov.uk/government/publications/national-planning-policy-framework--2">gov.uk/government/publications/national-planning-policy-framework--2</a></li>
      <li><strong>Footnote 7 and the tilted balance.</strong> NPPF paragraph 11(d) and footnote 7 (numbering as at December 2024).</li>
      <li><strong>Roydon Conservation Area Appraisal.</strong> Published by EFDC.</li>
    </ul>
  </div>

  <h2>Statute</h2>
  <div class="reading">
    <ul>
      <li><strong>Lee Valley Regional Park Act 1966.</strong> <a href="https://www.legislation.gov.uk/ukla/1966/41/contents">legislation.gov.uk/ukla/1966/41/contents</a> &mdash; in particular Section 12 (statutory purpose).</li>
      <li><strong>Wildlife and Countryside Act 1981</strong> &mdash; the underlying legislation for the Lee Valley SSSI.</li>
      <li><strong>Conservation of Habitats and Species Regulations 2017</strong> &mdash; the underlying framework for Habitats Regulations Assessment of effects on the Epping Forest SAC and Lee Valley SPA.</li>
      <li><strong>Planning (Listed Buildings and Conservation Areas) Act 1990</strong> &mdash; Sections 66 and 72, the statutory duties on heritage assets and Conservation Areas.</li>
    </ul>
  </div>

  <h2>Maps and constraints</h2>
  <div class="reading">
    <ul>
      <li><strong>EFDC interactive constraints map.</strong> <a href="https://www.eppingforestdc.gov.uk/">eppingforestdc.gov.uk</a> &mdash; navigate to Planning, then Constraints. Temple Farm sits inside the Lee Valley Regional Park boundary, inside the Lee Valley SSSI Impact Risk Zone, inside Flood Zones 2 and 3 (in part), within the Roydon Conservation Area, and adjacent to Grade I and Grade II listed buildings.</li>
    </ul>
  </div>

  <h2>Marketing material</h2>
  <div class="reading">
    <ul>
      <li><strong>Savills informal tender brochure (April 2023).</strong> Marketing pack for the informal tender deadline of 14 June 2023. Confirms the 2021 extension of the Promotion Agreement to 2026 and the scope of the agreement (pasture only).</li>
    </ul>
  </div>

  <h2>Parish Council material</h2>
  <div class="reading">
    <ul>
      <li><strong>Roydon Parish Council, 20 January 2026.</strong> Public confirmation of Dandara&rsquo;s public consultation plan.</li>
      <li><strong>Roydon Parish Council, 7 February 2026.</strong> &ldquo;Housing development in the Parish of Roydon&rdquo; written summary.</li>
      <li><strong>Roydon Parish Council, May 2026.</strong> Latest News page &ldquo;Temple Farm Housing Development Plans.&rdquo;</li>
    </ul>
  </div>

</main>
""")


# -----------------------------------------------
# ACTION HUB
# -----------------------------------------------
PAGES['act/index.html'] = page("Take Action", "act", f"""
<main>
  {issue_line("File · Take Action")}

  <div class="reading">
    <span class="kicker">Pre-application stage</span>
    <h1>Take <em>action</em></h1>
    <p class="dek">Pre-drafted emails to the bodies whose position will shape what Dandara chooses to submit. Click a tile, your mail client opens with the message ready to send. Personalise the first line. Hit send.</p>

    <div class="panel note">
      <h4>How this works</h4>
      <p class="mb-0">Each page below has three or four different email versions. The page picks one at random when you open it. That way, the inbox at the receiving end sees genuinely varied messages, not 80 copies of the same email. Statutory consultees take varied individual representations more seriously than form-letter campaigns. <strong>Adding a sentence in your own words at the top of the message makes a real difference</strong> &mdash; even one line on your road or your family or why this matters to you.</p>
    </div>
  </div>

  <h2 class="no-rule">Who to email</h2>

  <div class="grid-2">
    <a class="tile" href="/act/lvrpa/">
      <span class="meta">Statutory authority</span>
      <h3>Lee Valley Regional Park Authority</h3>
      <p>The Park was created by Act of Parliament in 1966. Temple Farm sits inside its boundary. The Authority&rsquo;s position carries weight with the District Council.</p>
      <span class="arrow">Pre-drafted email →</span>
    </a>
    <a class="tile" href="/act/natural-england/">
      <span class="meta">Statutory consultee</span>
      <h3>Natural England</h3>
      <p>The site sits inside the Impact Risk Zone for the Lee Valley SSSI. Vehicle emissions from any development engage the Epping Forest SAC. Both trigger mandatory consultation.</p>
      <span class="arrow">Pre-drafted email →</span>
    </a>
    <a class="tile" href="/act/mp/">
      <span class="meta">Constituency MP</span>
      <h3>Chris Vince MP</h3>
      <p>The MP can write to EFDC&rsquo;s planning lead and to the Secretary of State, and can ask written parliamentary questions on grey belt and footnote 7 protections.</p>
      <span class="arrow">Pre-drafted email →</span>
    </a>
    <a class="tile" href="/act/parish/">
      <span class="meta">Local government</span>
      <h3>Roydon Parish Council</h3>
      <p>The Parish Council is a statutory consultee in its own right. Let the Clerk know you support a strong Parish response and want to be notified when Temple Farm comes to the agenda.</p>
      <span class="arrow">Pre-drafted email →</span>
    </a>
    <a class="tile" href="/act/register/">
      <span class="meta">For the record</span>
      <h3>Register your concern</h3>
      <p>Add your name and address to the residents&rsquo; register of concern. The list is what makes formal representations weighty at the planning stage.</p>
      <span class="arrow">Add your name →</span>
    </a>
    <a class="tile disabled" href="/act/object/">
      <span class="meta">Once application is lodged</span>
      <h3>Object to a planning application</h3>
      <p>This page is dormant until a planning application is formally lodged with EFDC. At that point it becomes the most important page on the site and gets the case officer&rsquo;s name, the application reference, the consultation deadline, and pre-drafted objection templates.</p>
      <span class="arrow">Available when needed →</span>
    </a>
  </div>

  <h2>If your mail client doesn&rsquo;t open</h2>
  <div class="reading">
    <p>Some browsers and devices, particularly work computers and some Android setups, don&rsquo;t have a default email handler configured. If a button doesn&rsquo;t open your mail client, each action page has an &ldquo;or copy the text&rdquo; panel below the button. Click to expand, copy the full message and the recipient address, then paste into whatever mail you do use (Gmail in the browser, your phone&rsquo;s mail app, your work webmail).</p>
  </div>

</main>
""")


# Helper to build an action page
def action_page(slug, title, to, intro_html, variants, cc=None):
    """Build a single action page with mailto: variants."""
    import json
    variants_js = json.dumps(variants)
    cc_js = json.dumps(cc) if cc else 'null'

    return page(title, "act", f"""
<main>
  {issue_line(f"File · Take Action · {title}")}

  <div class="reading">
    <span class="kicker">Pre-drafted email</span>
    <h1>{title}</h1>

    {intro_html}

    <div class="panel note">
      <h4>Before you send</h4>
      <p>Add a sentence in your own words at the top of the message &mdash; about your road, your family, your view, anything specific to you. Even one line of personalisation lifts this from a form letter to a residents&rsquo; representation. Look for the highlighted <span class="placeholder">[Add a personal line here]</span> in the template below and replace it with your own line.</p>
    </div>

    <div class="btn-row">
      <a href="#" class="btn primary" data-mailto>Open in your mail client</a>
    </div>
    <p class="text-meta tiny" data-variant-info>&nbsp;</p>

    <div class="email-template">
      <div class="email-meta">
        <div><strong>To:</strong> <span data-to></span></div>
        {'<div><strong>Cc:</strong> <span data-cc></span></div>' if cc else ''}
        <div><strong>Subject:</strong> <span data-subject></span></div>
      </div>
      <div data-body></div>
    </div>

    <details class="copy-text">
      <summary>If the button doesn&rsquo;t work, copy the text</summary>
      <p class="tiny text-meta">Some browsers and devices block <code>mailto:</code> links. Copy the recipient address and the full message body above, paste them into your mail client manually.</p>
    </details>

    <hr>

    <h3>What happens next</h3>
    <p>Once you&rsquo;ve sent the email, the recipient will typically acknowledge receipt within a few days and issue a substantive response within two to four weeks. Replies from statutory bodies become evidence later, so file or print whatever comes back.</p>

    <p>While you&rsquo;re here, consider also:</p>
    <ul>
      <li><a href="/act/register/">Registering your concern</a> on the residents&rsquo; list.</li>
      <li>Sending one of the other pre-drafted emails to a different stakeholder.</li>
      <li>Sharing this page&rsquo;s URL with a neighbour.</li>
    </ul>

  </div>
</main>

<script src="/js/templates.js"></script>
<script>
window.ROYDON_ACTION = {{
  to: {json.dumps(to)},
  cc: {cc_js},
  variants: {variants_js}
}};
</script>
""")


# -----------------------------------------------
# LVRPA — Lee Valley Regional Park Authority
# -----------------------------------------------
LVRPA_VARIANTS = [
    {
        "subject": "Pre-application activity at Temple Farm, Roydon, within the Lee Valley Regional Park",
        "body": """Dear Lee Valley Regional Park Authority,

[Add a personal line here about your connection to Roydon, your road, how long you have lived here. Even one sentence is enough.]

I am writing as a resident of Roydon to register concern about pre-application activity at Temple Farm, High Street, Roydon CM19 5FU. Archaeological evaluation by Colchester Archaeological Trust was observed on the pasture in April and May 2026, and Roydon Parish Council has confirmed that Dandara Homes intends to apply for outline planning permission for around 200 to 250 homes on the 70-acre site.

The site sits firmly within the Lee Valley Regional Park boundary on the District Council's own constraints map. Residential development at this scale is plainly inconsistent with the statutory purpose of the Park under Section 12 of the Lee Valley Regional Park Act 1966, namely the development, improvement, preservation and management of the Park for recreation, sport, entertainment and as a nature reserve.

I would like the Authority to make its position on this site known at the pre-application stage rather than wait for formal consultation. The early position of statutory consultees materially shapes what a developer chooses to submit, and a Park Authority position registered now will save considerable public-resource cost later.

Yours sincerely,
[Your name]
[Your address, including postcode]"""
    },
    {
        "subject": "Temple Farm, Roydon - request for the Authority's pre-application position",
        "body": """Dear Sir or Madam,

[Add a personal line here. One sentence about your connection to the village or your view on this matters.]

I am writing as a resident of Roydon about the proposed Dandara development at Temple Farm, High Street, Roydon CM19 5FU. The pasture forms part of the Lee Valley Regional Park, and Dandara Homes has formally approached Roydon Parish Council stating an intention to apply for outline planning permission for 200 to 250 homes.

Two things concern me particularly. First, the cumulative effect on the Park's amenity value of placing a settlement of this size within a corridor whose statutory purpose under the 1966 Act is recreation, sport, entertainment and nature conservation. A development of 250 homes is not a marginal addition; it permanently changes the character of the Park in this section.

Second, the precedent. If the Park boundary does not function as a meaningful constraint at Temple Farm, it is unclear what protection it offers anywhere along the corridor.

I would be grateful if the Authority could register its position with the District Council and with Dandara at the pre-application stage. I understand that earlier appeal evidence has confirmed Park engagement and that an Inspector dismissed a much smaller scheme on this exact land in 2022.

Yours sincerely,
[Your name]
[Your address, including postcode]"""
    },
    {
        "subject": "Statutory protection of the Lee Valley Park, Temple Farm Roydon development",
        "body": """Dear Lee Valley Regional Park Authority,

[Personal line, one sentence about why this matters to you specifically.]

As a Roydon resident I am writing to flag pre-application activity at Temple Farm, High Street, Roydon CM19 5FU, where Dandara Homes intends to seek outline planning permission for approximately 250 dwellings on a 70-acre pasture.

This site sits within the Lee Valley Regional Park. In 2022 a Planning Inspector (Wyatt, appeal reference APP/J1535/W/21/3275842) dismissed an appeal for just five dwellings on this exact land. The current proposal is fifty times larger.

I would like to ask whether the Authority has been notified of Dandara's pre-application work and, if so, what response it has given. If not, I would be grateful if you could open a file on the site and register the Authority's interest in any subsequent pre-application correspondence.

The Park's statutory protections under the 1966 Act are precisely the kind of constraint that earlier Inspectors have used to dis-apply the presumption in favour of sustainable development. The Authority's early engagement materially helps to maintain that protection.

Yours sincerely,
[Your name]
[Your address, including postcode]"""
    },
    {
        "subject": "Heritage and Park amenity concerns at Temple Farm, Roydon (CM19 5FU)",
        "body": """Dear Sir or Madam,

[One personal sentence here, in your own words, about your interest in this issue.]

I am writing as a resident of Roydon about Temple Farm, where Dandara is preparing a planning application for 200 to 250 homes on a pasture sitting fully within the Lee Valley Regional Park boundary.

The site has unusual layered protections that all engage at once. It is within the Park. It sits in the Impact Risk Zone for the Lee Valley SSSI. It is adjacent to the Grade I listed St Peter's Church and the Grade II listed Temple Farmhouse, within the Roydon Conservation Area. Parts sit in Flood Zones 2 and 3. A 2022 appeal Inspector dismissed five dwellings on this exact land.

The Park Authority has a statutory duty to maintain the character and purpose of the Park. At Temple Farm that character is closely linked to the open setting of St Peter's Church, the view from the river path, and the visual continuity of the Park along the Roydon stretch. A 250-home scheme would damage all three.

I would be grateful if the Authority could register an early position with the District Council and ask to receive Dandara's pre-application materials when they are circulated.

Yours sincerely,
[Your name]
[Your address, including postcode]"""
    }
]

PAGES['act/lvrpa/index.html'] = action_page(
    slug="lvrpa",
    title="Email the Lee Valley Regional Park Authority",
    to="info@leevalleypark.org.uk",
    intro_html="""
    <p class="dek">The Park was created by Act of Parliament in 1966 and exists to protect a specific corridor through Essex, Hertfordshire and London for recreation, sport, entertainment, and nature. Temple Farm sits inside it.</p>
    <p>The Authority is a statutory body with its own planning interests. A position registered by them now, before any application is lodged, materially shapes what Dandara chooses to submit and is harder to overturn later.</p>
    """,
    variants=LVRPA_VARIANTS
)


# -----------------------------------------------
# NATURAL ENGLAND
# -----------------------------------------------
NE_VARIANTS = [
    {
        "subject": "Pre-application activity at Temple Farm, Roydon (CM19 5FU), SSSI IRZ and Epping Forest SAC",
        "body": """Dear Natural England,

[Add a personal line about your connection to Roydon or to the Lee Valley.]

I am writing as a resident of Roydon to flag pre-application activity at Temple Farm, High Street, Roydon CM19 5FU. Dandara Homes has formally approached Roydon Parish Council stating an intention to apply for outline planning permission for 200 to 250 homes on the 70-acre site, and archaeological evaluation was observed on the pasture in April and May 2026.

The site engages Natural England in two specific ways that I wanted to flag now rather than wait for formal consultation.

The first is the Lee Valley SSSI Impact Risk Zone. The development site sits within the IRZ for the Lee Valley SSSI, which triggers mandatory Natural England consultation on residential development of this scale.

The second is the Epping Forest SAC, engaged via vehicle emissions. This was confirmed by Planning Inspector S J Wyatt in dismissing an earlier appeal on this same land in July 2022 (appeal reference APP/J1535/W/21/3275842, at paragraph 21).

It would be useful if Natural England could register an interest in any pre-application correspondence relating to Temple Farm, so that your position is taken into account before any application is submitted.

Yours sincerely,
[Your name]
[Your address, including postcode]"""
    },
    {
        "subject": "Temple Farm Roydon, request for Natural England's pre-application engagement",
        "body": """Dear Sir or Madam,

[One personal sentence about why this matters to you.]

As a Roydon resident I am writing about Temple Farm, where Dandara Homes is preparing an application for 200 to 250 homes on 70 acres of pasture. The site is identified as engaging Natural England's statutory remit through two independent routes.

First, it sits inside the Impact Risk Zone for the Lee Valley SSSI, which makes Natural England a mandatory consultee on any residential planning application of this scale.

Second, traffic from the proposed development engages the Epping Forest Special Area of Conservation through nitrogen deposition and vehicle emissions. Inspector Wyatt confirmed this at paragraph 21 of appeal reference APP/J1535/W/21/3275842, which dismissed a five-dwelling scheme on this exact land in July 2022.

I would be grateful if Natural England could register its interest in Dandara's pre-application work and engage with the District Council at this early stage. The Habitats Regulations Assessment that any planning application will require is more useful as a constraint when scoped early than when challenged late.

Yours sincerely,
[Your name]
[Your address, including postcode]"""
    },
    {
        "subject": "Habitats Regulations engagement at Temple Farm, Roydon",
        "body": """Dear Natural England,

[Add a personal sentence in your own words.]

I am writing as a resident of Roydon to ask Natural England to register an interest in pre-application work being carried out at Temple Farm, High Street, Roydon CM19 5FU.

Dandara Homes has approached Roydon Parish Council stating an intention to apply for outline planning permission for 200 to 250 homes on the 70-acre pasture. Archaeological evaluation was observed on site in April and May 2026, consistent with pre-application work six to twelve months before submission.

The site engages Natural England through the Lee Valley SSSI Impact Risk Zone (within which the site sits) and through the Epping Forest SAC (engaged by additional traffic). The 2022 appeal decision on this exact land (Wyatt, appeal reference APP/J1535/W/21/3275842) confirms both engagements.

I would be grateful if you could open a file on the site and ask to be consulted on Dandara's pre-application materials before any formal submission. A Habitats Regulations Assessment that is properly scoped at the pre-application stage is a more robust constraint than one challenged after submission.

Yours sincerely,
[Your name]
[Your address, including postcode]"""
    }
]

PAGES['act/natural-england/index.html'] = action_page(
    slug="natural-england",
    title="Email Natural England",
    to="enquiries@naturalengland.org.uk",
    intro_html="""
    <p class="dek">Natural England is the Government&rsquo;s statutory adviser on the natural environment in England. Temple Farm engages them on two grounds.</p>
    <p>The site sits inside the Impact Risk Zone for the Lee Valley SSSI, which automatically triggers consultation on residential development of this scale. Separately, traffic from any housing scheme engages the Epping Forest Special Area of Conservation through vehicle emissions, as a Planning Inspector confirmed in 2022.</p>
    """,
    variants=NE_VARIANTS
)


# -----------------------------------------------
# MP — Chris Vince
# -----------------------------------------------
MP_VARIANTS = [
    {
        "subject": "Constituent matter, proposed development at Temple Farm, Roydon (CM19 5FU)",
        "body": """Dear Mr Vince,

[Add a personal line here. Your road, how long you have lived in the village, why this matters to your family. Even one sentence helps.]

I am writing as a constituent in Roydon.

Temple Farm, approximately 68 acres of pasture on the western edge of the village, is being prepared for a large-scale residential planning application by Dandara. Archaeological evaluation by Colchester Archaeological Trust was observed on the site in April and May 2026, which usually precedes an application by six to twelve months. Roydon Parish Council's published notice confirms the scheme is for 200 to 250 homes.

The site is within the Lee Valley Regional Park, protected by an Act of Parliament (1966). It sits within an Impact Risk Zone for the Lee Valley SSSI, with engagement to the Epping Forest SAC via vehicle emissions confirmed in earlier appeal evidence. It is adjacent to Grade I listed St Peter's Church, within the historic setting of Grade II Temple Farmhouse, and within the Roydon Conservation Area. A Planning Inspector dismissed a much smaller scheme on this exact land in July 2022 (appeal reference APP/J1535/W/21/3275842), applying the "footnote 7" carve-out under the NPPF. The site is not allocated in the adopted Local Plan (March 2023).

What would be most useful, if you are willing, is for you to write to EFDC's planning lead. Just to make clear that you are aware of the site, that you have constituent concerns about it, and that you would expect EFDC to engage properly with the statutory consultees before any decision is taken.

Thank you for your time.

Yours sincerely,
[Your name]
[Your address, including postcode]"""
    },
    {
        "subject": "Temple Farm, Roydon, please write to EFDC planning",
        "body": """Dear Mr Vince,

[One personal sentence. Why does this matter to you specifically?]

I am a constituent in Roydon writing about Temple Farm, where Dandara Homes is preparing an outline planning application for 200 to 250 dwellings.

The site is one of the most layered for planning constraints in the constituency. It is inside the Lee Valley Regional Park (Lee Valley Regional Park Act 1966). It sits within the Impact Risk Zone for the Lee Valley SSSI. Its traffic engages the Epping Forest SAC. It is adjacent to a Grade I listed church and inside a Conservation Area. Two Planning Inspectors (Wyatt 2022, Hughes 2023) have applied the footnote 7 carve-out in the NPPF to dismiss appeals at this site and nearby. The site is not allocated for housing in the March 2023 Local Plan.

What I would find most useful, as a single specific request, is for you to write to EFDC's planning lead. Just a short letter from you noting that you are aware of pre-application activity at Temple Farm, that you have constituent concerns, and that you would expect EFDC to consult the statutory bodies thoroughly before any decision. A letter from the MP carries weight that constituent letters alone cannot.

Yours sincerely,
[Your name]
[Your address, including postcode]"""
    },
    {
        "subject": "Footnote 7 protection in Roydon, constituent enquiry",
        "body": """Dear Mr Vince,

[Personal sentence in your own words.]

As a constituent in Roydon I am writing about Temple Farm, a 70-acre pasture on the western edge of the village currently the subject of a Dandara Promotion Agreement. Pre-application work has been observed and the developer has stated an intention to apply for 200 to 250 homes.

This site sits within multiple statutory protections, the most important of which (the Lee Valley Regional Park Act 1966) is on the statute book and is unaffected by the December 2024 NPPF revisions on grey belt. Two Planning Inspectors have already used the footnote 7 mechanism to dismiss appeals in Roydon (Wyatt on Temple Farm itself in 2022, Hughes on the Old Coal Yard in 2023).

I would value your engagement on this in one of three ways: a letter to EFDC's planning lead, a letter to the Secretary of State for HCLG on grey belt and footnote 7 protections in practice, or a written parliamentary question on the same. I appreciate you cannot do all three, but any one would be helpful.

Yours sincerely,
[Your name]
[Your address, including postcode]"""
    }
]

PAGES['act/mp/index.html'] = action_page(
    slug="mp",
    title="Email Chris Vince MP",
    to="chris.vince.mp@parliament.uk",
    intro_html="""
    <p class="dek">Chris Vince is the Member of Parliament for Harlow. The Roydon, Eastwick and Gilston ward sits in his constituency for parliamentary purposes.</p>
    <p>The MP can usefully do three things at this stage: write to EFDC&rsquo;s planning lead, write to the Secretary of State for HCLG, or ask a written parliamentary question on grey belt or footnote 7 protections. The pre-drafted templates ask for the first of these &mdash; the most tractable single ask.</p>
    <p class="small text-meta">Double-check at <a href="https://www.writetothem.com">writetothem.com</a> that your postcode falls within the Harlow constituency before you send. The 2024 boundary changes mean some Roydon addresses sit in different constituencies.</p>
    """,
    variants=MP_VARIANTS
)


# -----------------------------------------------
# PARISH COUNCIL
# -----------------------------------------------
PARISH_VARIANTS = [
    {
        "subject": "Temple Farm, support for a strong Parish Council position",
        "body": """Dear Clerk,

[Add a personal line about your road or how long you have lived in the village.]

I am writing as a resident of Roydon to register my support for a strong Parish Council position on the proposed Dandara development at Temple Farm.

I have read the Council's Latest News page on this and I am grateful for the Council's earlier work in keeping Temple Farm out of the 2023 Local Plan allocations. The 2026 archaeological evaluation and Dandara's formal approach to the Council mean we are now at the pre-application stage, and I think the Council's voice will be one of the most important the District Council will hear when an application is lodged.

I would like to be notified, if possible, of the agenda item where Temple Farm is discussed at a future Council meeting so I can attend the public participation slot. I would also like to support the Council in whatever formal correspondence it considers sending to the Lee Valley Regional Park Authority, Natural England, and other statutory consultees, ahead of any application.

Thank you for the time you put into this.

Yours sincerely,
[Your name]
[Your address, including postcode]"""
    },
    {
        "subject": "Temple Farm pre-application, Parish Council response",
        "body": """Dear Clerk,

[Personal sentence about your interest in this matter.]

I am a resident of Roydon writing about the proposed Temple Farm development. The Council's recent published note confirms Dandara's intention to apply for 200 to 250 homes, and pre-application archaeological work has been observed on the pasture.

I wanted to write briefly to say that I support a strong Parish Council position on this and to ask whether there is a meeting at which Temple Farm is on the agenda. I would value the chance to hear the Council's thinking and to attend the public participation slot if appropriate.

I am separately corresponding with the Lee Valley Regional Park Authority, Natural England, and our MP, but I think a coordinated Parish Council voice will carry more weight than any individual letter. Please let me know if there is anything specific I, or the village more broadly, can do to support the Council's response.

Yours sincerely,
[Your name]
[Your address, including postcode]"""
    },
    {
        "subject": "Resident support for the Parish Council on Temple Farm",
        "body": """Dear Clerk,

[One personal line in your own words.]

I am writing as a resident of Roydon to express my support for a robust Parish Council response to the pre-application activity at Temple Farm.

I am aware the Council has been monitoring this since at least early 2026, including the Dandara private briefing that was postponed in January and the public statements that have followed. I think the Council's institutional voice is going to matter more than any individual letter when an application is formally lodged.

I would like to be informed when Temple Farm next appears on a Parish Council agenda, and I would be grateful to know whether the Council intends to make formal pre-application enquiries to the statutory consultees. If there is anything I or other residents can do to support the Council's response, please do let me know.

Yours sincerely,
[Your name]
[Your address, including postcode]"""
    }
]

# Parish Council email - the user will need to find the actual Clerk email from the Parish Council website
PAGES['act/parish/index.html'] = action_page(
    slug="parish",
    title="Email Roydon Parish Council",
    to="clerk@roydonparishcouncil.org.uk",
    intro_html="""
    <p class="dek">Roydon Parish Council is a statutory consultee in its own right. The Council&rsquo;s formal position carries significant weight with the District Council and the statutory consultees.</p>
    <p>The ask here is different from the other action emails. You are not lodging an objection. You are letting the Clerk know you support a strong Parish response and asking to be notified when Temple Farm comes to the agenda.</p>
    <p class="small text-meta">Check <a href="https://www.roydonparishcouncil.org.uk">roydonparishcouncil.org.uk</a> for the current Clerk&rsquo;s name and email before sending. The pre-drafted email opens to <code>clerk@roydonparishcouncil.org.uk</code> as the default, but the actual address may differ.</p>
    """,
    variants=PARISH_VARIANTS
)


# -----------------------------------------------
# REGISTER OF CONCERN
# -----------------------------------------------
PAGES['act/register/index.html'] = page("Register your concern", "act", f"""
<main>
  {issue_line("File · Take Action · Register of concern")}

  <div class="reading">
    <span class="kicker">Residents&rsquo; register</span>
    <h1>Register your <em>concern</em></h1>
    <p class="dek">Add your name to the residents&rsquo; register of concern on Temple Farm. Used in any future formal representation to demonstrate the scale of local opposition.</p>

    <div class="panel note">
      <h4>What this is for</h4>
      <p class="mb-0">This is a register of named Roydon residents who have publicly recorded concern about the proposed Dandara development at Temple Farm. It is not a petition (which is treated by planning authorities as a single collective representation) but a register of named individuals each able to be cited in formal submissions and in the eventual consultation response. Postcodes are collected so submissions can be weighted by proximity to the site, which is what carries weight with planning officers and Inspectors.</p>
    </div>

    <h2 class="no-rule">How your information is used</h2>
    <p>Your details are stored privately and only used for representations on Temple Farm planning matters. They are not shared with any third party except as part of an aggregated submission to the District Council, the Lee Valley Regional Park Authority, the Planning Inspectorate (in the event of appeal), or other statutory consultees. They are never sold and never shared with the developer. You can ask to be removed at any time by emailing <a href="mailto:roydonsociety@gmail.com">roydonsociety@gmail.com</a>. See also the <a href="/privacy/">privacy page</a>.</p>

    <hr>

    <div class="panel">
      <h3 class="mt-0">The form</h3>
      <p>The form below is an embedded Google Form. Submissions go to a private Google Sheet on the campaign Gmail account. If the form doesn&rsquo;t load, you can <a href="mailto:roydonsociety@gmail.com?subject=Register%20of%20concern%20-%20Temple%20Farm&body=Please%20add%20me%20to%20the%20register%20of%20concern.%0A%0AName%3A%0AFull%20address%3A%0APostcode%3A%0AOptional%20comment%3A">email your details directly</a> instead.</p>

      <p class="text-meta tiny"><em>This form is a placeholder. Once the Google Form has been created on the campaign account, paste its embed URL into this page. Steps to create one are in the README.</em></p>

      <!--
        TO ENABLE THE FORM:
        1. Sign in to forms.google.com on the roydonsociety@gmail.com account
        2. Create a new form titled "Register of concern - Temple Farm"
        3. Add fields:
           - Full name (short text, required)
           - Full address including postcode (short text, required)
           - Email address (email, optional)
           - Why this matters to you, in your own words (long text, optional)
           - Consent (checkbox: "I am happy for my name to be cited in submissions to planning bodies on Temple Farm")
        4. Click Send -> embed icon (<>)
        5. Copy the iframe src URL and replace the comment block below with the iframe.
      -->

      <div style="padding: 3rem 1rem; background: #f7f3ea; border: 1px dashed #c9c0ae; text-align: center;">
        <p class="text-meta">Google Form embed will appear here once configured.</p>
      </div>
    </div>

    <p class="mt-6"><a href="/act/">&larr; Back to all actions</a></p>

  </div>
</main>
""")


# -----------------------------------------------
# OBJECT (dormant placeholder)
# -----------------------------------------------
PAGES['act/object/index.html'] = page("Object to a planning application", "act", f"""
<main>
  {issue_line("File · Take Action · Object")}

  <div class="reading">
    <span class="kicker">Dormant</span>
    <h1>Object to a planning <em>application</em></h1>
    <p class="dek">This page becomes active once Dandara formally lodges an outline planning application with Epping Forest District Council. It will be by far the most important page on this site during the 21-day consultation window.</p>

    <div class="panel warn">
      <h3 class="mt-0">Currently dormant</h3>
      <p class="mb-0">No planning application for Temple Farm has been lodged at the time of writing ({ISSUE_DATE}). As soon as one is, this page will be activated with:</p>
      <ul class="mb-0">
        <li>The application reference number</li>
        <li>The case officer&rsquo;s name and email at EFDC</li>
        <li>The direct link to the planning portal page for the application</li>
        <li>The exact consultation deadline (typically 21 days from validation)</li>
        <li>A countdown to that deadline</li>
        <li>Several pre-drafted objection template variants</li>
        <li>The grounds on which an objection should be framed (heritage, ecology, Park Act, footnote 7)</li>
        <li>Notes on what makes an objection count under the planning rules</li>
      </ul>
    </div>

    <h2 class="no-rule">In the meantime</h2>
    <p>The most useful things to do before an application is lodged are the four pre-application emails (to the Lee Valley Regional Park Authority, Natural England, the MP, and the Parish Council), plus adding your name to the residents&rsquo; register of concern.</p>

    <div class="btn-row">
      <a href="/act/" class="btn primary">See the action templates</a>
      <a href="/act/register/" class="btn">Register your concern</a>
    </div>

    <h3>When the application lands, how to know</h3>
    <p>The site will be updated within 24 hours of the application appearing on the EFDC planning portal. You can:</p>
    <ul>
      <li>Sign up to HMLR Property Alerts on the three Temple Farm titles (EX311401, EX316455, EX420012). Free from <a href="https://www.gov.uk/property-alert">gov.uk/property-alert</a>. Catches anything material at the title level.</li>
      <li>Set up an EFDC weekly planning list email through the District Council&rsquo;s planning portal.</li>
      <li>Add your email to the residents&rsquo; register of concern (form above), which doubles as a notification list when an application is lodged.</li>
    </ul>

  </div>
</main>
""")


# -----------------------------------------------
# ABOUT
# -----------------------------------------------
PAGES['about/index.html'] = page("About", "about", f"""
<main>
  {issue_line("Colophon")}

  <div class="reading">
    <span class="kicker">About this site</span>
    <h1>About <em>roydon.fyi</em></h1>
    <p class="dek">An information portal for residents of Roydon, Essex. Run by volunteers. Free to use. No tracking, no ads, no cookies.</p>

    <h2 class="no-rule">What this site is</h2>
    <p>roydon.fyi publishes briefings, evidence, and ways to engage with the planning process on matters affecting the village of Roydon, Essex. The current focus is the proposed Dandara development at Temple Farm, but the site is designed to outlast any single campaign.</p>

    <p>It is run by volunteers under the name <strong>Friends of Roydon</strong>, an unincorporated residents&rsquo; association. Friends of Roydon is not a registered charity, not a political party, not a campaigning organisation in any formal sense. It is residents who care about the village and have given time to setting out the facts clearly.</p>

    <h2>What this site is not</h2>
    <p>It is not affiliated with Roydon Parish Council, with Epping Forest District Council, with the Lee Valley Regional Park Authority, with any political party, with any developer, or with any landowner.</p>
    <p>It is not a substitute for the Parish Council. Where the Parish Council&rsquo;s statutory consultee role applies, that is where the institutional voice of the village sits. This site complements that, it does not replicate it.</p>
    <p>It is not a forum or a discussion board. Conversation about local matters belongs in the village&rsquo;s WhatsApp groups, Facebook groups, and the pub. This site is a publication.</p>

    <h2>Editorial approach</h2>
    <p>Three principles:</p>
    <ol>
      <li><strong>Sources before opinions.</strong> Every claim on this site is sourced. Every reference is checkable. Where a claim cannot be sourced, it is flagged as such.</li>
      <li><strong>Plain English alongside the technical.</strong> Each long-form briefing has a short plain-English companion. Anyone in the village should be able to engage with the issue regardless of background.</li>
      <li><strong>Action over commentary.</strong> The site exists to help residents do something useful, not to host long-form commentary. The pre-drafted email templates are the heart of the operation.</li>
    </ol>

    <h2>How to support the site</h2>
    <p>The most useful thing residents can do is engage with the action pages and the register of concern. The site does not solicit donations and does not need money. If a moment arrives where outside funds become necessary (a planning consultant retainer, for example), the answer would be a coordinated approach through the Parish Council, not a crowdfund.</p>

    <h2>Contact</h2>
    <p>For all correspondence: <a href="mailto:roydonsociety@gmail.com">roydonsociety@gmail.com</a></p>
    <p>Replies usually within a few days. Run by volunteers, please be patient.</p>

    <h2>Colophon</h2>
    <p class="smaller">Set in Fraunces (for headlines) and Manrope (for body text), both available free from Google Fonts. Built as static HTML, hosted on Cloudflare Pages. No tracking, no analytics, no third-party scripts, no cookies. The site weighs less than 200KB and loads in under a second on any modern connection. Source code and content are kept simple so the site can be maintained by anyone with basic web skills if the current maintainers move on.</p>

  </div>
</main>
""")


# -----------------------------------------------
# CONTACT
# -----------------------------------------------
PAGES['contact/index.html'] = page("Contact", "contact", f"""
<main>
  {issue_line("Contact")}

  <div class="reading">
    <span class="kicker">Get in touch</span>
    <h1>Contact <em>us</em></h1>
    <p class="dek">One inbox. Replies usually within a few days. Run by volunteers.</p>

    <h2 class="no-rule">Email</h2>
    <p><a href="mailto:roydonsociety@gmail.com" class="btn primary">roydonsociety@gmail.com</a></p>

    <h2>What this address is for</h2>
    <ul>
      <li>Comments or corrections on anything published on this site.</li>
      <li>Information or evidence relevant to the Temple Farm campaign that you would like to share.</li>
      <li>Questions about the briefings, the action templates, or the register of concern.</li>
      <li>Press enquiries.</li>
      <li>Requests to be added to or removed from any list held on the site.</li>
    </ul>

    <h2>What it is not for</h2>
    <ul>
      <li>Reporting planning breaches or other matters that should go to Epping Forest District Council.</li>
      <li>Parish Council matters, which belong with the Clerk at <a href="https://www.roydonparishcouncil.org.uk">roydonparishcouncil.org.uk</a>.</li>
      <li>Lobbying individual residents. This inbox does not exist to drive village politics, it exists to publish public information.</li>
    </ul>

    <h2>Response time</h2>
    <p>This is a volunteer operation. Most emails are answered within a few days. Anything urgent, please flag in the subject line and we will do our best.</p>

  </div>
</main>
""")


# -----------------------------------------------
# PRIVACY
# -----------------------------------------------
PAGES['privacy/index.html'] = page("Privacy", "about", f"""
<main>
  {issue_line("Privacy")}

  <div class="reading">
    <span class="kicker">Privacy policy</span>
    <h1>Privacy</h1>
    <p class="dek">Short, plain, honest. The information collected on this site is limited and the use of it is constrained.</p>

    <h2 class="no-rule">What we collect</h2>
    <p>The site itself collects nothing. There are no analytics, no tracking pixels, no cookies, no third-party scripts beyond the Google Fonts CDN (which sees only your IP address as part of normal HTTP requests for the font files).</p>

    <p>Two specific actions on the site involve sharing information voluntarily:</p>
    <ul>
      <li><strong>The register of concern.</strong> You submit your name, address (including postcode), optionally an email address, and optionally a free-text note. This is stored in a private Google Sheet on the roydonsociety@gmail.com account.</li>
      <li><strong>Emails sent through the action templates.</strong> You write directly to the named recipient (Lee Valley Regional Park Authority, Natural England, etc.) from your own email account. The site itself does not see or store anything about the email you send.</li>
    </ul>

    <h2>What we do with it</h2>
    <p>Register of concern data is used only for the following purposes:</p>
    <ul>
      <li>Aggregated submissions to the District Council, statutory consultees, and the Planning Inspectorate on Temple Farm matters, where the named residents have ticked the consent box.</li>
      <li>Notification of significant developments (an application being lodged, a consultation opening, an appeal being filed).</li>
    </ul>

    <p>The data is not:</p>
    <ul>
      <li>Sold, ever, to anyone, for any purpose.</li>
      <li>Shared with the developer or with anyone acting for the developer.</li>
      <li>Used for political campaigning beyond the planning matters described.</li>
      <li>Shared with other residents&rsquo; associations or campaign groups without specific consent.</li>
    </ul>

    <h2>Your rights</h2>
    <p>You can ask to be removed from the register at any time by emailing <a href="mailto:roydonsociety@gmail.com">roydonsociety@gmail.com</a>. Removal is usually within 48 hours and we will confirm by email when it&rsquo;s done.</p>
    <p>You can ask for a copy of the information held about you. Same email address.</p>

    <h2>Data Protection</h2>
    <p>Friends of Roydon is an unincorporated residents&rsquo; association and holds the register as a domestic / community-purpose data controller for the purposes of the UK Data Protection Act 2018 and UK GDPR. Where a question arises that this short policy does not answer, please email and we&rsquo;ll respond directly.</p>

    <h2>This site uses no cookies</h2>
    <p>That&rsquo;s deliberate. No cookie banner is shown because there is nothing to consent to. No session is tracked. Each visit is anonymous to us.</p>

  </div>
</main>
""")


# -----------------------------------------------
# THANKS
# -----------------------------------------------
PAGES['thanks/index.html'] = page("Thank you", "act", f"""
<main>
  {issue_line("Thank you")}

  <div class="reading text-center">
    <h1 style="margin-top: 3rem;">Thank you.</h1>
    <p class="dek" style="margin: 0 auto 3rem;">Your concern has been registered. The number is now one larger than it was a minute ago.</p>

    <div class="panel note text-center">
      <h3 class="mt-0">Whilst you&rsquo;re here</h3>
      <p>The single most useful next step is to send one of the pre-drafted emails to a statutory body. Each takes about 60 seconds.</p>
      <div class="btn-row" style="justify-content: center;">
        <a href="/act/lvrpa/" class="btn primary">Email LVRPA</a>
        <a href="/act/natural-england/" class="btn">Email Natural England</a>
        <a href="/act/mp/" class="btn">Email the MP</a>
      </div>
    </div>

    <p class="mt-6"><a href="/">&larr; Back to the homepage</a></p>

  </div>
</main>
""")


# -----------------------------------------------
# DOWNLOADS
# -----------------------------------------------
PAGES['downloads/index.html'] = page("Downloads", "about", f"""
<main>
  {issue_line("Downloads")}

  <div class="reading">
    <span class="kicker">Source files</span>
    <h1>Downloads</h1>
    <p class="dek">PDFs and Word documents of the briefings, the evidence, and supporting material. For anyone who wants the source files for printing, sharing, or working with offline.</p>

    <h2 class="no-rule">Briefings</h2>
    <ul>
      <li><strong><a href="/downloads/temple-farm-residents-briefing-v2.docx">Residents&rsquo; briefing (v2, Word)</a></strong> &mdash; About 1,500 words, plain English, the version intended for general circulation.</li>
      <li><strong><a href="/downloads/temple-farm-parish-council-briefing-v2.docx">Parish Council briefing (v2, Word)</a></strong> &mdash; About 3,650 words, the version sent to Roydon Parish Council with planning detail and suggested actions for the Council to consider.</li>
      <li><strong><a href="/downloads/temple-farm-roydon-briefing-v2.docx">Full briefing (v2, Word)</a></strong> &mdash; About 12,100 words, the technical document with the full appeal analysis, anchor defences, grey belt analysis, and references.</li>
    </ul>

    <h2>Title register</h2>
    <ul>
      <li><strong><a href="/downloads/2026-05-13_summary_of_title_EX311401_GOV_UK.pdf">HMLR title register, EX311401</a></strong> &mdash; Accessed 13 May 2026. The principal Temple Farm title. Includes Property Register, Proprietorship Register, and Charges Register.</li>
    </ul>

    <h2>Reusing this material</h2>
    <p>The briefings are written by Friends of Roydon and are free to use, reproduce, and share for the purposes of resident representation on Temple Farm. If you adapt them for use elsewhere, please email so we can keep a record. Attribution to roydon.fyi is appreciated but not required.</p>

  </div>
</main>
""")


# -----------------------------------------------
# 404
# -----------------------------------------------
PAGES['404.html'] = page("Not found", "home", f"""
<main>
  {issue_line("404")}

  <div class="reading text-center">
    <h1 style="margin-top: 3rem;">Page not found.</h1>
    <p class="dek" style="margin: 0 auto 3rem;">The page you were looking for doesn&rsquo;t exist on this site. It may have been moved, or you may have followed a link that&rsquo;s no longer valid.</p>

    <div class="btn-row" style="justify-content: center;">
      <a href="/" class="btn primary">Home</a>
      <a href="/temple-farm/" class="btn">Temple Farm</a>
      <a href="/act/" class="btn">Take Action</a>
    </div>

  </div>
</main>
""")


# ============================================================
# Write all files
# ============================================================

written = 0
for path, content in PAGES.items():
    full_path = SITE_DIR / path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.write_text(content)
    written += 1
    print(f"  wrote {path} ({len(content):,} bytes)")

print(f"\n✓ {written} pages written")
