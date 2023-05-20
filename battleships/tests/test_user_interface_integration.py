import unittest

from lib.user_interface import UserInterface
from lib.game import Game
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock


class TestUserInterface(unittest.TestCase):
    def test_ship_setup_scenario(self):
        io = TerminalInterfaceHelperMock()
        interface = UserInterface(io, Game())
        io.expect_print("Welcome to the game!")
        io.expect_print("Set up your ships first.")

        # first iteration
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))

        # second iteration
        io.expect_print("You have these ships remaining: 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("1")
        io.expect_print("Which column?")
        io.provide("3")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..SSS.....",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))

        # third iteration
        io.expect_print("You have these ships remaining: 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("9")
        io.expect_print("Which column?")
        io.provide("5")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..SSS.....",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "....SSS...",
            ".........."
        ]))

        # fourth iteration
        io.expect_print("You have these ships remaining: 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("4")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("7")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..SSS.....",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "S.........",
            "S.........",
            "S...SSS...",
            "S........."
        ]))

        # fifth iteration
        io.expect_print("You have these ships remaining: 5")
        io.expect_print("Which do you wish to place?")
        io.provide("5")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("6")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..SSS.....",
            "..........",
            ".S........",
            ".S........",
            "..........",
            ".S........",
            "SS........",
            "SS........",
            "SS..SSS...",
            "SS........"
        ]))

        io.expect_print("Done, for now!")
        interface.place_ships()
