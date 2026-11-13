import os
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle, Spacer, KeepTogether

# ----------------------------------------------------------------------
# 1. Native Vector Problem Analysis Box (Comparison Table)
# ----------------------------------------------------------------------
def get_native_problem_component(styles, width=515):
    reactive_content = [
        Paragraph("<b>CONVENTIONAL SURVEILLANCE PARADIGM</b><br/><font size=6.8 color='#991B1B'>Reactive, Fragmented & Delayed</font>", 
                  ParagraphStyle('RTitle', fontName='DejaVuSans-Bold', fontSize=8.0, leading=10.5, textColor=colors.HexColor('#991B1B'), alignment=1)),
        Spacer(1, 4),
        Paragraph("&bull; <b>Day 0:</b> Pathogen transmission begins undetected in water/drains.", 
                  ParagraphStyle('RItem', fontName='DejaVuSans', fontSize=7.0, leading=9.5, textColor=colors.HexColor('#7F1D1D'))),
        Paragraph("&bull; <b>Day 7-10:</b> Hospital emergency rooms overwhelmed by clinical surges.", 
                  ParagraphStyle('RItem', fontName='DejaVuSans', fontSize=7.0, leading=9.5, textColor=colors.HexColor('#7F1D1D'))),
        Paragraph("&bull; <b>Day 14:</b> Paper registers compiled at district administrative office.", 
                  ParagraphStyle('RItem', fontName='DejaVuSans', fontSize=7.0, leading=9.5, textColor=colors.HexColor('#7F1D1D'))),
        Paragraph("&bull; <b>Day 16+:</b> Retrospective crisis response deployed post-transmission.", 
                  ParagraphStyle('RItem', fontName='DejaVuSans', fontSize=7.0, leading=9.5, textColor=colors.HexColor('#7F1D1D'))),
        Paragraph("&bull; <b>Impact:</b> Severe medicine stockouts, ICU deficits & preventable deaths.", 
                  ParagraphStyle('RItem', fontName='DejaVuSans', fontSize=7.0, leading=9.5, textColor=colors.HexColor('#7F1D1D')))
    ]

    predictive_content = [
        Paragraph("<b>HEALTHMAP AI PREDICTIVE PARADIGM</b><br/><font size=6.8 color='#0F766E'>Predictive, Geospatial & Pre-emptive</font>", 
                  ParagraphStyle('PTitle', fontName='DejaVuSans-Bold', fontSize=8.0, leading=10.5, textColor=colors.HexColor('#0F766E'), alignment=1)),
        Spacer(1, 4),
        Paragraph("&bull; <b>Day -10:</b> Early precursor telemetry flagged (turbidity, rainfall spikes).", 
                  ParagraphStyle('PItem', fontName='DejaVuSans', fontSize=7.0, leading=9.5, textColor=colors.HexColor('#115E59'))),
        Paragraph("&bull; <b>Day -7:</b> Spatial AI predicts sub-ward Outbreak Vulnerability (OVI).", 
                  ParagraphStyle('PItem', fontName='DejaVuSans', fontSize=7.0, leading=9.5, textColor=colors.HexColor('#115E59'))),
        Paragraph("&bull; <b>Day -5:</b> Automated containment geo-fences & citizen mobile alerts.", 
                  ParagraphStyle('PItem', fontName='DejaVuSans', fontSize=7.0, leading=9.5, textColor=colors.HexColor('#115E59'))),
        Paragraph("&bull; <b>Day -3:</b> Proactive dispatch of fogging drones, beds & platelet stocks.", 
                  ParagraphStyle('PItem', fontName='DejaVuSans', fontSize=7.0, leading=9.5, textColor=colors.HexColor('#115E59'))),
        Paragraph("&bull; <b>Impact:</b> Contagion curve flattened before hospital admission peak.", 
                  ParagraphStyle('PItem', fontName='DejaVuSans', fontSize=7.0, leading=9.5, textColor=colors.HexColor('#115E59')))
    ]

    col_w = (width - 15) / 2
    t = Table([[reactive_content, predictive_content]], colWidths=[col_w, col_w])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#FEF2F2')),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor('#F0FDFA')),
        ('BOX', (0,0), (0,0), 1.2, colors.HexColor('#F87171')),
        ('BOX', (1,0), (1,0), 1.2, colors.HexColor('#2DD4BF')),
        ('PADDING', (0,0), (-1,-1), 7),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    return t

