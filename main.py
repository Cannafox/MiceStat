from MiceStat import MiceStat

# WINDOW_TITLE =


def main():
    miceStat = MiceStat()

    try:
        miceStat.run()
    except Exception as e:
        print(f"MiceStat crashed.\n{e}")
    finally:
        print("MiceStat is off")


if __name__ == "__main__":
    main()
