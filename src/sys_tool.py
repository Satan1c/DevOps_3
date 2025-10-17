import sys


def run():
	if len(sys.argv) > 1:
		if sys.argv[1] in ["-h", "--help"]:
			print("Для виведення тексту, виконайте скрипт без аргументів")

		return

	print("командна строка")


if __name__ == "__main__":
	run()
