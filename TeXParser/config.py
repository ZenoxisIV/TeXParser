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

TITLE = "ANNEX A-5: EXISTING INFORMATION & COMMUNICATIONS TECHNOLOGY (ICT) INFRASTRUCTURE INVENTORY"
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

FILL_OUT_INSTRUCTIONS_BULLET_OFFSET = "3.5em"