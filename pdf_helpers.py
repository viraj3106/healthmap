import os
import sys
import matplotlib
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

# Register Unicode-capable TrueType Font (DejaVu Sans)
ttf_folder = os.path.join(os.path.dirname(matplotlib.__file__), 'mpl-data', 'fonts', 'ttf')
pdfmetrics.registerFont(TTFont('DejaVuSans', os.path.join(ttf_folder, 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', os.path.join(ttf_folder, 'DejaVuSans-Bold.ttf')))
pdfmetrics.registerFont(TTFont('DejaVuSans-Oblique', os.path.join(ttf_folder, 'DejaVuSans-Oblique.ttf')))
pdfmetrics.registerFont(TTFont('DejaVuSans-BoldOblique', os.path.join(ttf_folder, 'DejaVuSans-BoldOblique.ttf')))

registerFontFamily('DejaVuSans', 
                   normal='DejaVuSans', 
                   bold='DejaVuSans-Bold', 
                   italic='DejaVuSans-Oblique', 
                   boldItalic='DejaVuSans-BoldOblique')

# ----------------------------------------------------------------------
# Custom NumberedCanvas for professional Running Headers and Footers
# ----------------------------------------------------------------------
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("DejaVuSans", 7.5)
        self.setFillColor(colors.HexColor("#64748B"))

        page_w, page_h = A4

        # Header (Pages 2+)
        if self._pageNumber > 1:
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.75)
            self.line(40, page_h - 38, page_w - 40, page_h - 38)
            self.drawString(40, page_h - 30, "HEALTHMAP AI - Integrated Geographical Public Health Risk Intelligence")
            self.drawRightString(page_w - 40, page_h - 30, "Team: Cloud Commanders")

        # Footer (All pages)
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.75)
        self.line(40, 40, page_w - 40, 40)
        self.drawString(40, 28, "Hackathon Slot-II Proposal Submission | Team: Cloud Commanders")
        self.drawRightString(page_w - 40, 28, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

# ----------------------------------------------------------------------
# Style Generator
# ----------------------------------------------------------------------
def create_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        'DocHeaderTitle',
        parent=styles['Normal'],
        fontName='DejaVuSans-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=4
    ))

    styles.add(ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='DejaVuSans-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#0D9488'),
        spaceAfter=10
    ))

    styles.add(ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='DejaVuSans-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#0F2537'),
        spaceBefore=12,
        spaceAfter=5,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        'SubSectionHeading',
        parent=styles['Normal'],
        fontName='DejaVuSans-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#0369A1'),
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontName='DejaVuSans',
        fontSize=8.8,
        leading=13.0,
        textColor=colors.HexColor('#1E293B'),
        spaceAfter=5
    ))

    styles.add(ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontName='DejaVuSans',
        fontSize=8.6,
        leading=12.5,
        textColor=colors.HexColor('#1E293B'),
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=3.5
    ))

    styles.add(ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='DejaVuSans-Oblique',
        fontSize=8.4,
        leading=12.0,
        textColor=colors.HexColor('#0F766E')
    ))

    styles.add(ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='DejaVuSans-Bold',
        fontSize=8.2,
        leading=11.0,
        textColor=colors.white,
        alignment=1 # Center
    ))

    styles.add(ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='DejaVuSans',
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor('#1E293B')
    ))

    styles.add(ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='DejaVuSans-Bold',
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor('#0F172A')
    ))

    styles.add(ParagraphStyle(
        'ImageCaption',
        parent=styles['Normal'],
        fontName='DejaVuSans-Oblique',
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor('#64748B'),
        alignment=1,
        spaceBefore=3,
        spaceAfter=8
    ))

    return styles

# ----------------------------------------------------------------------
# Helper to create top title banner card
# ----------------------------------------------------------------------
def create_title_banner(doc_number, doc_title, styles):
    content = []
    
    banner_data = [
        [
            Paragraph("<b>HACKATHON SUBMISSION - SLOT-II</b> &nbsp;|&nbsp; <b>TEAM: CLOUD COMMANDERS</b>", 
                      ParagraphStyle('BannerTop', fontName='DejaVuSans-Bold', fontSize=7.5, textColor=colors.HexColor('#0D9488'))),
            Paragraph("<b>STATUS: SUBMISSION READY</b>", 
                      ParagraphStyle('BannerStat', fontName='DejaVuSans-Bold', fontSize=7.5, textColor=colors.HexColor('#15803D'), alignment=2))
        ],
        [
            Paragraph(f"<b>Part {doc_number}: {doc_title}</b>", 
                      ParagraphStyle('BannerH1', fontName='DejaVuSans-Bold', fontSize=14, leading=17, textColor=colors.HexColor('#0F172A'))),
            Paragraph("<b>Problem Statement:</b><br/>HEALTHMAP AI - Integrated Geographical Public Health Risk Intelligence", 
                      ParagraphStyle('BannerH2', fontName='DejaVuSans', fontSize=7.8, leading=11, textColor=colors.HexColor('#334155'), alignment=2))
        ]
    ]
    t = Table(banner_data, colWidths=[315, 200])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor('#CBD5E1')),
        ('LINEBELOW', (0,0), (-1,0), 0.75, colors.HexColor('#E2E8F0')),
        ('PADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    content.append(t)
    content.append(Spacer(1, 10))
    return content

# ----------------------------------------------------------------------
# Helper to create styled callout boxes
# ----------------------------------------------------------------------
def create_callout(text, styles, title="KEY STRATEGIC INSIGHT"):
    callout_data = [[
        Paragraph(f"<b>{title}</b><br/>{text}", styles['CalloutText'])
    ]]
    t = Table(callout_data, colWidths=[515])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0FDFA')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#99F6E4')),
        ('LINELEFT', (0,0), (0,0), 3.5, colors.HexColor('#0D9488')),
        ('PADDING', (0,0), (-1,-1), 7),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    return t

print("DejaVuSans Unicode font registered and helper styles updated.")
