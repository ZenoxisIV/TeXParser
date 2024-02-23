# =============================================================================
# CONFIGURATION FILE
# This is the config file for the TeXParser project.
# Instructions:
# 1. Fill in the necessary information for the paper.
# 2. Run the main.py file to generate the TeX file.
# 3. Compile the TeX file using a LaTeX compiler.
# =============================================================================

TEX_FILENAME = "ICT_Inventory.tex"

PAPER = "a4paper"
FONT_SIZE = 10
PAPER_TYPE = "article"
MARGIN = "2cm"

# ===================================================================================================================
# GUIDELINES:
# If you want to add bold text, enclose the text with \textbf{<text>}.
# If you want to add italicized text, enclose the text with \textit{<text>}.
# If ypu want to add underline text, enclose the text with \underline{<text>}.
# If you want to add a hyperlink, enclose the text with \href{<link>}{<text>}.
# If you want to add a footnote mark, use \footnotemark[<symbol>].
# Lastly, make sure to add a 'r' just right before you write inside the "" to avoid escape characters issues!
# ===================================================================================================================

# If the title is too long on generation, kindly split the text for each line.
# Note: Triple single quotes should be placed at the start and end of the first and last word, respectively.
TITLE = '''ANNEX A-5: EXISTING INFORMATION & COMMUNICATIONS
TECHNOLOGY (ICT) INFRASTRUCTURE INVENTORY'''

AGENCY_NAME = "University of the Philippines Diliman"
RESPONDENT = "Dr. Manuel C. Ramos, Jr."
POSITION = "Director"
DIVISION = "University Computer Center"
TELEPHONE = "8981-8500 local 2050"
EMAIL = "computer.center@upd.edu.ph"

LINK_COLOR = "black"
CITE_COLOR = "black"
URL_COLOR = "black"

# ======================================
OBJECTIVES = {
    "title": "Objectives",

    "b1": "To identify the hardware, software, network and other ICT resources being used to manage information by National Government Agencies (NGAs), Government-owned and Controlled Corporations (GOCCs), State Colleges and Universities (SUCs), and Constitutional and Financial Autonomous Group (CFAG);",

    "b2": "To update existing benchmark and standards; and",

    "b3": "To provide inputs to the MITHI Steering Committee in determining the ICT budget requirements of the agency.",
}

OBJECTIVES_BULLET_OFFSET = "3.5em"
# ======================================

# ======================================
SECTIONS = {
    "1": "HARDWARE / OTHER ICT EQUIPMENT",
    "1.1": "Number of Computing Devices and Peripherals by Type and by Year Acquired",
    "1.2": "Number of Computing Devices and Peripherals by Usage",
    "1.3": "Number of Servers by Capacity and by Location",
    "2": "SOFTWARE, APPLICATION SYSTEMS, INFORMATION SYSTEMS AND DATABASES",
    "2.1": "Operating Systems",
    "2.1.1": "OS for Stand-alone PCs (desktops and laptops)",
    "2.1.2": "OS for Workstations (desktops and laptops)",
    "2.1.3": "OS for Servers",
    "2.2": "Office Automation Software",
    "2.3": "Operational Oversight / Administrative Systems",
    "2.4": "Operational Strategic Information Systems",
    "2.5": "Databases",
    "3": "NETWORK",
}

# For footnote marks in sections, add \protect just before the \footnotemark command.
SECTION_NOTES = {
    "2.3": r"(please refer to the examples\protect\footnotemark[7] below.)",
    "2.4": r"(please refer to the examples\protect\footnotemark[12] below.)",
    "2.5": r"(please include only existing databases)",
}
# ======================================

# ======================================
FILL_OUT_INSTRUCTIONS = {
    "title": "Fill-out Instruction",

    "b1": 'Please count all existing computing devices and peripherals owned or leased by your office that are functioning including those acquired through projects. In case of multi-year contract for leased units, then just write the number of units under the appropriate year when the leased units were acquired. Do not include in succeeding years unless another batch was leased. Reference year is last year. Kindly replace "last year" and preceding years by the actual year number. For example, if last year is 2013, then write 2013 under the 1st column. For last 2 years, write 2012 and for last 3 years, write 2011.',
}

