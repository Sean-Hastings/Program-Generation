import argparse
import xlsxwriter

from src.utils.rpe import add_rpe_chart


def build_program(worksheet, args):
    # Build Header
    cur_row = build_header(worksheet, args)
    # Build Template
    cur_row = build_template(worksheet, args, cur_row)
    # Build Body
    build_body(worksheet, args, cur_row)


def build_header(worksheet, args):
    pass


def build_template(worksheet, args, top_row):
    pass


def build_body(worksheet, args, top_row):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a program template with specified features.")
    # Functional arguments
    parser.add_argument("--gen_path", type=str, default="./new_program.xlsx", help="File path to save the program at.")
    parser.add_argument("--n_waves", type=int, default=4, help="Number of waves to program for.")
    parser.add_argument("--n_weeks", type=int, default=3, help="Number of weeks per wave.")
    parser.add_argument("--n_days", type=int, default=5, help="Number of days per week.")
    parser.add_argument("--max_lifts", type=int, default=3, help="Number of core lifts per day to make space for.")
    parser.add_argument("--max_accessories", type=int, default=2, help="Number of accesory lifts per day to make space for.")
    parser.add_argument("--max_sets", type=int, default=6, help="Number of sets per core lift to make space for.")
    parser.add_argument("--n_lifts", type=int, default=4, help="Number of unique lifts to track maxes for.")

    args = parser.parse_args()

    workbook = xlsxwriter.Workbook(args.gen_path)

    # Build Program
    program_worksheet = workbook.add_worksheet("Program")
    build_program(program_worksheet, args)

    # Build Main analysis sheet

    # Build relative intensity/load chart sheet

    # Build absolute intensity/load chart sheet

    add_rpe_chart(workbook)
    # add_pril_chart(workbook)

    # List args in a worksheet

    workbook.close()
