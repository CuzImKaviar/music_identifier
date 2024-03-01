def tester(var: str = "default") -> None:
    print(var)

if __name__ == "__main__":
    tester()
    tester("parameter")
    tester(None)