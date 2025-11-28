from pathlib import Path
from members_card.generate_card import generate_cards
from members_card.main import create_parser, process_args


def test_generate_cards():
    names = [f"Adhérent {i}" for i in range(13)]
    background_color_2 = (0, 166, 82)
    background_color_1 = (255, 255, 255)
    paper_format = "a4"
    logo = Path(__file__).parent / "resources" / "logo.svg"
    qrcode_url = "https://www.mon.url.fr"
    title = "MON TITRE"
    footer_1 = "footer 1"
    footer_2 = "footer 2"
    pdf = generate_cards(
        names,
        background_color_1=background_color_1,
        background_color_2=background_color_2,
        paper_format=paper_format,
        qrcode_url=qrcode_url,
        logo_path=logo,
        title=title,
        footer_1=footer_1,
        footer_2=footer_2,
    )
    assert pdf.pages_count == 2


def test_cli(tmp_path):
    resources_path = Path(__file__).parent / "resources"
    output_path = tmp_path / "output.pdf"
    args_list = [
        str(resources_path / "adherents.csv"),
        str(output_path),
        "--name-columns",
        "Nom",
        "Prénom",
        # "--logo",
        # str(resources_path / "logo.svg")
    ]
    parser = create_parser()
    args = parser.parse_args(args_list)
    process_args(args)
    assert output_path.exists()
