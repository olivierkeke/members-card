import qrcode
from fpdf import FlexTemplate, FPDF
from fpdf.pattern import LinearGradient
from pathlib import Path
from typing import Optional


def generate_cards(
    names: list[str],
    background_color_1: int | tuple[int, int, int] | str,
    background_color_2: int | tuple[int, int, int] | str,
    paper_format: str | tuple[int, int],
    qrcode_url: Optional[str],
    logo_path: Path,
    title: str,
    footer_1: str,
    footer_2: str,
    title_color: int = 0x000000,
    name_color: int = 0x000000,
    footer_color: int = 0x000000,
) -> FPDF:
    if qrcode_url is not None:
        qr = qrcode.QRCode()
        qr.add_data(qrcode_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="transparent")

    elements = [
        {
            "name": "title",
            "type": "T",
            "x1": 0,
            "x2": 85,
            "y1": 3,
            "y2": 9,
            "size": 16,
            "bold": True,
            "foreground": title_color,
            "align": "C",
            "text": title,
        },
        {
            "name": "logo",
            "type": "I",
            "x1": 40,
            "x2": 80,
            "y1": 10,
            "y2": 50,
            "align": "C",
            "text": str(logo_path) if logo_path is not None else None,
        },
        {
            "name": "name",
            "type": "T",
            "x1": 5,
            "x2": 10,
            "y1": 14,
            "y2": 20,
            "font": "helvetica",
            "size": 12,
            "bold": True,
            "foreground": name_color,
            "text": "Nom",
        },
        {"name": "qrcode", "type": "I", "x1": 10, "x2": 35, "y1": 22, "y2": 47},
        {
            "name": "footer",
            "type": "T",
            "x1": 0,
            "x2": 85,
            "y1": 50,
            "y2": 52,
            "size": 6,
            "align": "C",
            "foreground": footer_color,
            "text": footer_1,
        },
        {
            "name": "footer2",
            "type": "T",
            "x1": 0,
            "x2": 85,
            "y1": 52,
            "y2": 54,
            "size": 6,
            "align": "C",
            "foreground": footer_color,
            "text": footer_2,
        },
    ]
    pdf = FPDF(orientation="landscape", format=paper_format)

    paper_width = pdf.w
    paper_height = pdf.h
    nb_rows = paper_height // 55
    nb_cols = paper_width // 85
    nb_cards_per_page = nb_rows * nb_cols
    margex = round((paper_width - nb_cols * 85) / 2.0)
    margey = round((paper_height - nb_rows * 55) / 2.0)

    for i, member in enumerate(names):
        if i % nb_cards_per_page == 0:
            pdf.add_page()
        id_in_page = i % nb_cards_per_page
        row = id_in_page % nb_cols
        col = id_in_page // nb_rows
        offsetx = 85 * col + margex
        offsety = 55 * row + margey
        linear_grad = LinearGradient(
            from_x=85 + offsetx,  # Starting x-coordinate
            from_y=0 + offsety,  # Starting y-coordinate
            to_x=offsetx,  # Ending x-coordinate
            to_y=55 + offsety,  # Ending y-coordinate
            colors=[background_color_2, background_color_1],  # Start -> End color
        )
        with pdf.use_pattern(linear_grad):
            # Draw a rectangle that will be filled with the gradient
            pdf.rect(x=offsetx, y=offsety, w=85, h=55, style="FD")
        template = FlexTemplate(pdf, elements=elements)
        template["name"] = member
        # template["surname"] = member["NOM"]
        # template["birthday"] = "Non renseignée" if pd.isna(member["date de naissance"]) else member["date de naissance"]
        if qrcode_url is not None:
            template["qrcode"] = img.get_image()
        template.render(offsetx=offsetx, offsety=offsety)

    return pdf
