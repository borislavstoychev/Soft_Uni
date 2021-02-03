from pyfiglet import figlet_format


def art(msg):
    ascii_art = figlet_format(msg)
    return ascii_art

print(art(input()))