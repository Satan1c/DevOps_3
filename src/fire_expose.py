import fire

import utils


class CLI:
	"""
	Tool to say hello or goodbye.

	Methods:
	  - greet(name): Greet a person by name.
	  - goodbye(name): Say goodbye to a person by name.
	"""

	def greet(self, name: str) -> None:
		"""
		Greet a person by name.

		Example:
		  py src.fire_expose greet Alice
		"""
		return utils.greet(name)

	def goodbye(self, name: str) -> None:
		"""
		Say goodbye to a person by name.

		Example:
		  py src.fire_expose goodbye Bob
		"""
		return utils.goodbye(name)


if __name__ == "__main__":
	fire.Fire(CLI)
