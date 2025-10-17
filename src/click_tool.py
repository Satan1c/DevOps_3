import sys


def run():
	if len(sys.argv) > 1:
		command = sys.argv[1]
		if command in ["-h", "--help"]:
			print("-n/--name <ім'я> : Виводить привітання з вказаним ім'ям")
			return
		elif command in ["-n", "--name"]:
			if len(sys.argv) > 2:
				name = sys.argv[2]
				if name.lower().startswith("p"):
					print("Ім’я не підходить")
					return
				print(f"Привіт, {sys.argv[2]}!")
			else:
				print(f"Будь ласка, вкажіть ім'я після {command}")
			return

		return

	print("--help : Показати довідку")


if __name__ == "__main__":
	run()
