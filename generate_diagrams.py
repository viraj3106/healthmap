import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Set global styles
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#CBD5E1'
plt.rcParams['axes.linewidth'] = 1.0

# -------------------------------------------------------------
# 1. Problem Analysis Diagram: Current Reactive vs HealthMap AI
# -------------------------------------------------------------
def make_problem_diagram():
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#F8FAFC')

    # Draw two comparison boxes
    # Reactive Box
    rect1 = patches.FancyBboxPatch((0.5, 1.0), 4.0, 7.5, boxstyle="round,pad=0.2",
                                  ec="#EF4444", fc="#FEF2F2", lw=2)
    ax.add_patch(rect1)
    ax.text(2.5, 8.0, "CURRENT CONVENTIONAL PARADIGM\n(Reactive & Disconnected)", 
            ha='center', va='center', fontsize=12, fontweight='bold', color="#991B1B")
    
    reactive_steps = [
        "1. Outbreak Occurs Unnoticed (Day 0)",
        "2. Hospital Admissions Surge (Day 7-10)",
        "3. Manual Reporting & Delayed Aggregation (Day 14)",
        "4. Health Department Alerted Post-Crisis (Day 16)",
        "5. Overwhelmed ICUs & Resource Stockouts",
        "6. High Preventable Morbidity & Fatalities"
    ]
    for i, step in enumerate(reactive_steps):
        ax.text(0.8, 6.8 - i*1.0, f"• {step}", fontsize=9.5, color="#7F1D1D", va='top')

    # Proactive Box (HealthMap AI)
    rect2 = patches.FancyBboxPatch((5.5, 1.0), 4.0, 7.5, boxstyle="round,pad=0.2",
                                  ec="#0D9488", fc="#F0FDFA", lw=2)
    ax.add_patch(rect2)
    ax.text(7.5, 8.0, "HEALTHMAP AI PARADIGM\n(Predictive, Spatial & Integrated)", 
            ha='center', va='center', fontsize=12, fontweight='bold', color="#115E59")

    proactive_steps = [
        "1. Precursor Telemetry Detected (Day -10)\n   (Rainfall spikes, water turbidity, OTC pharma surges)",
        "2. Spatial AI Computes Outbreak Vulnerability (Day -7)",
        "3. Automated Early Warning & Containment Zones (Day -5)",
        "4. Proactive Resource & Staff Pre-positioning (Day -3)",
        "5. Targeted Municipal Vector Fogging / Water Neutralization",
        "6. Outbreak Curve Flattened Before Hospital Surge"
    ]
    for i, step in enumerate(proactive_steps):
        ax.text(5.8, 6.8 - i*1.0, f"✔ {step}", fontsize=9.5, color="#134E4A", va='top')

    ax.set_xlim(0, 10)
    ax.set_ylim(0.5, 9.2)
    ax.axis('off')
    plt.title("Epidemiological Paradigm Shift: Traditional Surveillance vs. HealthMap AI", 
              fontsize=14, fontweight='bold', pad=15, color='#0F172A')
    plt.tight_layout()
    plt.savefig("assets/diagram_problem_analysis.png", dpi=300)
    plt.close()

