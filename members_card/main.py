from argparse import ArgumentParser, Namespace
from pathlib import Path

import pandas as pd

from .generate_card import generate_cards


def create_parser() -> ArgumentParser:
    parser = ArgumentParser(prog="members-card")
    parser.add_argument("members_csv", type=Path, help="CSV file with members list")
    parser.add_argument("output_file", type=Path, help="Output pdf file path")
    parser.add_argument(
        "--name-columns",
        "-n",
        required=True,
        nargs="+",
        type=str,
        default=[],
        help="Columns of the CSV file to use as name",
    )
    parser.add_argument(
        "--name-color", "-nc", type=int, default=0x000000, help="color of the name text"
    )
    parser.add_argument(
        "--background-color-1",
        "-c1",
        nargs=3,
        type=int,
        default=(0, 166, 82),
        metavar=("RED", "GREEN", "BLUE"),
        help="Background color of the bottom left angle",
    )
    parser.add_argument(
        "--background-color-2",
        "-c2",
        nargs=3,
        type=int,
        default=(255, 255, 255),
        metavar=("RED", "GREEN", "BLUE"),
        help="Background color of the top right angle",
    )
    parser.add_argument(
        "--paper-format", "-p", type=str, default="a4", help="Paper format"
    )
    parser.add_argument(
        "--qrcode-url", "-q", type=str, help="Sting to encode in the qrcode"
    )
    parser.add_argument("--logo", "-l", type=Path, help="Logo")
    parser.add_argument("--title", "-t", type=str, default="", help="Card title")
    parser.add_argument(
        "--title-color", "-tc", type=int, default=0x000000, help="Title color"
    )
    parser.add_argument(
        "--footer-1", "-f1", type=str, default="", help="Footer first line"
    )
    parser.add_argument(
        "--footer-2", "-f2", type=str, default="", help="Footer seconde line"
    )
    parser.add_argument(
        "--footer-color", "-fc", type=int, default=0x000000, help="Footer color"
    )

    return parser


def process_args(args: Namespace):
    members_df = pd.read_csv(args.members_csv)
    names = [" ".join(member[args.name_columns]) for _, member in members_df.iterrows()]
    print(args.background_color_1)
    pdf = generate_cards(
        names,
        background_color_1=args.background_color_1,
        background_color_2=args.background_color_2,
        paper_format=args.paper_format,
        qrcode_url=args.qrcode_url,
        logo_path=args.logo,
        title=args.title,
        footer_1=args.footer_1,
        footer_2=args.footer_2,
        title_color=args.title_color,
        name_color=args.name_color,
        footer_color=args.footer_color,
    )
    pdf.output(args.output_file)


def cli():
    parser = create_parser()

    args = parser.parse_args()

    process_args(args)


if __name__ == "__main__":
    cli()
