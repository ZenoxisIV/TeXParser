# ======================================
# MISC CONFIGURATIONS
# ======================================

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
# #: \# NOTE: # must be escaped even for the <link> in \href{<link>}{<text>}
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
FILL_OUT_INSTRUCTIONS = {
    "title": "Fill-out Instruction",

    "b1": 'Please count all existing computing devices and peripherals owned or leased by your office that are functioning including those acquired through projects. In case of multi-year contract for leased units, then just write the number of units under the appropriate year when the leased units were acquired. Do not include in succeeding years unless another batch was leased. Reference year is last year. Kindly replace "last year" and preceding years by the actual year number. For example, if last year is 2013, then write 2013 under the 1st column. For last 2 years, write 2012 and for last 3 years, write 2011.',
}

FILL_OUT_INSTRUCTIONS_BULLET_OFFSET = "3.5em"
# ======================================

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
# ======================================