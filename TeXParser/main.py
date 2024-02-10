# =============================================================================
# TeXParser -- TeX/LaTeX Parser
# This is the main file for the TeXParser project.
# =============================================================================

if __name__ == "__main__":
    import generators.paper_structure as TeXDoc
    import generators.paper_headers as TeXHead
    import generators.paper_frames as TeXFrame
    import generators.paper_lists as TeXList
    import utilities.style_fix as TeXStyle
    import config as cfg
    
    NEWLINE = '\n'

    doc = TeXDoc.Document(cfg.PAPER, cfg.FONT_SIZE, cfg.PAPER_TYPE)
    title = TeXHead.Title(cfg.TITLE)
    mdframe = TeXFrame.MDFrame(
        content=[
            r"AGENCY NAME: " + f"{cfg.EMAIL}" + r"\\",
            r"Respondent (IS Planner/CIO/MIS Head)" + f"{doc.generate_footnote_mark('1')}: " + f"{cfg.RESPONDENT}" + r"\\",
            r"Position/D\'esignation: " + f"{cfg.POSITION}" + r"\\",
            r"Division/Section/Unit: " + f"{cfg.DIVISION}" + r"\\",
            r"Telephone/Fax Number: " + f"{cfg.TELEPHONE}" +  r"\\",
            r"Respondent's Email Address: " + f"{cfg.EMAIL}",
        ]
    )
    objectives = TeXList.Bullet(cfg.OBJECTIVES)
    fill_out_instructions = TeXList.Bullet(cfg.FILL_OUT_INSTRUCTIONS)

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
        doc.import_package("geometry", [f"margin={cfg.MARGIN}", cfg.PAPER]),
        NEWLINE,
        title.generate_titleformat(cfg.FONT_SIZE),
        NEWLINE,
        TeXStyle.generate_hypersetup(cfg.LINK_COLOR, cfg.CITE_COLOR, cfg.URL_COLOR),
        NEWLINE * 2,
        TeXStyle.generate_newcommand_TAB(),
        NEWLINE,
        TeXStyle.generate_fancystyle(),
        TeXStyle.clear_fancyhf(),
        TeXStyle.set_headerrule(0),
        TeXStyle.set_fancyfooter(['R'], r"\small\emph{Page \thepage\ of \pageref{LastPage}}\hspace{15pt}"),
        NEWLINE,
        doc.begin_document(),
        NEWLINE * 2,
        title.generate_title(),
        NEWLINE,
        mdframe.generate_mdframe(),
        NEWLINE * 2,
        TeXStyle.bold_text(TeXStyle.italic_text(cfg.OBJECTIVES["title"] + ':')),
        NEWLINE,
        objectives.begin_bullet(cfg.OBJECTIVES_BULLET_OFFSET),
        objectives.generate_bullets(),
        objectives.end_bullet(),
        NEWLINE,
        TeXHead.Section(cfg.SECTIONS["1"]).generate_section(),
        TeXStyle.bold_text(cfg.FILL_OUT_INSTRUCTIONS["title"] + ':'),
        NEWLINE,
        fill_out_instructions.begin_bullet(cfg.FILL_OUT_INSTRUCTIONS_BULLET_OFFSET),
        TeXStyle.modify_substring(fill_out_instructions.generate_bullets(), "Reference year is last year", TeXStyle.bold_text),
        fill_out_instructions.end_bullet(),
        NEWLINE,
        TeXHead.Subsection(cfg.SECTIONS["1.1"]).generate_subsection(),
        NEWLINE * 2,
        doc.end_document(),
    ]

    tex_file = open(cfg.TEX_FILENAME, "w+")
    tex_file.writelines(build_TeX)
    tex_file.close()