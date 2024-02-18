# =============================================================================
# TeXParser -- TeX/LaTeX Parser
# This is the main file for the TeXParser project.
# =============================================================================
from generators import paper_structure as TeXDoc
from generators import paper_headers as TeXHead
from generators import paper_frames as TeXFrame
from generators import paper_lists as TeXList
from generators import paper_tables as TeXTable
from utilities import style_fix as TeXStyle
from utilities import format_fix as TeXFormat
from utilities import json_extract as TeXJSON
import config as cfg

def main():
    NEWLINE = '\n'

    doc = TeXDoc.Document(cfg.PAPER, cfg.FONT_SIZE, cfg.PAPER_TYPE)
    title = TeXHead.Title(cfg.TITLE)
    mdframe = TeXFrame.MDFrame(
        content=[
            r"AGENCY NAME: " + f"{cfg.EMAIL}" + r"\\",
            r"Respondent (IS Planner/CIO/MIS Head)" + f"{TeXStyle.generate_footnote_mark('1')}: " + f"{cfg.RESPONDENT}" + r"\\",
            r"Position/D\'esignation: " + f"{cfg.POSITION}" + r"\\",
            r"Division/Section/Unit: " + f"{cfg.DIVISION}" + r"\\",
            r"Telephone/Fax Number: " + f"{cfg.TELEPHONE}" +  r"\\",
            r"Respondent's Email Address: " + f"{cfg.EMAIL}",
        ]
    )
    objectives = TeXList.Bullet(cfg.OBJECTIVES)
    fill_out_instructions = TeXList.Bullet(cfg.FILL_OUT_INSTRUCTIONS)

    table1_1 = TeXTable.Tabular()

    build_TeX = [
        # --- IMPORTANT NOTE: The following lines should not be changed nor modified. ---
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
        TeXFormat.generate_sectionformat(cfg.FONT_SIZE),
        NEWLINE,
        # --- END OF IMPORTANT NOTE ---

        # Color of hyperlinks, citations, and URLs
        TeXStyle.generate_hypersetup(cfg.LINK_COLOR, cfg.CITE_COLOR, cfg.URL_COLOR),

        NEWLINE * 2,

        # Some header and footer configurations for the document (modifiable but exercise caution)
        TeXFormat.generate_fancystyle(),
        TeXFormat.clear_fancyhf(),
        TeXFormat.set_headerrule(0),
        TeXFormat.set_fancyfooter(['R'], r"\small\emph{Page \thepage\ of \pageref{LastPage}}\hspace{15pt}"),

        NEWLINE,

        # This marks the start of the document (DO NOT REMOVE)
        doc.begin_document(),

        NEWLINE * 2,

        # Title of the document
        title.generate_title(),

        NEWLINE,

        # Metadata for the document
        mdframe.generate_mdframe(),

        NEWLINE * 2,

        # Objectives
        TeXStyle.bold_text(TeXStyle.italic_text(cfg.OBJECTIVES["title"] + ':')),
        NEWLINE,
        objectives.begin_bullet(cfg.OBJECTIVES_BULLET_OFFSET),
        objectives.generate_bullets(),
        objectives.end_bullet(),

        NEWLINE,

        # Section 1
        TeXHead.Section(cfg.SECTIONS["1"]).generate_section(),

        # Fill-out instructions
        TeXStyle.bold_text(cfg.FILL_OUT_INSTRUCTIONS["title"] + ':'),
        NEWLINE,
        fill_out_instructions.begin_bullet(cfg.FILL_OUT_INSTRUCTIONS_BULLET_OFFSET),
        TeXStyle.modify_substring(fill_out_instructions.generate_bullets(), "Reference year is last year", TeXStyle.bold_text),
        fill_out_instructions.end_bullet(),

        NEWLINE,

        # Section 1.1
        TeXHead.Subsection(cfg.SECTIONS["1.1"]).generate_subsection(),
        TeXStyle.generate_footnote_text("1", cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text("2", cfg.FOOTNOTES),
        NEWLINE * 2,

        table1_1.begin_table('H'),
        table1_1.set_arraystretch(1.5),
        table1_1.toggle_centering(),
        table1_1.begin_adjustbox("6in"),
        table1_1.begin_tabular(cfg.TABLE_COLUMN_FORMATS["1.1"]),
        table1_1.generate_horizontal_line(),

        NEWLINE,
        
        #TODO - make variables for localhost and table in config.py
        table1_1.generate_entries(TeXJSON.parseJSONData(TeXJSON.requestJSONData("http://localhost/TeXParser/json_test.php"), "cd_year")),

        table1_1.end_tabular(),
        table1_1.end_adjustbox(),
        table1_1.end_table(),

        # This marks the end of the document (DO NOT REMOVE)
        doc.end_document(),
    ]

    tex_file = open(cfg.TEX_FILENAME, "w+")
    tex_file.writelines(build_TeX)
    tex_file.close()

if __name__ == "__main__":
    main()