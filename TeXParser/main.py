# =============================================================================
# TeXParser -- TeX/LaTeX Parser
# This is the main file for the TeXParser project.
# =============================================================================
import generators.paper_structure as TeXDoc
import generators.paper_headers as TeXHead
import generators.paper_frames as TeXFrame
import generators.paper_lists as TeXList
import generators.paper_tables as TeXTable
import generators.paper_questionnaire as TeXQues

import utilities.fix_style as TeXStyle
import utilities.fix_format as TeXFormat
import utilities.extract_json as TeXJSON

import settings.config as cfg
import settings.db_config as db_cfg
import settings.footer_config as foot_cfg
import settings.misc_config as misc_cfg

def main():
    # *** CONSTANTS ***
    NEWLINE = '\n'
    REQUEST_DATA_URL = "http://localhost/TeXParser/json_test.php"
    JSON_DATA = TeXJSON.requestJSONData(REQUEST_DATA_URL)

    # *** CLASS INIT (DOCUMENT) ***
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
    objectives = TeXList.Bullet(misc_cfg.OBJECTIVES)
    fill_out_instructions = TeXList.Bullet(misc_cfg.FILL_OUT_INSTRUCTIONS)

    # *** CLASS INIT (OVERRIDE) ***
    subsect_override = TeXFormat.OverrideFormat()

    # *** CLASS INIT (TABLES) ***
    tables: list[TeXTable.Tabular] = list()
    for key, value in cfg.TABLE_FORMATS.items():
        tables.append(TeXTable.Tabular({key: value}))

    # *** CLASS INIT (QUESTIONNAIRE) ***
    NETWORK_DATA = TeXJSON.parseJSONData(JSON_DATA, "network")
    net_ques_y_n = TeXQues.Questionnaire(NETWORK_DATA, {"3": "p{0.25cm} p{10cm} cc"}, ["YES", "NO"])
    net_ques_pbx = TeXQues.Questionnaire(NETWORK_DATA, {"3": "p{0.25cm} p{4cm} cccc"}, ["Private", "Hosted", "VoIP PBX or IP-PBX", "Hosted IP"])
    net_ques_moa = TeXQues.Questionnaire(NETWORK_DATA, {"3": "p{0.25cm} p{13.75cm}"}, db_cfg.QUES_OPTION_MAPPING["3.8"])
    net_ques_blank = TeXQues.Questionnaire(NETWORK_DATA, {"3": "p{0.25cm} p{13.75cm}"})

    SECURITY_DATA = TeXJSON.parseJSONData(JSON_DATA, "security")
    sec_ques_y_n = TeXQues.Questionnaire(SECURITY_DATA, {"4": "p{0.25cm} p{10cm} cc"}, ["YES", "NO"])
    sec_ques_meas = TeXQues.Questionnaire(SECURITY_DATA, {"4": "p{0.25cm} p{13.75cm}"}, db_cfg.QUES_OPTION_MAPPING["4.2"])

    # *** TeX Builder ***
    build_TeX = [
        # !!! IMPORTANT NOTE: The following lines should ideally not be changed nor modified. !!!
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
        # !!! END OF IMPORTANT NOTE !!!

        # === Color of hyperlinks, citations, and URLs ===
        TeXStyle.generate_hypersetup(cfg.LINK_COLOR, cfg.CITE_COLOR, cfg.URL_COLOR),

        NEWLINE * 2,

        # === Some header and footer configurations for the document ===
        TeXFormat.generate_fancystyle(),
        TeXFormat.clear_fancyhf(),
        TeXFormat.set_headerrule(0),
        TeXFormat.set_fancyfooter(['R'], r"\small\emph{Page \thepage\ of \pageref{LastPage}}\hspace{15pt}"),

        NEWLINE,

        # !!! This marks the start of the document (DO NOT REMOVE) !!!
        doc.begin_document(),

        NEWLINE * 2,

        # === Title of the document ===
        title.generate_title(),

        NEWLINE,

        # === Metadata for the document ===
        mdframe.generate_mdframe(),

        NEWLINE * 2,

        # === Objectives ===
        TeXStyle.bold_text(TeXStyle.italic_text(misc_cfg.OBJECTIVES["title"] + ':')),
        NEWLINE,
        objectives.begin_bullet(misc_cfg.OBJECTIVES_BULLET_OFFSET),
        objectives.generate_bullets(),
        objectives.end_bullet(),

        NEWLINE,

        # === Section 1 ===
        TeXStyle.generate_section(cfg.SECTIONS["1"]),

        # === Fill-out instructions ===
        TeXStyle.bold_text(misc_cfg.FILL_OUT_INSTRUCTIONS["title"] + ':'),
        NEWLINE,
        fill_out_instructions.begin_bullet(misc_cfg.FILL_OUT_INSTRUCTIONS_BULLET_OFFSET),
        TeXStyle.modify_substring(fill_out_instructions.generate_bullets(), "Reference year is last year", TeXStyle.bold_text),
        fill_out_instructions.end_bullet(),

        NEWLINE,

        # === Subsection 1.1 === 
        TeXStyle.generate_subsection(cfg.SECTIONS["1.1"]),
        TeXStyle.generate_footnote_text('1', foot_cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('2', foot_cfg.FOOTNOTES),
        NEWLINE * 2,

        tables[0].begin_table('H'),
        tables[0].set_arraystretch(1.5),
        tables[0].toggle_centering(),
        tables[0].begin_adjustbox("6in"),
        tables[0].begin_tabular("1.1"),
        tables[0].generate_horizontal_line(),

        NEWLINE,
        
        tables[0].generate_headers([
            tables[0].generate_multicolumn(1, "|c|", tables[0].generate_multirow(3, TeXStyle.bold_text("TYPES"))),
            tables[0].generate_multicolumn(7, "c|", TeXStyle.bold_text("TOTAL NUMBER OF FUNCTIONING UNITS BY YEAR ACQUIRED")) + r" \\ " + tables[0].generate_cline(2, 8),
            NEWLINE,
            tables[0].generate_multicolumn(2, "c|", TeXStyle.bold_text("$<$Last Year$>$")),
            tables[0].generate_multicolumn(2, "c|", TeXStyle.bold_text("$<$Last 2 Years$>$")),
            tables[0].generate_multicolumn(2, "c|", TeXStyle.bold_text("$<$Last 3 Years$>$")),
            tables[0].generate_multicolumn(1, "c|", tables[0].generate_multirow(2, TeXStyle.bold_text("More than 3 years"))) + r" \\ " + tables[0].generate_cline(2, 7),
            NEWLINE,
            tables[0].generate_multicolumn(1, "c|", TeXStyle.bold_text("Owned")),
            tables[0].generate_multicolumn(1, "c|", TeXStyle.bold_text("Leased")),
            tables[0].generate_multicolumn(1, "c|", TeXStyle.bold_text("Owned")),
            tables[0].generate_multicolumn(1, "c|", TeXStyle.bold_text("Leased")),
            tables[0].generate_multicolumn(1, "c|", TeXStyle.bold_text("Owned")),
            tables[0].generate_multicolumn(1, "c|", TeXStyle.bold_text("Leased")),
            tables[0].generate_multicolumn(1, "c|") + r" \\ " + tables[0].generate_horizontal_line(),
        ]),

        NEWLINE,
        
        TeXStyle.modify_substring(
            tables[0].generate_entries(
                TeXJSON.parseJSONData(
                    JSON_DATA, db_cfg.FORM_NAMES["1.1"]
                ), 
            default_fields=cfg.TABLE_DEFAULT_FIELDS["1.1"], limit=16
            ), "Mobile Phone", TeXStyle.append_footnotemark, '2'
        ),

        tables[0].end_tabular(),
        tables[0].end_adjustbox(),
        tables[0].end_table(),

        NEWLINE,

        # === Subsection 1.2 ===
        TeXStyle.generate_subsection(cfg.SECTIONS["1.2"]),
        TeXStyle.generate_footnote_text('3', foot_cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('4', foot_cfg.FOOTNOTES),
        NEWLINE * 2,

        tables[1].begin_table('H'),
        tables[1].set_arraystretch(1.5),
        tables[1].toggle_centering(),
        tables[1].begin_adjustbox(r"\textwidth"),
        tables[1].begin_tabular("1.2"),
        tables[1].generate_horizontal_line(),

        NEWLINE,

        tables[1].generate_headers([
            tables[1].generate_multicolumn(1, "|c|", tables[1].generate_multirow(2, TeXStyle.bold_text("TYPES"))),

            tables[1].generate_multicolumn(3, "c|", TeXStyle.bold_text("Operations")),

            TeXStyle.bold_text(tables[1].begin_tabular(r"@{}c@{}", "c") + r"General Administration\\ and Support Services\\ Support to Operations" + 
            TeXStyle.generate_footnote_mark('3') + tables[1].end_tabular()),

            tables[1].begin_tabular(r"@{}c@{}", "c") + TeXStyle.bold_text("Projects") + r"\\" +  TeXStyle.italic_text("(Not agency-funded)") + 
            tables[1].end_tabular() + r" \\ " + tables[1].generate_cline(2, 6),

            tables[1].generate_multicolumn(1, "c|", TeXStyle.bold_text("Employees")),
            tables[1].generate_multicolumn(1, "c|", TeXStyle.bold_text("Training")),
            tables[1].generate_multicolumn(1, "c|", TeXStyle.bold_text("Frontline Services") + TeXStyle.generate_footnote_mark('4')),
            TeXStyle.bold_text(""),
            TeXStyle.bold_text("") + r" \\ " + tables[1].generate_horizontal_line()
        ]),

        NEWLINE,

        tables[1].generate_entries(
            TeXJSON.parseJSONData(
                JSON_DATA, db_cfg.FORM_NAMES["1.2"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["1.2"]
        ),

        tables[1].end_tabular(),
        tables[1].end_adjustbox(),
        tables[1].end_table(),

        NEWLINE,

        # === Subsection 1.3 ===
        TeXStyle.generate_subsection(cfg.SECTIONS["1.3"]),

        tables[2].begin_table('H'),
        tables[2].set_arraystretch(1.5),
        tables[2].toggle_centering(),
        tables[2].begin_adjustbox("4in"),
        tables[2].begin_tabular("1.3"),
        tables[2].generate_horizontal_line(),

        NEWLINE,

        tables[2].generate_headers([
            tables[2].generate_multicolumn(1, "|c|", tables[2].generate_multirow(2, TeXStyle.bold_text("TOTAL CAPACITY OF HDD"))),

            tables[2].generate_multicolumn(2, "c|", TeXStyle.bold_text("LOCATION")) + r" \\ " + tables[2].generate_cline(2, 3),

            tables[2].generate_multicolumn(1, "c|", TeXStyle.bold_text("IN-HOUSE")),
            tables[2].generate_multicolumn(1, "c|", TeXStyle.bold_text("CO-LOCATED")) + r" \\ " + tables[2].generate_horizontal_line()
        ]),

        NEWLINE,

        tables[2].generate_entries(
            TeXJSON.parseJSONData(
                JSON_DATA, db_cfg.FORM_NAMES["1.3"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["1.3"]
        ),

        tables[2].end_tabular(),
        tables[2].end_adjustbox(),
        tables[2].end_table(),

        NEWLINE,

        # === Section 2 ===
        TeXStyle.generate_section(cfg.SECTIONS["2"]),

        # === Subsection 2.1 ===
        TeXStyle.generate_subsection(cfg.SECTIONS["2.1"]),

        # === Subsubsection 2.1.1 ===
        TeXStyle.generate_subsubsection(cfg.SECTIONS["2.1.1"]),
        TeXStyle.generate_footnote_text('5', foot_cfg.FOOTNOTES),
        NEWLINE * 2,

        tables[3].begin_table('H'),
        tables[3].set_arraystretch(1.5),
        tables[3].toggle_centering(),
        tables[3].begin_adjustbox("5.5in"),
        tables[3].begin_tabular("2.1.1"),
        tables[3].generate_horizontal_line(),

        NEWLINE,

        tables[3].generate_headers([
            tables[3].generate_multicolumn(1, "|c|", "OPERATING SYSTEM"),
            tables[3].generate_multicolumn(1, "c|", f"Lifetime License?{TeXStyle.generate_footnote_mark('5')}"),
            tables[3].generate_multicolumn(1, "c|", "If not, write below the year of expiration") + r" \\ " + tables[3].generate_horizontal_line()
        ]),

        NEWLINE,

        tables[3].generate_entries(
            TeXJSON.parseJSONData(
                JSON_DATA, db_cfg.FORM_NAMES["2.1.1"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["2.1.1"], tickbox_cols=db_cfg.TICKBOX_COLS["2.1.1"]
        ),

        tables[3].end_tabular(),
        tables[3].end_adjustbox(),
        tables[3].end_table(),

        NEWLINE,

        # === Subsubsection 2.1.2 ===
        TeXStyle.generate_subsubsection(cfg.SECTIONS["2.1.2"]),

        tables[4].begin_table('H'),
        tables[4].set_arraystretch(1.5),
        tables[4].toggle_centering(),
        tables[4].begin_adjustbox("5.5in"),
        tables[4].begin_tabular("2.1.2"),
        tables[4].generate_horizontal_line(),

        NEWLINE,

        tables[4].generate_headers([
            tables[4].generate_multicolumn(1, "|c|", "OPERATING SYSTEM"),
            tables[4].generate_multicolumn(1, "c|", "Lifetime License?"),
            tables[4].generate_multicolumn(1, "c|", "If not, write below the year of expiration") + r" \\ " + tables[4].generate_horizontal_line()
        ]),

        NEWLINE,

        tables[4].generate_entries(
            TeXJSON.parseJSONData(
                JSON_DATA, db_cfg.FORM_NAMES["2.1.2"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["2.1.2"], tickbox_cols=db_cfg.TICKBOX_COLS["2.1.2"]
        ),

        tables[4].end_tabular(),
        tables[4].end_adjustbox(),
        tables[4].end_table(),

        NEWLINE,

        # === Subsubsection 2.1.3 ===
        TeXStyle.generate_subsubsection(cfg.SECTIONS["2.1.3"]),

        tables[5].begin_table('H'),
        tables[5].set_arraystretch(1.5),
        tables[5].toggle_centering(),
        tables[5].begin_adjustbox("5.5in"),
        tables[5].begin_tabular("2.1.3"),
        tables[5].generate_horizontal_line(),

        NEWLINE,

        tables[5].generate_headers([
            tables[5].generate_multicolumn(1, "|c|", "OPERATING SYSTEM"),
            tables[5].generate_multicolumn(1, "c|", "Lifetime License?"),
            tables[5].generate_multicolumn(1, "c|", "If not, write below the year of expiration") + r" \\ " + tables[5].generate_horizontal_line()
        ]),

        NEWLINE,

        tables[5].generate_entries(
            TeXJSON.parseJSONData(
                JSON_DATA, db_cfg.FORM_NAMES["2.1.3"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["2.1.3"], tickbox_cols=db_cfg.TICKBOX_COLS["2.1.3"]
        ),

        tables[5].end_tabular(),
        tables[5].end_adjustbox(),
        tables[5].end_table(),

        NEWLINE,

        # === Subsection 2.2 ===
        TeXStyle.generate_subsection(cfg.SECTIONS["2.2"]),

        tables[6].begin_table('H'),
        tables[6].set_arraystretch(1.5),
        tables[6].toggle_centering(),
        tables[6].begin_adjustbox("6.5in"),
        tables[6].begin_tabular("2.2"),
        tables[6].generate_horizontal_line(),

        NEWLINE,

        tables[6].generate_headers([
            tables[6].generate_multicolumn(1, "|c|", "SOFTWARE / APPLICATION PACKAGE"),
            tables[6].generate_multicolumn(1, "c|", "Lifetime License?"),
            tables[6].generate_multicolumn(1, "c|", "If not, write below the year of expiration") + r" \\ " + tables[6].generate_horizontal_line()
        ]),

        NEWLINE,

        tables[6].generate_entries(
            TeXJSON.parseJSONData(
                JSON_DATA, db_cfg.FORM_NAMES["2.2"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["2.2"], tickbox_cols=db_cfg.TICKBOX_COLS["2.2"]
        ),

        tables[6].end_tabular(),
        tables[6].end_adjustbox(),
        tables[6].end_table(),

        NEWLINE,

        # === Subsection 2.3 ===
        subsect_override.begingroup(), # Start wrapper for the section title.
        subsect_override.change_titleformat(cfg.FONT_SIZE, "subsection", "runin"), # Simply just to allow text beside a section title.

        TeXStyle.modify_substring(TeXStyle.generate_subsection(cfg.SECTIONS["2.3"]), "Oversight", TeXStyle.append_footnotemark, '6', True),
        cfg.SECTION_NOTES["2.3"],
        TeXStyle.generate_footnote_text('6', foot_cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('7', foot_cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('8', foot_cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('9', foot_cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('10', foot_cfg.FOOTNOTES),

        NEWLINE,

        tables[7].begin_table('H'),
        tables[7].set_arraystretch(1.5),
        tables[7].toggle_centering(),
        tables[7].begin_adjustbox(r"\textwidth"),
        tables[7].begin_tabular("2.3"),
        tables[7].generate_horizontal_line(),

        NEWLINE,

        tables[7].generate_headers([
            tables[7].generate_multicolumn(1, "|c|", tables[7].begin_tabular(r"@{}c@{}", "c") + "NAME OF SYSTEM" + r"\\" + 
                                            r"(Please list down the \\ name/s of your \\ administrative system/s)" + tables[7].end_tabular()),

            tables[7].begin_tabular(r"@{}c@{}", "c") + r"Own Intellectual \\ Property," + 
                                            r"\\" +  "Y or N?" + TeXStyle.generate_footnote_mark('8') + tables[7].end_tabular(),

            tables[7].begin_tabular(r"@{}c@{}", "c") + r"DEVELOPMENT \\ PLATFORM" + 
                                            r"\\" +  r"(ex. LAMP, .NET, \\ Java)" + tables[7].end_tabular(),

            tables[7].begin_tabular(r"@{}c@{}", "c") + r"WORKING \\ ENVIRONMENT" + 
                                            TeXStyle.generate_footnote_mark('9') + r"\\" +  r"(Use codes \\ below)" + tables[7].end_tabular(),

            tables[7].begin_tabular(r"@{}c@{}", "c") + r"MAINTENANCE \\ COST" + tables[7].end_tabular(),

            tables[7].begin_tabular(r"@{}c@{}", "c") + "USE" + TeXStyle.generate_footnote_mark('10') + 
                                            r"\\" +  r"(Pls. write codes \\ only; refer below)" + tables[7].end_tabular(),

            tables[7].begin_tabular(r"@{}c@{}", "c") + "Others" + r"\\" +  r"(Please specify \\ if USE code is 15)" + tables[7].end_tabular() + 
                r" \\ " + tables[7].generate_horizontal_line(),

        ]),

        NEWLINE,

        tables[7].generate_entries(
            TeXJSON.parseJSONData(
                JSON_DATA, db_cfg.FORM_NAMES["2.3"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["2.3"]
        ),

        tables[7].end_tabular(),
        tables[7].end_adjustbox(),
        tables[7].end_table(),

        NEWLINE,

        # === Subsection 2.4 ===
        TeXStyle.modify_substring(TeXStyle.generate_subsection(cfg.SECTIONS["2.4"]), "Operational", TeXStyle.append_footnotemark, '11', True),
        cfg.SECTION_NOTES["2.4"],
        TeXStyle.generate_footnote_text('11', foot_cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('12', foot_cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('13', foot_cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('14', foot_cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('15', foot_cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('16', foot_cfg.FOOTNOTES),
        TeXStyle.generate_footnote_text('17', foot_cfg.FOOTNOTES),

        NEWLINE,

        tables[8].begin_table('H'),
        tables[8].set_arraystretch(1.5),
        tables[8].toggle_centering(),
        tables[8].begin_adjustbox(r"\textwidth"),
        tables[8].begin_tabular("2.4"),
        tables[8].generate_horizontal_line(),

        NEWLINE,

        tables[8].generate_headers([
            tables[8].generate_multicolumn(1, "|c|", tables[8].begin_tabular(r"@{}c@{}", "c") + "NAME OF SYSTEM" + r"\\" + 
                                            r"(Please list down the \\ name/s of your \\ administrative system/s)" + tables[8].end_tabular()),

            tables[8].begin_tabular(r"@{}c@{}", "c") + r"Own Intellectual \\ Property," + 
                                            r"\\" +  "Y or N?" + TeXStyle.generate_footnote_mark('8') + tables[8].end_tabular(),

            tables[8].begin_tabular(r"@{}c@{}", "c") + r"DEVELOPMENT \\ PLATFORM" + 
                                            r"\\" +  r"(ex. LAMP, .NET, \\ Java)" + tables[8].end_tabular(),

            tables[8].begin_tabular(r"@{}c@{}", "c") + r"WORKING \\ ENVIRONMENT" + 
                                            TeXStyle.generate_footnote_mark('9') + r"\\" +  r"(Use codes \\ below)" + tables[8].end_tabular(),

            tables[8].begin_tabular(r"@{}c@{}", "c") + r"MAINTENANCE \\ COST" + tables[8].end_tabular(),

            tables[8].begin_tabular(r"@{}c@{}", "c") + "USE" + TeXStyle.generate_footnote_mark('10') + 
                                            r"\\" +  r"(Pls. write codes \\ only; refer below)" + tables[8].end_tabular(),

            tables[8].begin_tabular(r"@{}c@{}", "c") + "Others" + r"\\" +  r"(Please specify \\ if USE code is 15)" + tables[8].end_tabular() + 
                r" \\ " + tables[8].generate_horizontal_line(),

        ]),

        NEWLINE,

        tables[8].generate_entries(
            TeXJSON.parseJSONData(
                JSON_DATA, db_cfg.FORM_NAMES["2.4"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["2.4"]
        ),

        tables[8].end_tabular(),
        tables[8].end_adjustbox(),
        tables[8].end_table(),

        NEWLINE,

        # === Subsection 2.5 ===
        TeXStyle.generate_subsection(cfg.SECTIONS["2.5"]),
        cfg.SECTION_NOTES["2.5"],

        NEWLINE,

        tables[9].begin_table('H'),
        tables[9].set_arraystretch(1.5),
        tables[9].toggle_centering(),
        tables[9].begin_adjustbox(r"\textwidth"),
        tables[9].begin_tabular("2.5"),
        tables[9].generate_horizontal_line(),

        NEWLINE,

        tables[9].generate_headers([
            tables[9].generate_multicolumn(1, "|c|", "NAME OF DATABASE"),

            tables[9].begin_tabular(r"@{}c@{}", "c") + r"Own Intellectual \\ Property," + 
                                            r"\\" +  "Y or N?" + TeXStyle.generate_footnote_mark('8') + tables[9].end_tabular(),

            tables[9].begin_tabular(r"@{}c@{}", "c") + r"BRIEF \\ DESCRIPTION AND \\ KEY FIELDS" + TeXStyle.generate_footnote_mark('16') + tables[9].end_tabular(),

            tables[9].begin_tabular(r"@{}c@{}", "c") + r"DATABASE \\ MANAGEMENT \\ SOFTWARE" + 
                                            TeXStyle.generate_footnote_mark('17') + r"\\" +  r"USED" + tables[9].end_tabular(),

            tables[9].begin_tabular(r"@{}c@{}", "c") + r"MAINTENANCE \\ COST" + tables[9].end_tabular(),

            tables[9].begin_tabular(r"@{}c@{}", "c") + "USE" + TeXStyle.generate_footnote_mark('10') + 
                                            r"\\" +  r"(Pls. write codes \\ only; refer below)" + tables[9].end_tabular(),

            tables[9].begin_tabular(r"@{}c@{}", "c") + "Others" + r"\\" +  r"(Please specify \\ if USE code is 15)" + tables[9].end_tabular() + 
                r" \\ " + tables[9].generate_horizontal_line(),

        ]),

        NEWLINE,

        tables[9].generate_entries(
            TeXJSON.parseJSONData(
                JSON_DATA, db_cfg.FORM_NAMES["2.5"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["2.5"]
        ),

        tables[9].end_tabular(),
        tables[9].end_adjustbox(),
        tables[9].end_table(),

        NEWLINE,

        subsect_override.endgroup(), # End wrapper

        # === Section 3 ====
        TeXStyle.generate_section(cfg.SECTIONS["3"]),

        TeXStyle.vertical_space("-2em"),

        net_ques_y_n.generate_options_inline(cfg.QUESTIONS["3"], 0, 4, start_col_search="LAN"),
        TeXStyle.vertical_space("-2.25em"), # remove whitespace in between the tables
        net_ques_pbx.generate_options_inline(cfg.QUESTIONS["3"], 5, 5, start_col_search="PBX_Setup"),
        TeXStyle.vertical_space("-2.25em"),
        net_ques_y_n.generate_options_inline(cfg.QUESTIONS["3"], 6, 6, start_col_search="Internet"),
        TeXStyle.vertical_space("-2.25em"),
        net_ques_moa.generate_options_multi(cfg.QUESTIONS["3"][7], q_idx=7, start_col_search="MOA", num_of_cols=3, col_adjust="4.5in"),
        TeXStyle.vertical_space("-2.25em"),
        net_ques_blank.generate_fill_blank(cfg.QUESTIONS["3"], 8, 11, start_col_search="ISPs"),
        TeXStyle.vertical_space("-2.25em"),
        net_ques_y_n.generate_options_inline(cfg.QUESTIONS["3"], 12, 12, start_col_search="Website"),
        TeXStyle.vertical_space("-2.25em"),
        net_ques_blank.generate_fill_blank(cfg.QUESTIONS["3"], 13, 13, start_col_search="URL"),

        # === Section 4 ===
        TeXStyle.generate_section(cfg.SECTIONS["4"]),

        TeXStyle.vertical_space("-2em"),

        sec_ques_y_n.generate_options_inline(cfg.QUESTIONS["4"], 0, 0, start_col_search="Protection"),
        TeXStyle.vertical_space("-2.25em"),
        sec_ques_meas.generate_options_multi(cfg.QUESTIONS["4"][1], q_idx=1, start_col_search="Measures", num_of_cols=2, col_adjust="6in", col_format="p{7cm}p{6cm}"),

        # === Section 5 ===
        TeXStyle.generate_section(cfg.SECTIONS["5"]),

        NEWLINE * 2,

        # !!! This marks the end of the document (DO NOT REMOVE) !!!
        doc.end_document()
    ]

    tex_file = open(cfg.TEX_FILENAME, "w+")
    tex_file.writelines(build_TeX)
    tex_file.close()

if __name__ == "__main__":
    main()
