


if __name__ == "__main__":
    import generators.document as TeXDoc
    import generators.title as TeXTitle
    import generators.mdframe as TeXFrame
    import utilities.style as TeXStyle

    PAPER = "a4paper"
    FONT_SIZE = 10
    TITLE = "ANNEX A-5: EXISTING INFORMATION & COMMUNICATIONS TECHNOLOGY (ICT) INFRASTRUCTURE INVENTORY"
    AGENCY_NAME = "University of the Philippines Diliman"
    RESPONDENT = "Dr. Manuel C. Ramos, Jr."
    POSITION = "Director"
    DIVISION = "University Computer Center"
    TELEPHONE = "8981-8500 local 2050"
    EMAIL = "computer.center@upd.edu.ph"

    doc = TeXDoc.Document(PAPER, FONT_SIZE, "article")
    title = TeXTitle.Title(TITLE)
    mdframe = TeXFrame.MDFrame(
        content=[
            r"AGENCY NAME: " + f"{EMAIL}" + r"\\",
            r"Respondent (IS Planner/CIO/MIS Head)\footnotemark[1]: " + f"{RESPONDENT}" + r"\\",
            r"Position/D\'esignation: " + f"{POSITION}" + r"\\",
            r"Division/Section/Unit: " + f"{DIVISION}" + r"\\",
            r"Telephone/Fax Number: " + f"{TELEPHONE}" +  r"\\",
            r"Respondent's Email Address: " + f"{EMAIL}" + r"\\",
        ]
    )

    build_TeX = [
        doc.generate_document(),
        title.generate_title(),
        title.generate_titleformat(FONT_SIZE),
        mdframe.generate_mdframe(),
        TeXStyle.generate_hypersetup("black", "black", "black"),
        TeXStyle.generate_newcommands(),
        TeXStyle.generate_fancyheader(),
    ]

    print(''.join(build_TeX))