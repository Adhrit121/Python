


in_folder=False
import curses

def clean_menu():
    # Clean up curses
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

# Define the options
main_options = ["CryptoGraphy","Wifi","Rat","Tools","Other"]
selected_option = 0
wifi_options=["Games",""]
    # Initialize curses
stdscr = curses.initscr()
curses.cbreak()
curses.noecho()
stdscr.keypad(True)
    # Define the colors
curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    # Define the rendering function
def render_menu():
    stdscr.clear()
    if not in_folder:
        stdscr.addstr(0, 0, "[arrow keys:change options] [c:quit] [spacebar:select option] ", curses.A_BOLD)
    else:
        stdscr.addstr(0, 0, "[arrow keys:change options] [c:quit] [spacebar:select option] [r:return to previous options]", curses.A_BOLD)
    for i, option in enumerate(main_options):
        if i == selected_option:
            stdscr.addstr(i + 2, 0, option, curses.color_pair(1))
        else:
            stdscr.addstr(i + 2, 0, option, curses.color_pair(2))
    stdscr.refresh()
    # Render the initial menu
render_menu()
    # Main loop
while True:
    if in_main:
        time.sleep(0.01)
        key = stdscr.getch()
        if key == curses.KEY_UP:
            selected_option = max(selected_option - 1, 0)
            render_menu()
        elif key == curses.KEY_DOWN:
            selected_option = min(selected_option + 1, len(main_options) - 1)
            render_menu()
        elif key == ord(" "):
            # The spacebar was clicked, execute the selected option
            stdscr.addstr(5, 0, "You clicked: " + main_options[selected_option])
            print("You clicked: " + main_options[selected_option])
            stdscr.refresh()
            # Clean up curses
            clean_menu()
            run_script(str(main_options[selected_option]).strip())
            break
        elif key == ord('c'):
            clean_menu()
            updating_print("Quitting")
            clear()
            print("#AdhritIsGreat/n")
            time.sleep(1)
            print("Bye :)")
            break