# -------------------------------------------------------------
# 2. Solution Architecture Diagram
# -------------------------------------------------------------
def make_architecture_diagram():
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')

    tiers = [
        {"name": "TIER 4: DECISION & CITIZEN INTERFACES", "color": "#1E3A8A", "bg": "#EFF6FF", 
         "items": "Chief Medical Officer GIS Command Center  |  Hospital Surge Load-Balancer  |  Citizen Mobile Alert PWA  |  GenAI SitRep Copilot", "y": 6.8},
        {"name": "TIER 3: GEOSPATIAL AI & EPIDEMIOLOGY ENGINE", "color": "#0D9488", "bg": "#F0FDFA", 
         "items": "Space-Time Graph Neural Networks (ST-GNN)  |  SEIR-Spatial Diffusion Models  |  Outbreak Vulnerability Index (OVI)  |  Moran's I Clustering", "y": 4.8},
        {"name": "TIER 2: SPATIAL DATA FABRIC & INDEXING", "color": "#4F46E5", "bg": "#EEF2FF", 
         "items": "Uber H3 Hexagonal Grid (Res 8/9)  |  PostgreSQL + PostGIS  |  TimescaleDB Telemetry  |  Geo-Anonymization (Differential Privacy)", "y": 2.8},
        {"name": "TIER 1: MULTI-MODAL INGESTION LAYER", "color": "#0369A1", "bg": "#F0F9FF", 
         "items": "Hospital EHR/OPD Streams  |  Municipal IoT Sensors (Water pH/Turbidity, AQI)  |  IMD Weather & Satellite NDVI  |  Citizen Symptoms Crowdsourcing", "y": 0.8}
    ]

    for tier in tiers:
        # Box
        rect = patches.FancyBboxPatch((0.5, tier["y"]), 9.0, 1.5, boxstyle="round,pad=0.15",
                                      ec=tier["color"], fc=tier["bg"], lw=2)
        ax.add_patch(rect)
        # Title
        ax.text(1.0, tier["y"] + 1.15, tier["name"], fontsize=11, fontweight='bold', color=tier["color"])
        # Items
        ax.text(1.0, tier["y"] + 0.45, tier["items"], fontsize=9.2, color="#334155", weight='medium')

        # Add connector arrow down except for Tier 1
        if tier["y"] > 1.0:
            arrow = patches.FancyArrowPatch((5.0, tier["y"]), (5.0, tier["y"] - 0.5),
                                           arrowstyle='<->', mutation_scale=15, color='#64748B', lw=1.5)
            ax.add_patch(arrow)

    ax.set_xlim(0, 10)
    ax.set_ylim(0.2, 8.8)
    ax.axis('off')
    plt.title("HealthMap AI: 4-Tier Integrated Geospatial Intelligence Architecture", 
              fontsize=14, fontweight='bold', pad=15, color='#0F172A')
    plt.tight_layout()
    plt.savefig("assets/diagram_solution_architecture.png", dpi=300)
    plt.close()