FILL_OUT_INSTRUCTIONS_BULLET_OFFSET = "3.5em"
# ======================================

# ======================================
FOOTNOTES = {
    "1": "In case all three positions are occupied by different persons, then the IS Planner should have priority in answering this survey.",
    "2": "Count only the mobile phones owned or leased by your agency.",
    "3": "Those used in planning, coordination, internal training, monitoring and evaluation",
    "4": "Those used by external clients",
    "5": r"Mark if yes. Examples are OEM license (software is already installed in the hardware) and Enterprise (Perpetual) license, which does not require renewal and is for life long. (source: \href{http://www.manageengine.com/products/service-desk/help/adminguide/configurations/software/software-license-type.html}{http://www.manageengine.com/products/service-desk/help/adminguide/configurations/software/software-license-type.html})",
    "6": "Include only those currently being used by your office or agency.",
    "7": "Payroll System, 201 File Information and Promotion System, Vehicle Monitoring System, Document Tracking System, Attendance and Leave Monitoring System, Financial Management Information System, Inventory System, Records Management System",
    "8": "Write Y for Yes if your agency has intellectual property right to the system. Write N for No.",
    "9": r"\underline{WORKING ENVIRONMENT}: \textbf{S} - Stand alone; \textbf{C} - Client-Server; \textbf{W} - Web-based",
    "10": r"\underline{USE}: \textbf{1} - Public Financial Management; \textbf{2} - Citizen Frontline Services; \textbf{3} - Ease of Doing Business; \textbf{4} - Higher Education; \textbf{5} - Basic Education; \textbf{6} - Health; \textbf{7} - Justice, Peace and Order; \textbf{8} - Energy; \textbf{9} - Land and Other Geospatial Information; \textbf{10} - Disaster and Climate Change Management; \textbf{11} - Public Works and Transport; \textbf{12} - iGov and ICT Infrastructure; \textbf{13} - Transparency and Citizen's Participation; \textbf{14} - Citizen Registry; \textbf{15} - Others, please specify.",
    "11": "Include only those currently being used by your office or agency.",
    "12": r"eCensus, Electronic Filing and Payment System, eTIN, Government e-Procurement System, Automated Customs Operations System, Electronic Customs Clearance Facility, Licensure Examination \& Registration Integrated System, Machine Readable Passports and Visas, Philippine Land Registration and Information System, Government Employees Management Information System, e-GSIS, eReal Property Tax System, Business Permit \& License System, iRegister, Hospital Operations and Management Information System",
    "13": "Write Y for Yes if your agency has intellectual property right to the database. Write N for No.",
    "14": r"\underline{WORKING ENVIRONMENT}: \textbf{S} - Stand alone; \textbf{C} - Client-Server; \textbf{W} - Web-based",
    "15": r"\underline{USE}: \textbf{1} - Public Financial Management; \textbf{2} - Citizen Frontline Services; \textbf{3} - Ease of Doing Business; \textbf{4} - Higher Education; \textbf{5} - Basic Education; \textbf{6} - Health; \textbf{7} - Justice, Peace and Order; \textbf{8} - Energy; \textbf{9} - Land and Other Geospatial Information; \textbf{10} - Disaster and Climate Change Management; \textbf{11} - Public Works and Transport; \textbf{12} - iGov and ICT Infrastructure; \textbf{13} - Transparency and Citizen's Participation; \textbf{14} - Citizen Registry; \textbf{15} - Others, please specify.",
    "16": "Briefly describe the purpose or importance of the database.",
    "17": "Examples of DBMS are MS Excel, MS Access, MS SQL Server, MySQL, IBM's DB2, Oracle SQL, Sybase SQL, Informix, FoxPro",
}
# ======================================

