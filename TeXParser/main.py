# =============================================================================
# TeXparser -- TeX/LaTeX Parser
# This is the main file for the TeXparser project.
# =============================================================================

if __name__ == "__main__":
    import generators.paper_structure as TeXDoc
    import generators.paper_headers as TeXHead
    import generators.paper_frames as TeXFrame
    import utilities.style_fix as TeXStyle

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

    TEX_FILENAME = "ICT_Inventory.tex"

    NEWLINE = '\n'

    doc = TeXDoc.Document(PAPER, FONT_SIZE, PAPER_TYPE)
    title = TeXHead.Title(TITLE)
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
        NEWLINE,
        doc.import_package("inputenc", ["utf8"]),
        ''.join([doc.import_package(pkg) for pkg in ["amssymb", "float", "url"]]),
        doc.import_package("hyperref", ["final"]),
        NEWLINE,
        ''.join([doc.import_package(pkg) for pkg in ["latexsym", "setspace", "enumitem", "makecell", 
                                                       "multicol", "multirow", "lastpage", "mdframed",
                                                       "titlesec"]]),
        doc.import_package("footmisc", ["bottom"]),
        NEWLINE,
        ''.join([doc.import_package(pkg) for pkg in ["fancyhdr", "newfloat", "graphicx", "array"]]),
        doc.import_package("adjustbox", ["export"]),
        NEWLINE,
        doc.import_package("geometry", [f"margin={MARGIN}", PAPER]),
        NEWLINE,
        title.generate_titleformat(FONT_SIZE),
        NEWLINE,
        TeXStyle.generate_hypersetup(LINK_COLOR, CITE_COLOR, URL_COLOR),
        NEWLINE,
        TeXStyle.generate_newcommands(),
        NEWLINE,
        TeXStyle.generate_fancyheader(),
        NEWLINE,
        doc.begin_document(),
        NEWLINE * 2,
        title.generate_title(),
        NEWLINE,
        mdframe.generate_mdframe(),
        NEWLINE * 2,
        doc.end_document(),
    ]

    tex_file = open(TEX_FILENAME, "w+")
    tex_file.writelines(build_TeX)
    tex_file.close()