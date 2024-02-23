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
    REQUEST_DATA_URL = "http://localhost/TeXParser/json_test.php"

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

    tables = TeXTable.Tabular(cfg.TABLE_FORMATS)
    ovr_subsection = TeXFormat.OverrideFormat()

    build_TeX = [
        # --- IMPORTANT NOTE: The following lines should ideally not be changed nor modified. ---
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

        # === Color of hyperlinks, citations, and URLs ===
        TeXStyle.generate_hypersetup(cfg.LINK_COLOR, cfg.CITE_COLOR, cfg.URL_COLOR),

        NEWLINE * 2,

        # === Some header and footer configurations for the document ===
        TeXFormat.generate_fancystyle(),
        TeXFormat.clear_fancyhf(),
        TeXFormat.set_headerrule(0),
        TeXFormat.set_fancyfooter(['R'], r"\small\emph{Page \thepage\ of \pageref{LastPage}}\hspace{15pt}"),

        NEWLINE,

        # === This marks the start of the document (DO NOT REMOVE) ===
        doc.begin_document(),

        NEWLINE * 2,

        # === Title of the document ===
        title.generate_title(),

        NEWLINE,

        # === Metadata for the document ===
        mdframe.generate_mdframe(),

        NEWLINE * 2,

        # === Objectives ===
        TeXStyle.bold_text(TeXStyle.italic_text(cfg.OBJECTIVES["title"] + ':')),
        NEWLINE,
        objectives.begin_bullet(cfg.OBJECTIVES_BULLET_OFFSET),
        objectives.generate_bullets(),
        objectives.end_bullet(),

        NEWLINE,

        # === Section 1 ===
        TeXStyle.generate_section(cfg.SECTIONS["1"]),

        # === Fill-out instructions ===
        TeXStyle.bold_text(cfg.FILL_OUT_INSTRUCTIONS["title"] + ':'),
        NEWLINE,
        fill_out_instructions.begin_bullet(cfg.FILL_OUT_INSTRUCTIONS_BULLET_OFFSET),
        TeXStyle.modify_substring(fill_out_instructions.generate_bullets(), "Reference year is last year", TeXStyle.bold_text),
        fill_out_instructions.end_bullet(),

        NEWLINE,

        # === Subsection 1.1 === 
        TeXStyle.generate_subsection(cfg.SECTIONS["1.1"]),
        TeXStyle.generate_footnote_text('1', cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('2', cfg.FOOTNOTES),
        NEWLINE * 2,

        tables.begin_table('H'),
        tables.set_arraystretch(1.5),
        tables.toggle_centering(),
        tables.begin_adjustbox("6in"),
        tables.begin_tabular("1.1"),
        tables.generate_horizontal_line(),

        NEWLINE,
        
        tables.generate_headers([
            tables.generate_multicolumn(1, "|c|", tables.generate_multirow(3, TeXStyle.bold_text("TYPES"))),
            tables.generate_multicolumn(7, "c|", TeXStyle.bold_text("TOTAL NUMBER OF FUNCTIONING UNITS BY YEAR ACQUIRED")) + ' ' + r"\\" + ' ' + tables.generate_cline(2, 8),
            NEWLINE,
            tables.generate_multicolumn(2, "c|", TeXStyle.bold_text("$<$Last Year$>$")),
            tables.generate_multicolumn(2, "c|", TeXStyle.bold_text("$<$Last 2 Years$>$")),
            tables.generate_multicolumn(2, "c|", TeXStyle.bold_text("$<$Last 3 Years$>$")),
            tables.generate_multicolumn(1, "c|", tables.generate_multirow(2, TeXStyle.bold_text("More than 3 years"))) + ' ' + r"\\" + ' ' + tables.generate_cline(2, 7),
            NEWLINE,
            tables.generate_multicolumn(1, "c|", TeXStyle.bold_text("Owned")),
            tables.generate_multicolumn(1, "c|", TeXStyle.bold_text("Leased")),
            tables.generate_multicolumn(1, "c|", TeXStyle.bold_text("Owned")),
            tables.generate_multicolumn(1, "c|", TeXStyle.bold_text("Leased")),
            tables.generate_multicolumn(1, "c|", TeXStyle.bold_text("Owned")),
            tables.generate_multicolumn(1, "c|", TeXStyle.bold_text("Leased")),
            tables.generate_multicolumn(1, "c|") + ' ' + r"\\" + ' ' + tables.generate_horizontal_line(),
        ]),

        NEWLINE,
        
        TeXStyle.modify_substring(
            tables.generate_entries(
                TeXJSON.parseJSONData(
                    TeXJSON.requestJSONData(REQUEST_DATA_URL), cfg.TABLE_FORM_NAMES["1.1"]
                ), 
            default_fields=cfg.TABLE_DEFAULT_FIELDS["1.1"], limit=16
            ), "Mobile Phone", TeXStyle.append_footnotemark, '2'
        ),

        tables.end_tabular(),
        tables.end_adjustbox(),
        tables.end_table(),

        NEWLINE,

        # === Subsection 1.2 ===
        TeXStyle.generate_subsection(cfg.SECTIONS["1.2"]),
        TeXStyle.generate_footnote_text('3', cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('4', cfg.FOOTNOTES),
        NEWLINE * 2,

        tables.begin_table('H'),
        tables.set_arraystretch(1.5),
        tables.toggle_centering(),
        tables.begin_adjustbox(r"\textwidth"),
        tables.begin_tabular("1.2"),
        tables.generate_horizontal_line(),

        NEWLINE,

        tables.generate_headers([
            tables.generate_multicolumn(1, "|c|", tables.generate_multirow(2, TeXStyle.bold_text("TYPES"))),

            tables.generate_multicolumn(3, "c|", TeXStyle.bold_text("Operations")),

            TeXStyle.bold_text(tables.begin_tabular(r"@{}c@{}", "c") + r"General Administration\\ and Support Services\\ Support to Operations" + 
            TeXStyle.generate_footnote_mark('3') + tables.end_tabular()),

            tables.begin_tabular(r"@{}c@{}", "c") + TeXStyle.bold_text("Projects") + r"\\" +  TeXStyle.italic_text("(Not agency-funded)") + 
            tables.end_tabular() + ' ' + r"\\" + ' ' + tables.generate_cline(2, 6),

            tables.generate_multicolumn(1, "c|", TeXStyle.bold_text("Employees")),
            tables.generate_multicolumn(1, "c|", TeXStyle.bold_text("Training")),
            tables.generate_multicolumn(1, "c|", TeXStyle.bold_text("Frontline Services") + TeXStyle.generate_footnote_mark('4')),
            TeXStyle.bold_text(""),
            TeXStyle.bold_text("") + ' ' + r"\\" + ' ' + tables.generate_horizontal_line()
        ]),

        NEWLINE,

        tables.generate_entries(
            TeXJSON.parseJSONData(
                TeXJSON.requestJSONData(REQUEST_DATA_URL), cfg.TABLE_FORM_NAMES["1.2"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["1.2"]
        ),

        tables.end_tabular(),
        tables.end_adjustbox(),
        tables.end_table(),

        NEWLINE,

        # === Subsection 1.3 ===
        TeXStyle.generate_subsection(cfg.SECTIONS["1.3"]),

        tables.begin_table('H'),
        tables.set_arraystretch(1.5),
        tables.toggle_centering(),
        tables.begin_adjustbox("4in"),
        tables.begin_tabular("1.3"),
        tables.generate_horizontal_line(),

        NEWLINE,

        tables.generate_headers([
            tables.generate_multicolumn(1, "|c|", tables.generate_multirow(2, TeXStyle.bold_text("TOTAL CAPACITY OF HDD"))),

            tables.generate_multicolumn(2, "c|", TeXStyle.bold_text("LOCATION")) + ' ' + r"\\" + ' ' + tables.generate_cline(2, 3),

            tables.generate_multicolumn(1, "c|", TeXStyle.bold_text("IN-HOUSE")),
            tables.generate_multicolumn(1, "c|", TeXStyle.bold_text("CO-LOCATED")) + ' ' + r"\\" + ' ' + tables.generate_horizontal_line()
        ]),

        NEWLINE,

        tables.generate_entries(
            TeXJSON.parseJSONData(
                TeXJSON.requestJSONData(REQUEST_DATA_URL), cfg.TABLE_FORM_NAMES["1.3"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["1.3"]
        ),

        tables.end_tabular(),
        tables.end_adjustbox(),
        tables.end_table(),

        NEWLINE,

        # === Section 2 ===
        TeXStyle.generate_section(cfg.SECTIONS["2"]),

        # === Subsection 2.1 ===
        TeXStyle.generate_subsection(cfg.SECTIONS["2.1"]),

        # === Subsubsection 2.1.1 ===
        TeXStyle.generate_subsubsection(cfg.SECTIONS["2.1.1"]),
        TeXStyle.generate_footnote_text('5', cfg.FOOTNOTES),
        NEWLINE * 2,

        tables.begin_table('H'),
        tables.set_arraystretch(1.5),
        tables.toggle_centering(),
        tables.begin_adjustbox("5.5in"),
        tables.begin_tabular("2.1.1"),
        tables.generate_horizontal_line(),

        NEWLINE,

        tables.generate_headers([
            tables.generate_multicolumn(1, "|c|", "OPERATING SYSTEM"),
            tables.generate_multicolumn(1, "c|", f"Lifetime License?{TeXStyle.generate_footnote_mark('5')}"),
            tables.generate_multicolumn(1, "c|", "If not, write below the year of expiration") + ' ' + r"\\" + ' ' + tables.generate_horizontal_line()
        ]),

        NEWLINE,

        tables.generate_entries(
            TeXJSON.parseJSONData(
                TeXJSON.requestJSONData(REQUEST_DATA_URL), cfg.TABLE_FORM_NAMES["2.1.1"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["2.1.1"], bool_cols=cfg.TABLE_BOOL_COLS["2.1.1"]
        ),

        tables.end_tabular(),
        tables.end_adjustbox(),
        tables.end_table(),

        NEWLINE,

        # === Subsubsection 2.1.2 ===
        TeXStyle.generate_subsubsection(cfg.SECTIONS["2.1.2"]),

        tables.begin_table('H'),
        tables.set_arraystretch(1.5),
        tables.toggle_centering(),
        tables.begin_adjustbox("5.5in"),
        tables.begin_tabular("2.1.2"),
        tables.generate_horizontal_line(),

        NEWLINE,

        tables.generate_headers([
            tables.generate_multicolumn(1, "|c|", "OPERATING SYSTEM"),
            tables.generate_multicolumn(1, "c|", "Lifetime License?"),
            tables.generate_multicolumn(1, "c|", "If not, write below the year of expiration") + ' ' + r"\\" + ' ' + tables.generate_horizontal_line()
        ]),

        NEWLINE,

        tables.generate_entries(
            TeXJSON.parseJSONData(
                TeXJSON.requestJSONData(REQUEST_DATA_URL), cfg.TABLE_FORM_NAMES["2.1.2"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["2.1.2"], bool_cols=cfg.TABLE_BOOL_COLS["2.1.2"]
        ),

        tables.end_tabular(),
        tables.end_adjustbox(),
        tables.end_table(),

        NEWLINE,

        # === Subsubsection 2.1.3 ===
        TeXStyle.generate_subsubsection(cfg.SECTIONS["2.1.3"]),

        tables.begin_table('H'),
        tables.set_arraystretch(1.5),
        tables.toggle_centering(),
        tables.begin_adjustbox("5.5in"),
        tables.begin_tabular("2.1.2"),
        tables.generate_horizontal_line(),

        NEWLINE,

        tables.generate_headers([
            tables.generate_multicolumn(1, "|c|", "OPERATING SYSTEM"),
            tables.generate_multicolumn(1, "c|", "Lifetime License?"),
            tables.generate_multicolumn(1, "c|", "If not, write below the year of expiration") + ' ' + r"\\" + ' ' + tables.generate_horizontal_line()
        ]),

        NEWLINE,

        tables.generate_entries(
            TeXJSON.parseJSONData(
                TeXJSON.requestJSONData(REQUEST_DATA_URL), cfg.TABLE_FORM_NAMES["2.1.3"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["2.1.3"], bool_cols=cfg.TABLE_BOOL_COLS["2.1.3"]
        ),

        tables.end_tabular(),
        tables.end_adjustbox(),
        tables.end_table(),

        NEWLINE,

        # === Subsection 2.2 ===
        TeXStyle.generate_subsection(cfg.SECTIONS["2.2"]),

        tables.begin_table('H'),
        tables.set_arraystretch(1.5),
        tables.toggle_centering(),
        tables.begin_adjustbox("6.5in"),
        tables.begin_tabular("2.2"),
        tables.generate_horizontal_line(),

        NEWLINE,

        tables.generate_headers([
            tables.generate_multicolumn(1, "|c|", "SOFTWARE / APPLICATION PACKAGE"),
            tables.generate_multicolumn(1, "c|", "Lifetime License?"),
            tables.generate_multicolumn(1, "c|", "If not, write below the year of expiration") + ' ' + r"\\" + ' ' + tables.generate_horizontal_line()
        ]),

        NEWLINE,

        tables.generate_entries(
            TeXJSON.parseJSONData(
                TeXJSON.requestJSONData(REQUEST_DATA_URL), cfg.TABLE_FORM_NAMES["2.2"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["2.2"], bool_cols=cfg.TABLE_BOOL_COLS["2.2"]
        ),

        tables.end_tabular(),
        tables.end_adjustbox(),
        tables.end_table(),

        NEWLINE,

        # === Subsection 2.3 ===
        ovr_subsection.begingroup(), # Start wrapper for the section title.
        ovr_subsection.change_titleformat(cfg.FONT_SIZE, "subsection", "runin"), # Simply just to allow text beside a section title.

        TeXStyle.modify_substring(TeXStyle.generate_subsection(cfg.SECTIONS["2.3"]), "Oversight", TeXStyle.append_footnotemark, '6', True),
        cfg.SECTION_NOTES["2.3"],
        TeXStyle.generate_footnote_text('6', cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('7', cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('8', cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('9', cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('10', cfg.FOOTNOTES),

        NEWLINE,

        tables.begin_table('H'),
        tables.set_arraystretch(1.5),
        tables.toggle_centering(),
        tables.begin_adjustbox(r"\textwidth"),
        tables.begin_tabular("2.3"),
        tables.generate_horizontal_line(),

        NEWLINE,

        tables.generate_headers([
            tables.generate_multicolumn(1, "|c|", tables.begin_tabular(r"@{}c@{}", "c") + "NAME OF SYSTEM" + r"\\" + 
                                            r"(Please list down the \\ name/s of your \\ administrative system/s)" + tables.end_tabular()),

            tables.begin_tabular(r"@{}c@{}", "c") + r"Own Intellectual \\ Property," + 
                                            r"\\" +  "Y or N?" + TeXStyle.generate_footnote_mark('8') + tables.end_tabular(),

            tables.begin_tabular(r"@{}c@{}", "c") + r"DEVELOPMENT \\ PLATFORM" + 
                                            r"\\" +  r"(ex. LAMP, .NET, \\ Java)" + tables.end_tabular(),

            tables.begin_tabular(r"@{}c@{}", "c") + r"WORKING \\ ENVIRONMENT" + 
                                            TeXStyle.generate_footnote_mark('9') + r"\\" +  r"(Use codes \\ below)" + tables.end_tabular(),

            tables.begin_tabular(r"@{}c@{}", "c") + r"MAINTENANCE \\ COST" + tables.end_tabular(),

            tables.begin_tabular(r"@{}c@{}", "c") + "USE" + TeXStyle.generate_footnote_mark('10') + 
                                            r"\\" +  r"(Pls. write codes \\ only; refer below)" + tables.end_tabular(),

            tables.begin_tabular(r"@{}c@{}", "c") + "Others" + r"\\" +  r"(Please specify \\ if USE code is 15)" + tables.end_tabular() + 
                ' ' + r"\\" + ' ' + tables.generate_horizontal_line(),

        ]),

        NEWLINE,

        tables.generate_entries(
            TeXJSON.parseJSONData(
                TeXJSON.requestJSONData(REQUEST_DATA_URL), cfg.TABLE_FORM_NAMES["2.3"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["2.3"]
        ),

        tables.end_tabular(),
        tables.end_adjustbox(),
        tables.end_table(),

        NEWLINE,

        # === Subsection 2.4 ===
        TeXStyle.modify_substring(TeXStyle.generate_subsection(cfg.SECTIONS["2.4"]), "Operational", TeXStyle.append_footnotemark, '11', True),
        cfg.SECTION_NOTES["2.4"],
        TeXStyle.generate_footnote_text('11', cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('12', cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('13', cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('14', cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('15', cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('16', cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('17', cfg.FOOTNOTES),

        NEWLINE,

        tables.begin_table('H'),
        tables.set_arraystretch(1.5),
        tables.toggle_centering(),
        tables.begin_adjustbox(r"\textwidth"),
        tables.begin_tabular("2.4"),
        tables.generate_horizontal_line(),

        NEWLINE,

        tables.generate_headers([
            tables.generate_multicolumn(1, "|c|", tables.begin_tabular(r"@{}c@{}", "c") + "NAME OF SYSTEM" + r"\\" + 
                                            r"(Please list down the \\ name/s of your \\ administrative system/s)" + tables.end_tabular()),

            tables.begin_tabular(r"@{}c@{}", "c") + r"Own Intellectual \\ Property," + 
                                            r"\\" +  "Y or N?" + TeXStyle.generate_footnote_mark('8') + tables.end_tabular(),

            tables.begin_tabular(r"@{}c@{}", "c") + r"DEVELOPMENT \\ PLATFORM" + 
                                            r"\\" +  r"(ex. LAMP, .NET, \\ Java)" + tables.end_tabular(),

            tables.begin_tabular(r"@{}c@{}", "c") + r"WORKING \\ ENVIRONMENT" + 
                                            TeXStyle.generate_footnote_mark('9') + r"\\" +  r"(Use codes \\ below)" + tables.end_tabular(),

            tables.begin_tabular(r"@{}c@{}", "c") + r"MAINTENANCE \\ COST" + tables.end_tabular(),

            tables.begin_tabular(r"@{}c@{}", "c") + "USE" + TeXStyle.generate_footnote_mark('10') + 
                                            r"\\" +  r"(Pls. write codes \\ only; refer below)" + tables.end_tabular(),

            tables.begin_tabular(r"@{}c@{}", "c") + "Others" + r"\\" +  r"(Please specify \\ if USE code is 15)" + tables.end_tabular() + 
                ' ' + r"\\" + ' ' + tables.generate_horizontal_line(),

        ]),

        NEWLINE,

        tables.generate_entries(
            TeXJSON.parseJSONData(
                TeXJSON.requestJSONData(REQUEST_DATA_URL), cfg.TABLE_FORM_NAMES["2.4"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["2.4"]
        ),

        tables.end_tabular(),
        tables.end_adjustbox(),
        tables.end_table(),

        NEWLINE,

        # === Subsection 2.5 ===
        TeXStyle.generate_subsection(cfg.SECTIONS["2.5"]),
        cfg.SECTION_NOTES["2.5"],

        NEWLINE,

        tables.begin_table('H'),
        tables.set_arraystretch(1.5),
        tables.toggle_centering(),
        tables.begin_adjustbox(r"\textwidth"),
        tables.begin_tabular("2.4"),
        tables.generate_horizontal_line(),

        NEWLINE,

        tables.generate_headers([
            tables.generate_multicolumn(1, "|c|", "NAME OF DATABASE"),

            tables.begin_tabular(r"@{}c@{}", "c") + r"Own Intellectual \\ Property," + 
                                            r"\\" +  "Y or N?" + TeXStyle.generate_footnote_mark('8') + tables.end_tabular(),

            tables.begin_tabular(r"@{}c@{}", "c") + r"BRIEF \\ DESCRIPTION AND \\ KEY FIELDS" + TeXStyle.generate_footnote_mark('16') + tables.end_tabular(),

            tables.begin_tabular(r"@{}c@{}", "c") + r"DATABASE \\ MANAGEMENT \\ SOFTWARE" + 
                                            TeXStyle.generate_footnote_mark('17') + r"\\" +  r"USED" + tables.end_tabular(),

            tables.begin_tabular(r"@{}c@{}", "c") + r"MAINTENANCE \\ COST" + tables.end_tabular(),

            tables.begin_tabular(r"@{}c@{}", "c") + "USE" + TeXStyle.generate_footnote_mark('10') + 
                                            r"\\" +  r"(Pls. write codes \\ only; refer below)" + tables.end_tabular(),

            tables.begin_tabular(r"@{}c@{}", "c") + "Others" + r"\\" +  r"(Please specify \\ if USE code is 15)" + tables.end_tabular() + 
                ' ' + r"\\" + ' ' + tables.generate_horizontal_line(),

        ]),

        NEWLINE,

        # tables.generate_entries(
        #     TeXJSON.parseJSONData(
        #         TeXJSON.requestJSONData(REQUEST_DATA_URL), cfg.TABLE_FORM_NAMES["2.5"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["2.5"]
        # ),

        tables.end_tabular(),
        tables.end_adjustbox(),
        tables.end_table(),

        NEWLINE,

        ovr_subsection.endgroup(), # End wrapper

        # === Section 3 ====
        TeXStyle.generate_section(cfg.SECTIONS["3"]),

        # generate_network_checklist

        # generate_security_checklist

        # generate_archiving_checklist


        NEWLINE * 2,

        # === This marks the end of the document (DO NOT REMOVE) ===
        doc.end_document()
    ]

    tex_file = open(cfg.TEX_FILENAME, "w+")
    tex_file.writelines(build_TeX)
    tex_file.close()

if __name__ == "__main__":
    main()
