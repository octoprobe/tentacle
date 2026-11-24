import pathlib

DIRECTORY_OF_THIS_FILE = pathlib.Path(__file__).parent


def main():
    with (DIRECTORY_OF_THIS_FILE / "PinSocket_2x20_P2.54mm_Vertical.wrl").open(
        "w"
    ) as f_out:
        with (DIRECTORY_OF_THIS_FILE / "PinSocket_2x20_P2.54mm_Vertical-ori.wrl").open(
            "r"
        ) as f_in:
            for line in f_in.readlines():
                if line.startswith("coord Coordinate { point"):
                    # y_offset_socket = 11.0 - 2.75
                    # y_offset_pin = 23.2 - 6.0
                    # y_offset_socket = 11.0 - 2.75*2.54
                    # y_offset_pin = 23.2 - 6.0*2.54
                    y_offset_socket = 11.0/2.54 - 2.75
                    y_offset_pin = 23.2/2.54 - 4.0
                    for y, y_offset in (
                        # "-0.961",
                        # "-0.984",
                        # "-1.039",
                        # "0.079", # Case - important!
                        ("0.079", y_offset_socket),
                        ("-1.921", y_offset_pin),
                        ("-1.220", y_offset_pin),
                    ):
                        y_new = f"{float(y)-y_offset:0.3f}"
                        # print(y, y_new)
                        line = line.replace(y, y_new)
                    # line = line.replace(" -1.220,", " -2.220")
                f_out.write(line)


if __name__ == "__main__":
    main()