# ----------------------------------------------------------------------
# 2. Native Vector Architecture Component (4 Tiers)
# ----------------------------------------------------------------------
def get_native_architecture_component(styles, width=515):
    tiers = [
        {
            "badge": "TIER 4: DECISION SUPPORT & CITIZEN INTERFACES",
            "desc": "Chief Medical Officer GIS War-Room | Hospital Surge Load-Balancer | Citizen Mobile Alert PWA | Claude 3.5 SitRep Copilot",
            "bg": "#EFF6FF", "border": "#60A5FA", "badge_col": "#1D4ED8"
        },
        {
            "badge": "TIER 3: GEOSPATIAL AI & EPIDEMIOLOGY FORECASTING ENGINE",
            "desc": "Spatial-Temporal Graph Neural Networks (ST-GNN) | SEIR Spatial Diffusion | Outbreak Vulnerability Index (OVI) | Moran's I Hotspots",
            "bg": "#F0FDFA", "border": "#2DD4BF", "badge_col": "#0F766E"
        },
        {
            "badge": "TIER 2: SPATIAL DATA FABRIC & UNIFIED INDEXING",
            "desc": "Uber H3 Hexagonal Grid (Res 8/9) | PostgreSQL 16 + PostGIS Spatial Engine | TimescaleDB Telemetry | Differential Privacy Engine",
            "bg": "#EEF2FF", "border": "#818CF8", "badge_col": "#4338CA"
        },
        {
            "badge": "TIER 1: MULTI-MODAL INGESTION & SENSING FABRIC",
            "desc": "Hospital EHR/OPD Streams | Municipal IoT Sensors (Water pH, Turbidity, AQI) | IMD Weather & Satellite NDVI | Citizen Crowdsourcing",
            "bg": "#F0F9FF", "border": "#38BDF8", "badge_col": "#0369A1"
        }
    ]

    tier_rows = []
    for tier in tiers:
        cell_content = [
            Paragraph(f"<font color='{tier['badge_col']}'><b>{tier['badge']}</b></font>", 
                      ParagraphStyle('TBadge', fontName='DejaVuSans-Bold', fontSize=8.0, leading=10.0)),
            Spacer(1, 2),
            Paragraph(tier['desc'], 
                      ParagraphStyle('TDesc', fontName='DejaVuSans', fontSize=7.2, leading=9.5, textColor=colors.HexColor('#1E293B')))
        ]
        tier_rows.append([cell_content])

    t = Table(tier_rows, colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#EFF6FF')),
        ('BACKGROUND', (0,1), (0,1), colors.HexColor('#F0FDFA')),
        ('BACKGROUND', (0,2), (0,2), colors.HexColor('#EEF2FF')),
        ('BACKGROUND', (0,3), (0,3), colors.HexColor('#F0F9FF')),
        ('BOX', (0,0), (0,0), 1, colors.HexColor('#93C5FD')),
        ('BOX', (0,1), (0,1), 1, colors.HexColor('#99F6E4')),
        ('BOX', (0,2), (0,2), 1, colors.HexColor('#C7D2FE')),
        ('BOX', (0,3), (0,3), 1, colors.HexColor('#BAE6FD')),
        ('PADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    return t

# ----------------------------------------------------------------------
# 3. Native Vector Methodology Pipeline Component (5 Phases)
# ----------------------------------------------------------------------
def get_native_methodology_component(styles, width=515):
    phases = [
        ("PHASE 1", "Data Ingestion & Hygiene", "Clinical OPD, water telemetry & satellite data geocoded to Uber H3 hex grid with differential privacy."),
        ("PHASE 2", "Environmental Coupling", "DLNM captures 7-14 day lagged correlations between rainfall spikes, turbidity, and pathogen incubation."),
        ("PHASE 3", "Spatial-Temporal AI", "ST-GNN models epidemic propagation across contiguous hexagonal neighborhoods; Moran's I flags hotspots."),
        ("PHASE 4", "Model Calibration & SHAP", "Historical backtesting validates accuracy (AUC > 0.88); TreeSHAP attributes exact risk driver percentages."),
        ("PHASE 5", "Automated Response Dispatch", "Direct API triggers: drone fogging routes, hospital bed pre-positioning, and citizen PWA boil-water alerts.")
    ]

    p_cells = []
    cell_w = (width - 16) / 5
    for tag, title, body in phases:
        content = [
            Paragraph(f"<b>{tag}</b>", ParagraphStyle('PTag', fontName='DejaVuSans-Bold', fontSize=7.2, leading=9, textColor=colors.HexColor('#0D9488'), alignment=1)),
            Paragraph(f"<b>{title}</b>", ParagraphStyle('PTitle', fontName='DejaVuSans-Bold', fontSize=7.0, leading=9, textColor=colors.HexColor('#0F172A'), alignment=1)),
            Spacer(1, 2),
            Paragraph(body, ParagraphStyle('PBody', fontName='DejaVuSans', fontSize=6.2, leading=8.5, textColor=colors.HexColor('#334155'), alignment=1))
        ]
        p_cells.append(content)

    t = Table([p_cells], colWidths=[cell_w]*5)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('PADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    return t

# ----------------------------------------------------------------------
# 4. Native Vector Tech Stack Component (4 Columns)
# ----------------------------------------------------------------------
def get_native_tech_stack_component(styles, width=515):
    categories = [
        ("FRONTEND & GIS", "#0284C7", ["Next.js 15 (React 19)", "Tailwind CSS", "Mapbox GL JS", "Deck.gl HexagonLayer", "Apache ECharts"]),
        ("BACKEND & APIS", "#0D9488", ["FastAPI (Python 3.13)", "Uvicorn ASGI", "Celery Workers", "Redis Message Queue", "WebSocket Streaming"]),
        ("SPATIAL DATABASE", "#6366F1", ["PostgreSQL 16", "PostGIS Spatial Engine", "Uber H3 Spatial Hex", "TimescaleDB Telemetry", "Prisma ORM"]),
        ("AI / ML & GENAI", "#8B5CF6", ["PyTorch & PyG (ST-GNN)", "LightGBM & XGBoost", "GeoPandas & PySAL", "Claude 3.5 Sonnet RAG", "LangChain & FAISS"])
    ]

    cards = []
    card_w = (width - 15) / 4
    for title, col, tools in categories:
        items_p = [Paragraph(f"&bull; {tool}", ParagraphStyle('TItem', fontName='DejaVuSans', fontSize=6.8, leading=9.2, textColor=colors.HexColor('#1E293B'))) for tool in tools]
        content = [
            Paragraph(f"<b>{title}</b>", ParagraphStyle('CH', fontName='DejaVuSans-Bold', fontSize=7.4, leading=10, textColor=colors.HexColor(col), alignment=1)),
            Spacer(1, 3),
        ] + items_p
        cards.append(content)

    t = Table([cards], colWidths=[card_w]*4)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('PADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    return t

# ----------------------------------------------------------------------
# 5. Native Vector Expected Outcomes Scorecard Component
# ----------------------------------------------------------------------
def get_native_outcomes_component(styles, width=515):
    metrics = [
        ("14 DAYS", "Early Warning Lead Time", "Identifies outbreak precursors 10-14 days prior to clinical surge (vs. 2 days delayed)", "#0D9488", "#F0FDFA"),
        ("0.89 AUC", "Outbreak Predictive Accuracy", "Validated on historical seasonal Dengue & Cholera epidemic datasets", "#0284C7", "#F0F9FF"),
        ("460m", "Hyper-Local Micro Resolution", "Uber H3 discrete global hexagonal grid down to street & sub-ward scale", "#6366F1", "#EEF2FF"),
        ("76%", "Hospital Bed Deficit Mitigation", "Proactive patient triage load-balancing prevents emergency ICU saturation", "#16A34A", "#F0FDF4")
    ]

    cards = []
    card_w = (width - 15) / 4
    for val, title, desc, col, bg in metrics:
        content = [
            Paragraph(f"<b>{val}</b>", ParagraphStyle('MVal', fontName='DejaVuSans-Bold', fontSize=12, leading=14, textColor=colors.HexColor(col), alignment=1)),
            Spacer(1, 2),
            Paragraph(f"<b>{title}</b>", ParagraphStyle('MTit', fontName='DejaVuSans-Bold', fontSize=7.2, leading=9, textColor=colors.HexColor('#0F172A'), alignment=1)),
            Spacer(1, 2),
            Paragraph(desc, ParagraphStyle('MDesc', fontName='DejaVuSans', fontSize=6.2, leading=8.2, textColor=colors.HexColor('#475569'), alignment=1))
        ]
        cards.append(content)

    t = Table([cards], colWidths=[card_w]*4)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#F0FDFA')),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor('#F0F9FF')),
        ('BACKGROUND', (2,0), (2,0), colors.HexColor('#EEF2FF')),
        ('BACKGROUND', (3,0), (3,0), colors.HexColor('#F0FDF4')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('PADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    return t

# ----------------------------------------------------------------------
# 6. Native Vector Prototype UI Mockup Component
# ----------------------------------------------------------------------
def get_native_prototype_component(styles, width=515):
    left_panel = [
        Paragraph("<b>GEOSPATIAL WAR-ROOM MAP VIEW (Uber H3 Res 8)</b>", 
                  ParagraphStyle('MBHead', fontName='DejaVuSans-Bold', fontSize=7.5, leading=10, textColor=colors.HexColor('#0284C7'))),
        Spacer(1, 3),
        Paragraph("<b>Status:</b> Dynamic Choropleth Heatmap Active | <b>Granularity:</b> 460m Hexagons", 
                  ParagraphStyle('MBSub', fontName='DejaVuSans', fontSize=6.8, leading=9, textColor=colors.HexColor('#334155'))),
        Paragraph("&bull; <b>Hex #8860145b:</b> OVI 88.4/100 [<font color='#DC2626'><b>CRITICAL DENGUE SURGE</b></font>] - 42 Cases Projected", 
                  ParagraphStyle('MBItem1', fontName='DejaVuSans', fontSize=6.8, leading=9, textColor=colors.HexColor('#7F1D1D'))),
        Paragraph("&bull; <b>Hex #8860145c:</b> OVI 64.2/100 [<font color='#D97706'><b>ELEVATED RISK</b></font>] - Water Pipe Turbidity Spike", 
                  ParagraphStyle('MBItem2', fontName='DejaVuSans', fontSize=6.8, leading=9, textColor=colors.HexColor('#92400E'))),
        Paragraph("&bull; <b>Hex #8860145d:</b> OVI 18.1/100 [<font color='#16A34A'><b>SAFE / NORMAL</b></font>] - Baseline Clinical Reporting", 
                  ParagraphStyle('MBItem3', fontName='DejaVuSans', fontSize=6.8, leading=9, textColor=colors.HexColor('#166534')))
    ]

    right_panel = [
        Paragraph("<b>GENAI INCIDENT COPILOT (Claude 3.5 RAG)</b>", 
                  ParagraphStyle('CPHead', fontName='DejaVuSans-Bold', fontSize=7.5, leading=10, textColor=colors.HexColor('#7C3AED'))),
        Spacer(1, 3),
        Paragraph("<b>Query:</b> <i>'Generate intervention plan for Ward 14 surge'</i>", 
                  ParagraphStyle('CPQuery', fontName='DejaVuSans-Oblique', fontSize=6.8, leading=9, textColor=colors.HexColor('#475569'))),
        Paragraph("&bull; <b>Action 1:</b> Deploy 4 drone ultra-low volume fogging units to drain corridors.", 
                  ParagraphStyle('CPRec1', fontName='DejaVuSans', fontSize=6.6, leading=8.8, textColor=colors.HexColor('#1E293B'))),
        Paragraph("&bull; <b>Action 2:</b> Pre-allocate 35 platelet units to Civil District Hospital triage.", 
                  ParagraphStyle('CPRec2', fontName='DejaVuSans', fontSize=6.6, leading=8.8, textColor=colors.HexColor('#1E293B'))),
        Paragraph("&bull; <b>Action 3:</b> Broadcast localized boil-water advisory to 12,400 citizen PWAs.", 
                  ParagraphStyle('CPRec3', fontName='DejaVuSans', fontSize=6.6, leading=8.8, textColor=colors.HexColor('#1E293B')))
    ]

    col_w = (width - 15) / 2
    t = Table([[left_panel, right_panel]], colWidths=[col_w, col_w])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#F0F9FF')),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor('#FAF5FF')),
        ('BOX', (0,0), (0,0), 1, colors.HexColor('#7DD3FC')),
        ('BOX', (1,0), (1,0), 1, colors.HexColor('#D8B4FE')),
        ('PADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    return t