# ======================================
# LEGEND:
# l - left-align
# c - center-align
# r - right-align
# p{<width>} - paragraph (fixed width; word-wrapping)
# | - vertical separator
# ======================================
TABLE_FORMATS = {
    # === SECTION 1 ===
    "1.1": "|p{6.5cm}|c|c|c|c|c|c|c|",
    "1.2": "|l|c|c|c|c|c|",
    "1.3": "|l|c|c|",

    # === SECTION 2 ===
    "2.1.1": "|p{6.5cm}|c|c|",
    "2.1.2": "|p{6.5cm}|c|c|",
    "2.1.3": "|p{6.5cm}|c|c|",

    "2.2": "|p{6.5cm}|c|c|",
    "2.3": "|p{4cm}|c|c|c|c|c|c|",
    "2.4": "|p{4cm}|c|c|c|c|c|c|",
    "2.5": "|p{4cm}|c|c|c|c|c|c|",
}

TABLE_DEFAULT_FIELDS = {
    # === SECTION 1 ===
    "1.1": ["Mainframe", 
            "Servers", 
            "Desktop PC", 
            "Laptop / Notebook / Netbook PC", 
            "Mobile Phone (incl. smart phones)", 
            "Tablet PC", 
            "Multi-function printer (print, copy, etc.)",
            "Printer only", 
            "Digital Camera (Include DSLR, if any)", 
            "Wide-format Printer or Plotter",
            "Small Scanner (ex. flatbed scanner)", 
            "Smart Card Reader", 
            "Wide-format Scanner", 
            "External Hard Drive", 
            "Generator Set"
            ],
    "1.2": ["Servers",
            "Desktop PC",
            "Laptop / Notebook / Netbook PC",
            "Multi-function printer (print, copy, etc.)",
            "Printer only"
            ],
    "1.3": ["Above 4 TB",
            "2 TB to 4 TB",
            "Below 2 TB"
            ],
    
    # === SECTION 2 ===
    "2.1.1": ["Older than Windows XP",
              "Windows XP",
              "Windows Vista",
              "Windows 7",
              "Windows 8 and up",
              "Linux",
              "Mac OS",
              "Mac OS X"
              ],

    "2.1.2": ["Older than Windows XP",
              "Windows XP",
              "Windows Vista",
              "Windows 7",
              "Windows 8 and up",
              "Solaris",
              "Linux",
              "Mac OS"
              ],

    "2.1.3": ["Windows NT",
              "Windows 2000",
              "Windows Server 2003",
              "Windows Server 2008",
              "Windows Server 2012",
              "Solaris",
              "OpenSolaris",
              "OS/2",
              "Linux",
              "Mac OS X Server"
              ],

    "2.2": ["Older than MS Office 2003",
            "MS Office 2003",
            "MS Office XP",
            "MS Office 2007",
            "MS Office 2010",
            "MS Visio",
            "MS Project",
            "Open Project",
            "Open Office",
            ],

    "2.3": [],

    "2.4": [],

    "2.5": ["CRS",
            "iLib",
            "DormApp"],
}
# ======================================


# ======================================
# DATABASE-RELATED SETTINGS
# ======================================
TABLE_FORM_NAMES = {
    "1.1": "cd_year",
    "1.2": "cd_usage",
    "1.3": "servers",
    "2.1.1": "pc_os",
    "2.1.2": "ws_os",
    "2.1.3": "server_os",
    "2.2": "automation_software",
    "2.3": "admin_systems",
    "2.4": "si_systems",
    "2.5": "databases",
}

TABLE_BOOL_COLS = {
    "1.1": [],
    "1.2": [],
    "1.3": [],
    "2.1.1": ["Lifetime"],
    "2.1.2": ["Lifetime"],
    "2.1.3": ["Lifetime"],
    "2.2": ["Lifetime"],
    "2.3": [],
    "2.4": [],
    "2.5": [],
}
# ======================================
