from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def generate_audit_report(website, grade, executive_summary, strengths, critical_issues, quick_wins, recommendations, investment, output_file):
    doc = SimpleDocTemplate(output_file, pagesize=letter,
                           rightMargin=0.75*inch, leftMargin=0.75*inch,
                           topMargin=0.75*inch, bottomMargin=0.75*inch)

    styles = getSampleStyleSheet()
    dark = HexColor('#1a1a2e')
    accent = HexColor('#0066cc')

    title_style = ParagraphStyle('Title', fontSize=24, textColor=white, spaceAfter=6, fontName='Helvetica-Bold', alignment=TA_CENTER)
    subtitle_style = ParagraphStyle('Subtitle', fontSize=12, textColor=HexColor('#ccddff'), spaceAfter=4, fontName='Helvetica', alignment=TA_CENTER)
    heading_style = ParagraphStyle('Heading', fontSize=14, textColor=accent, spaceAfter=8, spaceBefore=16, fontName='Helvetica-Bold')
    body_style = ParagraphStyle('Body', fontSize=10, textColor=HexColor('#333333'), spaceAfter=6, fontName='Helvetica', leading=14)
    bullet_style = ParagraphStyle('Bullet', fontSize=10, textColor=HexColor('#333333'), spaceAfter=4, fontName='Helvetica', leftIndent=20, leading=14)

    story = []

    # Header
    header_data = [[Paragraph("Website Audit Report", title_style)],
                   [Paragraph(website, subtitle_style)],
                   [Paragraph(f"Overall Grade: {grade}", subtitle_style)]]
    header_table = Table(header_data, colWidths=[6.5*inch])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), dark),
        ('PADDING', (0,0), (-1,-1), 16),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 20))

    # Executive Summary
    story.append(Paragraph("Executive Summary", heading_style))
    story.append(HRFlowable(width="100%", thickness=1, color=accent))
    story.append(Spacer(1, 8))
    story.append(Paragraph(executive_summary, body_style))

    # Critical Issues
    story.append(Paragraph("Critical Issues", heading_style))
    story.append(HRFlowable(width="100%", thickness=1, color=HexColor('#cc0000')))
    story.append(Spacer(1, 8))
    for i, issue in enumerate(critical_issues, 1):
        story.append(Paragraph(f"{i}. {issue}", bullet_style))

    # Quick Wins
    story.append(Paragraph("Quick Wins (Free and Fast)", heading_style))
    story.append(HRFlowable(width="100%", thickness=1, color=HexColor('#009900')))
    story.append(Spacer(1, 8))
    for win in quick_wins:
        story.append(Paragraph(f"* {win}", bullet_style))

    # Strengths
    story.append(Paragraph("What's Working Well", heading_style))
    story.append(HRFlowable(width="100%", thickness=1, color=accent))
    story.append(Spacer(1, 8))
    for strength in strengths:
        story.append(Paragraph(f"* {strength}", bullet_style))

    # Recommendations
    story.append(Paragraph("Recommended Improvements", heading_style))
    story.append(HRFlowable(width="100%", thickness=1, color=accent))
    story.append(Spacer(1, 8))
    for rec in recommendations:
        story.append(Paragraph(f"* {rec}", bullet_style))

    # Investment
    story.append(Paragraph("Estimated Investment", heading_style))
    story.append(HRFlowable(width="100%", thickness=1, color=accent))
    story.append(Spacer(1, 8))
    story.append(Paragraph(investment, body_style))

    # Footer
    story.append(Spacer(1, 20))
    footer_data = [[Paragraph("Prepared by Terrence Crawford | AI-Powered Web Consulting",
                              ParagraphStyle('Footer', fontSize=9, textColor=white, alignment=TA_CENTER, fontName='Helvetica'))]]
    footer_table = Table(footer_data, colWidths=[6.5*inch])
    footer_table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), dark), ('PADDING', (0,0), (-1,-1), 12)]))
    story.append(footer_table)

    doc.build(story)
    print(f"PDF saved to {output_file}")


# E33 Audit Report
generate_audit_report(
    website="ethirtythree.com",
    grade="B-",
    executive_summary="E33 is a professional security and surveillance company founded by a former LAPD detective. The site is clean and professional, but a broken View All link on the homepage is sending potential customers to a dead page, and missing SEO metadata is making the business nearly invisible on Google.",
    strengths=[
        "Clean, dark security aesthetic -- looks professional and trustworthy",
        "Clear it is a security company within 5 seconds",
        "Contact forms on every page make it easy to reach out",
        "Strong credentials -- former LAPD detective adds credibility",
        "Good service descriptions with clear explanations",
        "Live booking system works correctly"
    ],
    critical_issues=[
        "Broken View All Services link -- sends visitors to a 404 dead page (Fix: 5 min, $0)",
        "Missing page title and meta description -- nearly invisible on Google (Fix: 10 min, $0)",
        "Residential page shows Services 3 placeholder title in Google results (Fix: 2 min, $0)"
    ],
    quick_wins=[
        "Fix the broken View All button -- link it to the correct services page",
        "Fix the Services 3 placeholder title on the residential page",
        "Add SEO title and meta description to homepage",
        "Make the footer phone number clickable on mobile",
        "Fix the double period typo (day or night..)"
    ],
    recommendations=[
        "Add a Background and Private Investigations page",
        "Add pricing ranges to reduce visitor hesitation",
        "Add client testimonials to build trust",
        "Update navigation to include Investigations link"
    ],
    investment="Total estimated investment: $0-$550. The most impactful fixes cost nothing and take under 15 minutes combined. Quick wins can be done by the business owner directly in Squarespace.",
    output_file="/Users/terrencecrawford/Desktop/ethirtythree-audit-report.pdf"
)
