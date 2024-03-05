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

import logging
import os

def main():
    # *** CONSTANTS ***
    NEWLINE = '\n'
    EMPTY = ""
    REQUEST_DATA_URL = "http://localhost/TeXParser/json_test.php"
    JSON_DATA = TeXJSON.requestJSONData(REQUEST_DATA_URL)

    # *** CLASS INIT (DOCUMENT TOP) ***
    docu = TeXDoc.Document(cfg.PAPER, cfg.FONT_SIZE, cfg.PAPER_TYPE)
    title = TeXHead.Title(cfg.TITLE)
    metadata = TeXFrame.MDFrame(
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
    override_pref = TeXFormat.OverrideFormat()

    # *** CLASS INIT (TABLES) ***
    tables: list[TeXTable.Tabular] = list()
    for key, value in cfg.TABLE_FORMATS.items():
        tables.append(TeXTable.Tabular({key: value}))

    # *** CLASS INIT (QUESTIONNAIRE) ***
    NETWORK_DATA = TeXJSON.parseJSONData(JSON_DATA, db_cfg.FORM_NAMES["3"])
    net_ques_y_n = TeXQues.Questionnaire(NETWORK_DATA, {"3": "p{0.25cm} p{10cm} cc"}, ["YES", "NO"])
    net_ques_pbx = TeXQues.Questionnaire(NETWORK_DATA, {"3": "p{0.25cm} p{4cm} cccc"}, ["Private", "Hosted", "VoIP PBX or IP-PBX", "Hosted IP"])
    net_ques_moa = TeXQues.Questionnaire(NETWORK_DATA, {"3": "p{0.25cm} p{13.75cm}"}, db_cfg.QUES_OPTION_MAPPING["3.8"])
    net_ques_blank = TeXQues.Questionnaire(NETWORK_DATA, {"3": "p{0.25cm} p{13.75cm}"})

    SECURITY_DATA = TeXJSON.parseJSONData(JSON_DATA, db_cfg.FORM_NAMES["4"])
    sec_ques_y_n = TeXQues.Questionnaire(SECURITY_DATA, {"4": "p{0.25cm} p{10cm} cc"}, ["YES", "NO"])
    sec_ques_meas = TeXQues.Questionnaire(SECURITY_DATA, {"4": "p{0.25cm} p{13.75cm}"}, db_cfg.QUES_OPTION_MAPPING["4.2"])

    ARCHIVING_DATA = TeXJSON.parseJSONData(JSON_DATA, db_cfg.FORM_NAMES["5"])
    arch_ques_y_n = TeXQues.Questionnaire(ARCHIVING_DATA, {"5": "p{0.25cm} p{10cm} cc"}, ["YES", "NO"])
    arch_ques_sys = TeXQues.Questionnaire(ARCHIVING_DATA, {"5": "p{0.25cm} p{13.75cm}"}, db_cfg.QUES_OPTION_MAPPING["5.2"])
    arch_ques_elecdata = TeXQues.Questionnaire(ARCHIVING_DATA, {"5": "p{0.25cm} p{13.75cm}"}, db_cfg.QUES_OPTION_MAPPING["5.3"])
    arch_ques_mos = TeXQues.Questionnaire(ARCHIVING_DATA, {"5": "p{0.25cm} p{13.75cm}"}, db_cfg.QUES_OPTION_MAPPING["5.4"])
    arch_ques_elecinfo = TeXQues.Questionnaire(ARCHIVING_DATA, {"5": "p{0.25cm} p{13.75cm}"}, db_cfg.QUES_OPTION_MAPPING["5.5"])

    CENTER_DATA = TeXJSON.parseJSONData(JSON_DATA, db_cfg.FORM_NAMES["7"])
    cen_ques_y_n = TeXQues.Questionnaire(CENTER_DATA, {"7": "p{0.25cm} p{10cm} cc"}, ["YES", "NO"])
    cen_ques_blank = TeXQues.Questionnaire(CENTER_DATA, {"7": "p{0.25cm} p{13.75cm}"})
    cen_ques_hous_out = TeXQues.Questionnaire(CENTER_DATA, {"7": "p{0.25cm} p{10cm} cc"}, ["In-house", "Outsourced"])

    ICT_ISSUES_DATA = TeXJSON.parseJSONData(JSON_DATA, db_cfg.FORM_NAMES["8.2"])
    issues_ques_proj = TeXQues.Questionnaire(ICT_ISSUES_DATA, {"8.2": "p{0.25cm} p{13.75cm}"}, db_cfg.QUES_OPTION_MAPPING["8.2"])


    # *** CLASS INIT (DOCUMENT BOTTOM) ***
    send_ques = TeXFrame.MDFrame(
        content=[
            "Please send accomplished questionnaire to:"
        ]
    )

    receiver = TeXFrame.MDFrame(
        content=[
            TeXStyle.bold_text(cfg.OFFICE_NAME) + r"\\",
            cfg.OFFICE_TYPE + r"\\",
            cfg.OFFICE_ADDRESS + r"\\",
            f"or email soft copy to {TeXStyle.bold_text(TeXFormat.translation_table(cfg.OFFICE_EMAIL))}" + r"\\",
            TeXFormat.force_linebreak(),
            f"You may download the form at {cfg.OFFICE_LINK}." + r"\\",
            f"Call {cfg.OFFICE_CONTACTS[0]} or {cfg.OFFICE_CONTACTS[1]} for assistance."
        ]
    )


    # *** TeX Builder ***
    build_TeX = [
        # !!! IMPORTANT NOTE: The following lines should ideally not be changed nor modified. !!!
        docu.generate_document(),
        NEWLINE,
        docu.import_package("inputenc", ["utf8"]),
        ''.join([docu.import_package(pkg) for pkg in ["amssymb", "float", "url"]]),
        docu.import_package("hyperref", ["final"]),
        NEWLINE,
        ''.join([docu.import_package(pkg) for pkg in ["latexsym", "setspace", "enumitem", "makecell", 
                                                       "multicol", "multirow", "lastpage", "mdframed",
                                                       "titlesec"]]),
        docu.import_package("footmisc", ["bottom"]),
        NEWLINE,
        ''.join([docu.import_package(pkg) for pkg in ["fancyhdr", "newfloat", "graphicx", "array"]]),
        docu.import_package("adjustbox", ["export"]),
        NEWLINE,
        docu.import_package("geometry", [f"margin={cfg.MARGIN}", cfg.PAPER]),
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
        docu.begin_document(),

        NEWLINE * 2,

        # === Title of the document ===
        title.generate_title(),

        NEWLINE,

        # === Metadata for the document ===
        metadata.generate_mdframe(),

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
            default_fields=cfg.TABLE_DEFAULT_FIELDS["1.1"], limit=17
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
            TeXStyle.bold_text(EMPTY),
            TeXStyle.bold_text(EMPTY) + r" \\ " + tables[1].generate_horizontal_line()
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
        override_pref.begingroup(), # Start wrapper for the section title.
        override_pref.change_titleformat(cfg.FONT_SIZE, "subsection", "runin"), # Simply just to allow text beside a section title.

        TeXStyle.modify_substring(TeXStyle.generate_subsection(cfg.SECTIONS["2.3"]), "Oversight", TeXStyle.append_footnotemark, '6', True),
        cfg.SECTION_NOTES["2.3"],
        ''.join([TeXStyle.generate_footnote_text(str(num), foot_cfg.FOOTNOTES) for num in range(6, 11)]),

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
        ''.join([TeXStyle.generate_footnote_text(str(num), foot_cfg.FOOTNOTES) for num in range(11, 18)]),

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

        override_pref.endgroup(), # End wrapper

        # === Section 3 ====
        TeXStyle.generate_section(cfg.SECTIONS["3"]),

        TeXStyle.vertical_space("-2em"),

        net_ques_y_n.generate_options_inline(cfg.QUESTIONS["3"], 0, 4, start_col_search="LAN"),
        TeXStyle.vertical_space("-2.25em"), # remove whitespace in between the tables
        net_ques_pbx.generate_options_inline(cfg.QUESTIONS["3"], 5, 5, start_col_search="PBX_Setup"),
        TeXStyle.vertical_space("-2.25em"),
        net_ques_y_n.generate_options_inline(cfg.QUESTIONS["3"], 6, 6, start_col_search="Internet"),
        TeXStyle.vertical_space("-2.25em"),
        net_ques_moa.generate_options_multi(cfg.QUESTIONS["3"], q_idx=7, start_col_search="MOA", num_of_cols=3, col_adjust="4.5in"),
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
        sec_ques_meas.generate_options_multi(cfg.QUESTIONS["4"], q_idx=1, start_col_search="Measures", num_of_cols=2, col_adjust="6in", col_format="p{7cm}p{6cm}"),

        # === Section 5 ===
        TeXStyle.generate_section(cfg.SECTIONS["5"]),

        TeXStyle.vertical_space("-2em"),

        arch_ques_y_n.generate_options_inline(cfg.QUESTIONS["5"], 0, 0, start_col_search="System"),
        TeXStyle.vertical_space("-2.25em"),
        arch_ques_sys.generate_options_multi(cfg.QUESTIONS["5"], q_idx=1, start_col_search="System_type", num_of_cols=3, col_adjust="4.5in"),
        TeXStyle.vertical_space("-2.25em"),
        arch_ques_elecdata.generate_options_multi(cfg.QUESTIONS["5"], q_idx=2, start_col_search="Electronic_mode", num_of_cols=2, col_adjust="4.5in", col_format="p{4.75cm}p{4.75cm}"),
        TeXStyle.vertical_space("-2.25em"),
        arch_ques_mos.generate_options_multi(cfg.QUESTIONS["5"], q_idx=3, start_col_search="Conventional_Medium", num_of_cols=2, col_adjust="6in", col_format="p{7cm}p{6cm}"),
        TeXStyle.vertical_space("-2.25em"),
        arch_ques_elecinfo.generate_options_multi(cfg.QUESTIONS["5"], q_idx=4, start_col_search="Electronic_Info", num_of_cols=2, col_adjust="6in", col_format="p{7cm}p{6cm}"),

        # === Section 6 ===
        TeXStyle.generate_section(cfg.SECTIONS["6"]),

        NEWLINE,

        tables[10].begin_table('H'),
        tables[10].set_arraystretch(1.5),
        tables[10].toggle_centering(),
        tables[10].begin_adjustbox(r"\textwidth"),
        tables[10].begin_tabular("6"),
        tables[10].generate_horizontal_line(),

        NEWLINE,

        tables[10].generate_headers([
            tables[10].generate_multicolumn(1, "|c|", "SPECIAL SOLUTIONS PACKAGE"),

            tables[10].begin_tabular(r"@{}c@{}", "c") + r"USE" + TeXStyle.generate_footnote_mark('18') +
                                            r"\\" +  "(Pls. write  codes only; refer below)"  + tables[10].end_tabular(),

            tables[10].begin_tabular(r"@{}c@{}", "c") + "Others" + r"\\" +  r"(Please specify \\ if USE code is 15)" + tables[10].end_tabular(),

            tables[10].generate_multicolumn(1, "c|", "MAINTENANCE COST") + r" \\ " + tables[10].generate_horizontal_line(),
        ]),

        NEWLINE,

        tables[10].generate_entries(
            TeXJSON.parseJSONData(
                JSON_DATA, db_cfg.FORM_NAMES["6"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["6"]
        ),

        tables[10].end_tabular(),
        tables[10].end_adjustbox(),
        tables[10].end_table(),

        NEWLINE,

        # === Section 7 ===
        TeXStyle.generate_section(cfg.SECTIONS["7"]),

        TeXStyle.vertical_space("-2em"),

        cen_ques_y_n.generate_options_inline(cfg.QUESTIONS["7"], 0, 0, start_col_search="Data_center"),
        TeXStyle.vertical_space("-2.25em"),
        cen_ques_blank.generate_fill_blank(cfg.QUESTIONS["7"], 1, 1, start_col_search="Sites"),
        TeXStyle.vertical_space("-2.25em"),
        cen_ques_hous_out.generate_options_inline(cfg.QUESTIONS["7"], 2, 2, start_col_search="Maintenance"),
        TeXStyle.vertical_space("-2.25em"),
        cen_ques_y_n.generate_fill_blank(cfg.QUESTIONS["7"], 3, 3, start_col_search="Back-up_site", col_format="5.25in"),

        # === Section 8 ===
        TeXStyle.generate_section(cfg.SECTIONS["8"]),
        ''.join([TeXStyle.generate_footnote_text(str(num), foot_cfg.FOOTNOTES) for num in range(18, 24)]),

        # === Subsection 8.1 ===
        TeXStyle.generate_subsection(cfg.SECTIONS["8.1"]),

        NEWLINE,

        tables[11].begin_table('H'),
        tables[11].set_arraystretch(1.5),
        tables[11].toggle_centering(),
        tables[11].begin_adjustbox(r"\textwidth"),
        tables[11].begin_tabular("8.1"),
        tables[11].generate_horizontal_line(),

        NEWLINE,

        tables[11].generate_headers([
            tables[11].generate_multirow(2, "PROJECT NAME" + TeXStyle.generate_footnote_mark('19')) ,

            tables[11].generate_multirow(2, "DESCRIPTION"),

            tables[11].generate_multicolumn(2, "c|", tables[11].begin_tabular(r"@{}c@{}", "c") + r"PERIOD" + 
                                            r"\\" +  "(in mm/dd/yyyy)"  + tables[11].end_tabular()),

            tables[11].generate_multirow(2,  tables[11].begin_tabular(r"@{}c@{}", "c") + r"COST" + TeXStyle.generate_footnote_mark('20') + 
                                         r"\\" +  "(in pesos)"  + tables[11].end_tabular()),

            tables[11].generate_multirow(2,  tables[11].begin_tabular(r"@{}c@{}", "c") + r"DEVELOPMENT" + r"\\" + "STRATEGY" + 
                                         TeXStyle.generate_footnote_mark('21') + r"\\" +  r"(Please write codes only)" + tables[11].end_tabular()),

            tables[11].generate_multirow(2,  tables[11].begin_tabular(r"@{}c@{}", "c") + r"STATUS" + TeXStyle.generate_footnote_mark('22') +
                                            r"\\" +  r"(Please write \\ codes only)" + tables[11].end_tabular()),     

            tables[11].generate_multirow(2,  tables[11].begin_tabular(r"@{}c@{}", "c") + r"USE" + TeXStyle.generate_footnote_mark('23') +
                                            r"\\" +  r"(Please write \\ codes only)" + tables[11].end_tabular()),

            tables[11].generate_multirow(2, tables[11].begin_tabular(r"@{}c@{}", "c") + "Others" + r"\\" +  r"(Please specify \\ if USE code is 15)" + 
                                            tables[11].end_tabular()) + r" \\ " + tables[11].generate_cline(3 , 4),
            
            EMPTY,

            tables[11].generate_multicolumn(1, "c|", tables[11].begin_tabular(r"@{}c@{}", "c") + "Start" + r"\\" + 
                                            "Date" + tables[11].end_tabular()),

            tables[11].begin_tabular(r"@{}c@{}", "c") + "End" + r"\\" + 
                                            "Date" + tables[11].end_tabular(),

            EMPTY,
            EMPTY,
            EMPTY,
            EMPTY,
            EMPTY + r"\\" + tables[11].generate_horizontal_line(),

        ]),

        NEWLINE,

        tables[11].generate_entries(
            TeXJSON.parseJSONData(
                JSON_DATA, db_cfg.FORM_NAMES["8.1"]), default_fields=cfg.TABLE_DEFAULT_FIELDS["8.1"]
        ),

        tables[11].end_tabular(),
        tables[11].end_adjustbox(),
        tables[11].end_table(),

        NEWLINE,

        # === Subsection 8.2 ===
        TeXStyle.generate_subsection(cfg.SECTIONS["8.2"]),

        TeXStyle.vertical_space("-1.25em"),

        issues_ques_proj.generate_options_multi(start_col_search="Issues", num_of_cols=2, col_adjust="6in", col_format="p{7cm}p{6cm}"),

        # === Outro ===
        send_ques.generate_mdframe(),

        NEWLINE,
        TeXStyle.vertical_space("-1.25em"),

        receiver.generate_mdframe(is_centered=True),

        NEWLINE,

        TeXStyle.bold_text(override_pref.change_fontsize("large") + ' ' + "Definition of Terms:") + ' ' + r"\\",

        NEWLINE,

        TeXStyle.process_text(misc_cfg.DEFINITION_OF_TERMS[0:11]),

        ''.join([TeXStyle.generate_footnote_text(str(num), foot_cfg.FOOTNOTES) for num in range(24, 33)]),

        NEWLINE,

        TeXFormat.toggle_noindent(),
        TeXStyle.process_text(misc_cfg.DEFINITION_OF_TERMS[11:]),

        ''.join([TeXStyle.generate_footnote_text(str(num), foot_cfg.FOOTNOTES) for num in range(33, 49)]),

        NEWLINE * 2,

        # !!! This marks the end of the document (DO NOT REMOVE) !!!
        docu.end_document()
    ]

    os.makedirs(cfg.TEX_FILEDIR, exist_ok=True)
    TEX_FILEPATH = os.path.join(cfg.TEX_FILEDIR, cfg.TEX_FILENAME)

    with open(TEX_FILEPATH, "w+") as TEX_FILE:
        TEX_FILE.writelines(build_TeX)

    TEX_FILE.close()

if __name__ == "__main__":
    logging.info("Executing TeXParser...")
    main()
    for _ in range(2): # Execute twice for .aux dependencies
        os.system(f"pdflatex --enable-installer --include-directory=pdfoutput --output-directory=pdfoutput  --interaction=nonstopmode --quiet {cfg.TEX_FILENAME}")
    logging.info("TeXParser terminated successfully without errors.")