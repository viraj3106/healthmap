import os
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import matplotlib

# Register DejaVuSans
ttf_folder = os.path.join(os.path.dirname(matplotlib.__file__), 'mpl-data', 'fonts', 'ttf')
pdfmetrics.registerFont(TTFont('DejaVuSans', os.path.join(ttf_folder, 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', os.path.join(ttf_folder, 'DejaVuSans-Bold.ttf')))
pdfmetrics.registerFont(TTFont('DejaVuSans-Oblique', os.path.join(ttf_folder, 'DejaVuSans-Oblique.ttf')))

# Slide Canvas
class SlideCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(SlideCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            if self._pageNumber > 1:
                self.saveState()
                self.setFont("DejaVuSans", 8)
                self.setFillColor(colors.HexColor("#64748B"))
                self.drawString(40, 20, "HEALTHMAP AI - Integrated Geographical Public Health Risk Intelligence")
                self.drawRightString(920, 20, f"Slide {self._pageNumber} of {num_pages}")
                self.restoreState()
            super(SlideCanvas, self).showPage()
        super(SlideCanvas, self).save()

def create_presentation_pdf():
    # 16:9 dimensions: 960 x 540 points
    doc = SimpleDocTemplate(
        "HEALTHMAP_AI_Presentation.pdf",
        pagesize=(960, 540),
        leftMargin=40,
        rightMargin=40,
        topMargin=35,
        bottomMargin=35
    )
    story = []

    # Slide 1: Exact layout matching user's uploaded image
    s1_data = [
        [Spacer(1, 100)],
        [Paragraph("<b>HEALTHMAP AI</b>", ParagraphStyle('S1Title', fontName='DejaVuSans-Bold', fontSize=38, leading=44, textColor=colors.HexColor('#1E293B'), alignment=1))],
        [Spacer(1, 10)],
        [Paragraph("Integrated Geographical Public Health Risk Intelligence", ParagraphStyle('S1Sub', fontName='DejaVuSans', fontSize=18, leading=24, textColor=colors.HexColor('#334155'), alignment=1))],
        [Spacer(1, 75)],
        [Paragraph("Team Name: Cloud Commanders", ParagraphStyle('S1Team', fontName='DejaVuSans', fontSize=15, leading=20, textColor=colors.HexColor('#1E293B'), alignment=1))],
        [Spacer(1, 6)],
        [Paragraph("Mentor: Mr. S. Venkatesh ( AP - CSE)", ParagraphStyle('S1Mentor', fontName='DejaVuSans', fontSize=15, leading=20, textColor=colors.HexColor('#1E293B'), alignment=1))]
    ]
    t_s1 = Table(s1_data, colWidths=[880])
    t_s1.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_s1)
    story.append(PageBreak())

    def make_header(title, category="HEALTHMAP AI · Integrated Public Health Intelligence"):
        return [
            Paragraph(f"<font color='#0D9488'><b>{category.upper()}</b></font>", ParagraphStyle('HCat', fontName='DejaVuSans-Bold', fontSize=9, leading=12)),
            Paragraph(f"<b>{title}</b>", ParagraphStyle('HTit', fontName='DejaVuSans-Bold', fontSize=20, leading=25, textColor=colors.HexColor('#0F2537'))),
            Spacer(1, 12)
        ]

    # Slide 2: The Problem
    story += make_header("The Problem: Risks Are Scattered, Not Seen Together")
    s2_left = [
        Paragraph("<b>TODAY: Health Data Sits in Separate Systems</b>", ParagraphStyle('P1', fontName='DejaVuSans-Bold', fontSize=12, textColor=colors.HexColor('#991B1B'))),
        Spacer(1, 8),
        Paragraph("&bull; Disease, weather, environment and geography are stored apart in unconnected silos.", ParagraphStyle('P2', fontName='DejaVuSans', fontSize=9.5, leading=14, textColor=colors.HexColor('#7F1D1D'))),
        Spacer(1, 4),
        Paragraph("&bull; Risks differ by locality, but health administrators cannot see them as one unified picture.", ParagraphStyle('P3', fontName='DejaVuSans', fontSize=9.5, leading=14, textColor=colors.HexColor('#7F1D1D'))),
        Spacer(1, 4),
        Paragraph("&bull; Surveillance updates arrive on a 14 to 21-day delay, forcing reactive crisis responses.", ParagraphStyle('P4', fontName='DejaVuSans', fontSize=9.5, leading=14, textColor=colors.HexColor('#7F1D1D'))),
        Spacer(1, 8),
        Paragraph("<b>Who is involved:</b> Public-health teams · Local administrators · Authorised analysts", ParagraphStyle('P5', fontName='DejaVuSans-Bold', fontSize=9.5, leading=14, textColor=colors.HexColor('#991B1B')))
    ]
    s2_right = [
        Paragraph("<b>5 Critical Gaps We Found</b>", ParagraphStyle('G1', fontName='DejaVuSans-Bold', fontSize=12, textColor=colors.HexColor('#0F2537'))),
        Spacer(1, 8),
        Paragraph("<b>1. Data held in separate systems:</b> Hospitals, labs, pharmacies, weather portals are disconnected.", ParagraphStyle('G2', fontName='DejaVuSans', fontSize=9, leading=13, textColor=colors.HexColor('#334155'))),
        Spacer(1, 4),
        Paragraph("<b>2. No combined, location-wise view:</b> District aggregates hide hyper-local street-level breeding spots.", ParagraphStyle('G3', fontName='DejaVuSans', fontSize=9, leading=13, textColor=colors.HexColor('#334155'))),
        Spacer(1, 4),
        Paragraph("<b>3. Weather and disease trends not linked:</b> Rainfall/temperature spikes precede outbreaks but are ignored.", ParagraphStyle('G4', fontName='DejaVuSans', fontSize=9, leading=13, textColor=colors.HexColor('#334155'))),
        Spacer(1, 4),
        Paragraph("<b>4. Estimates mixed up with confirmed reports:</b> Lack of clear separation between projections and lab cases.", ParagraphStyle('G5', fontName='DejaVuSans', fontSize=9, leading=13, textColor=colors.HexColor('#334155'))),
        Spacer(1, 4),
        Paragraph("<b>5. Hard to prioritise limited resources:</b> Fogging machines, beds, and medicines dispatched reactively.", ParagraphStyle('G6', fontName='DejaVuSans', fontSize=9, leading=13, textColor=colors.HexColor('#334155'))),
        Spacer(1, 8),
        Paragraph("<i>Our Boundary: Model estimates support decisions. They are shown separately from confirmed surveillance reports.</i>", ParagraphStyle('GB', fontName='DejaVuSans-Oblique', fontSize=8.5, leading=12, textColor=colors.HexColor('#0D9488')))
    ]
    t_s2 = Table([[s2_left, s2_right]], colWidths=[430, 430])
    t_s2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#FEF2F2')),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (0,0), 1.2, colors.HexColor('#F87171')),
        ('BOX', (1,0), (1,0), 1.2, colors.HexColor('#CBD5E1')),
        ('PADDING', (0,0), (-1,-1), 14),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_s2)
    story.append(PageBreak())

    # Slide 3: Our Solution
    story += make_header("Our Solution: One Platform, One Picture")
    sol_cards = [
        ("1. INTEGRATE", "Authorised disease surveillance, weather, environmental and geographical data into a single, unified PostGIS system.", "#0284C7", "#F0F9FF"),
        ("2. ASSESS", "Location-based predictive risk for mosquito-borne (Dengue), respiratory (AQI), and flood-related contamination hazards.", "#0D9488", "#F0FDFA"),
        ("3. VISUALISE", "Interactive GIS heatmap with intuitive filtering by disease, location, time period, and risk level on an H3 hexagonal grid.", "#6366F1", "#EEF2FF"),
        ("4. ACT", "Automated early-warning alerts, preventive citizen guidance, and resource prioritisation for frontline health teams.", "#16A34A", "#F0FDF4")
    ]
    cards_cells = []
    for title, desc, col, bg in sol_cards:
        cell = [
            Paragraph(f"<b>{title}</b>", ParagraphStyle('SCTit', fontName='DejaVuSans-Bold', fontSize=12, leading=15, textColor=colors.HexColor(col), alignment=1)),
            Spacer(1, 10),
            Paragraph(desc, ParagraphStyle('SCDesc', fontName='DejaVuSans', fontSize=9.5, leading=14, textColor=colors.HexColor('#334155'), alignment=1))
        ]
        cards_cells.append(cell)
    t_s3 = Table([cards_cells], colWidths=[215, 215, 215, 215])
    t_s3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#F0F9FF')),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor('#F0FDFA')),
        ('BACKGROUND', (2,0), (2,0), colors.HexColor('#EEF2FF')),
        ('BACKGROUND', (3,0), (3,0), colors.HexColor('#F0FDF4')),
        ('BOX', (0,0), (0,0), 1.2, colors.HexColor('#0284C7')),
        ('BOX', (1,0), (1,0), 1.2, colors.HexColor('#0D9488')),
        ('BOX', (2,0), (2,0), 1.2, colors.HexColor('#6366F1')),
        ('BOX', (3,0), (3,0), 1.2, colors.HexColor('#16A34A')),
        ('PADDING', (0,0), (-1,-1), 12),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_s3)
    story.append(Spacer(1, 18))
    notice = Table([[Paragraph("<b>✓ Core Principle:</b> Model estimates are always shown separately from confirmed surveillance reports.", ParagraphStyle('N1', fontName='DejaVuSans', fontSize=10, textColor=colors.HexColor('#0D9488')))]], colWidths=[880])
    notice.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0FDFA')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#99F6E4')),
        ('PADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(notice)
    story.append(PageBreak())

    # Slide 15 / Final Thank you
    story.append(Spacer(1, 100))
    s15_data = [
        [Paragraph("<b>Thank You</b>", ParagraphStyle('TYTitle', fontName='DejaVuSans-Bold', fontSize=40, leading=46, textColor=colors.HexColor('#0F2537'), alignment=1))],
        [Spacer(1, 10)],
        [Paragraph("<b>HEALTHMAP AI: Seeing Public-Health Risk, Place by Place</b>", ParagraphStyle('TYSub', fontName='DejaVuSans-Bold', fontSize=18, leading=24, textColor=colors.HexColor('#0D9488'), alignment=1))],
        [Spacer(1, 40)],
        [Paragraph("Team Name: Cloud Commanders", ParagraphStyle('TYTeam', fontName='DejaVuSans', fontSize=15, leading=20, textColor=colors.HexColor('#1E293B'), alignment=1))],
        [Spacer(1, 6)],
        [Paragraph("Mentor: Mr. S. Venkatesh ( AP - CSE)", ParagraphStyle('TYMentor', fontName='DejaVuSans', fontSize=15, leading=20, textColor=colors.HexColor('#1E293B'), alignment=1))],
        [Spacer(1, 20)],
        [Paragraph("<b>Questions & Discussion</b>", ParagraphStyle('TYQ', fontName='DejaVuSans-Bold', fontSize=15, leading=20, textColor=colors.HexColor('#0284C7'), alignment=1))]
    ]
    t_s15 = Table(s15_data, colWidths=[880])
    t_s15.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_s15)

    doc.build(story, canvasmaker=SlideCanvas)
    print("HEALTHMAP_AI_Presentation.pdf generated successfully.")

if __name__ == '__main__':
    create_presentation_pdf()

