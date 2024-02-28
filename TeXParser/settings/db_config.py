# ======================================
# DATABASE-RELATED CONFIGURATIONS
# ======================================

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
    "3": "network",
    "4": "security",
    "5": "archiving",
    "6": "special_solutions",
    "7": "data_center",
    "8.1": "ict_projects",
    "8.2": "ict_issues"
}
# ======================================

# ======================================
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

# ======================================
QUES_OPTION_MAPPING = {
    "3.8": {
        "Dial-up": "Dial-up",
        "DSL": "DSL",
        "ISDN": "ISDN",
        "Leased line": "Leased line",
        "Mobile phone": "Mobile phone",
        "Satellite": "Satellite",
        "WiFi": "WiFi",
        "Others": None,
    },

    "4.2": {
        "Policy": "Security Policy / Guideline",
        "Disaster Recovery Plan": "Disaster Recovery Plan",
        "Back-up power": "Back-up power unit (e.g. UPS, Generator)",
        "Digital signatures": "Digital signatures",
        "Encryption": "Encryption",
        "Off-site back-up": "Off-site back-up",
        "Hardware firewall": "Hardware firewall",
        "Physical restriction": "Physically restricted access to critical ICT equipment",
        "Software firewall": "Software firewall",
        "Secure servers": "Secure servers",
        "Security service": "Subscription to a security service (e.g. anti-virus software, intrusion alert)",
        "Non-local back-up media": "Storage of back-up media in localities other than the operating environment",
        "Security training": "Regular ICT security training of employees",
        "Others": None
    },

    "5.2": {
        "Manual": "Manual",
        "Electronic": "Electronic",
        "Both": "Both/Combination"
    },

    "5.3": {
        "Conventional": "Conventional",
        "Cloud": "Cloud"
    },

    "5.4": {
        "Optical disks": "Optical disks (e.g. CD-Rom, DVD)",
        "Hard Disk": "Hard Disk",
        "Tape": "Tape",
        "External Hard Drive": "External Hard Drive",
        "Microfiche": "Microfiche",
        "Diskette": "Diskette",
        "Others": None
    },

    "5.5": {
        "Publications": "Publications (Annual Report, Statistical Report, etc.)",
        "Letters": "Letters, memorandum orders, communications, etc.",
        "Audio-visual recordings": "Audio-visual recordings",
        "Unprocessed": "Unprocessed/Raw Data",
        "Maps": "Maps",
        "Photographs": "Photographs",
        "Public documents": "Public documents (civil registration forms, passports, land titles, etc.)",
        "Others": None
    },

    "8.2": {
        "Budget": "No budget or insufficient budget",
        "Delayed funding": "Delay in the release of projects funds",
        "Opposition": "Opposition or reluctance of stakeholders",
        "Support": "Lack of support by management",
        "Recruitment": "Difficulty in recruiting and/or retaining qualified ICT personnel",
        "ICT skill": "Low level of ICT skills among employees",
        "Bandwidth": "Unavailability of required bandwidth to support system/s",
        "Contracts": "Not used or seldom used by intended users and/or clients",
        "Usage": "Problems in contract management for outsourced services",
        "Procurement": "Problems in procurement",
        "Others": None
    }
}

# ======================================