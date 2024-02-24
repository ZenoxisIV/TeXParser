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

# ======================================
# DATABASE-RELATED SETTINGS
# ======================================
FORM_NAMES = {
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

TICKBOX_COLS = {
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
    "18": r"\underline{USE}: \textbf{1} - Public Financial Management; \textbf{2} - Citizen Frontline Services; \textbf{3} - Ease of Doing Business; \textbf{4} - Higher Education; \textbf{5} - Basic Education; \textbf{6} - Health; \textbf{7} - Justice, Peace and Order; \textbf{8} - Energy; \textbf{9} - Land and Other Geospatial Information; \textbf{10} - Disaster and Climate Change Management; \textbf{11} - Public Works and Transport; \textbf{12} - iGov and ICT Infrastructure; \textbf{13} - Transparency and Citizen's Participation; \textbf{14} - Citizen Registry; \textbf{15} - Others, please specify.",
    "19": r"\underline{PROJECT NAME}: In case an ICT project is divided in phases and its budget is given by phases, kindly list each phase as a separate project tagged as $<$Project Name$>$ Ph. 1, $<$Project Name$>$ Ph. 2, and so on.",
    "20": r"\underline{COST}: For ICT projects and project phases that \underline{ended in 2013 or earlier}, kindly provide the \textbf{\underline{actual}} \textbf{\underline{cost}} in pesos and not the proposed cost.",
    "21": r"\underline{DEVELOPMENT STRATEGY}: \textbf{I} - In-house;  \textbf{O} - Outsourced;  \textbf{C} - Combination",
    "22": r"\underline{STATUS}: \textbf{U} - Under Development;  \textbf{D} - For Deployment; \textbf{O} - Operational",
    "23": r"\underline{USE}: \textbf{1} - Public Financial Management; \textbf{2} - Citizen Frontline Services; \textbf{3} - Ease of Doing Business; \textbf{4} - Higher Education; \textbf{5} - Basic Education; \textbf{6} - Health; \textbf{7} - Justice, Peace and Order; \textbf{8} - Energy; \textbf{9} - Land and Other Geospatial Information; \textbf{10} - Disaster and Climate Change Management; \textbf{11} - Public Works and Transport; \textbf{12} - iGov and ICT Infrastructure; \textbf{13} - Transparency and Citizen's Participation; \textbf{14} - Citizen Registry; \textbf{15} - Others, please specify.",
    "24": "ISSP Template Revised 2003 iib",
    "25": r"\href{http://searchsecurity.techtarget.com/definition/Automated-Fingerprint-Identification-System}{http://searchsecurity.techtarget.com/definition/Automated-Fingerprint-Identification-System}",
    "26": r"\href{http://en.wikipedia.org/wiki/Cloud_computing}{http://en.wikipedia.org/wiki/Cloud\_computing}",
    "27": r"\href{http://searchsoa.techtarget.com/definition/collocation}{http://searchsoa.techtarget.com/definition/collocation}",
    "28": r"\href{http://searchdatacenter.techtarget.com/definition/data-center}{http://searchdatacenter.techtarget.com/definition/data-center}",
    "29": r"\href{http://computer.howstuffworks.com/10-types-of-computers.htm#page=2}{http://computer.howstuffworks.com/10-types-of-computers.htm#page=2}",
    "30": r"\href{http://linux.about.com/cs/linux101/g/digital_signatu.htm?terms=Digital+signature}{http://linux.about.com/cs/linux101/g/digital\_signatu.htm?terms=Digital+signature}",
    "31": r"\href{http://www.wisegeek.com/what-is-an-external-hard-drive.htm}{http://www.wisegeek.com/what-is-an-external-hard-drive.htm}",
    "32": r"\href{http://www.nwgis.com/gisdefn.htm}{http://www.nwgis.com/gisdefn.htm}",
    "33": "",
    "34": "",
    "35": "",
    "36": "",
    "37": "",
    "38": "",
    "39": "",
    "40": "",
    "41": "",
    "42": "",
    "43": "",
    "44": "",
    "45": "",
    "46": "",
    "47": "",
    "48": "",
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

SECT_THREE_QUESTIONS = [
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
    "If YES, what is the URL of your agency's web site?",
]


# ======================================
DEFINITION_OF_TERMS = [
    r"\textbf{Archiving} in general is a process that will ensure that information is preserved against technical obsolescence and physical damage. It will also help conserve very expensive resources and ensure that the research potential of the information is fully exploited. In the Philippine Statistical System (PSS), the adoption of archiving measures has been identified by the NSCB through Resolution No. 11 (s. 1997) as a key policy to ensure the preservation, systematic storage and retrieval of statistical data including records on their methodology, concepts and other metadata.\footnotemark[24]",

    r"\textbf{Automated Fingerprint Identification System} (AFIS) is a biometric identification (ID) methodology that uses digital imaging technology to obtain, store, and analyze fingerprint data.\footnotemark[25]",

    r"\textbf{Cloud computing} is the use of computing resources (hardware and software) that are delivered as a service over a network (typically the Internet).\footnotemark[26]",

    r"Co-located is an arrangement wherein a space is provided for a customer's telecommunications equipment on the service provider's premises.\footnotemark[27]",

    r"\textbf{Computing devices} include mainframes, minicomputers and microcomputers i.e. desktop personal computers (PCs), laptops PCs including notebooks and netbooks, and handheld devices like mobile phones including smart phones, Personal Digital Assistants (PDAs), palmtops, tablets and multimedia players.",

    r"\textbf{Data Center} is a centralized repository, either physical or virtual, for the storage, management, and dissemination of data and information organized around a particular body of knowledge or pertaining to a particular business.\footnotemark[28]",

    r"\textbf{Desktop PC} is a PC that is not designed for portability and is expected to be set up in a permanent location.\footnotemark[29]",

    r"\textbf{Digital signature} is an authentication code created with a sender's secret key and can be verified by a recipient using the sender's public key.\footnotemark[30]",

    r"\textbf{External hard drive} is a hard drive that sits outside the main computer tower in its own enclosure. It allows the user to back up or store important information separate from the main internal hard drive, which could become compromised, damaged or corrupted.\footnotemark[31]",

    r"\textbf{Firewall} is a hardware, software or a combination of the two protecting a computer network from unauthorized access.",

    r"\textbf{Geographic Information System} (GIS) is a system of hardware and software used for storage, retrieval, mapping, and analysis of geographic data.\footnotemark[32]",

    r'\textbf{Intranet} is "a private network that is contained within an enterprise. It may consist of many inter-linked LANs. The main purpose of an intranet is to share company information and computing resources among employees".\footnotemark[33]',

    r"\textbf{Laptop}, also called a \textbf{notebook}, is a portable PC that integrates the display, keyboard, a pointing device or trackball, processor, memory and hard drive all in a battery-operated package slightly larger than an average hardcover book.\footnotemark[34]",

    r'\textbf{Local Area Network} (LAN) is "a group of computers and associated devices that share a common communications line or wireless link and typically share the resources of a single processor or server within a small geographic area (for example, within an office building)".\footnotemark[35]',

    r"\textbf{Magnetic card reader} is a device used to read magnetic stripe cards, such as credit cards.\footnotemark[36]",

    r"\textbf{Mainframe} is an ultra high-performance computer made for high-volume, processor-intensive computing.\footnotemark[37]",

    r"\textbf{MICR reader} is a device that can recognize human readable characters printed on documents such as cheques using a special magnetic ink. MICR stands for Magnetic Ink Character Recognition.\footnotemark[38]",

    r"\textbf{Microfiche} is a sheet of microfilm (a film bearing a photographic record on a reduced scale of printed or other graphic matter) containing rows of microimages of pages of printed matters.\footnotemark[39]",

    r"\textbf{Mobile phone} is a handheld or wearable device that may not only have call and short messaging service (SMS) functions but may be integrated with common computer applications (email, database, multimedia, calendar/scheduler).",

    r"\textbf{Multimedia player} combine the functions of a PDA with multimedia features, such as a digital camera, an MP3 player and a video player\footnotemark[40].  This does not include digital voice recorders that only play and record audio files.",

    r"\textbf{Office automation software} are ready-made or in-house developed software packages that support clerical and other common office tasks.",

    r'\textbf{Original equipment manufacturer} (OEM) license covers software for stand-alone desktop PCs and laptops and MUST stay bundled with the computer system and NOT distributed as a separate (or stand-alone) product. This software will be identified or labeled "For Distribution Only With New Computer Hardware."\footnotemark[41]',

    r"\textbf{Outsourcing} is an arrangement in which one company provides services for another company that could also be or usually have been provided in-house.",

    r"\textbf{Oversight or administrative systems} are those application software that support development planning, fiscal and financial management and operations, auditing, personnel administration, and assets and supplies management.",

    r"\textbf{PABX} stands for private automatic branch exchange and is a telephone switching system used within a business or organization. It works by interconnecting telephone extensions to each other and to the outside public telephone network.\footnotemark[42]",

    r"\textbf{Palmtop}, more commonly known as \textbf{Personal Digital Assistant (PDA)}, is a tightly integrated computer that often uses flash memory instead of a hard drive for storage. This computer usually does not have keyboards but rely on touch screen technology for user input. Palmtops are typically smaller than a paperback novel, very lightweight with a reasonable battery life.\footnotemark[43]",

    r"\textbf{Server} is a computer that has been optimized to provide services to other computers over a network.\footnotemark[44]",

    r"\textbf{Smart card reader} is an electronic device that reads smart cards and can be an external device or a built-in feature of a keyboard, PC or laptop.\footnotemark[45]",

    r"\textbf{Stand-alone PCs} are independent computer units. They are \textbf{not} connected to any other PC or to the network and operate independently.",

    r"\textbf{Strategic information systems} are client-driven application software that support mission-critical operations and provide direct public access to government services.",

    r"\textbf{Tablet} is a mobile computer, larger than a mobile phone or personal digital assistant, integrated into a flat touch screen and primarily operated by touching the screen rather than using a physical keyboard. It often uses an onscreen virtual keyboard, a passive stylus pen, or a digital pen.\footnotemark[46]",

    r"\textbf{VOIP} is an acronym for Voice Over Internet Protocol, or in more common terms phone service over the Internet.\footnotemark[47]",

    r"\textbf{Web site} is your agency's presence on the Internet environment.",

    r"\textbf{Wide Area Network} is similar to a Local Area Network (LAN), but unlike LANs, WANs are not limited to a single location.\footnotemark[48]",

    r"\textbf{Workstations} are categorized as PCs attached to an office network (usually a Local Area Network) to differentiate it from Stand-alone PCs."
]