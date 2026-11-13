import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_slide_layout = prs.slide_layouts[6] # blank layout

    # Colors
    c_navy = RGBColor(0x0F, 0x25, 0x37)       # Primary title
    c_teal = RGBColor(0x0D, 0x94, 0x88)       # Primary accent
    c_blue = RGBColor(0x02, 0x84, 0xC7)       # Secondary accent
    c_slate = RGBColor(0x33, 0x41, 0x55)      # Body dark
    c_light_slate = RGBColor(0x64, 0x74, 0x8B) # Caption / subtitle
    c_bg_card = RGBColor(0xF8, 0xFA, 0xFC)    # Card background
    c_white = RGBColor(0xFF, 0xFF, 0xFF)
    c_red = RGBColor(0xDC, 0x26, 0x26)
    c_green = RGBColor(0x16, 0xA3, 0x4A)

    # Helper: Add Header to slides (except slide 1)
    def add_header(slide, title_text, category_text="HEALTHMAP AI · Integrated Public Health Intelligence"):
        # Header banner text
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.1))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_cat = tf.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.name = "Calibri"
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = c_teal

        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.name = "Calibri"
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = c_navy
        p_title.space_before = Pt(3)

    # -------------------------------------------------------------------------
    # SLIDE 1: Title Slide (EXACTLY matching the user's uploaded image style!)
    # -------------------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_slide_layout)
    
    # Title box (Top / Middle Center)
    tbox1 = s1.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(11.333), Inches(2.2))
    tf1 = tbox1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    p_main = tf1.paragraphs[0]
    p_main.text = "HEALTHMAP AI"
    p_main.font.name = "Calibri"
    p_main.font.size = Pt(46)
    p_main.font.bold = True
    p_main.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
    p_main.alignment = PP_ALIGN.CENTER

    p_sub = tf1.add_paragraph()
    p_sub.text = "Integrated Geographical Public Health Risk Intelligence"
    p_sub.font.name = "Calibri"
    p_sub.font.size = Pt(22)
    p_sub.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
    p_sub.space_before = Pt(14)
    p_sub.alignment = PP_ALIGN.CENTER

    # Lower Box (Team & Mentor details, centered)
    tbox_bottom = s1.shapes.add_textbox(Inches(1.0), Inches(4.7), Inches(11.333), Inches(1.8))
    tf_b = tbox_bottom.text_frame
    tf_b.word_wrap = True
    tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0

    p_team = tf_b.paragraphs[0]
    p_team.text = "Team Name: Cloud Commanders"
    p_team.font.name = "Calibri"
    p_team.font.size = Pt(18)
    p_team.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
    p_team.alignment = PP_ALIGN.CENTER

    p_mentor = tf_b.add_paragraph()
    p_mentor.text = "Mentor: Mr. S. Venkatesh ( AP - CSE)"
    p_mentor.font.name = "Calibri"
    p_mentor.font.size = Pt(18)
    p_mentor.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
    p_mentor.space_before = Pt(10)
    p_mentor.alignment = PP_ALIGN.CENTER

    # -------------------------------------------------------------------------
    # SLIDE 2: The Problem: Risks are scattered, not seen together
    # -------------------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_slide_layout)
    add_header(s2, "The Problem: Risks Are Scattered, Not Seen Together")

    # Left card: Today's Reality
    c1 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(5.6), Inches(4.8))
    c1.fill.solid()
    c1.fill.fore_color.rgb = RGBColor(0xFE, 0xF2, 0xF2)
    c1.line.color.rgb = RGBColor(0xF8, 0x71, 0x71)
    c1.line.width = Pt(1.5)
    tf_c1 = c1.text_frame
    tf_c1.word_wrap = True
    tf_c1.margin_left = Inches(0.3); tf_c1.margin_right = Inches(0.3); tf_c1.margin_top = Inches(0.3)

    p = tf_c1.paragraphs[0]
    p.text = "TODAY: Health Data Sits in Separate Systems"
    p.font.name = "Calibri"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = RGBColor(0x99, 0x1B, 0x1B)

    bullets = [
        "Disease, weather, environment and geography are stored apart in unconnected silos.",
        "Risks differ by locality, but health administrators cannot see them as one unified picture.",
        "Surveillance updates arrive on a 14 to 21-day delay, forcing reactive crisis responses.",
        "Key Stakeholders Involved: Public-health teams · Local administrators · Authorised analysts."
    ]
    for b in bullets:
        pb = tf_c1.add_paragraph()
        pb.text = "• " + b
        pb.font.name = "Calibri"; pb.font.size = Pt(11); pb.font.color.rgb = RGBColor(0x7F, 0x1D, 0x1D)
        pb.space_before = Pt(10)

    # Right card: 5 Gaps Found
    c2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.7), Inches(5.7), Inches(4.8))
    c2.fill.solid()
    c2.fill.fore_color.rgb = c_bg_card
    c2.line.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)
    c2.line.width = Pt(1.5)
    tf_c2 = c2.text_frame
    tf_c2.word_wrap = True
    tf_c2.margin_left = Inches(0.3); tf_c2.margin_right = Inches(0.3); tf_c2.margin_top = Inches(0.3)

    p = tf_c2.paragraphs[0]
    p.text = "5 Critical Gaps Identified"
    p.font.name = "Calibri"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = c_navy

    gaps = [
        ("1", "Data held in separate systems", "Hospitals, labs, pharmacies, weather portals are disconnected."),
        ("2", "No combined, location-wise view", "District aggregates hide hyper-local street-level breeding spots."),
        ("3", "Weather and disease trends not linked", "Rainfall/temperature spikes precede outbreaks but are ignored."),
        ("4", "Estimates mixed up with confirmed reports", "Lack of clear separation between projections and lab cases."),
        ("5", "Hard to prioritise limited resources", "Fogging machines, beds, and medicines dispatched reactively.")
    ]
    for num, title, desc in gaps:
        pb = tf_c2.add_paragraph()
        pb.text = f"[{num}] {title}: {desc}"
        pb.font.name = "Calibri"; pb.font.size = Pt(10.5); pb.font.color.rgb = c_slate
        pb.space_before = Pt(8)

    p_bound = tf_c2.add_paragraph()
    p_bound.text = "Our Boundary: Model estimates support decisions; they are always shown separately from confirmed surveillance reports."
    p_bound.font.name = "Calibri"; p_bound.font.size = Pt(9.5); p_bound.font.italic = True; p_bound.font.color.rgb = c_teal
    p_bound.space_before = Pt(10)

    # -------------------------------------------------------------------------
    # SLIDE 3: Our Solution: One Platform, One Picture
    # -------------------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_slide_layout)
    add_header(s3, "Our Solution: One Platform, One Picture")

    pillars = [
        ("1. INTEGRATE", "Authorised disease surveillance, weather, environmental and geographical data into a single, unified PostGIS system.", RGBColor(0x02, 0x84, 0xC7), RGBColor(0xF0, 0xF9, 0xFF)),
        ("2. ASSESS", "Location-based predictive risk for mosquito-borne (Dengue), respiratory (AQI), and flood-related contamination hazards.", RGBColor(0x0D, 0x94, 0x88), RGBColor(0xF0, 0xFD, 0xFA)),
        ("3. VISUALISE", "Interactive GIS heatmap with intuitive filtering by disease, location, time period, and risk level on an H3 hexagonal grid.", RGBColor(0x63, 0x66, 0xF1), RGBColor(0xEE, 0xF2, 0xFF)),
        ("4. ACT", "Automated early-warning alerts, preventive citizen guidance, and resource prioritisation for frontline health teams.", RGBColor(0x16, 0xA3, 0x4A), RGBColor(0xF0, 0xFD, 0xF4))
    ]

    for i, (title, desc, col, bg) in enumerate(pillars):
        x = Inches(0.8 + i * 2.95)
        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(2.8), Inches(4.3))
        card.fill.solid(); card.fill.fore_color.rgb = bg
        card.line.color.rgb = col; card.line.width = Pt(1.5)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.2); tf.margin_right = Inches(0.2); tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Calibri"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = "Calibri"; p2.font.size = Pt(11); p2.font.color.rgb = c_slate
        p2.space_before = Pt(12)

    # Bottom notice banner
    bot_b = s3.shapes.add_textbox(Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.6))
    p_bot = bot_b.text_frame.paragraphs[0]
    p_bot.text = "✓ Operational Principle: Model estimates are always shown separately from confirmed surveillance reports."
    p_bot.font.name = "Calibri"; p_bot.font.size = Pt(11); p_bot.font.bold = True; p_bot.font.color.rgb = c_teal

    # -------------------------------------------------------------------------
    # SLIDE 4: Data We Bring Together
    # -------------------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_slide_layout)
    add_header(s4, "Data We Bring Together (Multi-Source Ingestion Fabric)")

    data_sources = [
        ("1. Disease Surveillance", "Authorised clinical reports on selected diseases (ICD-10 coded), used strictly in aggregated, anonymized form to monitor trend velocities.", RGBColor(0x02, 0x84, 0xC7)),
        ("2. Weather & Meteorology", "Rainfall volume, ambient temperature, and relative humidity trends from meteorological services that shape mosquito breeding cycles.", RGBColor(0x0D, 0x94, 0x88)),
        ("3. Environmental Indicators", "Municipal sensor conditions such as water logging, pipeline turbidity, drainage quality, and local sanitation contexts.", RGBColor(0x63, 0x66, 0xF1)),
        ("4. Geographical Data", "Municipal ward boundaries, elevation terrain, flood-prone lowlands, population densities, and informal settlement ratios.", RGBColor(0x93, 0x33, 0xEA))
    ]

    for i, (title, desc, col) in enumerate(data_sources):
        y = Inches(1.7 + i * 1.15)
        bar = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.733), Inches(0.95))
        bar.fill.solid(); bar.fill.fore_color.rgb = c_bg_card
        bar.line.color.rgb = col; bar.line.width = Pt(1.5)
        tf = bar.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3); tf.margin_right = Inches(0.3); tf.margin_top = Inches(0.15)

        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Calibri"; p.font.size = Pt(12); p.font.bold = True; p.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = "Calibri"; p2.font.size = Pt(10); p2.font.color.rgb = c_slate
        p2.space_before = Pt(2)

    # Privacy notice
    p_box = s4.shapes.add_textbox(Inches(0.8), Inches(6.4), Inches(11.733), Inches(0.5))
    p_priv = p_box.text_frame.paragraphs[0]
    p_priv.text = "Privacy First: Aggregated population data only, with zero personal identifiers and role-based access for authorised officials."
    p_priv.font.name = "Calibri"; p_priv.font.size = Pt(10.5); p_priv.font.bold = True; p_priv.font.color.rgb = c_teal

    # -------------------------------------------------------------------------
    # SLIDE 5: How HEALTHMAP AI Works (7-Step Pipeline)
    # -------------------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_slide_layout)
    add_header(s5, "How HEALTHMAP AI Works: End-to-End Operational Pipeline")

    steps = [
        ("1. COLLECT", "Disease, weather, environment & geo streams"),
        ("2. CLEAN & LINK", "Aggregate & index to PostGIS / H3 hexagons"),
        ("3. MODEL", "Multi-model AI selects algorithm per hazard"),
        ("4. SCORE", "Compute Outbreak Vulnerability (OVI) 0-100"),
        ("5. VISUALISE", "Interactive GIS heatmap with filters"),
        ("6. ALERT", "SitRep bulletins for health admins"),
        ("7. ACT", "Prioritise fogging, beds & public outreach")
    ]

    for i, (st, desc) in enumerate(steps):
        x = Inches(0.8 + i * 1.68)
        card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(1.6), Inches(2.8))
        card.fill.solid(); card.fill.fore_color.rgb = RGBColor(0xF0, 0xFD, 0xFA)
        card.line.color.rgb = c_teal; card.line.width = Pt(1.2)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.1); tf.margin_right = Inches(0.1); tf.margin_top = Inches(0.2)

        p = tf.paragraphs[0]
        p.text = st
        p.font.name = "Calibri"; p.font.size = Pt(9.5); p.font.bold = True; p.font.color.rgb = c_teal; p.alignment = PP_ALIGN.CENTER

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = "Calibri"; p2.font.size = Pt(8.5); p2.font.color.rgb = c_slate; p2.space_before = Pt(8); p2.alignment = PP_ALIGN.CENTER

    # 3 Pillars underneath
    bottom_cards = [
        ("Explainable Risk", "Every score details its data sources, contributing factors, confidence interval, and limitations.", c_blue),
        ("Private by Design", "Strict aggregation, differential privacy geo-jittering, and role-based access for authorised teams.", c_teal),
        ("What Is New", "Simultaneous multi-hazard surveillance on one map, with cross-hazard overlap and resource priorities.", RGBColor(0x93, 0x33, 0xEA))
    ]
    for i, (btitle, bdesc, bcol) in enumerate(bottom_cards):
        x = Inches(0.8 + i * 3.95)
        c = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(4.9), Inches(3.8), Inches(1.8))
        c.fill.solid(); c.fill.fore_color.rgb = c_bg_card
        c.line.color.rgb = bcol; c.line.width = Pt(1.5)
        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.2); tf.margin_right = Inches(0.2); tf.margin_top = Inches(0.2)

        p = tf.paragraphs[0]
        p.text = btitle
        p.font.name = "Calibri"; p.font.size = Pt(12); p.font.bold = True; p.font.color.rgb = bcol

        p2 = tf.add_paragraph()
        p2.text = bdesc
        p2.font.name = "Calibri"; p2.font.size = Pt(10); p2.font.color.rgb = c_slate; p2.space_before = Pt(4)

    # -------------------------------------------------------------------------
    # SLIDE 6: Core Features
    # -------------------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_slide_layout)
    add_header(s6, "Core Features of HEALTHMAP AI")

    features = [
        ("1. Unified Data Dashboard", "Integrates disease surveillance, weather feeds, environmental sensors, and geography in a single pane of glass.", c_blue),
        ("2. Location-Based Risk Assessment", "Dynamically computes hyper-local risk scores per disease and public-health hazard at sub-ward scale.", c_teal),
        ("3. Interactive GIS Heatmap", "Real-time interactive map with multi-layer filtering by disease, locality, time window, and risk severity.", RGBColor(0x63, 0x66, 0xF1)),
        ("4. Centralised Alerts & Reports", "Instant situation briefings and alert routing directly for public-health teams and municipal administrators.", RGBColor(0x16, 0xA3, 0x4A)),
        ("5. Tailored Preventive Guidance", "Automated, location-specific advisories based on official public health guidelines broadcast to citizens.", RGBColor(0xD9, 0x77, 0x06)),
        ("6. Multi-Hazard Coverage", "Unified intelligence covering vector-borne diseases, acute respiratory infections, and flood/waterborne hazards.", RGBColor(0x93, 0x33, 0xEA))
    ]

    for i, (title, desc, col) in enumerate(features):
        row = i // 2
        col_idx = i % 2
        x = Inches(0.8 + col_idx * 5.95)
        y = Inches(1.7 + row * 1.6)

        c = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.75), Inches(1.4))
        c.fill.solid(); c.fill.fore_color.rgb = c_bg_card
        c.line.color.rgb = col; c.line.width = Pt(1.5)
        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.25); tf.margin_right = Inches(0.25); tf.margin_top = Inches(0.18)

        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Calibri"; p.font.size = Pt(12); p.font.bold = True; p.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = "Calibri"; p2.font.size = Pt(10); p2.font.color.rgb = c_slate; p2.space_before = Pt(3)

    # -------------------------------------------------------------------------
    # SLIDE 7: Multi-Model AI Architecture
    # -------------------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_slide_layout)
    add_header(s7, "Multi-Model AI Architecture")

    models = [
        ("MOSQUITO-BORNE (Dengue, Malaria)",
         "Inputs: Weather-lagged case trends, rainfall accumulation, temperature, stagnant-water pools.\nApproach: Time-series forecasting (Prophet / ARIMA) coupled with XGBoost regression & Moran's I spatial clustering.",
         RGBColor(0x0D, 0x94, 0x88)),
        ("RESPIRATORY INFECTIONS",
         "Inputs: Seasonal influenza patterns, Air Quality Index (PM2.5/PM10), temperature drops, population density.\nApproach: Distributed Lag Non-Linear Models (DLNM) + Scikit-Learn Random Forest classifiers.",
         RGBColor(0x02, 0x84, 0xC7)),
        ("FLOOD & WATER CONTAMINATION",
         "Inputs: Precipitation intensity, terrain elevation, storm drainage capacity, municipal water turbidity sensors.\nApproach: Geospatial feature engineering + Gradient Boosted Decision Trees for contamination spillover.",
         RGBColor(0x63, 0x66, 0xF1))
    ]

    for i, (title, desc, col) in enumerate(models):
        y = Inches(1.7 + i * 1.5)
        card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.733), Inches(1.3))
        card.fill.solid(); card.fill.fore_color.rgb = c_bg_card
        card.line.color.rgb = col; card.line.width = Pt(1.5)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3); tf.margin_right = Inches(0.3); tf.margin_top = Inches(0.15)

        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Calibri"; p.font.size = Pt(12); p.font.bold = True; p.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = "Calibri"; p2.font.size = Pt(10); p2.font.color.rgb = c_slate; p2.space_before = Pt(3)

    box_sel = s7.shapes.add_textbox(Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.6))
    p_sel = box_sel.text_frame.paragraphs[0]
    p_sel.text = "✓ An intelligent Model Selector picks or blends the optimal model for each hazard, reporting confidence and limitations with every score."
    p_sel.font.name = "Calibri"; p_sel.font.size = Pt(11); p_sel.font.bold = True; p_sel.font.color.rgb = c_teal

    # -------------------------------------------------------------------------
    # SLIDE 8: Explainable Risk Summary (Illustrative)
    # -------------------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_slide_layout)
    add_header(s8, "Explainable Risk Summary (Illustrative Output)")

    # Score Box Left
    sbox = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(4.2), Inches(4.8))
    sbox.fill.solid(); sbox.fill.fore_color.rgb = RGBColor(0xFE, 0xF2, 0xF2)
    sbox.line.color.rgb = RGBColor(0xEF, 0x44, 0x44); sbox.line.width = Pt(2)
    tf_sb = sbox.text_frame
    tf_sb.word_wrap = True
    tf_sb.margin_left = Inches(0.3); tf_sb.margin_top = Inches(0.4)

    p = tf_sb.paragraphs[0]
    p.text = "HAZARD ASSESSMENT"
    p.font.name = "Calibri"; p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = RGBColor(0x99, 0x1B, 0x1B)

    p_val = tf_sb.add_paragraph()
    p_val.text = "78 / 100"
    p_val.font.name = "Calibri"; p_val.font.size = Pt(44); p_val.font.bold = True; p_val.font.color.rgb = RGBColor(0xDC, 0x26, 0x26)
    p_val.space_before = Pt(8)

    p_badge = tf_sb.add_paragraph()
    p_badge.text = "LEVEL: HIGH RISK (Dengue Surge)"
    p_badge.font.name = "Calibri"; p_badge.font.size = Pt(13); p_badge.font.bold = True; p_badge.font.color.rgb = RGBColor(0x99, 0x1B, 0x1B)
    p_badge.space_before = Pt(6)

    p_loc = tf_sb.add_paragraph()
    p_loc.text = "Location: Ward 14 (Central Drainage Zone)\nLead Time: 10-14 Days Advance Warning"
    p_loc.font.name = "Calibri"; p_loc.font.size = Pt(10.5); p_loc.font.color.rgb = c_slate
    p_loc.space_before = Pt(14)

    # Explanation Right
    rbox = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.3), Inches(1.7), Inches(7.2), Inches(4.8))
    rbox.fill.solid(); rbox.fill.fore_color.rgb = c_bg_card
    rbox.line.color.rgb = RGBColor(0xCB, 0xD5, 0xE1); rbox.line.width = Pt(1.5)
    tf_rb = rbox.text_frame
    tf_rb.word_wrap = True
    tf_rb.margin_left = Inches(0.4); tf_rb.margin_top = Inches(0.3)

    p = tf_rb.paragraphs[0]
    p.text = "Why This Score? (SHAP Factor Attribution)"
    p.font.name = "Calibri"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = c_navy

    factors = [
        ("• Recent Rainfall Spikes (+42%):", "Heavy precipitation 10 days ago caused stagnant water pooling in unpaved lanes."),
        ("• Clinical Case Trajectory (+28%):", "Neighboring primary clinic reported abnormal fever/headache footfalls."),
        ("• Stagnant-Water Conditions (+18%):", "Sentinel-2 satellite NDVI indicates high moisture persistence in lowlands."),
        ("• Population Vulnerability (+12%):", "High population density with high proportion of informal housing.")
    ]
    for ft, fd in factors:
        p_f = tf_rb.add_paragraph()
        p_f.text = f"{ft} {fd}"
        p_f.font.name = "Calibri"; p_f.font.size = Pt(10); p_f.font.color.rgb = c_slate
        p_f.space_before = Pt(6)

    p_meta = tf_rb.add_paragraph()
    p_meta.text = "Sources: Authorised hospital registers, IMD weather stations, Sentinel-2 GIS\nConfidence: Medium-High (87%) | Limits: Model estimate for preventive action, not a clinical count."
    p_meta.font.name = "Calibri"; p_meta.font.size = Pt(9.5); p_meta.font.bold = True; p_meta.font.color.rgb = c_teal
    p_meta.space_before = Pt(12)

    # -------------------------------------------------------------------------
    # SLIDE 9: Interactive GIS Dashboard (Concept)
    # -------------------------------------------------------------------------
    s9 = prs.slides.add_slide(blank_slide_layout)
    add_header(s9, "Interactive GIS Dashboard (Concept Mockup)")

    # 3 sections: Filters, Map Heatmap, Alerts & Actions
    d_panels = [
        ("1. Multi-Layer Filters", "• Disease: Dengue, Malaria, Cholera\n• Location: Ward, Sub-ward, H3 Hexagon\n• Time Period: Past 30 Days + 14-Day Forecast\n• Risk Category: Low · Medium · High", c_blue, Inches(0.8), Inches(3.6)),
        ("2. Real-time GIS Heatmap", "• Hexagonal spatial grid (Uber H3 Res 8: 460m)\n• Color-coded risk clusters (Green / Amber / Red)\n• Environmental overlays: Water pipelines & AQI\n• Time slider for simulated outbreak diffusion", c_teal, Inches(4.7), Inches(4.3)),
        ("3. Alerts & Action Hub", "• High-Risk Localities: Priority flagging\n• Overlapping Hazards: Flood + Vector breeding\n• Suggested Inspections: Targeted larvicide fogging\n• Prevention Advice: Pre-allocate hospital ICU beds", RGBColor(0x93, 0x33, 0xEA), Inches(9.3), Inches(3.2))
    ]

    for title, desc, col, x, w in d_panels:
        c = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), w, Inches(4.8))
        c.fill.solid(); c.fill.fore_color.rgb = c_bg_card
        c.line.color.rgb = col; c.line.width = Pt(1.5)
        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.2); tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Calibri"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = "Calibri"; p2.font.size = Pt(10.5); p2.font.color.rgb = c_slate; p2.space_before = Pt(12)

    # -------------------------------------------------------------------------
    # SLIDE 10: New and Advanced Features
    # -------------------------------------------------------------------------
    s10 = prs.slides.add_slide(blank_slide_layout)
    add_header(s10, "New and Advanced Features")

    adv_features = [
        ("Multi-Model AI", "Selects or ensembles specialized machine learning models per disease or hazard rather than a generic one-size-fits-all model.", c_blue),
        ("Explainable Summaries", "Clear breakdown of contributing sources, environmental factors, confidence levels, and technical limitations.", c_teal),
        ("Cross-Hazard View", "Identifies geographic areas facing overlapping simultaneous risks (e.g. waterlogging + dengue breeding).", RGBColor(0x63, 0x66, 0xF1)),
        ("Resource Prioritisation", "Algorithmic decision support for drone fogging, municipal sanitation crews, and primary clinic staffing.", RGBColor(0x16, 0xA3, 0x4A)),
        ("Privacy-Preserving Analytics", "Differential privacy geo-perturbation, population-level aggregation, and secure role-based access.", RGBColor(0x93, 0x33, 0xEA))
    ]

    for i, (title, desc, col) in enumerate(adv_features):
        y = Inches(1.7 + i * 0.95)
        bar = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.733), Inches(0.8))
        bar.fill.solid(); bar.fill.fore_color.rgb = c_bg_card
        bar.line.color.rgb = col; bar.line.width = Pt(1.5)
        tf = bar.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.25); tf.margin_top = Inches(0.12)

        p = tf.paragraphs[0]
        p.text = f"{i+1}. {title}: "
        p.font.name = "Calibri"; p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = col

        run = p.add_run()
        run.text = desc
        run.font.name = "Calibri"; run.font.size = Pt(10); run.font.bold = False; run.font.color.rgb = c_slate

    # Cross hazard banner
    ch_box = s10.shapes.add_textbox(Inches(0.8), Inches(6.4), Inches(11.733), Inches(0.5))
    p_ch = ch_box.text_frame.paragraphs[0]
    p_ch.text = "★ Cross-Hazard Synergy: Flood Exposure + Mosquito Breeding -> Spatial Overlap = Priority Locality for Immediate Action."
    p_ch.font.name = "Calibri"; p_ch.font.size = Pt(10.5); p_ch.font.bold = True; p_ch.font.color.rgb = c_teal

    # -------------------------------------------------------------------------
    # SLIDE 11: Technology and Architecture
    # -------------------------------------------------------------------------
    s11 = prs.slides.add_slide(blank_slide_layout)
    add_header(s11, "Technology and Architecture Stack")

    tech_cols = [
        ("INTERFACE", "React / Next.js 15\nFlutter Mobile PWA\nMapbox GL JS & Leaflet\nDeck.gl HexagonLayer\nApache ECharts", c_blue),
        ("SERVICES & APIS", "Python 3.13\nFastAPI Microservices\nUvicorn ASGI Engine\nCelery Task Queues\nRedis Caching", c_teal),
        ("INTELLIGENCE CORE", "Scikit-Learn\nXGBoost Regressors\nTime-Series Forecasting\nPyTorch Geometric\nClaude 3.5 Sonnet RAG", RGBColor(0x63, 0x66, 0xF1)),
        ("DATA & SPATIAL FABRIC", "PostgreSQL 16\nPostGIS Spatial Extension\nUber H3 Discrete Hex\nTimescaleDB Telemetry\nGeoPandas & PySAL", RGBColor(0x93, 0x33, 0xEA))
    ]

    for i, (title, items, col) in enumerate(tech_cols):
        x = Inches(0.8 + i * 2.95)
        c = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(2.8), Inches(4.8))
        c.fill.solid(); c.fill.fore_color.rgb = c_bg_card
        c.line.color.rgb = col; c.line.width = Pt(1.5)
        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.2); tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Calibri"; p.font.size = Pt(12); p.font.bold = True; p.font.color.rgb = col; p.alignment = PP_ALIGN.CENTER

        p2 = tf.add_paragraph()
        p2.text = items
        p2.font.name = "Calibri"; p2.font.size = Pt(11); p2.font.color.rgb = c_slate; p2.space_before = Pt(14); p2.alignment = PP_ALIGN.CENTER

    # -------------------------------------------------------------------------
    # SLIDE 12: Privacy and Responsible Use
    # -------------------------------------------------------------------------
    s12 = prs.slides.add_slide(blank_slide_layout)
    add_header(s12, "Privacy and Responsible Use Safeguards")

    pillars_privacy = [
        ("1. Aggregated Analytics", "Population-level data only; no individual patient tracking or personally identifiable information (PII).", c_blue),
        ("2. Role-Based Access", "Authorised municipal health users see strictly what their administrative clearance allows (RBAC).", c_teal),
        ("3. Estimates vs. Facts", "All AI model outputs are prominently labelled as statistical estimates, distinct from confirmed lab tests.", RGBColor(0xD9, 0x77, 0x06)),
        ("4. Approved Guidance", "All automated citizen preventive messages strictly mirror approved WHO and Ministry of Health protocols.", RGBColor(0x16, 0xA3, 0x4A))
    ]

    for i, (title, desc, col) in enumerate(pillars_privacy):
        y = Inches(1.8 + i * 1.1)
        bar = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.733), Inches(0.9))
        bar.fill.solid(); bar.fill.fore_color.rgb = c_bg_card
        bar.line.color.rgb = col; bar.line.width = Pt(1.5)
        tf = bar.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3); tf.margin_top = Inches(0.12)

        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Calibri"; p.font.size = Pt(12); p.font.bold = True; p.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = "Calibri"; p2.font.size = Pt(10.5); p2.font.color.rgb = c_slate; p2.space_before = Pt(2)

    box_disclaimer = s12.shapes.add_textbox(Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.6))
    p_disc = box_disclaimer.text_frame.paragraphs[0]
    p_disc.text = "Important Mandate: HealthMap AI is a clinical decision-support and prevention tool for health authorities; it does not diagnose patients."
    p_disc.font.name = "Calibri"; p_disc.font.size = Pt(11); p_disc.font.bold = True; p_disc.font.color.rgb = RGBColor(0x99, 0x1B, 0x1B)

    # -------------------------------------------------------------------------
    # SLIDE 13: Implementation Roadmap
    # -------------------------------------------------------------------------
    s13 = prs.slides.add_slide(blank_slide_layout)
    add_header(s13, "Implementation Roadmap")

    phases = [
        ("PHASE 1: DATA FOUNDATION", "Connect authorised clinical and environmental datasets; configure PostgreSQL/PostGIS spatial store and Uber H3 hexagonal partitions.", c_blue),
        ("PHASE 2: MODEL BUILDING", "Train, calibrate and validate multi-model AI architectures per hazard (Time-series forecasting, DLNM, XGBoost).", c_teal),
        ("PHASE 3: DASHBOARD & ALERTS", "Build interactive GIS heatmap frontend, explainable SHAP summaries, automated SitRep alerts, and role-based access.", RGBColor(0x63, 0x66, 0xF1)),
        ("PHASE 4: PILOT & REFINE", "Deploy pilot in selected municipal corporation ward; test with active frontline health teams and incorporate feedback.", RGBColor(0x16, 0xA3, 0x4A))
    ]

    for i, (title, desc, col) in enumerate(phases):
        y = Inches(1.8 + i * 1.1)
        bar = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(11.733), Inches(0.9))
        bar.fill.solid(); bar.fill.fore_color.rgb = c_bg_card
        bar.line.color.rgb = col; bar.line.width = Pt(1.5)
        tf = bar.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3); tf.margin_top = Inches(0.12)

        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Calibri"; p.font.size = Pt(12); p.font.bold = True; p.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = "Calibri"; p2.font.size = Pt(10.5); p2.font.color.rgb = c_slate; p2.space_before = Pt(2)

    p_note = s13.shapes.add_textbox(Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.5))
    p_n = p_note.text_frame.paragraphs[0]
    p_n.text = "Phases follow a structured engineering lifecycle and can be adapted to specific municipal pilot partner timelines."
    p_n.font.name = "Calibri"; p_n.font.size = Pt(10.5); p_n.font.italic = True; p_n.font.color.rgb = c_slate

    # -------------------------------------------------------------------------
    # SLIDE 14: Expected Impact and Responsible Use
    # -------------------------------------------------------------------------
    s14 = prs.slides.add_slide(blank_slide_layout)
    add_header(s14, "Expected Impact and Responsible Use")

    # Left: Expected Impact
    c_left = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.2))
    c_left.fill.solid(); c_left.fill.fore_color.rgb = RGBColor(0xF0, 0xFD, 0xFA)
    c_left.line.color.rgb = c_teal; c_left.line.width = Pt(1.5)
    tf_l = c_left.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = Inches(0.3); tf_l.margin_top = Inches(0.3)

    p = tf_l.paragraphs[0]
    p.text = "EXPECTED SOCIETAL IMPACT"
    p.font.name = "Calibri"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = c_teal

    impacts = [
        "Spot emerging geographical risks 10-14 days early.",
        "Prioritise preventive municipal action (fogging & sanitization).",
        "Coordinate community protection and protect vulnerable slums.",
        "Flatten hospital admission curves and eliminate ICU bottlenecks.",
        "Restore public trust with transparent, science-backed guidance."
    ]
    for imp in impacts:
        pi = tf_l.add_paragraph()
        pi.text = "✔ " + imp
        pi.font.name = "Calibri"; pi.font.size = Pt(10.5); pi.font.color.rgb = RGBColor(0x13, 0x4E, 0x4A)
        pi.space_before = Pt(8)

    # Right: Responsible Use
    c_right = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.2))
    c_right.fill.solid(); c_right.fill.fore_color.rgb = RGBColor(0xF0, 0xF9, 0xFF)
    c_right.line.color.rgb = c_blue; c_right.line.width = Pt(1.5)
    tf_r = c_right.text_frame
    tf_r.word_wrap = True
    tf_r.margin_left = Inches(0.3); tf_r.margin_top = Inches(0.3)

    p = tf_r.paragraphs[0]
    p.text = "RESPONSIBLE USE COMMITMENTS"
    p.font.name = "Calibri"; p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = c_blue

    ethics = [
        "Estimates are clearly labelled and never shown as confirmed cases.",
        "Aggregated population data only with strict role-based access.",
        "Transparent limits: prediction quality depends on data freshness.",
        "Health advice rigorously mirrors approved public health directives.",
        "Provides decision-support for authorities, never automated diagnosis."
    ]
    for eth in ethics:
        pe = tf_r.add_paragraph()
        pe.text = "• " + eth
        pe.font.name = "Calibri"; pe.font.size = Pt(10.5); pe.font.color.rgb = RGBColor(0x0C, 0x4A, 0x6E)
        pe.space_before = Pt(8)

    # Bottom Tagline
    box_tag = s14.shapes.add_textbox(Inches(0.8), Inches(6.25), Inches(11.733), Inches(0.7))
    p_tag = box_tag.text_frame.paragraphs[0]
    p_tag.text = "One map. Clear reasons. Faster, fairer public-health action."
    p_tag.font.name = "Calibri"; p_tag.font.size = Pt(16); p_tag.font.bold = True; p_tag.font.color.rgb = c_navy; p_tag.alignment = PP_ALIGN.CENTER

    # -------------------------------------------------------------------------
    # SLIDE 15: Thank You Slide
    # -------------------------------------------------------------------------
    s15 = prs.slides.add_slide(blank_slide_layout)
    
    tbox_ty = s15.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.333), Inches(4.0))
    tf_ty = tbox_ty.text_frame
    tf_ty.word_wrap = True

    p_ty = tf_ty.paragraphs[0]
    p_ty.text = "Thank You"
    p_ty.font.name = "Calibri"; p_ty.font.size = Pt(44); p_ty.font.bold = True; p_ty.font.color.rgb = c_navy; p_ty.alignment = PP_ALIGN.CENTER

    p_tysub = tf_ty.add_paragraph()
    p_tysub.text = "HEALTHMAP AI: Seeing Public-Health Risk, Place by Place"
    p_tysub.font.name = "Calibri"; p_tysub.font.size = Pt(20); p_tysub.font.bold = True; p_tysub.font.color.rgb = c_teal; p_tysub.space_before = Pt(12); p_tysub.alignment = PP_ALIGN.CENTER

    p_team_end = tf_ty.add_paragraph()
    p_team_end.text = "Team Name: Cloud Commanders"
    p_team_end.font.name = "Calibri"; p_team_end.font.size = Pt(18); p_team_end.font.color.rgb = c_slate; p_team_end.space_before = Pt(26); p_team_end.alignment = PP_ALIGN.CENTER

    p_mentor_end = tf_ty.add_paragraph()
    p_mentor_end.text = "Mentor: Mr. S. Venkatesh ( AP - CSE)"
    p_mentor_end.font.name = "Calibri"; p_mentor_end.font.size = Pt(18); p_mentor_end.font.color.rgb = c_slate; p_mentor_end.space_before = Pt(8); p_mentor_end.alignment = PP_ALIGN.CENTER

    p_q = tf_ty.add_paragraph()
    p_q.text = "Questions & Discussion"
    p_q.font.name = "Calibri"; p_q.font.size = Pt(18); p_q.font.bold = True; p_q.font.color.rgb = c_blue; p_q.space_before = Pt(24); p_q.alignment = PP_ALIGN.CENTER

    out_path = "HEALTHMAP_AI_Presentation.pptx"
    prs.save(out_path)
    print(f"PowerPoint Presentation created successfully: {out_path}")

if __name__ == '__main__':
    create_deck()