# -------------------------------------------------------------
# 3. Methodology Flowchart Diagram
# -------------------------------------------------------------
def make_methodology_diagram():
    fig, ax = plt.subplots(figsize=(11, 5.5), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#F8FAFC')

    stages = [
        {"num": "PHASE 1", "title": "Data Ingestion &\nSpatial Cleansing", "desc": "EHR, IoT, Satellite & Civic Data\nCleaned, Geocoded & H3-Indexed", "col": "#0284C7", "x": 0.5},
        {"num": "PHASE 2", "title": "Environmental &\nEpidemic Fusion", "desc": "Lagged Rainfall, Temperature,\nPopulation Density & Water Flow", "col": "#0D9488", "x": 2.5},
        {"num": "PHASE 3", "title": "Spatial AI &\nDiffusion Modeling", "desc": "ST-GNN Outbreak Modeling,\nMoran's I & Anomaly Detection", "col": "#6366F1", "x": 4.5},
        {"num": "PHASE 4", "title": "Validation &\nExplainable AI", "desc": "Backtesting historical cycles,\nSHAP Factor Attribution", "col": "#D97706", "x": 6.5},
        {"num": "PHASE 5", "title": "Automated Response\n& Policy Dispatch", "desc": "Geo-fencing, Hospital Surge Alert,\nTargeted Municipal Remediation", "col": "#16A34A", "x": 8.5}
    ]

    for stage in stages:
        # Box
        rect = patches.FancyBboxPatch((stage["x"]-0.1, 1.2), 1.7, 3.8, boxstyle="round,pad=0.15",
                                      ec=stage["col"], fc="#FFFFFF", lw=2)
        ax.add_patch(rect)
        # Phase badge
        badge = patches.FancyBboxPatch((stage["x"]+0.1, 4.3), 1.3, 0.5, boxstyle="round,pad=0.08",
                                       ec=stage["col"], fc=stage["col"], lw=1)
        ax.add_patch(badge)
        ax.text(stage["x"]+0.75, 4.55, stage["num"], color="#FFFFFF", fontsize=9, fontweight='bold', ha='center', va='center')

        # Title
        ax.text(stage["x"]+0.75, 3.8, stage["title"], fontsize=10, fontweight='bold', color="#0F172A", ha='center', va='top')
        # Description
        ax.text(stage["x"]+0.75, 2.5, stage["desc"], fontsize=8, color="#475569", ha='center', va='top')

        # Arrow to next
        if stage["x"] < 8.0:
            arrow = patches.FancyArrowPatch((stage["x"]+1.65, 3.1), (stage["x"]+2.35, 3.1),
                                           arrowstyle='->', mutation_scale=15, color='#94A3B8', lw=2)
            ax.add_patch(arrow)

    ax.set_xlim(0, 10.5)
    ax.set_ylim(0.5, 5.5)
    ax.axis('off')
    plt.title("End-to-End Technical Methodology & Operational Pipeline", 
              fontsize=14, fontweight='bold', pad=15, color='#0F172A')
    plt.tight_layout()
    plt.savefig("assets/diagram_methodology_flowchart.png", dpi=300)
    plt.close()

# -------------------------------------------------------------
# 4. Technologies & Tools Diagram
# -------------------------------------------------------------
def make_tech_stack_diagram():
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')

    cols = [
        {"title": "FRONTEND & GIS", "color": "#0284C7", "x": 0.5,
         "tools": ["Next.js 15 (React 19)", "Tailwind CSS", "Mapbox GL JS / Leaflet", "Deck.gl HexagonLayer", "Apache ECharts"]},
        {"title": "BACKEND & PIPELINES", "color": "#0D9488", "x": 2.9,
         "tools": ["FastAPI (Python 3.13)", "Uvicorn ASGI", "Celery Distributed Workers", "Redis In-Memory Queue", "WebSockets Real-time"]},
        {"title": "SPATIAL DATABASE", "color": "#6366F1", "x": 5.3,
         "tools": ["PostgreSQL 16", "PostGIS Spatial Engine", "Uber H3 Spatial Hex", "TimescaleDB Telemetry", "Prisma ORM"]},
        {"title": "AI / ML & GENAI", "color": "#9333EA", "x": 7.7,
         "tools": ["PyTorch & PyTorch-Geometric", "XGBoost & Scikit-Learn", "GeoPandas & PySAL", "Claude 3.5 Sonnet (LLM)", "LangChain RAG Core"]}
    ]

    for col in cols:
        rect = patches.FancyBboxPatch((col["x"], 0.8), 2.1, 4.3, boxstyle="round,pad=0.15",
                                      ec=col["color"], fc="#F8FAFC", lw=2)
        ax.add_patch(rect)
        header = patches.FancyBboxPatch((col["x"], 4.4), 2.1, 0.7, boxstyle="round,pad=0.1",
                                        ec=col["color"], fc=col["color"], lw=1)
        ax.add_patch(header)
        ax.text(col["x"]+1.05, 4.75, col["title"], color="#FFFFFF", fontsize=9.5, fontweight='bold', ha='center', va='center')

        for i, tool in enumerate(col["tools"]):
            ax.text(col["x"]+0.15, 3.9 - i*0.7, f"• {tool}", fontsize=8.2, color="#1E293B", va='top')

    ax.set_xlim(0, 10.3)
    ax.set_ylim(0.4, 5.6)
    ax.axis('off')
    plt.title("HEALTHMAP AI: Production Technology & Tooling Stack", 
              fontsize=14, fontweight='bold', pad=15, color='#0F172A')
    plt.tight_layout()
    plt.savefig("assets/diagram_tech_stack.png", dpi=300)
    plt.close()

# -------------------------------------------------------------
# 5. Expected Outcomes Diagram (KPI Comparison)
# -------------------------------------------------------------
def make_outcomes_diagram():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.8), dpi=300)
    fig.patch.set_facecolor('#F8FAFC')
    ax1.set_facecolor('#FFFFFF')
    ax2.set_facecolor('#FFFFFF')

    # Bar chart: Outbreak Lead Time
    metrics = ['Outbreak Lead Time\n(Days Ahead)', 'Hospital Bed\nDeficit Reduction (%)', 'Targeted Vector\nFogging Efficiency (%)']
    trad = [2, 18, 25]
    hmap = [14, 76, 88]

    x = np.arange(len(metrics))
    width = 0.35

    ax1.bar(x - width/2, trad, width, label='Traditional Surveillance', color='#94A3B8')
    rects2 = ax1.bar(x + width/2, hmap, width, label='HealthMap AI', color='#0D9488')
    ax1.set_ylabel('Performance Value', fontsize=9.5, fontweight='bold', color='#1E293B')
    ax1.set_title('Operational Metric Improvements', fontsize=11, fontweight='bold', color='#0F172A')
    ax1.set_xticks(x)
    ax1.set_xticklabels(metrics, fontsize=8.5)
    ax1.legend(loc='upper left', fontsize=8.5)
    ax1.grid(axis='y', linestyle='--', alpha=0.5)

    # Attach values above bars
    for bar in rects2:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, yval + 1.5, f"{int(yval)}", ha='center', va='bottom', fontsize=9, fontweight='bold', color='#0D9488')

    # Radar / Attribute comparison on ax2
    labels = ['Predictive Precision', 'Geographic Granularity', 'Data Unification', 'Response Speed', 'Citizen Engagement']
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    trad_scores = [35, 30, 25, 40, 20]
    hmap_scores = [92, 95, 90, 94, 88]

    trad_scores += trad_scores[:1]
    hmap_scores += hmap_scores[:1]
    angles += angles[:1]

    ax2.remove()
    ax2 = fig.add_subplot(122, polar=True)
    ax2.set_facecolor('#FFFFFF')
    ax2.plot(angles, trad_scores, color='#94A3B8', linewidth=1.5, label='Traditional')
    ax2.fill(angles, trad_scores, color='#94A3B8', alpha=0.15)

    ax2.plot(angles, hmap_scores, color='#0284C7', linewidth=2, label='HealthMap AI')
    ax2.fill(angles, hmap_scores, color='#0284C7', alpha=0.25)

    ax2.set_xticks(angles[:-1])
    ax2.set_xticklabels(labels, fontsize=8, fontweight='medium', color='#1E293B')
    ax2.set_yticks([20, 40, 60, 80, 100])
    ax2.set_yticklabels(['20', '40', '60', '80', '100'], fontsize=7, color='#64748B')
    ax2.set_title('Capability Radar Comparison', fontsize=11, fontweight='bold', color='#0F172A', pad=15)
    ax2.legend(loc='lower right', bbox_to_anchor=(1.25, -0.05), fontsize=8.5)

    plt.suptitle("HealthMap AI: Quantitative & Strategic Performance Deliverables", 
                 fontsize=13, fontweight='bold', color='#0F172A', y=1.02)
    plt.tight_layout()
    plt.savefig("assets/diagram_expected_outcomes.png", dpi=300, bbox_inches='tight')
    plt.close()

