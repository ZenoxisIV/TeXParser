# =============================================================================
# MAIN CONFIGURATION FILE
# This is the main config file for the TeXParser project.
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

# If you want to add the following characters as TEXT, use the following mapping:
# %: \%
# $: \$
# &: \&
# #: \#
# _: \_
# {: \{
# }: \}
# ~: \textasciitilde
# ^: \textasciicircum
# \: \textbackslash
# <: $<$
# >: $>$

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
    "4": r"SECURITY, DISASTER RECOVERY \& BACK-UP",
    "5": "DATA ARCHIVING",
    "6": "SPECIAL SOLUTIONS AND OTHER SERVICES",
    "7": "DATA CENTER",
    "8": "ICT PROJECTS",
    "8.1": "Details of Ongoing ICT Projects",
    "8.2": "Issues Encountered in the Implementation of ICT Projects"
}

# For footnote marks in sections, add \protect just before the \footnotemark command.
SECTION_NOTES = {
    "2.3": r"(please refer to the examples\protect\footnotemark[7] below.)",
    "2.4": r"(please refer to the examples\protect\footnotemark[12] below.)",
    "2.5": r"(please include only existing databases)",
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

QUESTIONS = {
    "3": [
        "Does your agency have a Local Area Network (LAN)?",
        "Does your agency have an Intranet?",
        "If yes, does your agency have a Virtual Private Network (VPN)?",
        "Does your agency have a Wide Area Network (WAN)?",
        "Does your agency have a Private Automatic Branch Exchange (PABX or PBX)?",
        "If yes, what is the PBX set up?",
        "Is your agency connected to the Internet?",
        "What is/are your agency's mode/s of access to the Internet? (Check all items that are applicable)",
        "Who is (are) your Internet Service Provider(s)? If more than one, please state who is the primary and who is the secondary provider?",
        "What is the combined internet bandwidth (voice and data)?",
        "How many employees have access to the Internet in the office?",
        "How many employees have their own official e-mail address?",
        "Does your agency have a web site?",
        "If YES, what is the URL of your agency's web site?"
    ],

    "4": [
        "Does your agency have a protection scheme for your ICT resources?",
        "If YES, what is/are the measure/s being used by your office? (Check all applicable)"
    ],

    "5": [
        "Does you agency have a data archiving system?",
        "If yes, what type of data archiving system does your agency use?",
        "If electronic data archiving is being utilized, what is the mode?",
        "If conventional mode, what is the medium of storage of the archived data?",
        "What information is archived by your agency electronically? (Check all items that are applicable)"
    ]
}
