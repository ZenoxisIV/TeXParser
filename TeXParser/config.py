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

OBJECTIVES = {
    "title": "Objectives",

    "b1": "To identify the hardware, software, network and other ICT resources being used to manage information by National Government Agencies (NGAs), Government-owned and Controlled Corporations (GOCCs), State Colleges and Universities (SUCs), and Constitutional and Financial Autonomous Group (CFAG);",

    "b2": "To update existing benchmark and standards; and",

    "b3": "To provide inputs to the MITHI Steering Committee in determining the ICT budget requirements of the agency.",
}

OBJECTIVES_BULLET_OFFSET = "3.5em"

SECTIONS = {
    "1": "HARDWARE / OTHER ICT EQUIPMENT",
    "1.1": "Number of Computing Devices and Peripherals by Type and by Year Acquired",
}

FILL_OUT_INSTRUCTIONS = {
    "title": "Fill-out Instruction",

    "b1": 'Please count all existing computing devices and peripherals owned or leased by your office that are functioning including those acquired through projects. In case of multi-year contract for leased units, then just write the number of units under the appropriate year when the leased units were acquired. Do not include in succeeding years unless another batch was leased. Reference year is last year. Kindly replace "last year" and preceding years by the actual year number. For example, if last year is 2013, then write 2013 under the 1st column. For last 2 years, write 2012 and for last 3 years, write 2011.',
}

# LEGEND:
# l - left-align
# c - center-align
# r - right-align
# p{<width>} - paragraph (fixed width; word-wrapping)
# | - vertical separator
TABLE_FORMATS = {
    # SECTION 1
    "1.1": "|p{6.5cm}|c|c|c|c|c|c|c|",
    "1.2": "|l|ccc|c|c|",
    "1.3": "|l|cc|",

    # SECTION 2
    # SUBSECTION 2.1
    "2.1.1": "|p{6.5cm}|c|l|",
    "2.1.2": "|p{6.5cm}|c|l|",
    "2.1.3": "|p{6.5cm}|c|l|",

    "2.2": "|p{6.5cm}|c|l|",
    "2.3": "|p{4cm}|c|c|c|c|c|",
    "2.4": "|p{4cm}|c|c|c|c|c|",
    "2.5": "|p{4cm}|c|c|c|c|c|",
}

TABLE_DEFAULT_FIELDS = {
    # SECTION 1
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
            ]
}


FILL_OUT_INSTRUCTIONS_BULLET_OFFSET = "3.5em"

FOOTNOTES = {
    "1": "In case all three positions are occupied by different persons, then the IS Planner should have priority in answering this survey.",
    "2": "Count only the mobile phones owned or leased by your agency.",
    "3": "Those used in planning, coordination, internal training, monitoring and evaluation",
    "4": "Those used by external clients",
    "5": "Mark if yes. Examples are OEM license (software is already installed in the hardware) and Enterprise (Perpetual) license, which does not require renewal and is for life long. (source: http://www.manageengine.com/products/service-desk/help/adminguide/configurations/software/software-license-type.html)",
}