# -------------------------------------------------------------
# 6. Prototype / Solution Design Mockup Diagram
# -------------------------------------------------------------
def make_prototype_diagram():
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    ax.set_facecolor('#0F172A')
    fig.patch.set_facecolor('#0F172A')

    # Top Navbar
    nav = patches.Rectangle((0, 7.5), 10, 0.8, fc='#1E293B', ec='none')
    ax.add_patch(nav)
    ax.text(0.3, 7.9, "HEALTHMAP AI - Command Center  |  Ward Outbreak Intelligence", color='#38BDF8', fontsize=11, fontweight='bold')
    ax.text(8.5, 7.9, "● LIVE TELEMETRY", color='#10B981', fontsize=9, fontweight='bold')

    # Left Panel: Live GIS Map View Mockup
    map_box = patches.Rectangle((0.3, 0.8), 5.8, 6.4, fc='#1E293B', ec='#334155', lw=1.5)
    ax.add_patch(map_box)
    ax.text(0.6, 6.8, "Geospatial Outbreak Heatmap & Hexagonal Cluster Risk (H3 Res 8)", color='#F8FAFC', fontsize=9.5, fontweight='bold')

    # Draw simulated hexagons & hot spots on the map
    colors = ['#EF4444', '#F59E0B', '#10B981', '#EF4444', '#F59E0B']
    coords = [(2.0, 4.5), (3.2, 5.0), (4.5, 3.8), (2.8, 3.0), (3.8, 2.2)]
    for (cx, cy), col in zip(coords, colors):
        poly = patches.RegularPolygon((cx, cy), numVertices=6, radius=0.6, fc=col, ec='#0F172A', alpha=0.65, lw=1.5)
        ax.add_patch(poly)
    ax.text(2.0, 4.45, "Ward 14\n(Dengue: High)", color='#FFFFFF', fontsize=7.5, ha='center', va='center', fontweight='bold')
    ax.text(4.5, 3.75, "Ward 22\n(Cholera: Low)", color='#FFFFFF', fontsize=7.5, ha='center', va='center', fontweight='bold')

    # Right Panel 1: Outbreak Prediction Graph
    chart_box = patches.Rectangle((6.4, 4.2), 3.3, 3.0, fc='#1E293B', ec='#334155', lw=1.5)
    ax.add_patch(chart_box)
    ax.text(6.6, 6.8, "14-Day Epidemic Forecast (ST-GNN)", color='#38BDF8', fontsize=9, fontweight='bold')
    # Mini curve
    cx = np.linspace(6.6, 9.4, 20)
    cy = 4.8 + 1.2 * np.sin(np.linspace(0, 3, 20))
    ax.plot(cx, cy, color='#F43F5E', lw=2)
    ax.fill_between(cx, cy-0.2, cy+0.2, color='#F43F5E', alpha=0.2)
    ax.text(6.6, 4.5, "Surge Peak Expected: Day 9 (+340%)", color='#FDA4AF', fontsize=7.5)

    # Right Panel 2: GenAI Epidemiological Copilot
    copilot_box = patches.Rectangle((6.4, 0.8), 3.3, 3.1, fc='#1E293B', ec='#334155', lw=1.5)
    ax.add_patch(copilot_box)
    ax.text(6.6, 3.5, "GenAI SitRep Copilot (Claude 3.5)", color='#A855F7', fontsize=9, fontweight='bold')
    ax.text(6.6, 2.8, "Query: 'Action plan for Ward 14 surge?'", color='#94A3B8', fontsize=7.5, fontstyle='italic')
    ax.text(6.6, 2.4, "Recommendation:\n• Dispatch 4 mobile fogging units\n• Pre-allocate 45 platelet units to Civil Hosp\n• Issue contaminated water advisory to Zone B", 
            color='#E2E8F0', fontsize=7.5, va='top')

    ax.set_xlim(0, 10)
    ax.set_ylim(0.4, 8.5)
    ax.axis('off')
    plt.title("HealthMap AI: Interactive Command Center Mockup & Dashboard Interface", 
              fontsize=13, fontweight='bold', pad=12, color='#F8FAFC')
    plt.tight_layout()
    plt.savefig("assets/diagram_prototype_ui.png", dpi=300)
    plt.close()

if __name__ == '__main__':
    print("Generating diagrams for hackathon proposal documents...")
    make_problem_diagram()
    print("1/6 Problem diagram created.")
    make_architecture_diagram()
    print("2/6 Architecture diagram created.")
    make_methodology_diagram()
    print("3/6 Methodology diagram created.")
    make_tech_stack_diagram()
    print("4/6 Tech stack diagram created.")
    make_outcomes_diagram()
    print("5/6 Outcomes diagram created.")
    make_prototype_diagram()
    print("6/6 Prototype diagram created.")
    print("All diagrams generated successfully!")

